from __future__ import annotations

from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiPagedListResponse, ApiResponse
from ..models.employees import Employee


class EmployeesResource(BaseResource):
    _path = Endpoints.EMPLOYEES

    async def list(self, **filters: Any) -> ApiPagedListResponse[Employee]:
        raw = await self._list(filters or None)
        return ApiPagedListResponse[Employee].model_validate(raw)

    async def batch_get(self, ids: list[int], *, include_custom_fields: bool = False) -> dict[int, Employee]:  # type: ignore[override]
        params: dict[str, Any] = {}
        if include_custom_fields:
            params["includeCustomFields"] = True
        return await super().batch_get(ids, params=params or None)

    async def get(self, employee_id: int, *, include_custom_fields: bool = False) -> ApiResponse[Employee]:
        params: dict[str, Any] = {}
        if include_custom_fields:
            params["includeCustomFields"] = True
        raw = await self._get(employee_id, params=params or None)
        return ApiResponse[Employee].model_validate(raw)
