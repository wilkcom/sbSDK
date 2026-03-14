from ._base import BaseResource
from .._constants import Endpoints
from ..models._base import ApiResponse
from ..models.customer_categories import CustomerCategory, CustomerCategoryCreate


class CustomerCategoriesResource(BaseResource):
    _path = Endpoints.CUSTOMER_CATEGORIES

    async def create(self, data: CustomerCategoryCreate) -> ApiResponse[CustomerCategory]:
        raw = await self._create(data.model_dump(exclude_none=True))
        return ApiResponse[CustomerCategory].model_validate(raw)
