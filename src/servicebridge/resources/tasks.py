from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiPagedListResponse, ApiResponse
from ..models.tasks import Task, TaskCreate, TaskUpdate


class TasksResource(BaseResource):
    _path = Endpoints.TASKS

    async def list(self, **filters: Any) -> ApiPagedListResponse[Task]:
        raw = await self._list(filters or None)
        return ApiPagedListResponse[Task].model_validate(raw)

    async def get(self, task_id: int) -> ApiResponse[Task]:
        raw = await self._get(task_id)
        return ApiResponse[Task].model_validate(raw)

    async def create(self, data: TaskCreate) -> ApiResponse[Task]:
        raw = await self._create(data.model_dump(exclude_none=True))
        return ApiResponse[Task].model_validate(raw)

    async def update(self, task_id: int, data: TaskUpdate) -> ApiResponse[Task]:
        raw = await self._update(task_id, data.model_dump(exclude_none=True))
        return ApiResponse[Task].model_validate(raw)

    async def delete(self, task_id: int) -> ApiResponse[None]:
        raw = await self._delete(task_id)
        return ApiResponse[None].model_validate(raw)
