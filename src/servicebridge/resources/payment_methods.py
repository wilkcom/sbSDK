from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiListResponse
from ..models.payment_methods import PaymentMethod


class PaymentMethodsResource(BaseResource):
    _path = Endpoints.PAYMENT_METHODS

    async def list(self, **filters: Any) -> ApiListResponse[PaymentMethod]:
        raw = await self._client.request("GET", self._path, params=filters or None)
        return ApiListResponse[PaymentMethod].model_validate(raw)
