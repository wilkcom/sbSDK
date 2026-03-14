from ._base import SBBaseModel


class SalesRepresentative(SBBaseModel):
    Id: int | None = None
    FirstName: str | None = None
    LastName: str | None = None
    Email: str | None = None
    IsActive: bool | None = None
