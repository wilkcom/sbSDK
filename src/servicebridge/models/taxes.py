from ._base import SBBaseModel


class Tax(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    Rate: float | None = None
    IsActive: bool | None = None
