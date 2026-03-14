from ._base import SBBaseModel


class Company(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    Phone: str | None = None
    Email: str | None = None
    Website: str | None = None
    Address: str | None = None
    City: str | None = None
    State: str | None = None
    Zip: str | None = None
