from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiListResponse
from ..models.statistics import Statistic


class StatisticsResource(BaseResource):
    _path = Endpoints.STATISTICS

    async def list(self, **filters: Any) -> ApiListResponse[Statistic]:
        raw = await self._client.request("GET", self._path, params=filters or None)
        return ApiListResponse[Statistic].model_validate(raw)
