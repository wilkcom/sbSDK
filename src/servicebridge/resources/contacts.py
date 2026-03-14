from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiPagedListResponse, ApiResponse
from ..models.contacts import Contact, ContactCreate, ContactUpdate


class ContactsResource(BaseResource):
    _path = Endpoints.CONTACTS

    async def list(self, **filters: Any) -> ApiPagedListResponse[Contact]:
        raw = await self._list(filters or None)
        return ApiPagedListResponse[Contact].model_validate(raw)

    async def get(self, contact_id: int) -> ApiResponse[Contact]:
        raw = await self._get(contact_id)
        return ApiResponse[Contact].model_validate(raw)

    async def create(self, data: ContactCreate) -> ApiResponse[Contact]:
        raw = await self._create(data.model_dump(exclude_none=True))
        return ApiResponse[Contact].model_validate(raw)

    async def update(self, contact_id: int, data: ContactUpdate) -> ApiResponse[Contact]:
        raw = await self._update(contact_id, data.model_dump(exclude_none=True))
        return ApiResponse[Contact].model_validate(raw)

    async def delete(self, contact_id: int) -> ApiResponse[None]:
        raw = await self._delete(contact_id)
        return ApiResponse[None].model_validate(raw)
