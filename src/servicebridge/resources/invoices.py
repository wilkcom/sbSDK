from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiPagedListResponse, ApiResponse
from ..models.invoices import Invoice, InvoiceCreate, InvoiceUpdate


class InvoicesResource(BaseResource):
    _path = Endpoints.INVOICES

    async def list(self, **filters: Any) -> ApiPagedListResponse[Invoice]:
        raw = await self._list(filters or None)
        return ApiPagedListResponse[Invoice].model_validate(raw)

    async def get(self, invoice_id: int) -> ApiResponse[Invoice]:
        raw = await self._get(invoice_id)
        return ApiResponse[Invoice].model_validate(raw)

    async def create(self, data: InvoiceCreate) -> ApiResponse[Invoice]:
        raw = await self._create(data.model_dump(exclude_none=True))
        return ApiResponse[Invoice].model_validate(raw)

    async def update(self, invoice_id: int, data: InvoiceUpdate) -> ApiResponse[Invoice]:
        raw = await self._update(invoice_id, data.model_dump(exclude_none=True))
        return ApiResponse[Invoice].model_validate(raw)

    async def delete(self, invoice_id: int) -> ApiResponse[None]:
        raw = await self._delete(invoice_id)
        return ApiResponse[None].model_validate(raw)
