from __future__ import annotations

from typing import Any


class Enriched:
    """
    Generic wrapper that overlays extra fields on top of any SDK model.

    Attribute lookups check the overlay dict first, then fall through to the
    underlying base model. This lets you replace a stub reference
    (e.g. WorkOrderCustomerRef with Id+Name only) with a full fetched model
    (Customer with all fields + CustomFields) while keeping every other field
    on the base model accessible as normal.

    Usage:
        from servicebridge import Enriched

        customers = await client.customers.batch_get(customer_ids)
        enriched = [
            Enriched(wo, Customer=customers.get(wo.Customer.Id) if wo.Customer else None)
            for wo in wos.Data
        ]

        for wo in enriched:
            wo.WorkOrderNumber                      # falls through to WorkOrder
            wo.Branch.Name                          # falls through to WorkOrder
            wo.Customer.Email                       # full Customer model
            wo.Customer.CustomFields.get("Paid")    # custom field access
    """

    __slots__ = ("_base", "_overlay")

    def __init__(self, base: Any, **overlay: Any) -> None:
        object.__setattr__(self, "_base", base)
        object.__setattr__(self, "_overlay", overlay)

    def __getattr__(self, name: str) -> Any:
        overlay = object.__getattribute__(self, "_overlay")
        if name in overlay:
            return overlay[name]
        return getattr(object.__getattribute__(self, "_base"), name)

    def __repr__(self) -> str:
        base = object.__getattribute__(self, "_base")
        overlay = object.__getattribute__(self, "_overlay")
        return f"Enriched({base!r}, fields={list(overlay.keys())})"
