from ._base import SBBaseModel


class Payment(SBBaseModel):
    Id: int | None = None
    CustomerId: int | None = None
    InvoiceId: int | None = None
    Amount: float | None = None
    PaymentDate: str | None = None
    PaymentMethodId: int | None = None
    PaymentMethod: str | None = None
    ReferenceNumber: str | None = None
    Notes: str | None = None
    ExternalSystemId: str | None = None
    CreatedDate: str | None = None
    ModifiedDate: str | None = None


class PaymentCreate(SBBaseModel):
    CustomerId: int
    InvoiceId: int | None = None
    Amount: float
    PaymentDate: str | None = None
    PaymentMethodId: int | None = None
    ReferenceNumber: str | None = None
    Notes: str | None = None
    ExternalSystemId: str | None = None


class PaymentUpdate(SBBaseModel):
    Amount: float | None = None
    PaymentDate: str | None = None
    PaymentMethodId: int | None = None
    ReferenceNumber: str | None = None
    Notes: str | None = None
    ExternalSystemId: str | None = None
