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

    BATCH_CONCURRENCY = 30  # max simultaneous requests in batch_get

    async def _batch_gather(self, coros: list[Any], concurrency: int = BATCH_CONCURRENCY) -> list[Any]:
        """
        Run coroutines concurrently with a semaphore cap.
        Prevents batch_get from firing more than `concurrency` requests at once,
        keeping the effective rate well within the API's 50 req/s hard limit.
        """
        import asyncio

        sem = asyncio.Semaphore(concurrency)

        async def limited(coro: Any) -> Any:
            async with sem:
                return await coro

        return list(await asyncio.gather(*[limited(c) for c in coros]))

    async def batch_get(
        self, ids: list[int], *, params: dict[str, Any] | None = None
    ) -> dict[int, Any]:
        """
        Fetch multiple records by ID concurrently, capped at BATCH_CONCURRENCY
        simultaneous requests to avoid hitting API rate limits.

        Returns {id: model_data} — the Data field unwrapped from ApiResponse.
        """
        from ..models._base import ApiResponse

        unique_ids = list(dict.fromkeys(ids))  # deduplicate, preserve insertion order

        async def fetch_one(resource_id: int) -> tuple[int, Any]:
            raw = await self._get(resource_id, params=params)
            return resource_id, ApiResponse[Any].model_validate(raw).Data

        results = await self._batch_gather([fetch_one(i) for i in unique_ids])
        return dict(results)
