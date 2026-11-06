"""Ergonomics layer for the Lockally Python SDK.

Generator-agnostic helpers that sit alongside the generated ``lockally`` client:
automatic retries + rate-limit (429) handling, idempotency keys, cursor
pagination, and a typed error. See README.md for wiring.
"""
from .errors import LockallyApiError
from .send import Lockally, SendResult
from .idempotency import new_idempotency_key, with_idempotency_key
from .pagination import collect, paginate
from .webhook import (
    WEBHOOK_HEADER,
    WEBHOOK_MAX_SKEW_SECONDS,
    WebhookExpiredError,
    WebhookMalformedError,
    WebhookMismatchError,
    WebhookSecretError,
    WebhookVerificationError,
    verify_webhook,
)
from .retry import (
    RetryConfig,
    call_with_retry,
    make_urllib3_retry,
    parse_retry_after,
)

__all__ = [
    "Lockally",
    "verify_webhook",
    "WEBHOOK_HEADER",
    "WEBHOOK_MAX_SKEW_SECONDS",
    "WebhookVerificationError",
    "WebhookMalformedError",
    "WebhookExpiredError",
    "WebhookMismatchError",
    "WebhookSecretError",
    "SendResult",
    "LockallyApiError",
    "RetryConfig",
    "call_with_retry",
    "make_urllib3_retry",
    "parse_retry_after",
    "new_idempotency_key",
    "with_idempotency_key",
    "paginate",
    "collect",
]

__version__ = "0.1.0"
