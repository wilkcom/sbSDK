from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiPagedListResponse, ApiResponse
from ..models.branches import Branch, BranchCreate, BranchUpdate


class BranchesResource(BaseResource):
    _path = Endpoints.BRANCHES

    async def list(self, **filters: Any) -> ApiPagedListResponse[Branch]:
        raw = await self._list(filters or None)
        return ApiPagedListResponse[Branch].model_validate(raw)

    async def get(self, branch_id: int) -> ApiResponse[Branch]:
        raw = await self._get(branch_id)
        return ApiResponse[Branch].model_validate(raw)

    async def create(self, data: BranchCreate) -> ApiResponse[Branch]:
        raw = await self._create(data.model_dump(exclude_none=True))
        return ApiResponse[Branch].model_validate(raw)

    async def update(self, branch_id: int, data: BranchUpdate) -> ApiResponse[Branch]:
        raw = await self._update(branch_id, data.model_dump(exclude_none=True))
        return ApiResponse[Branch].model_validate(raw)

    async def delete(self, branch_id: int) -> ApiResponse[None]:
        raw = await self._delete(branch_id)
        return ApiResponse[None].model_validate(raw)
