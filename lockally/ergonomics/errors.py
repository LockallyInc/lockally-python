"""Typed error for the Lockally Python SDK ergonomics layer."""
from __future__ import annotations

import json
from typing import Any, Optional


class LockallyApiError(Exception):
    """A typed error mapped from a non-2xx Lockally API response.

    The generated client raises its own ``ApiException``; use
    :meth:`from_api_exception` to convert when you want structured fields.
    """

    def __init__(
        self,
        status: int,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        request_id: Optional[str] = None,
        body: Any = None,
    ) -> None:
        super().__init__(message or f"lockally: HTTP {status}")
        self.status = status
        self.code = code
        self.request_id = request_id
        self.body = body

    @property
    def retryable(self) -> bool:
        """True when the server signalled a transient condition."""
        return self.status == 429 or 500 <= self.status <= 599

    @classmethod
    def from_api_exception(cls, exc: Any) -> "LockallyApiError":
        """Best-effort map of the generated client's ApiException (duck-typed)."""
        status = int(getattr(exc, "status", 0) or 0)
        headers = getattr(exc, "headers", None) or {}
        request_id = None
        try:
            request_id = headers.get("x-request-id") or headers.get("X-Request-Id")
        except Exception:  # noqa: BLE001 - headers may be a plain mapping-like
            pass
        body = getattr(exc, "body", None)
        code = None
        message = None
        if isinstance(body, (bytes, bytearray)):
            try:
                body = body.decode("utf-8")
            except Exception:  # noqa: BLE001
                pass
        if isinstance(body, str):
            try:
                parsed = json.loads(body)
                body = parsed
            except Exception:  # noqa: BLE001
                parsed = None
            if isinstance(body, dict):
                err = body.get("error") if isinstance(body.get("error"), dict) else {}
                code = err.get("code") or body.get("code")
                message = err.get("message") or body.get("message")
        return cls(status, code=code, message=message, request_id=request_id, body=body)
