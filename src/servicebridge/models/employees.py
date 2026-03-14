from ._base import CustomFieldMap, SBBaseModel


class Employee(SBBaseModel):
    Id: int | None = None
    FirstName: str | None = None
    LastName: str | None = None
    Email: str | None = None
    Phone: str | None = None
    BranchId: int | None = None
    TeamId: int | None = None
    Status: str | None = None
    Type: str | None = None
    ExternalSystemId: str | None = None
    CreatedDate: str | None = None
    ModifiedDate: str | None = None
    CustomFields: CustomFieldMap | None = None
