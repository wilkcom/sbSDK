from ._base import BaseResource
from ..models._base import ApiListResponse
from ..models.accounting import AccountingAccount
from .._constants import Endpoints


class AccountingResource(BaseResource):
    _path = Endpoints.ACCOUNTING_ACCOUNTS

    async def list_accounts(self, *, fsm_account: str | None = None) -> ApiListResponse[AccountingAccount]:
        params = {}
        if fsm_account:
            params["fsmAccount"] = fsm_account
        raw = await self._client.request("GET", self._path, params=params or None)
        return ApiListResponse[AccountingAccount].model_validate(raw)
