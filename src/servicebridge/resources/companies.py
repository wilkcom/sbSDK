from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiPagedListResponse, ApiResponse
from ..models.companies import Company


class CompaniesResource(BaseResource):
    _path = Endpoints.COMPANIES

    async def list(self, **filters: Any) -> ApiPagedListResponse[Company]:
        raw = await self._list(filters or None)
        return ApiPagedListResponse[Company].model_validate(raw)

    async def get(self, company_id: int) -> ApiResponse[Company]:
        raw = await self._get(company_id)
        return ApiResponse[Company].model_validate(raw)
