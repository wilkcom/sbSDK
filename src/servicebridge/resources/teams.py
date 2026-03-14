from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiListResponse
from ..models.teams import Team


class TeamsResource(BaseResource):
    _path = Endpoints.TEAMS

    async def list(self, **filters: Any) -> ApiListResponse[Team]:
        raw = await self._client.request("GET", self._path, params=filters or None)
        return ApiListResponse[Team].model_validate(raw)
