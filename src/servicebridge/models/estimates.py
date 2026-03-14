from ._base import SBBaseModel


class Estimate(SBBaseModel):
    Id: int | None = None
    CustomerId: int | None = None
    LocationId: int | None = None
    Status: str | None = None
    TotalAmount: float | None = None
    BranchId: int | None = None
    TeamId: int | None = None
    JobCategoryId: int | None = None
    AssignedTo: int | None = None
    Notes: str | None = None
    ExternalSystemId: str | None = None
    CreatedDate: str | None = None
    ModifiedDate: str | None = None


class EstimateCreate(SBBaseModel):
    CustomerId: int
    LocationId: int | None = None
    BranchId: int | None = None
    TeamId: int | None = None
    JobCategoryId: int | None = None
    AssignedTo: int | None = None
    Notes: str | None = None
    ExternalSystemId: str | None = None


class EstimateUpdate(SBBaseModel):
    LocationId: int | None = None
    BranchId: int | None = None
    TeamId: int | None = None
    JobCategoryId: int | None = None
    AssignedTo: int | None = None
    Notes: str | None = None
    ExternalSystemId: str | None = None


class EstimateWon(SBBaseModel):
    Notes: str | None = None


class EstimateLost(SBBaseModel):
    Reason: str | None = None
    Notes: str | None = None


class EstimateReopen(SBBaseModel):
    Notes: str | None = None


class EstimateDuplicate(SBBaseModel):
    Notes: str | None = None


class EstimatePhoto(SBBaseModel):
    Id: int | None = None
    EstimateId: int | None = None
    Url: str | None = None
    Description: str | None = None
    PhotoType: str | None = None
    ExternalSystemId: str | None = None
    CreatedDate: str | None = None


class EstimateDocument(SBBaseModel):
    Id: int | None = None
    EstimateId: int | None = None
    Url: str | None = None
    Name: str | None = None
    Description: str | None = None
    ExternalSystemId: str | None = None
    ShowInCustomerPortal: bool | None = None
    CreatedDate: str | None = None
