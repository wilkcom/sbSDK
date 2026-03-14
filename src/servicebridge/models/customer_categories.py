from ._base import SBBaseModel


class CustomerCategory(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    Description: str | None = None


class CustomerCategoryCreate(SBBaseModel):
    Name: str
    Description: str | None = None
