from pydantic import Field
from ._base import SBBaseModel


class AccountingAccount(SBBaseModel):
    Id: int | None = None
    Name: str | None = None
    AccountNumber: str | None = None
    FsmAccount: str | None = None
