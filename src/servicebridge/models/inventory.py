from ._base import CustomFieldMap, SBBaseModel


class InventoryItem(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    Description: str | None = None
    Type: str | None = None  # "Product" or "Service"
    UnitPrice: float | None = None
    Cost: float | None = None
    GroupId: int | None = None
    ChargeTypeId: int | None = None
    UnitId: int | None = None
    IsActive: bool | None = None
    ExternalSystemId: str | None = None
    CreatedDate: str | None = None
    ModifiedDate: str | None = None
    CustomFields: CustomFieldMap | None = None


class InventoryProductCreate(SBBaseModel):
    Name: str
    Description: str | None = None
    UnitPrice: float | None = None
    Cost: float | None = None
    GroupId: int | None = None
    ChargeTypeId: int | None = None
    UnitId: int | None = None
    ExternalSystemId: str | None = None


class InventoryProductUpdate(SBBaseModel):
    Name: str | None = None
    Description: str | None = None
    UnitPrice: float | None = None
    Cost: float | None = None
    GroupId: int | None = None
    ChargeTypeId: int | None = None
    UnitId: int | None = None
    ExternalSystemId: str | None = None


class InventoryServiceCreate(SBBaseModel):
    Name: str
    Description: str | None = None
    UnitPrice: float | None = None
    Cost: float | None = None
    GroupId: int | None = None
    ChargeTypeId: int | None = None
    UnitId: int | None = None
    ExternalSystemId: str | None = None


class InventoryServiceUpdate(SBBaseModel):
    Name: str | None = None
    Description: str | None = None
    UnitPrice: float | None = None
    Cost: float | None = None
    GroupId: int | None = None
    ChargeTypeId: int | None = None
    UnitId: int | None = None
    ExternalSystemId: str | None = None


class InventoryChargeType(SBBaseModel):
    Id: int | None = None
    Name: str | None = None


class InventoryChargeTypeCreate(SBBaseModel):
    Name: str


class InventoryChargeTypeUpdate(SBBaseModel):
    Name: str | None = None


class InventoryGroup(SBBaseModel):
    Id: int | None = None
    Name: str | None = None


class InventoryGroupCreate(SBBaseModel):
    Name: str


class InventoryGroupUpdate(SBBaseModel):
    Name: str | None = None


class InventoryUnit(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    Abbreviation: str | None = None


class InventoryUnitCreate(SBBaseModel):
    Name: str
    Abbreviation: str | None = None
