from ._base import SBBaseModel


class Statistic(SBBaseModel):
    Name: str | None = None
    Value: float | None = None
    Period: str | None = None
