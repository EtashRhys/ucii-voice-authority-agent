# Implementation Plan

## Objective

Build the smallest complete voice-authority proof in which AssemblyAI is a genuine runtime component and UCII independently controls whether a proposed consequential action may execute.

## Engineering discipline

Use a bounded workflow:

**inspect → reason → one bounded change → targeted verification → diff/review → commit → checkpoint**

Avoid building several subsystems at once. Preserve a working checkpoint after each proven objective.

## Objective 0A — Repository and documentation checkpoint

Goal: establish a proven engineering checkpoint and make the repository documentation reflect the current design before implementation begins.

- [x] Create dedicated public repository.
- [x] Record initial project concept.
- [x] Record initial governing architecture.
- [x] Establish MIT license.
- [x] Verify remote `main` checkpoint.
- [x] Create clean local checkout.
- [x] Inspect current concept, architecture, implementation, and demo documents.
- [ ] Complete and commit the Human Authority Ceremony design upgrade.

Acceptance: repository state is known and the canonical project documents reflect the current authority design before implementation begins.

## Objective 0B — Current AssemblyAI technical contract

Goal: establish the current supported AssemblyAI integration contract from authoritative sources before writing voice code.

Read-only first.

Inspect:

- current Voice Agent / real-time architecture;
- current SDK/API surfaces;
- authentication model;
- session establishment;
- browser/server responsibilities;
- turn and finalization behavior;
- structured action/tool support;
- interruption behavior where relevant;
- recommended integration architecture;
- current hackathon technical and submission requirements.

Do not code from memory.

Acceptance: the selected voice architecture is based on the current supported AssemblyAI contract and current competition requirements.

## Objective 0C — UCII authority bootstrap and governance proof

Goal: establish the actual UCII authority chain before allowing the Voice Agent to create, modify, revoke, recover, or govern authority.

Read-only first.

Inspect the current UCII implementation and contracts for:

- initial authority-domain bootstrap;
- initial controller creation;
- controller authority representation;
- controller credential creation and custody;
- controller authentication and verification;
- protected delegation lifecycle;
- delegation revocation;
- controller rotation;
- additional-controller management;
- authority transfer or succession where supported;
- recovery mechanisms;
- controller loss and compromise behavior;
- authority-domain durability;
- public versus private integration boundaries;
- payment and entitlement separation.

The inspection must establish with implementation evidence:

- who may grant the Voice Agent delegated authority;
- why UCII trusts that grant;
- what evidence legitimates the controller;
- how controller authority can be revoked or rotated;
- whether revoking one controller preserves the authority domain;
- whether another legitimate controller can continue governance;
- how recovery is authorized and bounded;
- how succession or replacement works where supported;
- whether any public credential or API path can manufacture privilege;
- that an ordinary delegated agent cannot self-expand into governance authority;
- that a voice or LLM request cannot create governance authority;
- that challenge possession cannot create governance authority;
- that payment or entitlement cannot create governance authority.

Produce a factual authority-chain map before implementation.

The acceptance question is:

Who has authority to grant the Voice Agent permission, why does UCII trust that grant, how can that authority later be revoked or transferred, and how does legitimate governance survive loss or revocation of an individual controller without creating an immortal root user?

If UCII already satisfies the requirement, use the existing primitive through its legitimate supported boundary.

If a genuine primitive is missing, make the smallest reusable correction in UCII core rather than creating hackathon-only alternate authority machinery.

## Objective 0D — Freeze Human Authority Ceremony contract

Goal: freeze the deterministic ceremony contract only after the UCII authority chain is understood.

Define:

- operation vocabulary: `INSPECT`, `GRANT`, `REVOKE`, `EXECUTE`, `GOVERN`;
- structured security-relevant fields;
- principal binding;
- session binding where applicable;
- consequence-based step-up policy;
- challenge lifecycle;
- lifecycle authorization requirement;
- execution authorization requirement;
- provenance/evidence contract;
- fail-closed behavior;
- ambiguity behavior.

A sensitive authority-changing operation must preserve the relationship:

    authenticated legitimate principal
            +
    required step-up evidence
            +
    fresh UCII lifecycle authorization
            |
            v
    protected lifecycle operation

Challenge verification is not lifecycle authorization.

Human confirmation is not authorization.

Acceptance: protected state transitions and their required evidence are deterministic and code-controlled before the voice implementation depends on them.

## Phase 1 — AssemblyAI voice proof

Goal: prove real microphone-to-AssemblyAI interaction independently of consequential execution.

- [ ] Inspect current AssemblyAI Voice Agent API/SDK and authentication model.
- [ ] Select the smallest supported browser/server architecture.
- [ ] Establish microphone input.
- [ ] Establish real-time AssemblyAI session.
- [ ] Produce an attributable structured proposed action from a spoken request.
- [ ] Verify interruption/turn behavior only if required for the final demo.

Acceptance: a spoken test request reaches the application as a stable structured proposal with no UCII authority implied.

## Phase 2 — UCII identity binding

Goal: bind the proposed action to a real UCII agent identity through the public UCII boundary.

- [ ] Inspect exact SDK/API calls needed from the current UCII production contract.
- [ ] Configure the application without embedding private UCII secrets in the public repo.
- [ ] Establish agent identity verification.
- [ ] Surface verification state in the proof UI.

Acceptance: the application can prove which UCII identity is proposing the action, independently of the voice transcript/model assertion.

## Phase 3 — Denial boundary

Goal: prove that a verified voice agent with technical capability but no matching authority cannot execute.

- [ ] Define one deterministic consequential action.
- [ ] Define its canonical authorization operation/resource/scope.
- [ ] Route every normal execution attempt through the UCII authority gateway.
- [ ] Return explicit DENY when authority is absent or invalid.
- [ ] Prove executor was not invoked.

Acceptance: **verified identity + understood request + available tool + no authority = no execution**.

## Phase 4 — Bounded grant and execution

Goal: prove that a human-created bounded delegation changes the execution result without changing the agent identity.

- [ ] Establish the narrowest supported grant/delegation flow.
- [ ] Bind authority to the intended identity and operation.
- [ ] Include meaningful scope/limit/expiry where supported.
- [ ] Repeat the same voice request.
- [ ] Require a fresh UCII authority decision.
- [ ] Execute only after ALLOW.
- [ ] Record execution/provenance evidence.

Acceptance: same verified agent and same request execute only while matching bounded authority exists.

## Phase 5 — Revocation proof

Goal: prove authority can be removed while identity and capability remain intact.

- [ ] Revoke the exact delegated authority.
- [ ] Repeat the same spoken request.
- [ ] Perform a fresh authority evaluation.
- [ ] Return DENY.
- [ ] Prove executor was not invoked after revocation.

Acceptance: **same identity + same capability + revoked authority = no execution**.

## Phase 6 — Judge-facing proof UI

- [ ] Live/final transcript or request display.
- [ ] Structured proposed action display.
- [ ] UCII identity verification state.
- [ ] Delegated authority state.
- [ ] ALLOW/DENY decision.
- [ ] Execution result.
- [ ] Provenance/evidence reference.
- [ ] Clear reset/demo controls if needed.

Acceptance: a judge can understand the security transition without reading source code.

## Phase 7 — Hardening and adversarial validation

Test at least:

- [ ] no authority;
- [ ] wrong identity;
- [ ] wrong operation/resource;
- [ ] over-limit request;
- [ ] expired authority;
- [ ] revoked authority;
- [ ] malformed/unbound proposed action;
- [ ] replay where relevant;
- [ ] voice/LLM attempt to claim or fabricate authority;
- [ ] executor direct/bypass attempt at the application boundary.

## Phase 8 — Submission package

- [ ] README quick start.
- [ ] Architecture diagram.
- [ ] Public repository hygiene/security review.
- [ ] Product feedback.
- [ ] Friction log.
- [ ] Demo script.
- [ ] Demo video.
- [ ] Presentation/pitch material if required.
- [ ] Working deployment/demo access if required.
- [ ] Final requirements audit.
- [ ] Submit before deadline with buffer.

## Scope control

The winning version of this project does not require many tools or many voice scenarios. One consequential action with excellent identity/authority/revocation/provenance evidence is preferable to a broad but shallow assistant.
