from ._base import SBBaseModel


class Contact(SBBaseModel):
    Id: int | None = None
    CustomerId: int | None = None
    LocationId: int | None = None
    FirstName: str | None = None
    LastName: str | None = None
    Email: str | None = None
    Phone: str | None = None
    PhoneExt: str | None = None
    MobilePhone: str | None = None
    IsPrimary: bool | None = None
    ExternalSystemId: str | None = None
    CreatedDate: str | None = None
    ModifiedDate: str | None = None


class ContactCreate(SBBaseModel):
    CustomerId: int | None = None
    LocationId: int | None = None
    FirstName: str
    LastName: str | None = None
    Email: str | None = None
    Phone: str | None = None
    PhoneExt: str | None = None
    MobilePhone: str | None = None
    IsPrimary: bool | None = None
    ExternalSystemId: str | None = None


class ContactUpdate(SBBaseModel):
    FirstName: str | None = None
    LastName: str | None = None
    Email: str | None = None
    Phone: str | None = None
    PhoneExt: str | None = None
    MobilePhone: str | None = None
    IsPrimary: bool | None = None
    ExternalSystemId: str | None = None
