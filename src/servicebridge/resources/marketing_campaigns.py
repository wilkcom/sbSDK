from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiListResponse
from ..models.marketing_campaigns import MarketingCampaign


class MarketingCampaignsResource(BaseResource):
    _path = Endpoints.MARKETING_CAMPAIGNS

    async def list(self, **filters: Any) -> ApiListResponse[MarketingCampaign]:
        raw = await self._client.request("GET", self._path, params=filters or None)
        return ApiListResponse[MarketingCampaign].model_validate(raw)
