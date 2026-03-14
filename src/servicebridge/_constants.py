BASE_URL = "https://cloud.servicebridge.com/api/v4.5"


class Endpoints:
    LOGIN = "/Login"
    LOGOUT = "/Logout"
    ACCOUNTING_ACCOUNTS = "/Accounting/Accounts"
    ACTIVITY_NOTE = "/ActivityNote"
    ASSETS = "/Assets"
    BRANCHES = "/Branches"
    COMPANIES = "/Companies"
    CONTACTS = "/Contacts"
    CUSTOMER_CATEGORIES = "/CustomerCategories"
    CUSTOMERS = "/Customers"
    CUSTOM_FIELD_GROUPS = "/CustomFieldGroups"
    CUSTOM_FIELDS = "/CustomFields"
    EMPLOYEES = "/Employees"
    ESTIMATES = "/Estimates"
    INVENTORY = "/Inventory"
    INVENTORY_CHARGE_TYPES = "/Inventory/ChargeTypes"
    INVENTORY_GROUPS = "/Inventory/Groups"
    INVENTORY_PRODUCTS = "/Inventory/Products"
    INVENTORY_SERVICES = "/Inventory/Services"
    INVENTORY_UNITS = "/Inventory/Units"
    INVOICES = "/Invoices"
    JOB_CATEGORIES = "/JobCategories"
    JOB_TEMPLATES = "/JobTemplates"
    LEADS = "/Leads"
    LOCATIONS = "/Locations"
    MARKETING_CAMPAIGNS = "/MarketingCampaigns"
    MARKETING_CATEGORIES = "/MarketingCategories"
    PAYMENT_METHODS = "/PaymentMethods"
    PAYMENTS = "/Payments"
    REPORT = "/Report"
    SALES_REPRESENTATIVES = "/SalesRepresentatives"
    STATISTICS = "/Statistics"
    TASKS = "/Tasks"
    TAXES = "/Taxes"
    TEAMS = "/Teams"
    TERMS = "/Terms"
    USERS = "/Users"
    WORK_ORDERS = "/WorkOrders"

    # --- Nested endpoint helpers ---

    @staticmethod
    def customer_make_active(customer_id: int) -> str:
        return f"/Customers/{customer_id}/MakeActive"

    @staticmethod
    def customer_payment_cards(customer_id: int) -> str:
        return f"/Customers/{customer_id}/PaymentCards"

    @staticmethod
    def customer_payment_bank_accounts(customer_id: int) -> str:
        return f"/Customers/{customer_id}/PaymentBankAccounts"

    @staticmethod
    def estimate_photos(estimate_id: int) -> str:
        return f"/Estimates/{estimate_id}/Photos"

    @staticmethod
    def estimate_documents(estimate_id: int) -> str:
        return f"/Estimates/{estimate_id}/Documents"

    @staticmethod
    def estimate_won(estimate_id: int) -> str:
        return f"/Estimates/{estimate_id}/Won"

    @staticmethod
    def estimate_lost(estimate_id: int) -> str:
        return f"/Estimates/{estimate_id}/Lost"

    @staticmethod
    def estimate_reopen(estimate_id: int) -> str:
        return f"/Estimates/{estimate_id}/Reopen"

    @staticmethod
    def estimate_duplicate(estimate_id: int) -> str:
        return f"/Estimates/{estimate_id}/Duplicate"

    @staticmethod
    def work_order_photos(work_order_id: int) -> str:
        return f"/WorkOrders/{work_order_id}/Photos"
