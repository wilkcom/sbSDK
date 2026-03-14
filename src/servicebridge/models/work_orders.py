from ._base import CustomFieldMap, SBBaseModel


class WorkOrderMetadata(SBBaseModel):
    CreatedBy: str | None = None
    CreatedOn: str | None = None
    UpdatedOn: str | None = None
    UpdatedBy: str | None = None
    Version: int | None = None
    IsDeleted: bool | None = None


class WorkOrderRef(SBBaseModel):
    """Generic {Id, Name} reference — reused for Branch, Location, Vehicle, etc."""
    Id: int | None = None
    Name: str | None = None


class WorkOrderCustomerRef(WorkOrderRef):
    Inactive: bool | None = None


class WorkOrderContact(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    Email: str | None = None
    Phone: str | None = None
    CellPhone: str | None = None


class WorkOrderScheduler(SBBaseModel):
    SchedulerId: int | None = None
    SchedulerNumber: str | None = None
    ScheduleType: str | None = None


class WorkOrderGeoCoordinates(SBBaseModel):
    Latitude: float | None = None
    Longitude: float | None = None


class WorkOrderLineInventory(SBBaseModel):
    SKU: str | None = None
    Type: str | None = None
    Id: int | None = None
    Name: str | None = None


class WorkOrderLine(SBBaseModel):
    Id: int | None = None
    ParentId: int | None = None
    Inventory: WorkOrderLineInventory | None = None
    Price: float | None = None
    PriceBeforeServiceAgreement: float | None = None
    Quantity: float | None = None
    Description: str | None = None
    IsTaxable: bool | None = None
    Tax: WorkOrderRef | None = None
    Asset: WorkOrderRef | None = None


class WorkOrderDocument(SBBaseModel):
    Id: int | None = None
    WorkOrderId: int | None = None
    Name: str | None = None
    Description: str | None = None
    Url: str | None = None
    ShowInCustomerPortal: bool | None = None
    ExternalSystemId: str | None = None
    Metadata: WorkOrderMetadata | None = None


class WorkOrderTeamMember(SBBaseModel):
    EmployeeId: int | None = None
    UserId: int | None = None
    FirstName: str | None = None
    LastName: str | None = None
    Email: str | None = None
    Title: str | None = None
    IsAdditionalEmployee: bool | None = None


class WorkOrderVisit(SBBaseModel):
    Id: int | None = None
    Date: str | None = None
    Time: int | None = None
    EstimatedDuration: int | None = None
    ActualDuration: int | None = None
    TotalLaborDuration: int | None = None
    ArrivalWindow: int | None = None
    Team: WorkOrderRef | None = None
    TeamMembers: list[WorkOrderTeamMember] = []
    Status: str | None = None
    Number: int | None = None
    ExternalSystemId: str | None = None
    Metadata: WorkOrderMetadata | None = None


class WorkOrder(SBBaseModel):
    FsmAccount: int | None = None
    Id: int | None = None
    WorkOrderNumber: str | None = None
    Scheduler: WorkOrderScheduler | None = None
    Customer: WorkOrderCustomerRef | None = None
    Location: WorkOrderRef | None = None
    GeoCoordinates: WorkOrderGeoCoordinates | None = None
    CoordinatesCaptured: bool | None = None
    Contact: WorkOrderContact | None = None
    ThirdPartyBillPayer: WorkOrderRef | None = None
    BillingLocation: WorkOrderRef | None = None
    BillingContact: WorkOrderContact | None = None
    IsMarketingCampaignSetByLead: bool | None = None
    MarketingCampaign: WorkOrderRef | None = None
    JobCategory: WorkOrderRef | None = None
    SalesRepresentative: WorkOrderRef | None = None
    Description: str | None = None
    Status: str | None = None
    IsInvoiced: bool | None = None
    Branch: WorkOrderRef | None = None
    Vehicle: WorkOrderRef | None = None
    ConfirmationStatus: str | None = None
    WorkOrderDate: str | None = None
    DateFinished: str | None = None
    ActualDuration: int | None = None
    TotalLaborDuration: int | None = None
    DefaultAsset: WorkOrderRef | None = None
    EarliestArrival: int | None = None
    LatestDeparture: int | None = None
    Notes: str | None = None
    PrivateNotes: str | None = None
    InvoiceNotes: str | None = None
    ReminderType: str | None = None
    ReminderValue: int | None = None
    ReminderMessage: str | None = None
    TaxCalculation: str | None = None
    WorkOrderLines: list[WorkOrderLine] = []
    CustomFields: CustomFieldMap | None = None
    Documents: list[WorkOrderDocument] = []
    Visits: list[WorkOrderVisit] = []
    Skills: list[WorkOrderRef] = []
    TotalVisitsCount: int | None = None
    ServiceAgreement: WorkOrderRef | None = None
    Metadata: WorkOrderMetadata | None = None
    ExternalSystemId: str | None = None


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
