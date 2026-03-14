from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiListResponse, ApiResponse
from ..models.custom_field_groups import CustomFieldGroup, CustomFieldGroupCreate, CustomFieldGroupUpdate


class CustomFieldGroupsResource(BaseResource):
    _path = Endpoints.CUSTOM_FIELD_GROUPS

    async def list(self, type: str, **filters: Any) -> ApiListResponse[CustomFieldGroup]:
        params = {"type": type, **filters}
        raw = await self._client.request("GET", self._path, params=params)
        return ApiListResponse[CustomFieldGroup].model_validate(raw)

    async def get(self, group_id: int, type: str) -> ApiResponse[CustomFieldGroup]:
        raw = await self._get(group_id, params={"type": type})
        return ApiResponse[CustomFieldGroup].model_validate(raw)

    async def create(self, data: CustomFieldGroupCreate) -> ApiResponse[CustomFieldGroup]:
        raw = await self._create(data.model_dump(exclude_none=True))
        return ApiResponse[CustomFieldGroup].model_validate(raw)

    async def update(self, group_id: int, data: CustomFieldGroupUpdate) -> ApiResponse[CustomFieldGroup]:
        raw = await self._update(group_id, data.model_dump(exclude_none=True))
        return ApiResponse[CustomFieldGroup].model_validate(raw)

    async def delete(self, group_id: int, type: str) -> ApiResponse[None]:
        raw = await self._client.request("DELETE", f"{self._path}/{group_id}", params={"type": type})
        return ApiResponse[None].model_validate(raw)
