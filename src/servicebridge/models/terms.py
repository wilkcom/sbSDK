from ._base import SBBaseModel


class Term(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    DueDays: int | None = None
    IsActive: bool | None = None
