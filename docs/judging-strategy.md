# Judging Strategy

## Positioning

Do not position this as merely another voice chatbot or transcription interface.

The project should answer a harder question:

> When a voice agent understands a human request and has the technical capability to call a consequential tool, what independently determines whether it is actually allowed to execute?

UCII is the answer demonstrated by the build.

## Core judge takeaway

**Capability is not authority.**

The strongest proof is not a slide. It is the same real agent, with the same verified identity and same available tool, producing different execution outcomes solely because the independently verifiable authority state changed.

## 9.5+ quality target

The internal quality target is a judge-ready build capable of earning **9.5/10 or better**. This is an engineering and presentation target, not a prediction or guarantee of a competition score.

The highest-leverage requirement is one clean, reliable, end-to-end live proof:

**DENY → GRANT WITH STEP-UP → EXECUTE → REVOKE → DENY AGAIN**

The project is not demo-complete merely because each subsystem works independently. Demo completion requires one repeatable end-to-end run using real AssemblyAI input, real UCII identity/authority state, a real protected grant with required step-up, executor invocation only after a genuine UCII ALLOW, real revocation, a fresh post-revocation DENY, and a live proof UI derived from those actual states rather than presentation mocks.

Documentation, architecture, extra tools, and secondary scenarios do not substitute for this proof.

## Demo narrative

### 1. Establish capability

Speak the consequential request. AssemblyAI understands it and produces the proposed action.

### 2. Establish identity

Show that UCII cryptographically verifies the acting agent.

### 3. Deny

Show that verified identity is insufficient: no matching authority means the executor does not run.

### 4. Grant narrowly with step-up

Grant a bounded delegation tied to the relevant identity/action/scope/limit/expiry through the protected Human Authority Ceremony. Where policy requires step-up, the challenge must be real, request-bound, fresh, one-use, and independently verified. Challenge success confirms the required ceremony evidence; it does not itself manufacture lifecycle authority.

### 5. Execute

Repeat the same spoken request. A fresh UCII authority evaluation permits the action, and only then does the deterministic executor run. Execution evidence appears.

### 6. Revoke

Revoke the exact delegation without destroying the identity.

### 7. Deny again

Repeat the same request. AssemblyAI still understands it. The identity still verifies. The tool still exists. A fresh UCII evaluation denies execution because authority is revoked.

## Judge-facing proof surface

The UI must be a live proof surface, not a mockup. It must derive displayed state from the actual application/UCII execution path.

At minimum, make these facts immediately visible:

- finalized voice request / structured proposal;
- UCII identity verification state;
- current delegated authority state and relevant scope;
- governance/lifecycle ceremony state where applicable;
- step-up status when required;
- fresh policy/authorization decision with explicit ALLOW or DENY;
- reason for DENY;
- executor invoked / not invoked;
- execution result when allowed;
- provenance/evidence reference after meaningful transitions.

DENY must be visually unmistakable. A judge should not need source-code knowledge to determine whether execution was structurally blocked.

The first 20–30 seconds should establish the thesis:

> **This agent can understand me and has the tool. Understanding and capability still do not equal authority.**

## Demo reliability gate

The six-scene authority cycle must become boringly repeatable before secondary expansion:

**DENY → GRANT WITH STEP-UP → EXECUTE → REVOKE → DENY AGAIN**

Provide a deterministic Judge Mode / reset path that restores the demo to the known initial no-authority state without manufacturing authority or bypassing normal security boundaries.

Practice the exact sequence repeatedly. Before submission, record a tight 2–3 minute video of a proven run as a backup and as the primary asynchronous judging artifact where appropriate.

A reset control is operational convenience only. It must not become an alternate privileged authority path.

## Reality and disclosure standard

The README, demo, and presentation must distinguish clearly between:

- operations using the real UCII public/authoritative boundary;
- real AssemblyAI runtime behavior;
- real protected authority state and lifecycle transitions;
- deterministic local simulation used only for the safe consequential side effect, if selected;
- any temporarily stubbed lifecycle/governance seam that remains because the generalized HUMAN lifecycle-governance primitive is not yet implemented.

Do not imply production completeness for a stub. If a seam must temporarily be simulated, state exactly what is simulated and preserve the application contract so the real UCII primitive can replace it without changing the security model.

A deterministic consequential simulator is acceptable for the final side effect when it improves reliability; mocked identity, mocked authority decisions, mocked revocation, or a UI that merely pretends those states changed are not acceptable for the core proof.

## What this prevents

Make the prevented failures explicit:

- the voice agent cannot self-grant authority;
- understanding a command cannot create permission;
- the agent cannot expand its own scope, budget, resource, or expiry;
- successful OOB challenge possession cannot manufacture governance authority;
- payment or entitlement cannot manufacture authority;
- the executor cannot run through the normal application path without a genuine UCII ALLOW;
- revocation cannot be ignored by a stale decision;
- the same request must fail after revocation even though identity, voice capability, and tool availability remain intact.

## Differentiators to make visible

- real AssemblyAI voice integration rather than sponsor-name decoration;
- cryptographic agent identity independent of conversational claims;
- explicit separation of voice, intent, identity, authority, and execution;
- bounded delegated authority rather than broad permanent permission;
- protected human grant ceremony with step-up where required;
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
- polishing secondary features before the complete authority cycle is reliable;
- presenting mocked UI state as authoritative state;
- implying a competition result before judging.

## Presentation priority

A judge should understand the differentiator in the first few seconds:

**The voice system understands and proposes. UCII independently decides whether the verified agent has authority to act.**

Everything else should reinforce that sentence.
