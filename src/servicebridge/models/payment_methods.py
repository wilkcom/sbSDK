from ._base import SBBaseModel


class PaymentMethod(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    IsActive: bool | None = None
