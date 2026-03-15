from __future__ import annotations

from typing import TYPE_CHECKING, Any

import aiohttp

from .._pagination import fetch_all_pages

if TYPE_CHECKING:
    from .._client import APIClient


class BaseResource:
    """
    Abstract base for all resource classes. Injected with the live APIClient.

    Subclasses set _path and call self._list(), self._get(), etc.
    Never call self._client.request() directly from a resource — use the
    helpers here so pagination and conventions stay consistent.
    """

    _path: str

    def __init__(self, client: "APIClient") -> None:
        self._client = client

    # --- Helpers used by subclasses ---

    async def _list(self, params: dict[str, Any] | None = None) -> dict[str, Any]:
        """GET _path with automatic pagination."""
        return await fetch_all_pages(self._client, "GET", self._path, params=params)

    async def _get(
        self, resource_id: int | str, params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """GET _path/{id}"""
        return await self._client.request(
            "GET", f"{self._path}/{resource_id}", params=params
        )

    async def _create(self, payload: dict[str, Any]) -> dict[str, Any]:
        """POST _path"""
        return await self._client.request("POST", self._path, json=payload)

    async def _update(
        self, resource_id: int | str, payload: dict[str, Any]
    ) -> dict[str, Any]:
        """PUT _path/{id}"""
        return await self._client.request(
            "PUT", f"{self._path}/{resource_id}", json=payload
        )

    async def _delete(self, resource_id: int | str) -> dict[str, Any]:
        """DELETE _path/{id}"""
        return await self._client.request("DELETE", f"{self._path}/{resource_id}")

    async def _action(
        self, path: str, payload: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """POST to an action endpoint (e.g. /Estimates/{id}/Won)."""
        return await self._client.request("POST", path, json=payload)

    async def _upload(
        self, path: str, file_content: bytes, filename: str, **fields: str
    ) -> dict[str, Any]:
        """POST multipart/form-data to an upload endpoint (photos, documents)."""
        form = aiohttp.FormData()
        form.add_field("content", file_content, filename=filename)
        for key, value in fields.items():
            form.add_field(key, value)
        return await self._client.request("POST", path, data=form)

    async def batch_get(
        self, ids: list[int], *, params: dict[str, Any] | None = None
    ) -> dict[int, Any]:
        """
        Fetch multiple records by ID concurrently — all within the same coroutine.

        asyncio.gather fires all requests at once. Each request awaits its own
        rate_limiter.acquire() slot, so they queue automatically at up to 50/s.
        Works whether there are 1 or 500 unique IDs — no special setup needed.

        Returns {id: model_data} — the Data field unwrapped from ApiResponse.

        Usage:
            customers = await client.customers.batch_get([1, 2, 3])
            customers[1].Email
        """
        import asyncio

        from ..models._base import ApiResponse

        unique_ids = list(dict.fromkeys(ids))  # deduplicate, preserve insertion order

        async def fetch_one(resource_id: int) -> tuple[int, Any]:
            raw = await self._get(resource_id, params=params)
            return resource_id, ApiResponse[Any].model_validate(raw).Data

        results = await asyncio.gather(*[fetch_one(i) for i in unique_ids])
        return dict(results)
