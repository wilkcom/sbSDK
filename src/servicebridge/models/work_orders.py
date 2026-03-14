from ._base import SBBaseModel


class WorkOrder(SBBaseModel):
    Id: int | None = None
    CustomerId: int | None = None
    LocationId: int | None = None
    Status: str | None = None
    TotalAmount: float | None = None
    BranchId: int | None = None
    TeamId: int | None = None
    JobCategoryId: int | None = None
    AssignedTo: int | None = None
    ScheduledDate: str | None = None
    CompletedDate: str | None = None
    Notes: str | None = None
    ExternalSystemId: str | None = None
    CreatedDate: str | None = None
    ModifiedDate: str | None = None


class WorkOrderCreate(SBBaseModel):
    CustomerId: int
    LocationId: int | None = None
    BranchId: int | None = None
    TeamId: int | None = None
    JobCategoryId: int | None = None
    AssignedTo: int | None = None
    ScheduledDate: str | None = None
    Notes: str | None = None
    ExternalSystemId: str | None = None


class WorkOrderUpdate(SBBaseModel):
    LocationId: int | None = None
    BranchId: int | None = None
    TeamId: int | None = None
    JobCategoryId: int | None = None
    AssignedTo: int | None = None
    ScheduledDate: str | None = None
    Notes: str | None = None
    ExternalSystemId: str | None = None


class WorkOrderPhoto(SBBaseModel):
    Id: int | None = None
    WorkOrderId: int | None = None
    Url: str | None = None
    Description: str | None = None
    PhotoType: str | None = None
    ExternalSystemId: str | None = None
    CreatedDate: str | None = None
