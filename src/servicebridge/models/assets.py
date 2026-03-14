from ._base import SBBaseModel


class Asset(SBBaseModel):
    Id: int | None = None
    CustomerId: int | None = None
    LocationId: int | None = None
    Name: str | None = None
    Make: str | None = None
    Model: str | None = None
    SerialNumber: str | None = None
    InstallDate: str | None = None
    WarrantyExpirationDate: str | None = None
    Notes: str | None = None
    ExternalSystemId: str | None = None
    CreatedDate: str | None = None
    ModifiedDate: str | None = None
