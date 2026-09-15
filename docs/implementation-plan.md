# Implementation Plan

## Objective

Build the smallest complete voice-authority proof in which AssemblyAI is a genuine runtime component and UCII independently controls whether a proposed consequential action may execute.

## Engineering discipline

Use a bounded workflow:

**inspect → reason → one bounded change → targeted verification → diff/review → commit → checkpoint**

Avoid building several subsystems at once. Preserve a working checkpoint after each proven objective.

## Phase 0 — Foundation

- [x] Create dedicated public repository.
- [x] Record project concept.
- [x] Record governing architecture.
- [x] Establish MIT license.
- [ ] Verify current event requirements from authoritative sources.
- [ ] Freeze the minimum submission contract.

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
