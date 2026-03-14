import asyncio
import logging
import os
from datetime import datetime, timedelta, timezone
from typing import Any

import aiohttp
from dotenv import load_dotenv

from ._constants import BASE_URL, Endpoints
from ._rate_limiter import RateLimiter
from .exceptions import (
    APIError,
    AuthenticationError,
    ConfigurationError,
    NotFoundError,
    RateLimitError,
)

load_dotenv()

logger = logging.getLogger("servicebridge")

_TOKEN_TTL_HOURS = 24
_TOKEN_BUFFER_SECONDS = 30


class APIClient:
    """
    Low-level async HTTP client. Manages the aiohttp session, token auth,
    rate limiting, and HTTP error mapping. Not for direct use — use
    ServiceBridgeClient instead.
    """

    def __init__(
        self,
        user_id: str | None = None,
        password: str | None = None,
        base_url: str = BASE_URL,
    ) -> None:
        resolved_user = user_id or os.environ.get("API_USER_ID")
        resolved_pass = password or os.environ.get("API_PASSWORD")
        if not resolved_user or not resolved_pass:
            raise ConfigurationError(
                "API_USER_ID and API_PASSWORD must be set via arguments or environment variables."
            )
        self._user_id = resolved_user
        self._password = resolved_pass
        self._base_url = base_url.rstrip("/")

        self._token: str | None = None
        self._token_expiry: datetime = datetime.min.replace(tzinfo=timezone.utc)
        self._auth_lock = asyncio.Lock()

        self._session: aiohttp.ClientSession | None = None
        self._rate_limiter = RateLimiter()

    # --- Session lifecycle ---

    async def __aenter__(self) -> "APIClient":
        await self._ensure_session()
        return self

    async def __aexit__(self, *_: Any) -> None:
        await self.close()

    async def _ensure_session(self) -> None:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(
                headers={"Content-Type": "application/json"},
            )

    async def close(self) -> None:
        if self._session and not self._session.closed:
            await self._session.close()

    # --- Authentication ---

    def _token_is_valid(self) -> bool:
        now = datetime.now(tz=timezone.utc)
        return (
            self._token is not None
            and now < self._token_expiry - timedelta(seconds=_TOKEN_BUFFER_SECONDS)
        )

    async def _authenticate(self) -> None:
        async with self._auth_lock:
            if self._token_is_valid():
                return  # another coroutine refreshed while we waited
            await self._ensure_session()
            assert self._session is not None
            payload = {"UserId": self._user_id, "Password": self._password}
            # Auth call does not go through rate limiter to avoid deadlock on startup
            async with self._session.post(
                f"{self._base_url}{Endpoints.LOGIN}", json=payload
            ) as resp:
                if resp.status != 200:
                    raw = await resp.json()
                    raise AuthenticationError(resp.status, "Login failed", raw)
                data = await resp.json()
                self._token = data.get("Data")
                self._token_expiry = datetime.now(tz=timezone.utc) + timedelta(hours=_TOKEN_TTL_HOURS)
                logger.debug("Authenticated; token cached for %d hours.", _TOKEN_TTL_HOURS)

    # --- Request execution ---

    async def request(
        self,
        method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
        data: aiohttp.FormData | None = None,
        _retry: bool = True,
    ) -> dict[str, Any]:
        if not self._token_is_valid():
            await self._authenticate()

        await self._ensure_session()
        assert self._session is not None

        await self._rate_limiter.acquire()

        merged_params: dict[str, Any] = {**(params or {}), "sessionKey": self._token}

        # For multipart uploads, don't send the JSON content-type header
        request_headers: dict[str, str] = {}
        if data is not None:
            request_headers = {}  # let aiohttp set multipart content-type

        async with self._session.request(
            method,
            f"{self._base_url}{path}",
            params=merged_params,
            json=json,
            data=data,
            headers=request_headers if data else None,
        ) as resp:
            if resp.status == 401:
                if not _retry:
                    raise AuthenticationError(401, "Token refresh failed after retry.")
                logger.debug("401 received; refreshing token.")
                self._token = None
                await self._authenticate()
                return await self.request(
                    method, path, params=params, json=json, data=data, _retry=False
                )

            if resp.status == 404:
                raise NotFoundError(404, f"Resource not found: {path}")

            if resp.status == 429:
                raise RateLimitError(429, "API rate limit exceeded.")

            if resp.status >= 400:
                try:
                    raw = await resp.json()
                except Exception:
                    raw = {"Message": await resp.text()}
                raise APIError(resp.status, raw.get("Message", "Unknown error"), raw)

            return await resp.json()  # type: ignore[no-any-return]
