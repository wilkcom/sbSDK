from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiListResponse
from ..models.terms import Term


class TermsResource(BaseResource):
    _path = Endpoints.TERMS

    async def list(self, **filters: Any) -> ApiListResponse[Term]:
        raw = await self._client.request("GET", self._path, params=filters or None)
        return ApiListResponse[Term].model_validate(raw)
