from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict

T = TypeVar("T")


class SBBaseModel(BaseModel):
    """
    Base model for all ServiceBridge DTOs.
    - populate_by_name: accepts both alias (PascalCase) and field name (snake_case)
    - extra="allow": tolerates undocumented fields returned by the API
    """

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
        str_strip_whitespace=True,
    )


class ApiResponse(SBBaseModel, Generic[T]):
    """Envelope for single-item responses: {"Status": ..., "Data": {...}}"""

    Status: int | None = None
    Message: str | None = None
    Data: T | None = None


class ApiListResponse(SBBaseModel, Generic[T]):
    """Envelope for unpaginated list responses (small lookup tables)."""

    Status: int | None = None
    Message: str | None = None
    Data: list[T] = []


class ApiPagedListResponse(SBBaseModel, Generic[T]):
    """Envelope for paginated list responses."""

    Status: int | None = None
    Message: str | None = None
    Data: list[T] = []
    TotalCount: int | None = None
