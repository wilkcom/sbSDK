from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiListResponse
from ..models.sales_representatives import SalesRepresentative


class SalesRepresentativesResource(BaseResource):
    _path = Endpoints.SALES_REPRESENTATIVES

    async def list(self, **filters: Any) -> ApiListResponse[SalesRepresentative]:
        raw = await self._client.request("GET", self._path, params=filters or None)
        return ApiListResponse[SalesRepresentative].model_validate(raw)
