from ._base import SBBaseModel


class MarketingCampaign(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    CategoryId: int | None = None
    IsActive: bool | None = None
