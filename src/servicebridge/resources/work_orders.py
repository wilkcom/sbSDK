from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiPagedListResponse, ApiResponse
from ..models.work_orders import WorkOrder, WorkOrderCreate, WorkOrderPhoto, WorkOrderUpdate

if TYPE_CHECKING:
    from .._client import APIClient


class WorkOrderPhotosResource:
    def __init__(self, client: "APIClient", work_order_id: int) -> None:
        self._client = client
        self._path = Endpoints.work_order_photos(work_order_id)

    async def list(self) -> ApiPagedListResponse[WorkOrderPhoto]:
        from .._pagination import fetch_all_pages
        raw = await fetch_all_pages(self._client, "GET", self._path)
        return ApiPagedListResponse[WorkOrderPhoto].model_validate(raw)

    async def upload(
        self,
        file_content: bytes,
        filename: str,
        photo_type: str,
        description: str | None = None,
        external_system_id: str | None = None,
    ) -> ApiResponse[WorkOrderPhoto]:
        import aiohttp
        form = aiohttp.FormData()
        form.add_field("content", file_content, filename=filename)
        form.add_field("photoType", photo_type)
        if description:
            form.add_field("description", description)
        if external_system_id:
            form.add_field("externalSystemId", external_system_id)
        raw = await self._client.request("POST", self._path, data=form)
        return ApiResponse[WorkOrderPhoto].model_validate(raw)


class WorkOrdersResource(BaseResource):
    _path = Endpoints.WORK_ORDERS

    def photos(self, work_order_id: int) -> WorkOrderPhotosResource:
        return WorkOrderPhotosResource(self._client, work_order_id)

    async def list(self, **filters: Any) -> ApiPagedListResponse[WorkOrder]:
        raw = await self._list(filters or None)
        return ApiPagedListResponse[WorkOrder].model_validate(raw)

    async def get(self, work_order_id: int) -> ApiResponse[WorkOrder]:
        raw = await self._get(work_order_id)
        return ApiResponse[WorkOrder].model_validate(raw)

    async def create(self, data: WorkOrderCreate) -> ApiResponse[WorkOrder]:
        raw = await self._create(data.model_dump(exclude_none=True))
        return ApiResponse[WorkOrder].model_validate(raw)

    async def update(self, work_order_id: int, data: WorkOrderUpdate) -> ApiResponse[WorkOrder]:
        raw = await self._update(work_order_id, data.model_dump(exclude_none=True))
        return ApiResponse[WorkOrder].model_validate(raw)

    async def delete(self, work_order_id: int) -> ApiResponse[None]:
        raw = await self._delete(work_order_id)
        return ApiResponse[None].model_validate(raw)
