from ._base import SBBaseModel


class CustomFieldGroup(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    Type: str | None = None
    SortOrder: int | None = None


class CustomFieldGroupCreate(SBBaseModel):
    Name: str
    Type: str
    SortOrder: int | None = None


class CustomFieldGroupUpdate(SBBaseModel):
    Name: str | None = None
    SortOrder: int | None = None
