from ._base import SBBaseModel


class MarketingCategory(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    IsActive: bool | None = None
