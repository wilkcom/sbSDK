from ._base import SBBaseModel


class Invoice(SBBaseModel):
    Id: int | None = None
    CustomerId: int | None = None
    LocationId: int | None = None
    JobId: int | None = None
    Status: str | None = None
    TotalAmount: float | None = None
    BalanceDue: float | None = None
    DueDate: str | None = None
    InvoiceDate: str | None = None
    Notes: str | None = None
    ExternalSystemId: str | None = None
    CreatedDate: str | None = None
    ModifiedDate: str | None = None


class InvoiceCreate(SBBaseModel):
    CustomerId: int
    LocationId: int | None = None
    JobId: int | None = None
    DueDate: str | None = None
    InvoiceDate: str | None = None
    Notes: str | None = None
    ExternalSystemId: str | None = None


class InvoiceUpdate(SBBaseModel):
    DueDate: str | None = None
    InvoiceDate: str | None = None
    Notes: str | None = None
    ExternalSystemId: str | None = None
