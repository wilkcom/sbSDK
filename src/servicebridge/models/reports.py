from ._base import SBBaseModel


class Report(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    Type: str | None = None
    Data: dict | None = None
