# ServiceBridge Python SDK

An async Python SDK for the [ServiceBridge](https://cloud.servicebridge.com) field service management API v4.5.

## Features

- **Async-first** — built on `aiohttp`, fully `async`/`await`
- **Typed responses** — all responses are Pydantic models with IDE autocompletion
- **Auto-pagination** — large result sets are fetched automatically across pages
- **Rate limiting** — built-in token bucket enforcing 50 req/s and 60,000 req/hr
- **Token management** — session token cached for 24 hours, auto-refreshed on expiry
- **31 resource clients** — full coverage of the ServiceBridge v4.5 API

---

## Requirements

- Python 3.11+
- ServiceBridge API credentials (User ID + Password)

---

## Installation

```bash
pip install sbSDK
```

For development (editable install from source):

```bash
git clone https://github.com/wilkcom/sbSDK.git
cd sbSDK
pip install -e ".[dev]"
```

### Dependencies

| Package | Purpose |
|---|---|
| `aiohttp>=3.9` | Async HTTP client |
| `pydantic>=2.0` | Response models and validation |
| `python-dotenv>=1.0` | `.env` file support |

---

## Configuration

Credentials can be provided via environment variables or passed directly.

### Option 1 — Environment variables (recommended)

Copy `.env.example` to `.env` and fill in your credentials:

```
API_USER_ID=your_user_id
API_PASSWORD=your_password
```

The SDK loads `.env` automatically on import.

### Option 2 — Pass credentials directly

```python
client = ServiceBridgeClient(user_id="your_user_id", password="your_password")
```

---

## Quick Start

```python
import asyncio
from servicebridge import ServiceBridgeClient

async def main():
    async with ServiceBridgeClient() as client:
        # List all customers (auto-paginated)
        customers = await client.customers.list()
        for customer in customers.Data:
            print(customer.FirstName, customer.LastName)

asyncio.run(main())
```

Always use `ServiceBridgeClient` as an **async context manager** (`async with`). This ensures the underlying HTTP session is properly opened and closed.

If you need to manage the lifecycle manually:

```python
client = ServiceBridgeClient()
await client._api.__aenter__()
# ... do work ...
await client.close()
```

---

## Response Types

Every method returns a typed Pydantic envelope. There are three types:

| Type | Used for | Key fields |
|---|---|---|
| `ApiResponse[T]` | Single item (GET by id, POST, PUT) | `.Data` → one object |
| `ApiListResponse[T]` | Lookup/reference data | `.Data` → list of objects |
| `ApiPagedListResponse[T]` | Large entity lists | `.Data` → list, `.TotalCount` |

All response objects also have `.Status` (int) and `.Message` (str).

```python
result = await client.customers.get(customer_id=123)
print(result.Status)    # 200
print(result.Message)   # "OK"
print(result.Data)      # Customer object
print(result.Data.FirstName)
```

---

## Resource Reference

All resources are accessed as attributes on the client:

```python
async with ServiceBridgeClient() as client:
    client.customers
    client.work_orders
    client.invoices
    # etc.
```

### Standard CRUD pattern

Most resources support these methods:

```python
# List all (auto-paginated, returns all pages)
result = await client.{resource}.list()

# Get one by ID
result = await client.{resource}.get({resource}_id=123)

# Create
from servicebridge.models import {Name}Create
result = await client.{resource}.create({Name}Create(Field1="value", ...))

# Update (full replace — API uses PUT)
from servicebridge.models import {Name}Update
result = await client.{resource}.update({resource}_id=123, data={Name}Update(Field1="new"))

# Delete
result = await client.{resource}.delete({resource}_id=123)
```

---

## Resources

### Customers

```python
# List with optional filters
customers = await client.customers.list(
    nameFilter="Smith",
    branchFilter=5,
    includeInactiveCustomers=False,
    searchText="john",
)

# Get single customer (optionally with custom fields)
customer = await client.customers.get(customer_id=123, include_custom_fields=True)

# Create
from servicebridge.models import CustomerCreate
result = await client.customers.create(CustomerCreate(
    FirstName="Jane",
    LastName="Smith",
    Email="jane@example.com",
    Phone="555-1234",
))

# Update
from servicebridge.models import CustomerUpdate
result = await client.customers.update(123, CustomerUpdate(Email="new@example.com"))

# Delete
await client.customers.delete(customer_id=123)

# Reactivate an inactive customer
await client.customers.make_active(customer_id=123)

# Retrieve saved payment methods
cards = await client.customers.payment_cards(customer_id=123)
bank_accounts = await client.customers.payment_bank_accounts(customer_id=123)
```

---

### Work Orders

```python
work_orders = await client.work_orders.list(statusFilter="Open", branchFilter=2)
wo = await client.work_orders.get(work_order_id=456)

from servicebridge.models import WorkOrderCreate, WorkOrderUpdate
result = await client.work_orders.create(WorkOrderCreate(
    CustomerId=123,
    LocationId=10,
    ScheduledDate="2025-04-01",
))
await client.work_orders.update(456, WorkOrderUpdate(Notes="Updated note"))
await client.work_orders.delete(work_order_id=456)

# Photos sub-resource
photos = await client.work_orders.photos(work_order_id=456).list()

# Upload a photo
with open("photo.jpg", "rb") as f:
    result = await client.work_orders.photos(456).upload(
        file_content=f.read(),
        filename="photo.jpg",
        photo_type="Before",
        description="Before service",
    )
```

---

### Estimates

```python
estimates = await client.estimates.list(statusFilter="Open", customerFilter=123)
estimate = await client.estimates.get(estimate_id=789)

from servicebridge.models import EstimateCreate, EstimateWon, EstimateLost
result = await client.estimates.create(EstimateCreate(CustomerId=123))
await client.estimates.update(789, EstimateUpdate(Notes="Updated"))

# Status transitions
await client.estimates.mark_won(789, EstimateWon(Notes="Customer accepted"))
await client.estimates.mark_lost(789, EstimateLost(Reason="Price", Notes="Too expensive"))
await client.estimates.reopen(estimate_id=789)
new_id = await client.estimates.duplicate(estimate_id=789)

# Photos sub-resource
photos = await client.estimates.photos(estimate_id=789).list()
with open("photo.jpg", "rb") as f:
    await client.estimates.photos(789).upload(
        file_content=f.read(),
        filename="photo.jpg",
        photo_type="Before",
    )

# Documents sub-resource
docs = await client.estimates.documents(estimate_id=789).list()
with open("quote.pdf", "rb") as f:
    await client.estimates.documents(789).upload(
        file_content=f.read(),
        filename="quote.pdf",
        name="Quote v1",
        show_in_customer_portal=True,
    )
```

---

### Invoices

```python
invoices = await client.invoices.list(customerFilter=123, statusFilter="Unpaid")
invoice = await client.invoices.get(invoice_id=321)

from servicebridge.models import InvoiceCreate, InvoiceUpdate
result = await client.invoices.create(InvoiceCreate(
    CustomerId=123,
    DueDate="2025-05-01",
))
await client.invoices.update(321, InvoiceUpdate(Notes="Updated terms"))
await client.invoices.delete(invoice_id=321)
```

---

### Contacts

```python
contacts = await client.contacts.list(customerFilter=123, nameFilter="Jane")
contact = await client.contacts.get(contact_id=55)

from servicebridge.models import ContactCreate, ContactUpdate
result = await client.contacts.create(ContactCreate(
    CustomerId=123,
    FirstName="Jane",
    Email="jane@example.com",
    IsPrimary=True,
))
await client.contacts.update(55, ContactUpdate(Phone="555-9999"))
await client.contacts.delete(contact_id=55)
```

---

### Locations

```python
locations = await client.locations.list(customerId=123)
location = await client.locations.get(location_id=77)

from servicebridge.models import LocationCreate, LocationUpdate
result = await client.locations.create(LocationCreate(
    CustomerId=123,
    Address="123 Main St",
    City="Springfield",
    State="IL",
    Zip="62701",
))
await client.locations.update(77, LocationUpdate(City="Shelbyville"))
await client.locations.delete(location_id=77)
```

---

### Leads

```python
leads = await client.leads.list(statusFilter="New")
lead = await client.leads.get(lead_id=88)

from servicebridge.models import LeadCreate, LeadUpdate
result = await client.leads.create(LeadCreate(
    FirstName="Bob",
    Email="bob@example.com",
    Source="Website",
))
await client.leads.update(88, LeadUpdate(Status="Contacted"))
await client.leads.delete(lead_id=88)
```

---

### Payments

```python
payments = await client.payments.list(customerId=123)
payment = await client.payments.get(payment_id=99)

from servicebridge.models import PaymentCreate, PaymentUpdate
result = await client.payments.create(PaymentCreate(
    CustomerId=123,
    InvoiceId=321,
    Amount=250.00,
    PaymentMethodId=1,
))
await client.payments.update(99, PaymentUpdate(ReferenceNumber="CHK-1234"))
await client.payments.delete(payment_id=99)
```

---

### Inventory

Inventory has sub-resources for products, services, and lookup tables.

```python
# List all inventory items
items = await client.inventory.list(typeFilter="Product")
item = await client.inventory.get(inventory_id=10, include_custom_fields=True)
await client.inventory.delete(inventory_id=10)

# Products
from servicebridge.models import InventoryProductCreate, InventoryProductUpdate
result = await client.inventory.products.create(InventoryProductCreate(
    Name="Air Filter",
    UnitPrice=29.99,
    Cost=12.00,
))
await client.inventory.products.update(10, InventoryProductUpdate(UnitPrice=34.99))

# Services
from servicebridge.models import InventoryServiceCreate
result = await client.inventory.services.create(InventoryServiceCreate(
    Name="HVAC Tune-Up",
    UnitPrice=149.00,
))

# Charge Types
charge_types = await client.inventory.charge_types.list()
from servicebridge.models import InventoryChargeTypeCreate
await client.inventory.charge_types.create(InventoryChargeTypeCreate(Name="Labor"))
await client.inventory.charge_types.delete(charge_type_id=3)

# Groups
groups = await client.inventory.groups.list()
from servicebridge.models import InventoryGroupCreate
await client.inventory.groups.create(InventoryGroupCreate(Name="HVAC Parts"))

# Units
units = await client.inventory.units.list()
from servicebridge.models import InventoryUnitCreate
await client.inventory.units.create(InventoryUnitCreate(Name="Each", Abbreviation="ea"))
```

---

### Employees

```python
employees = await client.employees.list(statusFilter="Active", teamFilter=2)
employee = await client.employees.get(employee_id=5, include_custom_fields=True)
```

---

### Branches

```python
branches = await client.branches.list()
branch = await client.branches.get(branch_id=1)

from servicebridge.models import BranchCreate, BranchUpdate
result = await client.branches.create(BranchCreate(Name="North Branch", City="Springfield"))
await client.branches.update(1, BranchUpdate(Phone="555-0001"))
await client.branches.delete(branch_id=1)
```

---

### Tasks

```python
tasks = await client.tasks.list(jobId=456, statusFilter="Open")
task = await client.tasks.get(task_id=20)

from servicebridge.models import TaskCreate, TaskUpdate
result = await client.tasks.create(TaskCreate(
    JobId=456,
    Title="Replace filter",
    AssignedTo=5,
    DueDate="2025-04-15",
))
await client.tasks.update(20, TaskUpdate(Status="Completed"))
await client.tasks.delete(task_id=20)
```

---

### Activity Notes

```python
notes = await client.activity_notes.list(customerId=123)
note = await client.activity_notes.get(activity_note_id=30)

from servicebridge.models import ActivityNoteCreate, ActivityNoteUpdate
result = await client.activity_notes.create(ActivityNoteCreate(
    CustomerId=123,
    Note="Customer called to reschedule.",
))
await client.activity_notes.update(30, ActivityNoteUpdate(Note="Updated note"))
await client.activity_notes.delete(activity_note_id=30)
```

---

### Assets

```python
assets = await client.assets.list(customerId=123, locationId=77)
asset = await client.assets.get(asset_id=15)
```

---

### Custom Fields & Groups

```python
# type is required: "Customer", "Employee", "WorkOrder", etc.
fields = await client.custom_fields.list(type="Customer")
field = await client.custom_fields.get(field_id=4, type="Customer")

from servicebridge.models import CustomFieldCreate, CustomFieldUpdate
await client.custom_fields.create(CustomFieldCreate(
    Name="Account Number",
    Type="Customer",
    FieldType="Text",
))
await client.custom_fields.update(4, CustomFieldUpdate(IsRequired=True))
await client.custom_fields.delete(field_id=4, type="Customer")

# Groups follow the same pattern
groups = await client.custom_field_groups.list(type="Customer")
```

---

### Lookup / Reference Data

These resources are read-only and return small, unpaginated lists.

```python
companies = await client.companies.list()
teams = await client.teams.list()
taxes = await client.taxes.list()
terms = await client.terms.list()
payment_methods = await client.payment_methods.list()
job_categories = await client.job_categories.list()
job_templates = await client.job_templates.list()
marketing_campaigns = await client.marketing_campaigns.list()
marketing_categories = await client.marketing_categories.list()
sales_reps = await client.sales_representatives.list()
statistics = await client.statistics.list()
accounts = await client.accounting.list_accounts()
```

---

### Users

```python
users = await client.users.list()
user = await client.users.get(user_id=1)
```

---

### Reports

```python
report = await client.reports.get(reportType="Revenue", dateFrom="2025-01-01")
```

---

## Filtering and Query Parameters

All `list()` methods accept keyword arguments that are forwarded as query parameters. Use the parameter names from the [ServiceBridge API docs](https://cloud.servicebridge.com/developer/index):

```python
# Date range filter
estimates = await client.estimates.list(
    dateFromFilter="2025-01-01",
    dateToFilter="2025-03-31",
    statusFilter="Open",
    branchFilter=2,
    teamFilter=1,
)

# Change tracking (delta sync)
customers = await client.customers.list(changeTime="2025-03-01T00:00:00")

# Search by external system ID
employees = await client.employees.list(externalSystemId="ERP-001")
```

---

## Pagination

Pagination is **transparent**. When you call `list()`, the SDK automatically fetches all pages and returns the complete dataset — you never need to manage page numbers.

```python
# This fetches ALL customers across all pages automatically
all_customers = await client.customers.list()
print(f"Total: {len(all_customers.Data)}")
```

The API returns up to 500 records per page. The SDK detects when a page is full and continues fetching until all data is retrieved.

---

## Error Handling

The SDK raises typed exceptions for all error conditions:

```python
from servicebridge import (
    ServiceBridgeError,   # base class for all SDK errors
    APIError,             # non-2xx HTTP responses
    AuthenticationError,  # 401 after token refresh fails
    NotFoundError,        # 404
    RateLimitError,       # 429
    ConfigurationError,   # missing credentials at startup
)
```

### Example

```python
from servicebridge import NotFoundError, APIError, ServiceBridgeError

async with ServiceBridgeClient() as client:
    try:
        customer = await client.customers.get(customer_id=999999)

    except NotFoundError:
        print("Customer not found")

    except RateLimitError:
        print("Rate limit hit — slow down requests")

    except APIError as e:
        print(f"API error {e.status}: {e.message}")
        print(e.raw)   # full raw response dict

    except ServiceBridgeError as e:
        print(f"SDK error: {e}")
```

### Exception hierarchy

```
ServiceBridgeError
├── APIError(status, message, raw)
│   ├── AuthenticationError   # 401
│   ├── NotFoundError         # 404
│   └── RateLimitError        # 429
└── ConfigurationError        # missing credentials
```

---

## Rate Limiting

The SDK automatically enforces ServiceBridge API limits:

- **50 requests per second**
- **60,000 requests per hour**

A token-bucket algorithm is used. If your code sends requests faster than these limits, the SDK will automatically pause (using `asyncio.sleep`) until a slot is available. You do not need to implement any throttling yourself.

---

## Logging

The SDK uses Python's standard `logging` module under the `servicebridge` logger. To see debug output (token events, pagination progress):

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Or target just the SDK logger
logging.getLogger("servicebridge").setLevel(logging.DEBUG)
```

---

## Project Structure

```
src/servicebridge/
├── __init__.py          # ServiceBridgeClient — public entry point
├── _client.py           # HTTP session, token auth, error mapping
├── _constants.py        # All API endpoint paths (Endpoints class)
├── _pagination.py       # Auto-pagination logic
├── _rate_limiter.py     # Token-bucket rate limiter
├── exceptions.py        # Exception hierarchy
├── models/              # Pydantic response/request models
│   ├── _base.py         # ApiResponse[T], ApiListResponse[T], ApiPagedListResponse[T]
│   └── *.py             # One model file per resource
└── resources/           # Resource clients
    ├── _base.py         # BaseResource with shared HTTP helpers
    └── *.py             # One resource file per API resource
```

---

## Development

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Lint
ruff check src/

# Type check
mypy src/
```

---

## API Reference

Full ServiceBridge API documentation: [https://cloud.servicebridge.com/developer/index](https://cloud.servicebridge.com/developer/index)
