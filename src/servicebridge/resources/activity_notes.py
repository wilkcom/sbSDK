from typing import Any

from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiPagedListResponse, ApiResponse
from ..models.activity_note import ActivityNote, ActivityNoteCreate, ActivityNoteUpdate


class ActivityNotesResource(BaseResource):
    _path = Endpoints.ACTIVITY_NOTE

    async def list(self, **filters: Any) -> ApiPagedListResponse[ActivityNote]:
        raw = await self._list(filters or None)
        return ApiPagedListResponse[ActivityNote].model_validate(raw)

    async def get(self, activity_note_id: int) -> ApiResponse[ActivityNote]:
        raw = await self._get(activity_note_id)
        return ApiResponse[ActivityNote].model_validate(raw)

    async def create(self, data: ActivityNoteCreate) -> ApiResponse[ActivityNote]:
        raw = await self._create(data.model_dump(exclude_none=True))
        return ApiResponse[ActivityNote].model_validate(raw)

    async def update(self, activity_note_id: int, data: ActivityNoteUpdate) -> ApiResponse[ActivityNote]:
        raw = await self._update(activity_note_id, data.model_dump(exclude_none=True))
        return ApiResponse[ActivityNote].model_validate(raw)

    async def delete(self, activity_note_id: int) -> ApiResponse[None]:
        raw = await self._delete(activity_note_id)
        return ApiResponse[None].model_validate(raw)
