# Judging Strategy

## Positioning

Do not position this as merely another voice chatbot or transcription interface.

The project should answer a harder question:

> When a voice agent understands a human request and has the technical capability to call a consequential tool, what independently determines whether it is actually allowed to execute?

UCII is the answer demonstrated by the build.

## Core judge takeaway

**Capability is not authority.**

The strongest proof is not a slide. It is the same real agent, with the same verified identity and same available tool, producing different execution outcomes solely because the independently verifiable authority state changed.

## Demo narrative

### 1. Establish capability

Speak the consequential request. AssemblyAI understands it and produces the proposed action.

### 2. Establish identity

Show that UCII cryptographically verifies the acting agent.

### 3. Deny

Show that verified identity is insufficient: no matching authority means the executor does not run.

### 4. Grant narrowly

Grant a bounded delegation tied to the relevant identity/action/scope/limit/expiry.

### 5. Execute

Repeat the same spoken request. A fresh UCII authority evaluation permits the action, and execution evidence appears.

### 6. Revoke

Revoke the delegation without destroying the identity.

### 7. Deny again

Repeat the same request. AssemblyAI still understands it. The identity still verifies. The tool still exists. UCII denies execution because authority is revoked.

## Differentiators to make visible

- real AssemblyAI voice integration rather than sponsor-name decoration;
- cryptographic agent identity independent of conversational claims;
- explicit separation of voice, intent, identity, authority, and execution;
- bounded delegated authority rather than broad permanent permission;
- revocation that removes authority without deleting identity;
- fresh authority evaluation before consequential execution;
- executor structurally downstream of authorization;
- verifiable provenance/evidence;
- fail-closed behavior when required trust facts are absent.

## Avoid

- claiming that UCII invented voice agents or agent identity as a category;
- relying on buzzwords instead of executable proof;
- presenting LLM self-restraint as authorization;
- overbuilding many tools at the expense of one excellent authority proof;
- hiding the DENY path;
- making the demo depend on fragile external side effects when a deterministic consequential simulator can prove the architecture more reliably;
- implying a competition result before judging.

## Presentation priority

A judge should understand the differentiator in the first few seconds:

**The voice system understands and proposes. UCII independently decides whether the verified agent has authority to act.**

Everything else should reinforce that sentence.
