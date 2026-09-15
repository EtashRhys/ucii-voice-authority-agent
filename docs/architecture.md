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
