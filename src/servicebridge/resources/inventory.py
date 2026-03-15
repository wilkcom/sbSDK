from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiListResponse, ApiPagedListResponse, ApiResponse
from ..models.inventory import (
    InventoryChargeType,
    InventoryChargeTypeCreate,
    InventoryChargeTypeUpdate,
    InventoryGroup,
    InventoryGroupCreate,
    InventoryGroupUpdate,
    InventoryItem,
    InventoryProductCreate,
    InventoryProductUpdate,
    InventoryServiceCreate,
    InventoryServiceUpdate,
    InventoryUnit,
    InventoryUnitCreate,
)

if TYPE_CHECKING:
    from .._client import APIClient


class InventoryProductsResource:
    def __init__(self, client: "APIClient") -> None:
        self._client = client

    async def create(self, data: InventoryProductCreate) -> ApiResponse[InventoryItem]:
        raw = await self._client.request("POST", Endpoints.INVENTORY_PRODUCTS, json=data.model_dump(exclude_none=True))
        return ApiResponse[InventoryItem].model_validate(raw)

    async def update(self, product_id: int, data: InventoryProductUpdate) -> ApiResponse[InventoryItem]:
        raw = await self._client.request("PUT", f"{Endpoints.INVENTORY_PRODUCTS}/{product_id}", json=data.model_dump(exclude_none=True))
        return ApiResponse[InventoryItem].model_validate(raw)


class InventoryServicesResource:
    def __init__(self, client: "APIClient") -> None:
        self._client = client

    async def create(self, data: InventoryServiceCreate) -> ApiResponse[InventoryItem]:
        raw = await self._client.request("POST", Endpoints.INVENTORY_SERVICES, json=data.model_dump(exclude_none=True))
        return ApiResponse[InventoryItem].model_validate(raw)

    async def update(self, service_id: int, data: InventoryServiceUpdate) -> ApiResponse[InventoryItem]:
        raw = await self._client.request("PUT", f"{Endpoints.INVENTORY_SERVICES}/{service_id}", json=data.model_dump(exclude_none=True))
        return ApiResponse[InventoryItem].model_validate(raw)


class InventoryChargeTypesResource:
    def __init__(self, client: "APIClient") -> None:
        self._client = client

    async def list(self) -> ApiListResponse[InventoryChargeType]:
        raw = await self._client.request("GET", Endpoints.INVENTORY_CHARGE_TYPES)
        return ApiListResponse[InventoryChargeType].model_validate(raw)

    async def create(self, data: InventoryChargeTypeCreate) -> ApiResponse[InventoryChargeType]:
        raw = await self._client.request("POST", Endpoints.INVENTORY_CHARGE_TYPES, json=data.model_dump(exclude_none=True))
        return ApiResponse[InventoryChargeType].model_validate(raw)

    async def update(self, charge_type_id: int, data: InventoryChargeTypeUpdate) -> ApiResponse[InventoryChargeType]:
        raw = await self._client.request("PUT", f"{Endpoints.INVENTORY_CHARGE_TYPES}/{charge_type_id}", json=data.model_dump(exclude_none=True))
        return ApiResponse[InventoryChargeType].model_validate(raw)

    async def delete(self, charge_type_id: int) -> ApiResponse[None]:
        raw = await self._client.request("DELETE", f"{Endpoints.INVENTORY_CHARGE_TYPES}/{charge_type_id}")
        return ApiResponse[None].model_validate(raw)


class InventoryGroupsResource:
    def __init__(self, client: "APIClient") -> None:
        self._client = client

    async def list(self) -> ApiListResponse[InventoryGroup]:
        raw = await self._client.request("GET", Endpoints.INVENTORY_GROUPS)
        return ApiListResponse[InventoryGroup].model_validate(raw)

    async def create(self, data: InventoryGroupCreate) -> ApiResponse[InventoryGroup]:
        raw = await self._client.request("POST", Endpoints.INVENTORY_GROUPS, json=data.model_dump(exclude_none=True))
        return ApiResponse[InventoryGroup].model_validate(raw)

    async def update(self, group_id: int, data: InventoryGroupUpdate) -> ApiResponse[InventoryGroup]:
        raw = await self._client.request("PUT", f"{Endpoints.INVENTORY_GROUPS}/{group_id}", json=data.model_dump(exclude_none=True))
        return ApiResponse[InventoryGroup].model_validate(raw)

    async def delete(self, group_id: int) -> ApiResponse[None]:
        raw = await self._client.request("DELETE", f"{Endpoints.INVENTORY_GROUPS}/{group_id}")
        return ApiResponse[None].model_validate(raw)


class InventoryUnitsResource:
    def __init__(self, client: "APIClient") -> None:
        self._client = client

    async def list(self) -> ApiListResponse[InventoryUnit]:
        raw = await self._client.request("GET", Endpoints.INVENTORY_UNITS)
        return ApiListResponse[InventoryUnit].model_validate(raw)

    async def create(self, data: InventoryUnitCreate) -> ApiResponse[InventoryUnit]:
        raw = await self._client.request("POST", Endpoints.INVENTORY_UNITS, json=data.model_dump(exclude_none=True))
        return ApiResponse[InventoryUnit].model_validate(raw)

    async def delete(self, unit_id: int) -> ApiResponse[None]:
        raw = await self._client.request("DELETE", f"{Endpoints.INVENTORY_UNITS}/{unit_id}")
        return ApiResponse[None].model_validate(raw)


class InventoryResource(BaseResource):
    _path = Endpoints.INVENTORY

    def __init__(self, client: "APIClient") -> None:
        super().__init__(client)
        self.products = InventoryProductsResource(client)
        self.services = InventoryServicesResource(client)
        self.charge_types = InventoryChargeTypesResource(client)
        self.groups = InventoryGroupsResource(client)
        self.units = InventoryUnitsResource(client)

    async def list(self, **filters: Any) -> ApiPagedListResponse[InventoryItem]:
        raw = await self._list(filters or None)
        return ApiPagedListResponse[InventoryItem].model_validate(raw)

    async def batch_get(self, ids: list[int], *, include_custom_fields: bool = False) -> dict[int, InventoryItem]:  # type: ignore[override]
        params: dict[str, Any] = {}
        if include_custom_fields:
            params["includeCustomFields"] = "True"
        return await super().batch_get(ids, params=params or None)

    async def get(self, inventory_id: int, *, include_custom_fields: bool = False) -> ApiResponse[InventoryItem]:
        params: dict[str, Any] = {}
        if include_custom_fields:
            params["includeCustomFields"] = "True"
        raw = await self._get(inventory_id, params=params or None)
        return ApiResponse[InventoryItem].model_validate(raw)

    async def delete(self, inventory_id: int) -> ApiResponse[None]:
        raw = await self._delete(inventory_id)
        return ApiResponse[None].model_validate(raw)
