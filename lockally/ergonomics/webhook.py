"""Webhook signature verification.

Every delivery carries::

    X-Lockally-Signature: t=<unix-seconds>,v1=<hex(hmac_sha256(secret, t + "." + body))>

Verifying that by hand is an HMAC, a constant-time compare and a clock
window, in that order, and getting any of the three wrong fails quietly: a
``==`` on the digest leaks timing, a missing window accepts a replay, and
re-serialising the body before hashing rejects every real delivery. It is
exactly the code an official SDK should remove, and until now none of ours
had it.

The rules here are pinned against the server that signs the deliveries by a
shared fixture, ``sdk/ergonomics/testdata/webhook-cases.json``, generated
from ``internal/webhook``. Three of them are not what you would guess:

* The window is ONE-SIDED. Only a timestamp too far in the PAST is refused.
  A future one is accepted, so a verifier that rejects it would drop
  deliveries the server considers valid.
* Unknown pairs are IGNORED, so a later ``v2=`` scheme cannot break a
  verifier written today.
* The hex is decoded before comparison, so its case does not matter.

And the one that breaks most first attempts: THE SECRET IS HEX TEXT AND THE
KEY IS THE BYTES IT DECODES TO. ``signing_secret`` is BYTEA, so the
dispatcher signs with 32 raw bytes while the API shows you the hex of them,
once, at creation. Signing with the text gives a valid-looking digest that
never matches. Pass the ``str`` you were shown and it is decoded for you;
pass ``bytes`` and they are used as the key unchanged.
"""

from __future__ import annotations

import hmac
import time
from hashlib import sha256
from typing import Optional

#: The header carrying the signature.
WEBHOOK_HEADER = "X-Lockally-Signature"

#: How old a timestamp may be before it is refused as a replay. Matches the
#: server.
WEBHOOK_MAX_SKEW_SECONDS = 300


class WebhookVerificationError(Exception):
    """Base class, so one ``except`` can refuse the delivery."""


class WebhookMalformedError(WebhookVerificationError):
    """The header is not a readable signature."""


class WebhookExpiredError(WebhookVerificationError):
    """The signature is genuine but too old."""


class WebhookMismatchError(WebhookVerificationError):
    """The body does not match the signature. Treat as hostile, not a bug."""


class WebhookSecretError(WebhookVerificationError):
    """The secret is not the hex string the dashboard showed you.

    Separate from a mismatch because it is your configuration that is wrong,
    not the caller's signature.
    """


def verify_webhook(
    secret: bytes | str,
    body: bytes | str,
    header: str,
    *,
    now: Optional[float] = None,
    max_skew_seconds: int = WEBHOOK_MAX_SKEW_SECONDS,
) -> None:
    """Raise unless ``body`` was signed with ``secret``, as ``header`` claims.

    ``secret`` is the hex string from the dashboard, which is decoded for
    you, or the raw key bytes if you decoded it yourself.

    ``body`` MUST be the raw bytes as received. Parsing the JSON and dumping
    it again changes the bytes, and the signature is over the bytes::

        @app.post("/webhooks/lockally")
        def hook():
            try:
                verify_webhook(SECRET, request.get_data(), request.headers.get(WEBHOOK_HEADER, ""))
            except WebhookVerificationError:
                return "", 400
            event = request.get_json()   # safe to trust from here

    Returns ``None`` on success and raises a
    :class:`WebhookVerificationError` subclass otherwise, so that forgetting
    to check the result is a 500 rather than a silent accept.
    """
    # A str is the hex the dashboard showed you; bytes are the key itself.
    if isinstance(secret, str):
        try:
            secret_bytes = bytes.fromhex(secret.strip())
        except ValueError:
            raise WebhookSecretError(
                "signing secret is not valid hex; pass the string the dashboard "
                "showed you, or the decoded bytes"
            ) from None
    else:
        secret_bytes = secret
    body_bytes = body.encode() if isinstance(body, str) else body

    ts, sig_hex = _parse(header)

    try:
        ts_int = int(ts)
    except ValueError:
        raise WebhookMalformedError("t= is not an integer") from None

    current = time.time() if now is None else now
    # One-sided on purpose: see the module docstring.
    if current - ts_int > max_skew_seconds:
        raise WebhookExpiredError(
            f"signature is {int(current - ts_int)}s old; the window is {max_skew_seconds}s"
        )

    try:
        sig = bytes.fromhex(sig_hex)
    except ValueError:
        raise WebhookMalformedError("v1= is not hex") from None

    want = hmac.new(secret_bytes, ts.encode() + b"." + body_bytes, sha256).digest()

    # compare_digest, not ==: the comparison has to take the same time
    # whether the first byte is wrong or only the last.
    if not hmac.compare_digest(sig, want):
        raise WebhookMismatchError("HMAC does not match")


def _parse(header: str) -> tuple[str, str]:
    ts = sig = ""
    for part in header.split(","):
        key, sep, value = part.strip().partition("=")
        if not sep:
            raise WebhookMalformedError("expected k=v pairs")
        # Unknown keys are skipped rather than refused, so a later scheme
        # does not break a verifier written today.
        key = key.strip()
        if key == "t":
            ts = value.strip()
        elif key == "v1":
            sig = value.strip()
    if not ts or not sig:
        raise WebhookMalformedError("missing t= or v1=")
    return ts, sig
