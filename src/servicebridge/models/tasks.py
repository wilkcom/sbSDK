from ._base import SBBaseModel


class Task(SBBaseModel):
    Id: int | None = None
    JobId: int | None = None
    CustomerId: int | None = None
    Title: str | None = None
    Description: str | None = None
    Status: str | None = None
    AssignedTo: int | None = None
    DueDate: str | None = None
    CompletedDate: str | None = None
    ExternalSystemId: str | None = None
    CreatedDate: str | None = None
    ModifiedDate: str | None = None


class TaskCreate(SBBaseModel):
    JobId: int | None = None
    CustomerId: int | None = None
    Title: str
    Description: str | None = None
    AssignedTo: int | None = None
    DueDate: str | None = None
    ExternalSystemId: str | None = None


class TaskUpdate(SBBaseModel):
    Title: str | None = None
    Description: str | None = None
    Status: str | None = None
    AssignedTo: int | None = None
    DueDate: str | None = None
    ExternalSystemId: str | None = None
