# UCII Voice Authority Agent

> **Capability is not authority.**

A real-time AssemblyAI voice agent governed by UCII cryptographic identity and externally enforceable delegated authority.

**Live application:** https://voice.ucii.sportgen-ai.com/console-v2

## What it does

The voice agent can understand a request, reason about it, and propose an action. It does **not** decide for itself whether it has permission to act. UCII independently answers that question.

The final hackathon demonstration uses real AssemblyAI voice interaction and live UCII authority checks for two independent operations:

- `compute.purchase`
- `compute.inspect`

The demonstrated authority sequence is:

```text
compute.inspect   -> AUTHORIZED
compute.purchase  -> AUTHORIZED
human revokes purchase authority
compute.purchase  -> DENIED
compute.inspect   -> AUTHORIZED
```

The same Voice identity remains intact. Revoking one delegated capability does not destroy the identity or remove unrelated authority.

**Identity persists. Authority changes.**

## Why this matters

AI agents increasingly have the technical capability to call tools and APIs, access infrastructure, spend money, interact with enterprise systems, and control devices or robots.

Technical capability should not automatically create permission.

UCII Voice Authority separates:

**Voice != Intent != Identity != Authority != Execution**

The conversational model may understand and propose. UCII remains the external authority source.

## Architecture

```text
Human Voice
   |
   v
AssemblyAI Voice Agent
   |
   v
Structured Tool / Authority Request
   |
   v
Voice Authority Application
   |
   v
UCII Cryptographic Identity + Authority
   |
   +--> AUTHORIZED
   |
   +--> DENIED
   |
   v
Verified Voice Response + Visual Proof
```

### AssemblyAI

AssemblyAI provides the real-time conversational layer used by the project, including microphone interaction, live transcript handling, conversational voice responses, and structured tool calling.

### UCII

UCII provides the independent trust and authority layer: cryptographic AI-agent identity, protected credentials, delegated operation authority, fresh authorization checks, revocation, and authority-lifecycle evidence.

The AssemblyAI/LLM layer does not manufacture UCII authority.

## Security principle

A successful voice interaction proves that the system understood the human. It does **not** prove that the agent is authorized.

A verified identity proves who the agent is. It does **not** prove that the agent currently has permission for every operation.

Authority is separately delegated and separately revocable. The application therefore checks live UCII authority rather than treating model output, natural language, or tool availability as permission.

## Granular revocation

Before revocation:

```text
compute.purchase -> AUTHORIZED
compute.inspect  -> AUTHORIZED
```

After the human revokes purchase authority:

```text
compute.purchase -> DENIED
compute.inspect  -> AUTHORIZED
```

Only the targeted delegated capability is removed.

## Technology

- AssemblyAI Voice Agent
- Python / FastAPI
- Browser microphone and audio client
- Structured tool calls
- REST APIs
- UCII cryptographic identity and authority infrastructure
- ML-DSA-65 protected signing identity
- Protected controller/lifecycle authority
- Live delegated-authority evaluation and revocation

## Repository structure

```text
src/voice_authority/
    main.py
    console-v2.html
    ucii_authority_client.py
    protected_signer_client.py
    structured_proposal.py
    voice_lifecycle_cli.py

docs/
    architecture.md
    assemblyai-technical-contract.md
    demo-script.md
    human-authority-ceremony-contract.md
    judging-strategy.md
    submission-checklist.md
    voice-authority-project-status.md
```

## Core design rule

> **The LLM can propose. UCII decides whether the proposal is authorized.**

This allows an autonomous system to retain its identity and technical capabilities while humans and external policy control the specific authority it possesses.

## Broader application

The same architecture can govern autonomous systems operating payments, APIs, cloud infrastructure, enterprise services, robots, devices, machine-to-machine services, and other AI agents.

The goal is not to make an AI incapable of acting. The goal is to let it act **without giving it unlimited authority**.

---

**UCII Voice Authority Agent — AssemblyAI Voice Agent Hackathon, September 2026**
