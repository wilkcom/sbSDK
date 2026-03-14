from ._base import SBBaseModel


class Team(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    BranchId: int | None = None
    IsActive: bool | None = None
