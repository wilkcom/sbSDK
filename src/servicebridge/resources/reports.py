from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiResponse
from ..models.reports import Report


class ReportsResource(BaseResource):
    _path = Endpoints.REPORT

    async def get(self, **params: Any) -> ApiResponse[Report]:
        raw = await self._client.request("GET", self._path, params=params or None)
        return ApiResponse[Report].model_validate(raw)
