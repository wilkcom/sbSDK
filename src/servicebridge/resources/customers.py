from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiListResponse, ApiPagedListResponse, ApiResponse
from ..models.customers import Customer, CustomerCreate, CustomerUpdate, PaymentBankAccount, PaymentCard


class CustomersResource(BaseResource):
    _path = Endpoints.CUSTOMERS

    async def list(self, **filters: Any) -> ApiPagedListResponse[Customer]:
        raw = await self._list(filters or None)
        return ApiPagedListResponse[Customer].model_validate(raw)

    async def get(self, customer_id: int, *, include_custom_fields: bool = False) -> ApiResponse[Customer]:
        params: dict[str, Any] = {}
        if include_custom_fields:
            params["includeCustomFields"] = True
        raw = await self._get(customer_id, params=params or None)
        return ApiResponse[Customer].model_validate(raw)

    async def create(self, data: CustomerCreate) -> ApiResponse[Customer]:
        raw = await self._create(data.model_dump(exclude_none=True))
        return ApiResponse[Customer].model_validate(raw)

    async def update(self, customer_id: int, data: CustomerUpdate) -> ApiResponse[Customer]:
        raw = await self._update(customer_id, data.model_dump(exclude_none=True))
        return ApiResponse[Customer].model_validate(raw)

    async def delete(self, customer_id: int) -> ApiResponse[None]:
        raw = await self._delete(customer_id)
        return ApiResponse[None].model_validate(raw)

    async def make_active(self, customer_id: int) -> ApiResponse[None]:
        raw = await self._client.request("PUT", Endpoints.customer_make_active(customer_id))
        return ApiResponse[None].model_validate(raw)

    async def payment_cards(self, customer_id: int) -> ApiListResponse[PaymentCard]:
        raw = await self._client.request("GET", Endpoints.customer_payment_cards(customer_id))
        return ApiListResponse[PaymentCard].model_validate(raw)

    async def payment_bank_accounts(self, customer_id: int) -> ApiListResponse[PaymentBankAccount]:
        raw = await self._client.request("GET", Endpoints.customer_payment_bank_accounts(customer_id))
        return ApiListResponse[PaymentBankAccount].model_validate(raw)
