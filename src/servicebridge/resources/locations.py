from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiPagedListResponse, ApiResponse
from ..models.locations import Location, LocationCreate, LocationUpdate


class LocationsResource(BaseResource):
    _path = Endpoints.LOCATIONS

    async def list(self, **filters: Any) -> ApiPagedListResponse[Location]:
        raw = await self._list(filters or None)
        return ApiPagedListResponse[Location].model_validate(raw)

    async def get(self, location_id: int) -> ApiResponse[Location]:
        raw = await self._get(location_id)
        return ApiResponse[Location].model_validate(raw)

    async def create(self, data: LocationCreate) -> ApiResponse[Location]:
        raw = await self._create(data.model_dump(exclude_none=True))
        return ApiResponse[Location].model_validate(raw)

    async def update(self, location_id: int, data: LocationUpdate) -> ApiResponse[Location]:
        raw = await self._update(location_id, data.model_dump(exclude_none=True))
        return ApiResponse[Location].model_validate(raw)

    async def delete(self, location_id: int) -> ApiResponse[None]:
        raw = await self._delete(location_id)
        return ApiResponse[None].model_validate(raw)
