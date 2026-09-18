# Implementation Plan

## Objective

Build the smallest complete voice-authority proof in which AssemblyAI is a genuine runtime component and UCII independently controls whether a proposed consequential action may execute.

## Engineering discipline

Use a bounded workflow:

**inspect → reason → one bounded change → targeted verification → diff/review → commit → checkpoint**

Avoid building several subsystems at once. Preserve a working checkpoint after each proven objective.


## 9.5+ demo critical path

The internal quality target is a judge-ready build capable of earning **9.5/10 or better**. This is a quality target, not a predicted score.

From this checkpoint forward, the governing completion path is:

**DENY → GRANT WITH STEP-UP → EXECUTE → REVOKE → DENY AGAIN**

This end-to-end lifecycle takes precedence over tool breadth, secondary voice scenarios, cosmetic polish, and optional features.

### Critical-path requirements

- [ ] Freeze one deterministic, safe, visibly consequential action.
- [ ] Voice input produces the stable structured proposal through real AssemblyAI runtime integration.
- [ ] Bind the proposal to real UCII identity state.
- [ ] Perform a fresh UCII authority check and prove initial DENY.
- [ ] Prove the executor did not run on DENY.
- [ ] Perform the protected human GRANT ceremony through the real supported lifecycle boundary.
- [ ] Require real request-bound step-up evidence where the frozen ceremony policy requires it.
- [ ] Preserve the rule that successful challenge verification is evidence, not lifecycle authority.
- [ ] Repeat the same consequential request.
- [ ] Perform a fresh UCII authority check and obtain genuine ALLOW.
- [ ] Make the executor structurally unreachable through the normal path until ALLOW.
- [ ] Execute the deterministic consequential action and record evidence.
- [ ] Revoke the exact delegation through the protected lifecycle boundary.
- [ ] Repeat the same consequential request again.
- [ ] Perform a fresh post-revocation authority check and prove DENY.
- [ ] Prove the executor did not run after revocation.
- [ ] Surface every meaningful transition through live UI state derived from the real path.
- [ ] Attach provenance/evidence references to the judge-visible transitions.

### Demo-completion gate

The project is not demo-complete because microphone capture, AssemblyAI, UCII verification, grant/revoke, executor, or UI work independently.

Demo completion requires one repeatable end-to-end run using real AssemblyAI input, real UCII identity/authority state, a real protected grant with required step-up, executor invocation only after genuine UCII ALLOW, real revocation, and a fresh post-revocation DENY.

Mocked identity, authority, authorization, grant, revocation, or judge-facing state do not satisfy this gate.

A deterministic simulator may be used for the final consequential side effect when that makes the demonstration safer and more reliable, provided the authorization and lifecycle boundaries controlling it are real and the simulator is identified accurately.

### Live proof UI requirements

The judge-facing console must update from actual runtime state and expose at minimum:

- [ ] finalized voice request / structured proposal;
- [ ] identity verified / not verified;
- [ ] delegated authority state and applicable scope;
- [ ] governance/lifecycle ceremony state where relevant;
- [ ] step-up required / verified / failed where applicable;
- [ ] policy/authorization decision;
- [ ] explicit ALLOW or DENY and reason;
- [ ] executor invoked / not invoked;
- [ ] execution result;
- [ ] provenance/evidence reference.

DENY states must be visually unmistakable.

### Reliability and Judge Mode

- [ ] Provide a deterministic reset / Judge Mode that restores the known initial no-authority state without bypassing security or manufacturing privilege.
- [ ] Rehearse the exact lifecycle until repeatable.
- [ ] Verify reset cannot serve as an alternate privileged lifecycle path.
- [ ] Record a tight 2–3 minute successful run before submission as backup/asynchronous judging evidence.
- [ ] Open the demo with the concise thesis: **"This agent can understand me and has the tool. Understanding and capability still do not equal authority."**

### Reality / stub disclosure

Before submission, README and demo materials must state exactly which boundaries are real and which, if any, remain temporarily simulated.

If the generalized HUMAN lifecycle-governance runtime primitive identified by Objective 0C remains incomplete when the application reaches its grant ceremony, do not disguise that fact. Preserve the frozen ceremony/application contract, identify the temporary seam precisely, and replace it with the real reusable UCII primitive as soon as that primitive exists.

No temporary seam may allow AssemblyAI, the LLM, challenge possession, payment, entitlement, or the voice agent itself to become an authority root.

### Scope freeze

Until the complete lifecycle passes the demo-completion gate:

- do not add additional consequential tools;
- do not expand into secondary voice scenarios;
- do not build optional governance/recovery features that are unnecessary for the frozen demo;
- do not prioritize cosmetic work over live-state correctness;
- do not sacrifice DENY-path clarity for feature breadth.

One excellent consequential action with real authority transitions is the priority.


## Objective 0A — Repository and documentation checkpoint

Goal: establish a proven engineering checkpoint and make the repository documentation reflect the current design before implementation begins.

- [x] Create dedicated public repository.
- [x] Record initial project concept.
- [x] Record initial governing architecture.
- [x] Establish MIT license.
- [x] Verify remote `main` checkpoint.
- [x] Create clean local checkout.
- [x] Inspect current concept, architecture, implementation, and demo documents.
- [x] Complete and commit the Human Authority Ceremony design upgrade.

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

## Objective 0C — UCII Authority Bootstrap / Governance Proof

Status: **COMPLETE — READ-ONLY ARCHITECTURAL PROOF**

The completed inspection established the current UCII authority chain, the
existing HUMAN governance/recovery contract, the reusable protected lifecycle
machinery, and the exact missing runtime seam required by this project.

Canonical findings:

- UCII machine/agent identity, credential, authentication, verification,
  delegated authority, authorization, economic separation, and execution
  boundaries remain established.
- HUMAN authentication establishes an authenticated UCII identity but does not
  automatically establish lifecycle governance authority.
- UCII already has an identity-scoped controller-authority capability with
  hash-only persistence and protected verification.
- protected delegated grant/revoke machinery already exists and should be
  reused rather than duplicated;
- UCII's existing HUMAN custody/recovery contract already requires independently
  established recovery/lifecycle authority and supports OOB confirmation,
  multiple independently governed credentials, administrators, recovery
  credentials, stronger factors, and quorum;
- the inspected runtime does not yet establish the generalized policy-governed
  relationship between an authenticated HUMAN principal and authority to
  originate specific lifecycle/governance operations;
- payment and first-party entitlement remain economically useful but cannot
  establish governance or action authority; and
- Voice, AssemblyAI, transcripts, LLM reasoning, authentication, confirmation,
  OOB challenges, payment, and entitlement must not become alternate authority
  roots.

The exact reusable implementation seam is therefore a UCII HUMAN lifecycle
governance authority layer above the existing protected controller lifecycle
machinery.

Detailed evidence and the factual authority-chain map are recorded in:

`docs/ucii-human-governance-authority-chain.md`

Objective 0C does not implement the missing primitive.

## Objective 0D — Freeze Human Authority Ceremony contract

Status: **COMPLETE — CONTRACT FROZEN AND SEMANTICALLY VERIFIED**

Canonical ceremony contract:

`docs/human-authority-ceremony-contract.md`

Completion proof:

- deterministic ceremony states and terminal outcomes defined;
- operation vocabulary and consequence classes frozen;
- principal, session, ceremony, operation, and target binding defined;
- OOB challenge lifecycle and deterministic spoken verification defined;
- challenge verification explicitly separated from lifecycle authority;
- AssemblyAI / LLM explicitly excluded as authority sources;
- bootstrap, governance, recovery, and factor-change boundaries defined;
- fresh lifecycle and execution authorization requirements defined;
- entitlement and x402 explicitly separated from authority;
- Guardian-specific behavior excluded as a Voice dependency;
- fail-closed and ambiguity behavior defined;
- proof/provenance and secret-exclusion requirements defined;
- post-revocation fresh authorization semantics verified;
- Objective 0C missing-runtime dependency preserved; and
- cross-document semantic review passed before completion.

Objective 0D freezes the contract only. It does not implement the missing UCII
HUMAN lifecycle-governance runtime primitive.

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
