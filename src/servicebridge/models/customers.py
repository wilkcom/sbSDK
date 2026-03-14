from ._base import SBBaseModel


class Customer(SBBaseModel):
    Id: int | None = None
    FirstName: str | None = None
    LastName: str | None = None
    CompanyName: str | None = None
    Email: str | None = None
    Phone: str | None = None
    MobilePhone: str | None = None
    BranchId: int | None = None
    CustomerCategoryId: int | None = None
    IsActive: bool | None = None
    ExternalSystemId: str | None = None
    CreatedDate: str | None = None
    ModifiedDate: str | None = None
    CustomFields: list[dict] | None = None


class CustomerCreate(SBBaseModel):
    FirstName: str
    LastName: str | None = None
    CompanyName: str | None = None
    Email: str | None = None
    Phone: str | None = None
    MobilePhone: str | None = None
    BranchId: int | None = None
    CustomerCategoryId: int | None = None
    ExternalSystemId: str | None = None


class CustomerUpdate(SBBaseModel):
    FirstName: str | None = None
    LastName: str | None = None
    CompanyName: str | None = None
    Email: str | None = None
    Phone: str | None = None
    MobilePhone: str | None = None
    BranchId: int | None = None
    CustomerCategoryId: int | None = None
    ExternalSystemId: str | None = None


class PaymentCard(SBBaseModel):
    Id: int | None = None
    Last4: str | None = None
    CardType: str | None = None
    ExpirationMonth: int | None = None
    ExpirationYear: int | None = None
    IsDefault: bool | None = None


class PaymentBankAccount(SBBaseModel):
    Id: int | None = None
    AccountType: str | None = None
    Last4: str | None = None
    BankName: str | None = None
    IsDefault: bool | None = None
