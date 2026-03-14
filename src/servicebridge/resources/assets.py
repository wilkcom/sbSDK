from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiPagedListResponse, ApiResponse
from ..models.assets import Asset


class AssetsResource(BaseResource):
    _path = Endpoints.ASSETS

    async def list(self, **filters: Any) -> ApiPagedListResponse[Asset]:
        raw = await self._list(filters or None)
        return ApiPagedListResponse[Asset].model_validate(raw)

    async def get(self, asset_id: int) -> ApiResponse[Asset]:
        raw = await self._get(asset_id)
        return ApiResponse[Asset].model_validate(raw)
