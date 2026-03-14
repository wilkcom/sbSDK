from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiPagedListResponse, ApiResponse
from ..models.leads import Lead, LeadCreate, LeadUpdate


class LeadsResource(BaseResource):
    _path = Endpoints.LEADS

    async def list(self, **filters: Any) -> ApiPagedListResponse[Lead]:
        raw = await self._list(filters or None)
        return ApiPagedListResponse[Lead].model_validate(raw)

    async def get(self, lead_id: int) -> ApiResponse[Lead]:
        raw = await self._get(lead_id)
        return ApiResponse[Lead].model_validate(raw)

    async def create(self, data: LeadCreate) -> ApiResponse[Lead]:
        raw = await self._create(data.model_dump(exclude_none=True))
        return ApiResponse[Lead].model_validate(raw)

    async def update(self, lead_id: int, data: LeadUpdate) -> ApiResponse[Lead]:
        raw = await self._update(lead_id, data.model_dump(exclude_none=True))
        return ApiResponse[Lead].model_validate(raw)

    async def delete(self, lead_id: int) -> ApiResponse[None]:
        raw = await self._delete(lead_id)
        return ApiResponse[None].model_validate(raw)
