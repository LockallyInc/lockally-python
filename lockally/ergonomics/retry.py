"""Retry helpers: a urllib3 Retry factory for transport-level retries (the
recommended path, wired via ``configuration.retries``), plus a stdlib
``call_with_retry`` for higher-level flows."""
from __future__ import annotations

import email.utils
import random
import time
from dataclasses import dataclass
from typing import Any, Callable, Optional, TypeVar

from .errors import LockallyApiError

T = TypeVar("T")

RETRYABLE_STATUS = (429, 500, 502, 503, 504)


@dataclass
class RetryConfig:
    max_retries: int = 3
    base_delay: float = 0.2   # seconds
    max_delay: float = 20.0   # seconds


def make_urllib3_retry(config: Optional[RetryConfig] = None):
    """Build a urllib3 Retry for the generated client's Configuration.retries.

        from lockally import Configuration
        cfg = Configuration()
        cfg.retries = make_urllib3_retry()

    Retries 429 + 5xx, honors Retry-After, and backs off exponentially. Note
    urllib3 also needs the request to be safe to replay — pair mutating calls
    with an Idempotency-Key (see idempotency.with_idempotency_key).
    """
    from urllib3.util.retry import Retry  # imported lazily; only needed here

    config = config or RetryConfig()
    return Retry(
        total=config.max_retries,
        backoff_factor=config.base_delay,
        backoff_max=config.max_delay,
        status_forcelist=list(RETRYABLE_STATUS),
        respect_retry_after_header=True,
        allowed_methods=None,  # retry all methods; safe because we set idempotency keys
        raise_on_status=False,
    )


def default_retryable(exc: BaseException) -> bool:
    if isinstance(exc, LockallyApiError):
        return exc.retryable
    status = getattr(exc, "status", None)
    return isinstance(status, int) and status in RETRYABLE_STATUS


def call_with_retry(
    func: Callable[[], T],
    *,
    config: Optional[RetryConfig] = None,
    retryable: Callable[[BaseException], bool] = default_retryable,
    sleep: Callable[[float], None] = time.sleep,
    rand: Callable[[], float] = random.random,
) -> T:
    """Call ``func`` with exponential backoff + jitter on retryable errors.

    Honors a Retry-After hint on the raised error when present. Supplementary to
    the transport-level urllib3 retry; use for custom multi-step flows.
    """
    config = config or RetryConfig()
    attempt = 0
    while True:
        try:
            return func()
        except BaseException as exc:  # noqa: BLE001 - re-raised below if not retryable
            if attempt >= config.max_retries or not retryable(exc):
                raise
            ra = _retry_after_seconds(exc)
            delay = ra if ra is not None else _backoff(attempt, config, rand)
            attempt += 1
            sleep(min(delay, config.max_delay))


def _backoff(attempt: int, config: RetryConfig, rand: Callable[[], float]) -> float:
    exp = min(config.base_delay * (2 ** attempt), config.max_delay)
    return rand() * exp  # full jitter in [0, exp)


def _retry_after_seconds(exc: BaseException) -> Optional[float]:
    headers = getattr(exc, "headers", None)
    if not headers:
        return None
    try:
        value = headers.get("Retry-After") or headers.get("retry-after")
    except Exception:  # noqa: BLE001
        return None
    return parse_retry_after(value)


def parse_retry_after(value: Any) -> Optional[float]:
    """Retry-After (delta-seconds or HTTP-date) → seconds from now."""
    if value is None:
        return None
    s = str(value).strip()
    if s == "":
        return None
    try:
        return max(0.0, float(s))
    except ValueError:
        pass
    try:
        dt = email.utils.parsedate_to_datetime(s)
    except (TypeError, ValueError):
        return None
    if dt is None:
        return None
    return max(0.0, dt.timestamp() - time.time())
