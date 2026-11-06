"""Idempotency-key helpers.

The Lockally send endpoint requires an ``Idempotency-Key`` header; other
mutating calls accept one so a retried write is not applied twice. Generate a
fresh key per logical operation and reuse it across retries of that operation.
"""
from __future__ import annotations

import uuid
from typing import Dict, Optional

MUTATING_METHODS = frozenset({"POST", "PUT", "PATCH", "DELETE"})


def new_idempotency_key() -> str:
    """A fresh RFC 4122 v4 key."""
    return str(uuid.uuid4())


def with_idempotency_key(
    headers: Optional[Dict[str, str]],
    method: str = "POST",
) -> Dict[str, str]:
    """Return a copy of ``headers`` with an Idempotency-Key for mutating methods.

    A caller-supplied key is preserved; GET/HEAD are left untouched.

        api.send_email(request, _headers=with_idempotency_key(None))
    """
    out: Dict[str, str] = dict(headers or {})
    if method.upper() in MUTATING_METHODS and not _has_key(out, "Idempotency-Key"):
        out["Idempotency-Key"] = new_idempotency_key()
    return out


def _has_key(headers: Dict[str, str], name: str) -> bool:
    lname = name.lower()
    return any(k.lower() == lname for k in headers)
