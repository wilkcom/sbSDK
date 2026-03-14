from ._base import SBBaseModel


class ActivityNote(SBBaseModel):
    Id: int | None = None
    CustomerId: int | None = None
    LocationId: int | None = None
    JobId: int | None = None
    InvoiceId: int | None = None
    PaymentId: int | None = None
    Note: str | None = None
    ActivityNoteTypeId: int | None = None
    ActivityNoteType: str | None = None
    CreatedDate: str | None = None
    ModifiedDate: str | None = None
    ExternalSystemId: str | None = None


class ActivityNoteCreate(SBBaseModel):
    CustomerId: int | None = None
    LocationId: int | None = None
    JobId: int | None = None
    InvoiceId: int | None = None
    PaymentId: int | None = None
    Note: str
    ActivityNoteTypeId: int | None = None
    ExternalSystemId: str | None = None


class ActivityNoteUpdate(SBBaseModel):
    Note: str | None = None
    ActivityNoteTypeId: int | None = None
    ExternalSystemId: str | None = None
