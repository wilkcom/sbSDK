from ._base import SBBaseModel


class JobCategory(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    Description: str | None = None
    IsActive: bool | None = None
