# Changelog

All notable changes to this project are documented here.

---

## [0.1.4] — 2026-03-14

### Added
- `BaseResource.batch_get(ids)` — fetch multiple records by ID concurrently on any resource. Deduplicates IDs, fires all requests in parallel via `asyncio.gather`, and returns `dict[id, model]`. Rate limiting is handled automatically.
- `Enriched` wrapper class — overlay full fetched models onto any SDK result to enable chained access like `wo.Customer.CustomFields.get("Paid")`. Works for any resource pair and supports multiple enrichments per object.

### Example
```python
from servicebridge import ServiceBridgeClient, Enriched

async with ServiceBridgeClient() as client:
    wos = await client.work_orders.list()
    customer_ids = [wo.Customer.Id for wo in wos.Data if wo.Customer]
    customers = await client.customers.batch_get(customer_ids)

    enriched = [
        Enriched(wo, Customer=customers.get(wo.Customer.Id) if wo.Customer else None)
        for wo in wos.Data
    ]
    for wo in enriched:
        print(wo.WorkOrderNumber, wo.Customer.CustomFields.get("Paid"))
```

---

## [0.1.3] — 2026-03-14

### Changed
- `CustomFieldMap` updated to use the original field name as the key (no longer strips spaces). Access fields using their exact API name: `customer.CustomFields.get("Old Meter No")` or `customer.CustomFields["Old Meter No"]`.
- Author updated to Wilkcom in package metadata.

---

## [0.1.2] — 2026-03-14

### Added
- `WorkOrder` model fully expanded to match the complete API v4.5 response structure. Previously only 15 flat fields; now includes all nested objects and lists:
  - Nested objects: `Customer`, `Location`, `Branch`, `Contact`, `BillingContact`, `JobCategory`, `SalesRepresentative`, `Vehicle`, `Scheduler`, `GeoCoordinates`, `ServiceAgreement`, and more.
  - Nested lists: `WorkOrderLines`, `Visits`, `Documents`, `Skills`.
  - `Visits` includes `TeamMembers` with full employee details.
  - `Metadata` (CreatedBy, CreatedOn, UpdatedOn, etc.) on work order, visits, and documents.
  - `CustomFields: CustomFieldMap` for attribute-style access to custom fields.

---

## [0.1.1] — 2026-03-14

### Added
- `CustomFieldMap` — replaces `list[dict]` for `CustomFields` on `Customer`, `Employee`, and `InventoryItem` models. Provides `.get("Field Name")` and `["Field Name"]` access to custom fields without iterating the raw list.

---

## [0.1.0] — 2026-03-14

### Initial release

- Async Python SDK for the ServiceBridge field service management API v4.5.
- `ServiceBridgeClient` as the single public entry point with 31 resource clients.
- Auto-pagination: fetches all pages transparently (up to 500 records/page).
- Token-bucket rate limiter enforcing 50 req/s and 60,000 req/hr.
- Session token cached for 24 hours with automatic refresh.
- Typed Pydantic v2 response models for all resources.
- Nested sub-resources: `estimates.photos()`, `estimates.documents()`, `work_orders.photos()`, `inventory.products`, `inventory.services`, etc.
- Action endpoints: `estimates.mark_won()`, `mark_lost()`, `reopen()`, `duplicate()`.
- Typed exception hierarchy: `ServiceBridgeError`, `APIError`, `AuthenticationError`, `NotFoundError`, `RateLimitError`, `ConfigurationError`.
