"""
ServiceBridge Python SDK — async client for the ServiceBridge API v4.5.

Usage:
    import asyncio
    from servicebridge import ServiceBridgeClient

    async def main():
        async with ServiceBridgeClient() as client:
            customers = await client.customers.list()
            for c in customers.Data:
                print(c.FirstName, c.LastName)

    asyncio.run(main())
"""

from ._client import APIClient
from .exceptions import (
    APIError,
    AuthenticationError,
    ConfigurationError,
    NotFoundError,
    RateLimitError,
    ServiceBridgeError,
)
from .resources import (
    AccountingResource,
    ActivityNotesResource,
    AssetsResource,
    BranchesResource,
    CompaniesResource,
    ContactsResource,
    CustomerCategoriesResource,
    CustomersResource,
    CustomFieldGroupsResource,
    CustomFieldsResource,
    EmployeesResource,
    EstimatesResource,
    InventoryResource,
    InvoicesResource,
    JobCategoriesResource,
    JobTemplatesResource,
    LeadsResource,
    LocationsResource,
    MarketingCampaignsResource,
    MarketingCategoriesResource,
    PaymentMethodsResource,
    PaymentsResource,
    ReportsResource,
    SalesRepresentativesResource,
    StatisticsResource,
    TasksResource,
    TaxesResource,
    TeamsResource,
    TermsResource,
    UsersResource,
    WorkOrdersResource,
)


class ServiceBridgeClient:
    """
    Main entry point for the ServiceBridge SDK.

    Always use as an async context manager so the underlying HTTP session
    is properly opened and closed:

        async with ServiceBridgeClient() as client:
            result = await client.customers.list()

    Credentials are read from environment variables API_USER_ID and
    API_PASSWORD, or passed directly:

        client = ServiceBridgeClient(user_id="...", password="...")
    """

    def __init__(
        self,
        user_id: str | None = None,
        password: str | None = None,
        base_url: str | None = None,
    ) -> None:
        kwargs: dict = {}
        if base_url:
            kwargs["base_url"] = base_url
        self._api = APIClient(user_id=user_id, password=password, **kwargs)

        self.accounting = AccountingResource(self._api)
        self.activity_notes = ActivityNotesResource(self._api)
        self.assets = AssetsResource(self._api)
        self.branches = BranchesResource(self._api)
        self.companies = CompaniesResource(self._api)
        self.contacts = ContactsResource(self._api)
        self.customer_categories = CustomerCategoriesResource(self._api)
        self.customers = CustomersResource(self._api)
        self.custom_field_groups = CustomFieldGroupsResource(self._api)
        self.custom_fields = CustomFieldsResource(self._api)
        self.employees = EmployeesResource(self._api)
        self.estimates = EstimatesResource(self._api)
        self.inventory = InventoryResource(self._api)
        self.invoices = InvoicesResource(self._api)
        self.job_categories = JobCategoriesResource(self._api)
        self.job_templates = JobTemplatesResource(self._api)
        self.leads = LeadsResource(self._api)
        self.locations = LocationsResource(self._api)
        self.marketing_campaigns = MarketingCampaignsResource(self._api)
        self.marketing_categories = MarketingCategoriesResource(self._api)
        self.payment_methods = PaymentMethodsResource(self._api)
        self.payments = PaymentsResource(self._api)
        self.reports = ReportsResource(self._api)
        self.sales_representatives = SalesRepresentativesResource(self._api)
        self.statistics = StatisticsResource(self._api)
        self.tasks = TasksResource(self._api)
        self.taxes = TaxesResource(self._api)
        self.teams = TeamsResource(self._api)
        self.terms = TermsResource(self._api)
        self.users = UsersResource(self._api)
        self.work_orders = WorkOrdersResource(self._api)

    async def __aenter__(self) -> "ServiceBridgeClient":
        await self._api.__aenter__()
        return self

    async def __aexit__(self, *args: object) -> None:
        await self._api.__aexit__(*args)

    async def close(self) -> None:
        await self._api.close()


__all__ = [
    "ServiceBridgeClient",
    "ServiceBridgeError",
    "APIError",
    "AuthenticationError",
    "NotFoundError",
    "RateLimitError",
    "ConfigurationError",
]
