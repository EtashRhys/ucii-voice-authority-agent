# UCII Voice Authority Agent

A UCII-governed voice agent using AssemblyAI for real-time voice interaction with cryptographic identity, bounded delegated authority, revocation, and verifiable execution provenance.

## Core idea

The project demonstrates that understanding a spoken request is not the same thing as being authorized to execute it.

```text
Human Voice
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

## Security model

The project keeps these domains separate:

**Voice ≠ Intent ≠ Identity ≠ Authority ≠ Execution**

The voice layer may interpret a request and propose an action, but it does not create execution authority. UCII remains the independent trust and authority layer.

## Primary demo

1. A user speaks a consequential request.
2. AssemblyAI interprets the request and produces a structured proposed action.
3. UCII verifies the agent identity.
4. The agent has no matching delegated authority, so execution is denied.
5. A human grants tightly bounded authority for the exact action class, amount/scope, and expiry.
6. The same spoken request is repeated and succeeds.
7. The delegated authority is revoked.
8. The same cryptographically verified agent attempts the same action again and is denied.

The identity remains valid throughout. Only the authority state changes.

## Design principle

**Capability is not authority.**

The LLM/voice agent can propose. UCII decides whether the proposal is authorized to become a real action.

## Planned stack

- AssemblyAI Voice Agent API
- Browser microphone client
- Small Python/FastAPI application backend
- UCII public SDK/API boundary
- Deterministic consequential tool executor
- Compact visual status panel for identity, authority, decision, and provenance

## Repository purpose

This repository is the dedicated competition and reference implementation for the UCII voice-authority interaction surface. It is intentionally separate from the UCII core repository and from other environment-specific adapters such as Alexa+.

See `docs/` for the detailed project contract, architecture, implementation plan, judging strategy, demo plan, and submission checklist.
