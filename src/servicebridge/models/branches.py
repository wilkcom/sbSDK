from ._base import SBBaseModel


class Branch(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    Address: str | None = None
    City: str | None = None
    State: str | None = None
    Zip: str | None = None
    Phone: str | None = None
    Email: str | None = None
    IsActive: bool | None = None
    CreatedDate: str | None = None
    ModifiedDate: str | None = None


class BranchCreate(SBBaseModel):
    Name: str
    Address: str | None = None
    City: str | None = None
    State: str | None = None
    Zip: str | None = None
    Phone: str | None = None
    Email: str | None = None


class BranchUpdate(SBBaseModel):
    Name: str | None = None
    Address: str | None = None
    City: str | None = None
    State: str | None = None
    Zip: str | None = None
    Phone: str | None = None
    Email: str | None = None
