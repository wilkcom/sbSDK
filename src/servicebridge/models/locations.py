from ._base import SBBaseModel


class Location(SBBaseModel):
    Id: int | None = None
    CustomerId: int | None = None
    Name: str | None = None
    Address: str | None = None
    Address2: str | None = None
    City: str | None = None
    State: str | None = None
    Zip: str | None = None
    Country: str | None = None
    Phone: str | None = None
    Email: str | None = None
    IsActive: bool | None = None
    ExternalSystemId: str | None = None
    CreatedDate: str | None = None
    ModifiedDate: str | None = None


class LocationCreate(SBBaseModel):
    CustomerId: int
    Name: str | None = None
    Address: str | None = None
    Address2: str | None = None
    City: str | None = None
    State: str | None = None
    Zip: str | None = None
    Country: str | None = None
    Phone: str | None = None
    Email: str | None = None
    ExternalSystemId: str | None = None


class LocationUpdate(SBBaseModel):
    Name: str | None = None
    Address: str | None = None
    Address2: str | None = None
    City: str | None = None
    State: str | None = None
    Zip: str | None = None
    Country: str | None = None
    Phone: str | None = None
    Email: str | None = None
    ExternalSystemId: str | None = None
