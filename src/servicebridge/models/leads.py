from ._base import SBBaseModel


class Lead(SBBaseModel):
    Id: int | None = None
    FirstName: str | None = None
    LastName: str | None = None
    CompanyName: str | None = None
    Email: str | None = None
    Phone: str | None = None
    Status: str | None = None
    Source: str | None = None
    AssignedTo: int | None = None
    Notes: str | None = None
    ExternalSystemId: str | None = None
    CreatedDate: str | None = None
    ModifiedDate: str | None = None


class LeadCreate(SBBaseModel):
    FirstName: str
    LastName: str | None = None
    CompanyName: str | None = None
    Email: str | None = None
    Phone: str | None = None
    Source: str | None = None
    AssignedTo: int | None = None
    Notes: str | None = None
    ExternalSystemId: str | None = None


class LeadUpdate(SBBaseModel):
    FirstName: str | None = None
    LastName: str | None = None
    CompanyName: str | None = None
    Email: str | None = None
    Phone: str | None = None
    Status: str | None = None
    Source: str | None = None
    AssignedTo: int | None = None
    Notes: str | None = None
    ExternalSystemId: str | None = None
