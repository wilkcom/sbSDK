from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiListResponse
from ..models.job_templates import JobTemplate


class JobTemplatesResource(BaseResource):
    _path = Endpoints.JOB_TEMPLATES

    async def list(self, **filters: Any) -> ApiListResponse[JobTemplate]:
        raw = await self._client.request("GET", self._path, params=filters or None)
        return ApiListResponse[JobTemplate].model_validate(raw)
