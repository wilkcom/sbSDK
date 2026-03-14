from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiListResponse
from ..models.taxes import Tax


class TaxesResource(BaseResource):
    _path = Endpoints.TAXES

    async def list(self, **filters: Any) -> ApiListResponse[Tax]:
        raw = await self._client.request("GET", self._path, params=filters or None)
        return ApiListResponse[Tax].model_validate(raw)
