from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiPagedListResponse, ApiResponse
from ..models.users import User


class UsersResource(BaseResource):
    _path = Endpoints.USERS

    async def list(self, **filters: Any) -> ApiPagedListResponse[User]:
        raw = await self._list(filters or None)
        return ApiPagedListResponse[User].model_validate(raw)

    async def get(self, user_id: int) -> ApiResponse[User]:
        raw = await self._get(user_id)
        return ApiResponse[User].model_validate(raw)
