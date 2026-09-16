# Architecture

## Governing architecture

```text
Human Voice
   ↓
Browser Microphone Client
   ↓
AssemblyAI Voice Agent
   ↓
Structured Proposed Action
   ↓
UCII Identity + Authority Gateway
   ↓
ALLOW / DENY
   ↓
Deterministic Tool Executor
   ↓
UCII Provenance
   ↓
Spoken Response + Visual Proof
```

## Domain separation

The architecture MUST preserve:

**Voice ≠ Intent ≠ Identity ≠ Authority ≠ Execution**

Additional boundaries:

- successful speech recognition does not establish intent authority;
- model/tool-call generation does not establish execution authority;
- cryptographically verified identity does not imply delegated authority;
- delegated authority does not imply an action occurred;
- execution does not erase the authorization evidence that preceded it;
- revocation changes authority without requiring identity destruction;
- provenance records facts but does not create authority.

## Components

### 1. Browser voice client

Responsibilities:

- capture microphone audio;
- establish the supported AssemblyAI real-time voice session;
- render live/final conversational state as needed;
- present spoken responses;
- display a compact judge-facing proof surface.

The browser is not an authority source.

### 2. AssemblyAI voice layer

Responsibilities:

- real-time voice interaction;
- speech understanding/transcription capabilities used by the final integration;
- conversational orchestration where supported and appropriate;
- generation of a structured proposed action/tool request.

The AssemblyAI/LLM layer may propose an action. It MUST NOT grant itself UCII authority, bypass the gateway, or invoke the consequential executor through an alternate path.

### 3. Application backend / authority gateway

Planned implementation: small Python/FastAPI service.

Responsibilities:

- receive a structured proposed action;
- bind the request to the acting UCII identity;
- invoke UCII through its public SDK/API boundary;
- evaluate the relevant delegated authority;
- produce an explicit ALLOW/DENY decision;
- pass only authorized operations to the executor;
- preserve evidence needed for the visual proof and provenance chain.

### 4. UCII

UCII remains authoritative for the trust/authority functions exposed to this application, including the applicable identity, credential/authentication/verification, authorization/delegation, revocation, and provenance surfaces.

This repository MUST integrate through the supported public UCII boundary. It MUST NOT duplicate private UCII internals or invent an alternate trust root for the demo.

### 5. Deterministic consequential executor

The executor represents the real action boundary.

Requirements:

- deterministic enough for repeatable judging;
- safe and bounded for demonstration;
- impossible to reach through the normal application flow without a successful authority decision;
- produces explicit execution evidence;
- does not infer authority from natural language or model output.

### 6. Proof UI

The judge-facing UI should make the security state legible in seconds. At minimum, expose:

- spoken/requested action;
- agent identity status;
- delegated authority state;
- authorization decision;
- execution result;
- revocation state where relevant;
- provenance/evidence reference.

## Human Authority Ceremony Engine

Authority-changing voice requests require a deterministic orchestration layer between conversational understanding and the protected UCII lifecycle operation.

The conceptual flow is:

    Voice request
        |
        v
    Bounded structured operation
        |
        v
    Human Authority Ceremony Engine
        |
        +-- principal authentication
        +-- consequence / step-up policy
        +-- out-of-band challenge when required
        +-- fresh UCII lifecycle authorization
        +-- provenance/evidence
        |
        v
    Protected lifecycle operation or DENY

The ceremony engine is application code, not an LLM decision process. It should be reusable independently of AssemblyAI so future web, mobile, CLI, robot, or other voice interfaces can invoke the same protected UCII ceremonies.

The initial protected operation vocabulary should remain small:

- `INSPECT` — read identity, authority, or evidence state;
- `GRANT` — create bounded delegated authority;
- `REVOKE` — remove delegated authority;
- `EXECUTE` — request a consequential action under existing authority;
- `GOVERN` — controller, recovery, succession, or other critical governance operations.

Natural language proposes these operations. It does not authorize them.

### Protected grant progression

A representative `GRANT` ceremony is:

    IDLE
      |
      v
    VOICE_REQUEST
      |
      v
    STRUCTURED_GRANT
      |
      v
    PRINCIPAL_AUTHENTICATED
      |
      v
    STEP_UP_REQUIRED
      |
      v
    CHALLENGE_SENT
      |
      v
    CHALLENGE_VERIFIED
      |
      v
    AUTHORITY_CHECKED
      |
      v
    GRANT_EXECUTED
      |
      v
    COMPLETE

Invalid transitions, missing evidence, expiry, replay, unresolved identity, or unresolved authority fail closed.

### Out-of-band challenge

Where consequence policy requires step-up, a challenge may be delivered through an independently enrolled email or SMS channel.

The challenge MUST be:

- unpredictable;
- short-lived;
- single-use;
- bound to the ceremony;
- bound to the requested operation and target;
- bound to the principal or bootstrap candidate where applicable;
- bound to the session where applicable;
- attempt-limited;
- replay-protected;
- consumed after successful use.

The human may read the challenge aloud to the voice agent. AssemblyAI may transcribe that response, but deterministic protected code verifies it.

The LLM MUST NOT decide whether a challenge is sufficiently correct.

The challenge establishes required factor possession only. It does not establish lifecycle authority.

The protected relationship is:

    authenticated principal
            +
    required step-up evidence
            +
    fresh UCII lifecycle authorization
            |
            v
    protected authority change

### Challenge delivery boundary

A delivery provider transports the challenge only.

Conceptually:

    ChallengeService
            |
            v
    ChallengeDeliveryProvider
            |
            +-- Email
            +-- SMS

The provider does not determine:

- UCII identity;
- controller authority;
- authorization;
- recovery legitimacy;
- delegation;
- revocation;
- execution eligibility.

Compromise of a communication provider must not become equivalent to compromise of UCII governance authority.

### Consequence-based step-up

Ceremony friction should correspond to consequence.

A low-consequence `INSPECT` may use the established authenticated session without an additional challenge.

A consequential `EXECUTE` requires the acting identity, matching delegated authority, and a fresh authorization decision.

A sensitive `GRANT` or `REVOKE` requires an authenticated legitimate controller, required step-up evidence, and a fresh lifecycle authorization decision.

Critical `GOVERN` or recovery operations require the strongest applicable governance path established by UCII.

Human confirmation remains separate from authorization.

### Bootstrap and durable governance

The first controller cannot be legitimized merely because someone asks by voice to become the owner.

Before implementation, the UCII core must be inspected to establish the real bootstrap and governance contract, including initial controller creation, controller custody, rotation, revocation, additional controllers, recovery, succession, and authority-domain durability.

The desired invariant is:

    authority domain != individual creator

The initial creator must not become an immortal root merely because they were first.

After activation, an ordinary caller must not be able to reopen bootstrap through a conversational request.

If UCII already supplies the necessary governance primitive, this application must use it. If a genuine reusable primitive is missing, it belongs in UCII core rather than in a hackathon-only alternate trust path.

### Public-boundary discipline

The application must use supported UCII SDK/API and legitimate protected lifecycle integration paths.

It MUST NOT:

- access the UCII database directly to manufacture authority;
- mint privileged credentials outside the legitimate lifecycle;
- treat voice or model output as controller authority;
- treat challenge possession as controller authority;
- treat payment or entitlement as controller authority;
- create an alternate trust root merely to simplify the demo.

Payment and authority remain distinct. A legitimate first-party entitlement may waive a payment requirement where supported, but it never creates authority.

### Proof surface

The primary judge-facing state should become:

    WHO
    HEARD
    REQUEST
    STEP-UP
    AUTHORITY
    DECISION
    RESULT

This allows the demonstration to show that an unauthorized principal's request was understood correctly while the lifecycle operation still receives `DENY` because legitimate authority was not established.

## Canonical demo state transitions

### State A — verified but unauthorized

- voice request understood;
- agent identity verified;
- matching delegated authority absent;
- UCII decision: DENY;
- executor not invoked.

### State B — bounded authority active

- human grants a constrained delegation;
- same agent remains verified;
- same request is repeated;
- UCII establishes matching authority;
- decision: ALLOW;
- executor performs the bounded action;
- provenance records the sequence.

### State C — revoked

- delegated authority is revoked;
- identity remains verified;
- technical capability remains available;
- same request is repeated;
- fresh UCII authority evaluation fails;
- decision: DENY;
- executor not invoked.

## Fail-closed principle

If identity, authority, request binding, expiry, revocation status, or required evidence cannot be established, the consequential action does not execute.

## Non-goals for the initial build

- general-purpose voice assistant platform;
- broad catalog of tools;
- autonomous expansion of authority;
- hidden prompt-based authorization;
- third-party identity or authorization system replacing UCII;
- unnecessary SaaS dependencies;
- changes to UCII core merely to make the demo easier unless a genuine reusable core requirement is independently established.
