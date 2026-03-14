"""Transparent auto-pagination for paginated API endpoints."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ._client import APIClient

import logging

logger = logging.getLogger("servicebridge")

PAGE_SIZE_DEFAULT = 500  # max allowed by the API


async def fetch_all_pages(
    client: "APIClient",
    method: str,
    path: str,
    params: dict[str, Any] | None = None,
    page_size: int = PAGE_SIZE_DEFAULT,
) -> dict[str, Any]:
    """
    Fetch all pages for a paginated endpoint and return a single merged response.

    Continues fetching while the returned page is full (len == page_size).
    Returns the first-page envelope with all Data items merged in.
    """
    params = dict(params or {})
    params.setdefault("pageSize", page_size)
    params["page"] = 1

    first = await client.request(method, path, params=params)
    items: list[Any] = list(first.get("Data") or [])

    if len(items) < page_size:
        first["Data"] = items
        return first

    page = 2
    while True:
        params["page"] = page
        page_data = await client.request(method, path, params=params)
        batch: list[Any] = list(page_data.get("Data") or [])
        items.extend(batch)
        logger.debug("Fetched page %d (%d records)", page, len(batch))
        if len(batch) < page_size:
            break
        page += 1

    first["Data"] = items
    return first
