from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiPagedListResponse, ApiResponse
from ..models.payments import Payment, PaymentCreate, PaymentUpdate


class PaymentsResource(BaseResource):
    _path = Endpoints.PAYMENTS

    async def list(self, **filters: Any) -> ApiPagedListResponse[Payment]:
        raw = await self._list(filters or None)
        return ApiPagedListResponse[Payment].model_validate(raw)

    async def get(self, payment_id: int) -> ApiResponse[Payment]:
        raw = await self._get(payment_id)
        return ApiResponse[Payment].model_validate(raw)

    async def create(self, data: PaymentCreate) -> ApiResponse[Payment]:
        raw = await self._create(data.model_dump(exclude_none=True))
        return ApiResponse[Payment].model_validate(raw)

    async def update(self, payment_id: int, data: PaymentUpdate) -> ApiResponse[Payment]:
        raw = await self._update(payment_id, data.model_dump(exclude_none=True))
        return ApiResponse[Payment].model_validate(raw)

    async def delete(self, payment_id: int) -> ApiResponse[None]:
        raw = await self._delete(payment_id)
        return ApiResponse[None].model_validate(raw)
