from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiListResponse, ApiResponse
from ..models.custom_fields import CustomField, CustomFieldCreate, CustomFieldUpdate


class CustomFieldsResource(BaseResource):
    _path = Endpoints.CUSTOM_FIELDS

    async def list(self, type: str, **filters: Any) -> ApiListResponse[CustomField]:
        params = {"type": type, **filters}
        raw = await self._client.request("GET", self._path, params=params)
        return ApiListResponse[CustomField].model_validate(raw)

    async def get(self, field_id: int, type: str) -> ApiResponse[CustomField]:
        raw = await self._get(field_id, params={"type": type})
        return ApiResponse[CustomField].model_validate(raw)

    async def create(self, data: CustomFieldCreate) -> ApiResponse[CustomField]:
        raw = await self._create(data.model_dump(exclude_none=True))
        return ApiResponse[CustomField].model_validate(raw)

    async def update(self, field_id: int, data: CustomFieldUpdate) -> ApiResponse[CustomField]:
        raw = await self._update(field_id, data.model_dump(exclude_none=True))
        return ApiResponse[CustomField].model_validate(raw)

    async def delete(self, field_id: int, type: str) -> ApiResponse[None]:
        raw = await self._client.request("DELETE", f"{self._path}/{field_id}", params={"type": type})
        return ApiResponse[None].model_validate(raw)
