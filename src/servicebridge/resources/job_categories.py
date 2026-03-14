from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiListResponse
from ..models.job_categories import JobCategory


class JobCategoriesResource(BaseResource):
    _path = Endpoints.JOB_CATEGORIES

    async def list(self, **filters: Any) -> ApiListResponse[JobCategory]:
        raw = await self._client.request("GET", self._path, params=filters or None)
        return ApiListResponse[JobCategory].model_validate(raw)
