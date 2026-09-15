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
