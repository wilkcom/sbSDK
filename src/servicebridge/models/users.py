from ._base import SBBaseModel


class User(SBBaseModel):
    Id: int | None = None
    FirstName: str | None = None
    LastName: str | None = None
    Email: str | None = None
    Username: str | None = None
    Role: str | None = None
    IsActive: bool | None = None
    CreatedDate: str | None = None
    ModifiedDate: str | None = None
