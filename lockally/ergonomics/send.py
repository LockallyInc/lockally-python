"""The one call almost every integration makes, without the ceremony.

The generated client is a faithful translation of the spec, which means
sending looks like this::

    api = SendApi(ApiClient(Configuration(access_token=key)))
    api.send_email(
        idempotency_key=str(uuid.uuid4()),
        send_email_request=SendEmailRequest(from_=..., to=[...], text=...),
    )

Every part of that is correct and none of it is what anybody wants to read in
a quickstart. This wraps it, and only it.
"""
from __future__ import annotations

import json
import uuid
from dataclasses import dataclass
from typing import Any, Mapping, Optional, Sequence, Union
from urllib import error, request

from .errors import LockallyApiError

DEFAULT_BASE_URL = "https://api.lockally.com"

Addresses = Union[str, Sequence[str]]


def _list(v: Optional[Addresses]) -> Optional[list[str]]:
    if v is None:
        return None
    return [v] if isinstance(v, str) else list(v)


@dataclass(frozen=True)
class SendResult:
    """What the API returned. ``status`` is the field to branch on."""

    id: Optional[str]
    message_id: Optional[str]
    status: Optional[str]
    warning: Optional[str] = None


class Lockally:
    """A thin client over ``POST /v1/send``."""

    def __init__(self, api_key: str, *, base_url: str = DEFAULT_BASE_URL, opener=None):
        if not api_key:
            raise ValueError("lockally: an API key is required")
        self._key = api_key
        self._base = base_url.rstrip("/")
        # Injected in tests. urllib rather than requests so the ergonomics
        # layer adds no dependency the generated client does not already have.
        self._opener = opener or request.urlopen

    def send(
        self,
        *,
        from_: str,
        to: Addresses,
        subject: Optional[str] = None,
        text: Optional[str] = None,
        html: Optional[str] = None,
        cc: Optional[Addresses] = None,
        bcc: Optional[Addresses] = None,
        reply_to: Optional[Addresses] = None,
        reply_to_name: Optional[str] = None,
        template_id: Optional[str] = None,
        variables: Optional[Mapping[str, str]] = None,
        headers: Optional[Mapping[str, str]] = None,
        attachments: Optional[Sequence[Mapping[str, Any]]] = None,
        tags: Optional[Sequence[str]] = None,
        send_at: Optional[str] = None,
        unsubscribe: Optional[bool] = None,
        idempotency_key: Optional[str] = None,
    ) -> SendResult:
        """Send one message.

        ``idempotency_key`` is REQUIRED by the API, so when it is omitted this
        generates a UUID to keep the call working. That is a convenience, not
        a default to rely on: a generated key is new on every call, so
        retrying through this method sends a SECOND message rather than
        replaying the first. The key has to identify the message, which only
        the caller knows.

        Returns on 200 as well as 202. A 200 means nothing was queued, either
        because every recipient was suppressed or because the key was a test
        key. Both are successes; branch on ``status``.
        """
        body: dict[str, Any] = {
            "from": from_,
            "to": _list(to),
            "subject": subject,
            "text": text,
            "html": html,
            "cc": _list(cc),
            "bcc": _list(bcc),
            "reply_to": _list(reply_to),
            "reply_to_name": reply_to_name,
            "template_id": template_id,
            "variables": dict(variables) if variables else None,
            "headers": dict(headers) if headers else None,
            "attachments": [dict(a) for a in attachments] if attachments else None,
            "tags": list(tags) if tags else None,
            "send_at": send_at,
            "unsubscribe": unsubscribe,
        }
        body = {k: v for k, v in body.items() if v is not None}

        req = request.Request(
            f"{self._base}/v1/send",
            data=json.dumps(body).encode(),
            method="POST",
            headers={
                "Authorization": f"Bearer {self._key}",
                "Content-Type": "application/json",
                "Idempotency-Key": idempotency_key or str(uuid.uuid4()),
            },
        )

        try:
            with self._opener(req) as resp:
                payload = _decode(resp.read())
                return SendResult(
                    id=payload.get("id"),
                    message_id=payload.get("message_id"),
                    status=payload.get("status"),
                    warning=payload.get("warning"),
                )
        except error.HTTPError as exc:  # non-2xx
            payload = _decode(exc.read())
            raise LockallyApiError(
                exc.code,
                code=payload.get("code"),
                message=payload.get("title") or f"lockally: HTTP {exc.code}",
                request_id=payload.get("request_id") or exc.headers.get("x-request-id"),
                body=payload,
            ) from None


def _decode(raw: bytes) -> dict[str, Any]:
    if not raw:
        return {}
    try:
        parsed = json.loads(raw)
    except ValueError:
        # A non-JSON error body is itself the diagnostic: nginx answers an
        # oversized payload as HTML before the application sees it.
        return {}
    return parsed if isinstance(parsed, dict) else {}
