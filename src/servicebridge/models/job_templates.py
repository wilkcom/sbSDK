from ._base import SBBaseModel


class JobTemplate(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    Description: str | None = None
    JobCategoryId: int | None = None
    IsActive: bool | None = None
