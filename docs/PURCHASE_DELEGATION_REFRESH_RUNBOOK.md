# UCII Voice Authority — Purchase Delegation Refresh Runbook

## Purpose

Restore the Voice Authority demonstration after a purchasing delegation
has been revoked, without restoring the revoked delegation or disturbing
the independent compute.inspect authorization.

Preparing a fresh revocation authorization is NOT revocation. Do not
consume it until the human-confirmed revocation stage of the demo.

## Repositories and services

Voice repository:
`/opt/ucii/ucii-voice-authority-agent`

Core UCII repository:
`/opt/ucii/UCII`

Voice application:
`ucii-voice-authority-app.service`

Voice HTTP endpoint:
`http://127.0.0.1:8003`

Core UCII HTTP endpoint:
`http://127.0.0.1:8000`

Browser console:
`https://voice.ucii.sportgen-ai.com/console-v2`

Voice Identity:
`9df0ff8a-25d0-4340-be32-05e8263f1277`

Voice credential:
`fca03fa4-32c6-49fe-87b2-4b9e56453a66`

## September 26, 2026 — confirmed authority state

Previously revoked purchasing delegation:
`3048a56f-912f-401d-8f5e-58ed0f0ba4ad`

New purchasing delegation:
`5d0d2fe7-26d7-4f8e-94ac-affe4fd8eb61`

The old delegation must remain REVOKED. Never reuse its consumed
grant or revocation authorization.

The new delegation was successfully created through:

`src/voice_authority/voice_lifecycle_cli.py grant`

with operation `compute.purchase` and granted-by `Brad Phee`,
after preparing a fresh, one-use grant authorization.

The grant authorization was consumed once.

The independent compute.inspect delegation was not replaced or revoked.

## Exact refresh sequence

### 1. Inspect before making changes

Confirm the Voice repository, current branch, HEAD, origin/main and
working-tree status.

Identify the revoked purchasing delegation and the independent
inspection delegation.

Inspect the existing lifecycle authorization schema, CLI and
protected helper before creating new authorization evidence.

Never assume an old one-use authorization can be reused.

Preserve all existing uncommitted work.

### 2. Prepare a fresh, one-use grant authorization

Use the existing UCII controller lifecycle authorization contract.

Bind the authorization to:
- The actual Voice Identity.
- `GRANT_DELEGATED_AUTHORITY`.
- The intended `compute.purchase` operation.
- The authorized human controller.
- A new unique authorization ID.
- A short, explicit validity period.
- `max_uses: 1`.

The exact authorization schema and required signing/validation fields
must be taken from the current UCII implementation, not reconstructed
from memory.

Keep the authorization in the existing protected lifecycle
authorization location:

`/etc/ucii-voice-authority/lifecycle-authorization.json`

Preserve the previous authorization file before replacement.
Keep the new file root-owned and mode 0600.

Validate it with the real UCII lifecycle authorization loader before
attempting the grant.

### 3. Grant a NEW purchasing delegation

Invoke the existing Voice lifecycle CLI's grant operation.

Record the newly returned authority ID.

Verify the grant succeeded and that its one-use authorization was
consumed.

Do not reactivate or modify the previously revoked delegation.

### 4. Prepare the NEXT one-use revocation authorization

Before replacing the consumed grant authorization, preserve it.

Prepare a new authorization using the current UCII lifecycle contract:
- Operation: `REVOKE_DELEGATED_AUTHORITY`.
- Target: the NEW purchasing authority ID.
- A new unique authorization ID.
- `max_uses: 1`.
- A short, explicit expiration.
- Reason: `Human controller revocation during Voice Authority demo`.

Validate the new authorization with the real UCII loader.

The September 26 example was:

Authorization ID:
`voice-purchase-revoke-e373ed70-f4a2-404f-9e3f-b921d759c789`

Target:
`5d0d2fe7-26d7-4f8e-94ac-affe4fd8eb61`

Expiration:
`2026-09-27T01:09:47.679283+00:00`

This authorization is time-limited. NEVER assume it remains valid
during a later demo. If expired, prepare and validate a new one-use
authorization targeting the same currently active purchasing delegation.
Do not create another delegation merely because revocation evidence
expired.

DO NOT execute revocation during preparation.

### 5. Bind the console and backend to the NEW delegation

The demonstration's purchase-only revocation target must be the new
authority ID.

Inspect and update only the necessary references in:

`src/voice_authority/main.py`

`src/voice_authority/console-v2.html`

The backend constant is:

`PURCHASE_REVOKE_AUTHORITY_ID`

The console contains the corresponding proposal schema, validation,
session instructions and revocation-target checks.

In the September 26 refresh, one reference was changed in main.py
and six in console-v2.html.

Back up both files before editing. Confirm that all intended references
use the new ID and that the old revoked ID has not accidentally become
the target again.

Validate Python syntax and inspect the exact diff.

Do not replace the JavaScript body, reset the working tree, or modify
unrelated application files.

### 6. Restart the Voice application and wait for readiness

Restart only:

`sudo systemctl restart ucii-voice-authority-app.service`

Wait for the actual HTTP application to respond at:

`http://127.0.0.1:8003/openapi.json`

`systemctl is-active` alone does not prove HTTP readiness.

The September 26 first request failed because it ran before Uvicorn
was ready. That connection failure was not an authorization failure.

### 7. Verify BOTH operations through the Voice HTTP endpoint

The endpoint uses POST, not GET. The Voice app runs on port 8003,
not port 8000.

Purchase:

`curl --fail-with-body --silent --show-error --request POST 'http://127.0.0.1:8003/ucii/delegated/check?operation=compute.purchase'`

Inspection:

`curl --fail-with-body --silent --show-error --request POST 'http://127.0.0.1:8003/ucii/delegated/check?operation=compute.inspect'`

Required pre-revocation result for BOTH:

`"status":"AUTHORIZED"`

`"authorized":true`

`"source":"UCII_LIVE"`

Both responses were confirmed on September 26, 2026.

### 8. Diagnose UNAVAILABLE without issuing another grant

`UNAVAILABLE` is not `DENIED`.

The Voice endpoint calls `check_purchase_authority` in:

`src/voice_authority/ucii_authority_client.py`

It obtains a fresh protected signature and POSTs to:

`http://127.0.0.1:8000/v1/authorization/delegated/check`

The Voice endpoint catches AuthorityCheckError and can return a
generic HTTP 503 without exposing its underlying cause.

If inspection succeeds but purchasing returns UNAVAILABLE:
- Do not immediately re-grant.
- Do not revoke.
- Check the protected signer and upstream response.
- Compare a direct check with the browser-facing HTTP check.

For direct Python diagnostics, the Voice package requires:

`PYTHONPATH=/opt/ucii/ucii-voice-authority-agent/src`

Use the repository virtual environment:

`/opt/ucii/ucii-voice-authority-agent/.venv/bin/python`

The September 26 direct diagnostic initially failed because
PYTHONPATH was omitted. After correcting the import path, the
direct purchase check returned:

`AUTHORIZED: True`
`OPERATION: compute.purchase`
`SOURCE: UCII_LIVE`

A subsequent check through port 8003 confirmed that BOTH purchase
and inspection returned AUTHORIZED and UCII_LIVE.

Do not print signatures, private keys, credential fingerprints or
other protected signing material in diagnostics.

### 9. Execute revocation ONLY during the demonstration

Open and refresh the browser console. Connect AssemblyAI.

Demonstrate live inspection authorization first, followed by live
purchasing authorization.

Then initiate the purchase-only revocation ceremony and complete
the required human confirmation.

The backend confirmation route is:

`POST /ucii/purchase/revoke/confirm`

It invokes the protected helper:

`/usr/local/sbin/ucii-voice-revoke-purchase`

The helper must return verified revocation for the exact NEW
purchasing authority ID.

The pending ceremony is single-process and time-limited; an
application restart may discard it.

Do not execute the protected helper merely to test whether it works.

### 10. Verify the post-revocation result

After human-confirmed revocation, make fresh live UCII checks.

Required:
- `compute.purchase`: DENIED.
- `compute.inspect`: AUTHORIZED.
- Both results must come from `UCII_LIVE`.

An upstream failure or UNAVAILABLE response does not prove
revocation succeeded.

A revoked purchase delegation must stay revoked.

A future repeat of the demonstration requires a NEW purchasing
delegation and NEW one-use grant/revocation authorization evidence.

## Operational safeguards

- Never restore a revoked authority ID.
- Never reuse consumed lifecycle authorization evidence.
- Never confuse Voice Identity with Guardian Identity.
- Never revoke the independent inspection delegation.
- Never treat a successful signer operation as proof of authorization.
- Never treat an HTTP 503 as an authorization denial.
- Never restart or alter services unnecessarily.
- Never commit secrets or protected authorization files.
- Preserve the existing dirty working tree.
- Review the diff before any commit or push.

## Verification record

September 26, 2026:

Live Voice HTTP purchase check:
AUTHORIZED / UCII_LIVE

Live Voice HTTP inspection check:
AUTHORIZED / UCII_LIVE

The new purchasing delegation was active at this checkpoint.
The post-revocation sequence had NOT yet been demonstrated.
