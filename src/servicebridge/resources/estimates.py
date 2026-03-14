from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiPagedListResponse, ApiResponse
from ..models.estimates import (
    Estimate,
    EstimateCreate,
    EstimateDocument,
    EstimateDuplicate,
    EstimateLost,
    EstimatePhoto,
    EstimateReopen,
    EstimateUpdate,
    EstimateWon,
)

if TYPE_CHECKING:
    from .._client import APIClient


class EstimatePhotosResource:
    def __init__(self, client: "APIClient", estimate_id: int) -> None:
        self._client = client
        self._path = Endpoints.estimate_photos(estimate_id)

    async def list(self) -> ApiPagedListResponse[EstimatePhoto]:
        from .._pagination import fetch_all_pages
        raw = await fetch_all_pages(self._client, "GET", self._path)
        return ApiPagedListResponse[EstimatePhoto].model_validate(raw)

    async def upload(
        self,
        file_content: bytes,
        filename: str,
        photo_type: str,
        description: str | None = None,
        external_system_id: str | None = None,
    ) -> ApiResponse[EstimatePhoto]:
        import aiohttp
        form = aiohttp.FormData()
        form.add_field("content", file_content, filename=filename)
        form.add_field("photoType", photo_type)
        if description:
            form.add_field("description", description)
        if external_system_id:
            form.add_field("externalSystemId", external_system_id)
        raw = await self._client.request("POST", self._path, data=form)
        return ApiResponse[EstimatePhoto].model_validate(raw)


class EstimateDocumentsResource:
    def __init__(self, client: "APIClient", estimate_id: int) -> None:
        self._client = client
        self._path = Endpoints.estimate_documents(estimate_id)

    async def list(self) -> ApiPagedListResponse[EstimateDocument]:
        from .._pagination import fetch_all_pages
        raw = await fetch_all_pages(self._client, "GET", self._path)
        return ApiPagedListResponse[EstimateDocument].model_validate(raw)

    async def upload(
        self,
        file_content: bytes,
        filename: str,
        name: str | None = None,
        description: str | None = None,
        external_system_id: str | None = None,
        show_in_customer_portal: bool = False,
    ) -> ApiResponse[EstimateDocument]:
        import aiohttp
        form = aiohttp.FormData()
        form.add_field("content", file_content, filename=filename)
        if name:
            form.add_field("name", name)
        if description:
            form.add_field("description", description)
        if external_system_id:
            form.add_field("externalSystemId", external_system_id)
        form.add_field("showInCustomerPortal", str(show_in_customer_portal).lower())
        raw = await self._client.request("POST", self._path, data=form)
        return ApiResponse[EstimateDocument].model_validate(raw)


class EstimatesResource(BaseResource):
    _path = Endpoints.ESTIMATES

    def photos(self, estimate_id: int) -> EstimatePhotosResource:
        return EstimatePhotosResource(self._client, estimate_id)

    def documents(self, estimate_id: int) -> EstimateDocumentsResource:
        return EstimateDocumentsResource(self._client, estimate_id)

    async def list(self, **filters: Any) -> ApiPagedListResponse[Estimate]:
        raw = await self._list(filters or None)
        return ApiPagedListResponse[Estimate].model_validate(raw)

    async def get(self, estimate_id: int) -> ApiResponse[Estimate]:
        raw = await self._get(estimate_id)
        return ApiResponse[Estimate].model_validate(raw)

    async def create(self, data: EstimateCreate) -> ApiResponse[Estimate]:
        raw = await self._create(data.model_dump(exclude_none=True))
        return ApiResponse[Estimate].model_validate(raw)

    async def update(self, estimate_id: int, data: EstimateUpdate) -> ApiResponse[Estimate]:
        raw = await self._update(estimate_id, data.model_dump(exclude_none=True))
        return ApiResponse[Estimate].model_validate(raw)

    async def mark_won(self, estimate_id: int, data: EstimateWon | None = None) -> ApiResponse[Estimate]:
        payload = data.model_dump(exclude_none=True) if data else {}
        raw = await self._action(Endpoints.estimate_won(estimate_id), payload)
        return ApiResponse[Estimate].model_validate(raw)

    async def mark_lost(self, estimate_id: int, data: EstimateLost | None = None) -> ApiResponse[Estimate]:
        payload = data.model_dump(exclude_none=True) if data else {}
        raw = await self._action(Endpoints.estimate_lost(estimate_id), payload)
        return ApiResponse[Estimate].model_validate(raw)

    async def reopen(self, estimate_id: int, data: EstimateReopen | None = None) -> ApiResponse[Estimate]:
        payload = data.model_dump(exclude_none=True) if data else {}
        raw = await self._action(Endpoints.estimate_reopen(estimate_id), payload)
        return ApiResponse[Estimate].model_validate(raw)

    async def duplicate(self, estimate_id: int, data: EstimateDuplicate | None = None) -> ApiResponse[int]:
        payload = data.model_dump(exclude_none=True) if data else {}
        raw = await self._action(Endpoints.estimate_duplicate(estimate_id), payload)
        return ApiResponse[int].model_validate(raw)
