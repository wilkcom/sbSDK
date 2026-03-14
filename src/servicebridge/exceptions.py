class ServiceBridgeError(Exception):
    """Base exception for all SDK errors."""


class APIError(ServiceBridgeError):
    """Raised when the API returns a non-2xx status or an error payload."""

    def __init__(self, status: int, message: str, raw: dict | None = None) -> None:
        self.status = status
        self.message = message
        self.raw = raw
        super().__init__(f"[HTTP {status}] {message}")


class AuthenticationError(APIError):
    """Raised on 401 after a token refresh attempt fails."""


class NotFoundError(APIError):
    """Raised on 404."""


class RateLimitError(APIError):
    """Raised on 429 — request rate limit exceeded."""


class ConfigurationError(ServiceBridgeError):
    """Raised when required credentials are missing at startup."""
