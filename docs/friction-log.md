# Friction Log

Record concrete integration friction as it is encountered. Keep observations factual and separate from proposed fixes.

This is an internal UCII Labs engineering record for the AssemblyAI Voice Authority Agent build. It is not an AssemblyAI hackathon submission artifact. The purpose is to preserve real lessons while they are fresh and establish the logging discipline we intend to use from day one on later builds such as Alexa+.

| Date | Surface | Observation | Impact | Workaround / Resolution | Status |
|---|---|---|---|---|---|
| 2026-09-14 | Project foundation | No implementation friction recorded yet. | None | Repository initialized before integration work. | CLOSED |
| 2026-09-18 | UCII economic bootstrap | Normal product/service entitlement requires an already-established subject identity and active bound credential, so it cannot authorize a brand-new HUMAN's first economically gated `POST /v1/identity` request. | Exposed a bootstrap cycle: no identity → no credential → cannot prove normal entitlement → identity creation remains economically gated. | Kept identity creation protected and designed a separate short-lived, one-use Product Enrollment Capability only for pre-identity economic bootstrap. After identity/credential establishment, transition to normal credential-bound product entitlement. | RESOLVED |
| 2026-09-18 | Enrollment capability lifecycle | A simple consume-on-presentation model was unsafe: consuming before downstream provisioning could strand a legitimate participant on failure, while consuming only afterward could allow concurrent reuse. | Risk of either replay/concurrency exposure or destructive failure behavior. | Added `ISSUED → RESERVED → FINALIZED` semantics, with `RESERVED → RELEASED` on downstream failure so a valid retry remains possible. | RESOLVED |
| 2026-09-18 | Capability state ownership | Middleware-owned capability service construction would isolate state from the eventual protected issuer. | A correctly minted capability could be invisible to the x402 middleware instance expected to consume it. | Added dependency injection for the shared `ProductEnrollmentCapabilityService`; no public issuer endpoint or alternate trust root was introduced. | RESOLVED |
| 2026-09-18 | Capability issuance trust boundary | Once the capability primitive existed, directly exposing `issue()` through an ordinary API/browser/Voice/AssemblyAI path would have created reusable economic-bypass minting authority. | A functional shortcut could silently create a new trust root. | Separated mint authorization from the capability itself and added root-controlled `ProductEnrollmentIssuanceAuthorization`, exactly binding product, operation, method, path, validity interval, and one use. | RESOLVED |
| 2026-09-18 | Durable one-use issuance | In-memory consumption would not survive process restart and therefore could not enforce the intended one-use root authorization durably. | Restart/recovery could reopen an authorization that should already be exhausted. | Reused the existing UCII `ProvenanceRecorder` pattern. A deterministic consumption event derived from the authorization ID creates a durable replay boundary; duplicate consumption fails closed. | RESOLVED |
| 2026-09-18 | Consumption ordering | If durable consumption occurred before exact request validation, a wrong product/method/path or expired request could permanently exhaust an otherwise valid authorization. | Invalid or accidental requests could deny the legitimate enrollment ceremony. | Verify all exact bindings and freshness first; cross the durable consumption boundary only after verification succeeds. Tests proved invalid requests leave the ledger untouched. | RESOLVED |
| 2026-09-18 | Verification tooling | An initial production-surface guard also scanned test fixtures and matched a test `@app.post(PATH)`, producing a false positive. | Verification noise could be mistaken for an implementation/security failure. | Scoped the guard to the production artifact whose property it was intended to prove. Production-only inspection confirmed no capability-mint route. | RESOLVED |
| 2026-09-18 | UCII architecture reuse | The Voice build repeatedly appeared to need new infrastructure until existing UCII entitlement, provenance, controller-lifecycle consumption, and HUMAN governance seams were inspected closely. | Skipping inspection could have produced duplicate persistence, Voice-specific authority mechanisms, or alternate trust roots. | Continued inspect → reason → smallest correct change → verify, extending existing UCII primitives rather than creating parallel systems. | RESOLVED |

## 2026-09-18 engineering lessons

### Pre-identity admission and post-identity entitlement are different lifecycle states

The normal Voice Authority product entitlement is intentionally identity- and credential-bound. That is correct after onboarding, but it means a separate mechanism is required for the first economically gated identity-creation operation. The Product Enrollment Capability fills only that economic bootstrap gap.

### One-use security artifacts need explicit irreversible boundaries

Both enrollment-capability use and issuance-authorization use exposed timing questions. Reservation/finalization protects the downstream capability lifecycle, while durable provenance consumption protects the root-controlled issuance authorization. The irreversible step must occur only after all exact bindings have been verified.

### Mint authority is separate from capability possession

The authority to mint an enrollment capability is not the enrollment capability itself. The browser, Voice Agent, AssemblyAI runtime, transcript/model layer, payment path, and anonymous caller must not acquire reusable minting authority.

### Existing security infrastructure should be reused before new trust mechanisms are invented

The existing UCII provenance recorder supplied the durable replay boundary needed by 3H.7. Reusing it avoided creating a second persistence/trust mechanism for the same class of problem.

### Verification failures and implementation failures are not the same thing

A guard that is incorrectly scoped can fail even when the production artifact satisfies the intended invariant. Verification tooling must be inspected and corrected rather than treating every guard failure as proof that source code is wrong.

## Resulting architecture

Economic evaluation order:

`NORMAL PRODUCT ENTITLEMENT → PRODUCT ENROLLMENT CAPABILITY → x402 PAYMENT FALLBACK`

Protected first-use issuance path through the current checkpoint:

`ROOT-CONTROLLED EXACT ISSUANCE AUTHORIZATION → VALIDATION → DURABLE ONE-USE CONSUMPTION → NON-SECRET ISSUANCE PERMIT → [NEXT: PROTECTED ISSUER] → PRODUCT ENROLLMENT CAPABILITY`

Security separation:

`ISSUANCE AUTHORIZATION != ENROLLMENT CAPABILITY != IDENTITY != AUTHENTICATION != HUMAN GOVERNANCE != DELEGATED AUTHORITY != AUTHORIZATION != ENTITLEMENT != PAYMENT != EXECUTION`

## Current checkpoint

Objectives 3H.1 through 3H.7 are complete.

UCII core synchronized checkpoint:

`f5c14bd0b7c4313ce7f41114067e9810dc8ec3d7` — `Add enrollment issuance authorization`

Targeted/regression verification at the 3H.7 checkpoint:

- 23 issuance-authorization tests passed
- 20 enrollment-capability tests passed
- 10 existing controller-lifecycle consumption precedent tests passed
- **53/53 total passed**

Next:

**Objective 3H.8 — Protected Product Enrollment Capability Issuer — NOT STARTED**

## Logging rules

Capture real issues involving, for example:

- AssemblyAI documentation/API/SDK setup;
- real-time browser audio/session behavior;
- authentication/token handling;
- structured tool/action generation;
- UCII public SDK/API integration;
- identity/economic bootstrap;
- protected authority and capability boundaries;
- deployment/networking;
- demo reliability;
- sponsor platform behavior;
- submission tooling.

For each meaningful friction point, capture the task, expected behavior, actual behavior, impact, workaround/resolution, and reusable lesson while the evidence is fresh.

Do not manufacture friction for a competition bonus or narrative. Record what actually happens, when it happens, and how it affected the build.

---

### Protected issuer cannot share process-local enrollment capability state

**Objective:** 3H.8 — Protected Product Enrollment Capability issuer

**Status:** RESOLVED ARCHITECTURALLY — IMPLEMENTATION PENDING

**Observation**

Objective 3H.8A established that `ProductEnrollmentCapabilityService` currently retains enrollment capability state only in process memory:

- `_capabilities` is an in-memory dictionary;
- `_reserved` is an in-memory set;
- concurrency is protected only by a process-local `threading.Lock`;
- production `X402Middleware` constructs its own `ProductEnrollmentCapabilityService` when no service is injected.

A separately protected issuer process therefore cannot safely mint through its own instance of the current service and expect the public API middleware to observe the resulting capability.

Moving capability minting into the ordinary public API process merely to share the Python object would weaken the protected issuance boundary.

The inspection also confirmed that `ProductEnrollmentIssuancePermit` is a non-secret Python value and must not itself be treated as proof across the protected issuer trust boundary. The protected issuer must independently establish the authoritative issuance conditions rather than trusting a caller-constructed permit.

**Impact**

A naive protected-daemon implementation would create one of two failures:

1. the protected issuer would mint capability state that is invisible to the public API process; or
2. capability-minting authority would have to move into the public API process, collapsing the intended protection boundary.

Process-local capability state also does not survive restart and therefore cannot provide the required durable single-use lifecycle.

**Existing UCII precedent**

UCII already provides the required architectural patterns:

- settlement receipts use SQLAlchemy persistence and a unique identifier as the atomic concurrency boundary;
- entitlement replay uses durable `RESERVED -> CONSUMED` state with release after failed downstream execution;
- the protected controller-lifecycle service accepts only finite non-secret intent and independently establishes protected authority rather than accepting raw authority from its caller;
- `ProvenanceRecorder` provides durable append-only one-use issuance-authorization consumption, but is not the appropriate mutable operational store for capability reservation/finalization state.

**Resolution**

Use two deliberately separate durable concerns:

1. `ProvenanceRecorder` remains the authoritative durable one-use exhaustion boundary for Product Enrollment Capability issuance authorization.
2. Product Enrollment Capability operational state moves to UCII's existing SQLAlchemy persistence boundary.

The durable capability lifecycle preserves the existing behavioral contract:

`ISSUED -> RESERVED -> CONSUMED`

A failed downstream operation releases a valid `RESERVED` capability back to `ISSUED`. Expired capability state fails closed.

The raw bearer token is returned only at issuance. Only its digest may be persisted.

The protected issuer must independently establish and consume the exact root-controlled issuance authorization. It must not trust possession of a caller-created `ProductEnrollmentIssuancePermit` as authorization to mint.

**Implementation order**

1. Objective 3H.8B — durable Product Enrollment Capability state contract.
2. Verify issue/reserve/finalize/release behavior, concurrency, restart reconstruction, token-digest-only persistence, and existing x402 regressions.
3. Objective 3H.8C — protected issuer daemon / finite IPC boundary.
4. Connect protected issuance to the durable capability service.
5. Re-prove that browser, Voice Agent, AssemblyAI runtime, model/transcript layer, payment path, and anonymous product request do not possess reusable capability-minting authority.

**Security invariant**

`ISSUANCE AUTHORIZATION != ENROLLMENT CAPABILITY != IDENTITY != AUTHENTICATION != HUMAN GOVERNANCE != DELEGATED AUTHORITY != AUTHORIZATION != ENTITLEMENT != PAYMENT != EXECUTION`

**Inspection checkpoint**

UCII `main`:

`f5c14bd0b7c4313ce7f41114067e9810dc8ec3d7`

Objective 3H.8A was read-only. No UCII source changes were made and AssemblyAI was not invoked.
