# Project Concept

## UCII Voice Authority Agent

The UCII Voice Authority Agent is a voice-driven autonomous-agent reference implementation in which AssemblyAI provides the real-time conversational voice interface and UCII independently governs cryptographic identity, delegated authority, revocation, execution eligibility, and provenance.

The project exists to demonstrate a simple but important boundary:

> Understanding what a human said does not establish authority to act on it.

## Problem

Voice agents are increasingly able to understand requests, reason about them, call tools, and initiate real-world actions. A successful transcription, intent classification, or LLM tool call does not answer the security question: **is this agent actually authorized to perform this consequential action?**

Treating model confidence, conversational context, or a user's spoken request as execution authority collapses distinct trust domains.

## UCII proposition

This project keeps them separate:

**Voice ≠ Intent ≠ Identity ≠ Authority ≠ Execution**

AssemblyAI may establish what was spoken and participate in conversational/tool orchestration. UCII independently establishes whether the acting agent has a verified identity and whether a valid delegated authority permits the proposed operation.

The executor accepts only an authorized action. The voice/LLM layer cannot mint, expand, or substitute for authority.

## Human Authority Ceremony

The voice interface must also support protected human authority changes without turning conversation itself into authority.

For a sensitive `GRANT`, `REVOKE`, governance, or recovery operation, the intended pattern is:

1. the human requests the operation conversationally;
2. AssemblyAI produces a bounded structured proposal;
3. the relevant human principal is authenticated through the legitimate UCII path;
4. consequence policy determines whether step-up verification is required;
5. a short-lived, single-use challenge is delivered through an independently enrolled out-of-band channel such as email or SMS;
6. the human reads that challenge aloud;
7. AssemblyAI transcribes the response;
8. deterministic protected code verifies the challenge;
9. UCII performs a fresh lifecycle-authority check for the exact requested operation;
10. only then may the protected authority change occur.

The challenge proves possession of an enrolled factor. **It does not itself create authority.**

This preserves the stronger separation:

**Voice ≠ Intent ≠ Identity ≠ Authentication ≠ Authority ≠ Execution**

The reusable component behind this flow is a **Human Authority Ceremony Engine**: a deterministic state machine for protected bootstrap, step-up, grant, revoke, governance, recovery, and factor-enrollment/change ceremonies. AssemblyAI is the conversational interface to that engine, not its authority source.

## Bootstrap and governance prerequisite

Before implementing the first Voice Agent delegation, this project must inspect the actual UCII bootstrap and governance implementation and establish with evidence:

- who has authority to grant the Voice Agent delegated authority;
- why UCII trusts that controller;
- how initial and additional controller authority is established;
- how controller credentials are held, verified, rotated, and revoked;
- how governance survives loss or revocation of an individual controller;
- what recovery and succession mechanisms exist;
- that an ordinary delegated agent cannot promote itself into governance authority;
- that voice, LLM output, payment, entitlement, or possession of a challenge cannot manufacture authority.

If UCII already provides the required primitive, this project must use it through the legitimate supported boundary.

If a genuine primitive is missing, the correction belongs in UCII core as the smallest reusable improvement rather than as a hackathon-only alternate trust root.

## Primary proof

The same voice agent performs the same requested operation under changing authority state:

1. **Verified identity / no authority** — denied.
2. **Bounded authority granted** — permitted and executed.
3. **Authority revoked** — denied again.

The agent's identity and technical capability remain intact throughout the demonstration. Only the independently established authority state changes.

## Example consequential action

A representative demo request is:

> Purchase 20 units of compute for this workload.

The exact final tool may change during implementation, but it must remain deterministic, consequential enough to make authorization meaningful, safe for demonstration, and independently verifiable in the UI/provenance record.

A bounded delegation might constrain:

- permitted operation or category;
- maximum amount or quantity;
- target/resource scope;
- authorized agent identity;
- expiration;
- one-shot or repeat-use semantics where applicable.

## What this is not

This is not a generic talking chatbot, a voice transcription demo, or a policy prompt that asks an LLM to behave safely. It is not a replacement for UCII and it does not copy the UCII core into this repository.

It is an environment-specific voice interaction surface built against the UCII public boundary.

## Long-term value

The competition provides the forcing function, but the artifact is intended to survive it. The reusable capability is a UCII-governed voice-authority pattern that can later be adapted to other voice interfaces, devices, assistants, autonomous systems, and consequential tool environments.
