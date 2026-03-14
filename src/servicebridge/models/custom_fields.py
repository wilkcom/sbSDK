from ._base import SBBaseModel


class CustomField(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    Type: str | None = None
    FieldType: str | None = None
    GroupId: int | None = None
    SortOrder: int | None = None
    IsRequired: bool | None = None
    DefaultValue: str | None = None


class CustomFieldCreate(SBBaseModel):
    Name: str
    Type: str
    FieldType: str
    GroupId: int | None = None
    SortOrder: int | None = None
    IsRequired: bool | None = None
    DefaultValue: str | None = None


class CustomFieldUpdate(SBBaseModel):
    Name: str | None = None
    SortOrder: int | None = None
    IsRequired: bool | None = None
    DefaultValue: str | None = None
