from __future__ import annotations

from typing import Any, Generic, Iterator, TypeVar

from pydantic import BaseModel, ConfigDict
from pydantic_core import core_schema

T = TypeVar("T")


class CustomFieldMap:
    """Access for ServiceBridge custom fields.

    The API returns custom fields as a list of dicts:
        [{"Name": "Old Meter No", "Value": "12345"}, ...]

    This class provides access to custom fields:
        customer.CustomFields.get("Old Meter No", "default")
        customer.CustomFields["Old Meter No"]
        list(customer.CustomFields)  → raw list of dicts
    """

    def __init__(self, fields: list[dict[str, Any]]) -> None:
        self._raw: list[dict[str, Any]] = fields
        self._lookup: dict[str, str | None] = {
            f["Name"]: f.get("Value")
            for f in fields
            if "Name" in f
        }

    def __getitem__(self, key: str) -> str | None:
        return self._lookup[key]

    def get(self, name: str, default: str | None = None) -> str | None:
        return self._lookup.get(name, default)

    def __iter__(self) -> Iterator[dict[str, Any]]:
        return iter(self._raw)

    def __repr__(self) -> str:
        return f"CustomFieldMap({self._lookup})"

    # --- Pydantic v2 integration ---

    @classmethod
    def __get_pydantic_core_schema__(
        cls, _source_type: Any, _handler: Any
    ) -> core_schema.CoreSchema:
        return core_schema.no_info_plain_validator_function(
            cls._validate,
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda v: v._raw,
                info_arg=False,
            ),
        )

    @classmethod
    def _validate(cls, v: Any) -> "CustomFieldMap":
        if isinstance(v, cls):
            return v
        if isinstance(v, list):
            return cls(v)
        raise ValueError(f"Expected list of custom fields, got {type(v)}")


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
