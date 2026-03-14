from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiListResponse
from ..models.marketing_categories import MarketingCategory


class MarketingCategoriesResource(BaseResource):
    _path = Endpoints.MARKETING_CATEGORIES

    async def list(self, **filters: Any) -> ApiListResponse[MarketingCategory]:
        raw = await self._client.request("GET", self._path, params=filters or None)
        return ApiListResponse[MarketingCategory].model_validate(raw)
