# UCII Voice Authority Agent — Project Status

**Status date:** September 20, 2026

**Purpose:** This is the current project-status reference for Voice Authority. Use this instead of the historical build timeline when answering what has been completed, what is blocked, and what remains.

> **Core thesis:** Understanding a request does not create authority to execute it.

> **Security separation:** Voice is not intent. Intent is not identity. Identity is not authentication. Authentication is not step-up. Step-up is not authority. Authority is not authorization. Authorization is not entitlement. Entitlement is not payment. Payment is not execution.

---

## 0. Architecture and security model — COMPLETE

The fundamental architecture is established and documented.

- Core thesis established: **Understanding a request does not create authority to execute it.**
- AssemblyAI is strictly voice/conversation infrastructure.
- UCII remains the authoritative control plane.
- Voice-specific alternate trust roots are prohibited.
- Guardian-specific authority remains separate.
- First-party entitlement is explicitly separate from authority.
- HUMAN governance architecture is defined.
- Human Authority Ceremony contract is established.
- Security and provenance boundaries are established.

---

## 1. AssemblyAI runtime integration — LARGELY COMPLETE

The Voice side is already considerably beyond a prototype architecture.

Completed:

- AssemblyAI Voice Agent runtime selected.
- Browser/server architecture.
- Temporary browser-token architecture.
- Real WebSocket session establishment.
- Microphone/audio pipeline.
- Live input-turn observability.
- Partial and final transcript boundaries.
- Finalized-turn handling.
- Agent response/audio handling.
- Interruption semantics.
- Tool-call architecture.
- `propose_compute_purchase` bounded proposal.
- AssemblyAI tool calls are explicitly treated as proposals, not authorization.
- Voice Console/proof-UI foundation.

**Current assessment:** AssemblyAI is not the current project blocker.

---

## 2. UCII Voice identity — COMPLETE

The production identity exists and must not be recreated.

- Name: AssemblyAI Voice Authority Agent
- Type: AI_AGENT
- Identity ID: `9df0ff8a-25d0-4340-be32-05e8263f1277`
- Protected enrollment complete.
- Production identity active.
- Enrollment capability consumed.
- Controller-authority binding established.
- Durable production state established.

---

## 3. Voice cryptographic signing identity — COMPLETE

The Voice agent has its real production signing credential.

- ML-DSA-65 credential provisioned.
- Credential registered with UCII.
- Private key protected.
- Public-key/fingerprint binding verified.
- Protected signing proven cryptographically.
- Voice process cannot read the private key.
- Credential custody hardened to mode `0600`.
- No private key is stored in the UCII database.

This was a major production milestone.

---

## 4. Dedicated privilege separation — COMPLETE

Voice Authority has its own protected production security domain.

- Dedicated application Unix principal.
- Dedicated signer Unix principal.
- Dedicated signer IPC group.
- Dedicated protected Unix socket.
- Dedicated signer service.
- Protected signer service active.
- Voice application cannot read signer custody.
- Root-owned encrypted custody.
- No dependence on Guardian's signer or custody.

---

## 5. Voice controller authority — COMPLETE

Dedicated Voice controller authority exists.

- Identity-bound controller authority.
- Encrypted systemd credential custody.
- Correct lifecycle-loader format.
- Production loader acceptance proven.
- No plaintext exposure.
- Guardian authority isolated.
- Enrollment artifacts cleaned up.
- Production issuer enabled.

**Do not reopen this work.**

---

## 6. UCII entitlement/economic boundary — COMPLETE FOR CURRENT NEED

First-signing provisioning already produced the required first-party service entitlement.

- Active Voice service entitlement.
- Identity scoped.
- Covers the UCII authorization-execution economic path.
- UCII does not need to pay itself through x402.
- Entitlement does not create authority.

**Invariant:** Entitlement may waive payment. Entitlement is not authority.

Do not invent a second entitlement unless a real consumer proves one is required.

---

## 7. Generic delegated ActionAuthority — COMPLETE

UCII now supports generic delegated authority execution.

Completed:

- Exact operation authority.
- ACTIVE, REVOKED, EXPIRED, INVALID, and NOT_GRANTED states.
- Exact operation matching.
- No wildcard authority.
- Fresh evaluation on execution.
- Grant.
- Revoke.
- Historical authority preserved.
- Revoked authority cannot execute.
- Credential proof required.
- Authenticated identity required.
- Identity/credential binding required.
- Economic authorization remains separate.
- Protected execution occurs only after authorization.

Current Voice operation: `compute.purchase`.

---

## 8. Protected lifecycle authorization — COMPLETE

Grant and revoke cannot authorize themselves.

UCII now has:

- One-use controller lifecycle authorization.
- Exact identity binding.
- Exact operation and scope binding.
- Exact grantor binding.
- Exact revoke-authority and reason binding.
- Expiration.
- Maximum use count of one.
- Durable consumption.
- Provenance.
- Replay prevention.
- Protected controller lifecycle service.

An ordinary API caller therefore cannot simply request authority and manufacture it.

---

## 9. HUMAN step-up machinery — COMPLETE

UCII already contains the machinery necessary after legitimate HUMAN governance exists.

Completed:

- HumanGovernanceRelationship.
- Governance evaluator.
- Governance relationship service.
- HUMAN step-up factors.
- Step-up challenge issuance.
- Challenge expiration.
- Attempt limits.
- Deterministic verification.
- One-time consumption.
- Durable step-up evidence.
- Ceremony binding.
- Session binding.
- HUMAN identity binding.
- Target identity binding.
- Operation binding.

**Invariant:** Step-up verification is not authority.

---

## 10. HUMAN lifecycle authorization — COMPLETE

Once legitimate HUMAN governance exists, UCII supports this chain:

**Authenticated HUMAN → governance relationship → step-up evidence → HumanLifecycleAuthorization → protected grant/revoke.**

UCII can issue short-lived, one-use HUMAN lifecycle authorization with exact bindings.

This machinery is already present.

---

## 11. First-HUMAN governance bootstrap — CURRENT BLOCKER

This is the architectural hole discovered during production integration.

Production currently has zero HUMAN identities.

More importantly, UCII currently lacks the legitimate transition:

**No HUMAN governance → protected first-HUMAN bootstrap → first legitimate HUMAN governance.**

Simply calling `HumanGovernanceRelationshipService.establish()` is **not legitimate bootstrap**.

That service explicitly expects the caller's authority to have been established independently. Creating a HUMAN row, factor, or relationship directly merely to unblock the demo would create an alternate trust root and is prohibited.

### Unit 3G — IMMEDIATE NEXT WORK

**Protected First-HUMAN Bootstrap Reuse Boundary**

Unit 3G remains read-only first. Only after that inspection should the smallest correct implementation justified by the evidence begin.

Unit 3G must answer:

- Can existing protected controller authority anchor bootstrap?
- What constitutes an uninitialized governance domain?
- How is the first HUMAN legitimately established?
- How does bootstrap permanently close afterward?
- How is authority scoped to the Voice governance domain rather than all UCII?
- How does normal controller succession work?
- What recovery architecture must bootstrap preserve?
- How does factory reset work conceptually?
- Do governance generation/epoch semantics belong at the shared domain layer?
- What machine-side lifecycle pieces already exist?
- Can HUMAN and machine lifecycle share a governance-domain abstraction?

This is the current critical-path blocker.

---

## 12. Governance recovery and reset architecture — DESIGN REQUIREMENT

This requirement was discovered while analyzing first-HUMAN bootstrap.

The complete recovery/reset implementation is **not required before Voice can resume**, but bootstrap must not make these lifecycle operations impossible.

Required lifecycle:

**Bootstrap → normal governance → succession → recovery → factory reset → new governance generation.**

Still required eventually:

- Independent recovery authority.
- Lost-controller recovery.
- Compromised-controller recovery.
- Controller succession/replacement.
- Factory reset.
- Generation/epoch invalidation.
- Prevention of stale-authority resurrection.
- Cross-identity lifecycle treatment.

### Cross-identity requirement

The same inspection must cover machine identities.

**Machine identity is not governance authority.**

AI_AGENT, ROBOT, DEVICE, SERVICE, ORGANIZATION, and future identity types should not require separate incompatible authority roots if a reusable governance-domain lifecycle can safely serve them.

Machine credential possession must not automatically mean ultimate governance or ownership authority over that machine.

Unit 3G must distinguish which machine-side recovery/reset guarantees already exist, which are partial, and which remain future UCII-core work.

---

## 13. Establish Brad as Voice-domain HUMAN governor — BLOCKED BY UNIT 3G

Once the reusable bootstrap primitive exists, the intended chain is:

**Voice governance domain → protected bootstrap ceremony → Brad HUMAN identity → credential/authentication → step-up factor → HUMAN governance relationship → bootstrap CLOSED.**

This establishes governance for **this Voice Authority domain**. It must not create a universal UCII master account.

---

## 14. Voice GRANT ceremony — NEXT AFTER BOOTSTRAP

Target flow:

**Brad asks to allow the Voice Authority Agent to purchase compute → AssemblyAI produces a structured GRANT proposal → Brad authenticates → step-up challenge → challenge verification → fresh HUMAN governance evaluation → one-use lifecycle authorization → protected GRANT → `compute.purchase` becomes ACTIVE.**

Still to complete/integrate:

- Voice GRANT conversational flow.
- Out-of-band challenge delivery.
- Spoken challenge response.
- HUMAN lifecycle authorization invocation.
- Protected grant.
- Evidence UI.

---

## 15. Authorized EXECUTE ceremony — REMAINING

Canonical demonstration request:

> Purchase $35 of compute.

The completed flow must prove:

- Voice understands the request.
- Structured request is generated.
- Voice AI_AGENT is authenticated.
- ML-DSA proof is generated through the protected signer.
- Fresh ActionAuthority check occurs.
- `compute.purchase` is ACTIVE.
- Economic/budget policy accepts the amount.
- Entitlement handles the UCII economic requirement.
- Execution occurs.
- Provenance/evidence is displayed.

One technical inspection remains:

**Exact production authentication-token acquisition for the existing Voice AI_AGENT.**

The execute route is known to require it. The correct production acquisition path has not yet been proven and must not be guessed.

---

## 16. Amount-bound policy — REMAINING

Important distinction:

Authority for `compute.purchase` does **not** inherently mean authority for `compute.purchase <= $35`.

The **$35 ALLOW / $5,000 DENY** demonstration therefore requires a real independent budget/economic policy.

Still required:

- Locate the existing budget-policy seam.
- Verify exact amount binding.
- Connect it to Voice structured parameters.
- Demonstrate $35 ALLOW.
- Demonstrate $5,000 DENY.

This must not be faked in the UI or falsely represented as a property of ActionAuthority.

---

## 17. REVOKE ceremony — REMAINING

Target flow:

**Brad asks to revoke the Voice Agent's compute authority → step-up → fresh HUMAN governance evaluation → one-use lifecycle authorization → protected REVOKE → ActionAuthority becomes REVOKED.**

Still required:

- Voice REVOKE conversational flow.
- Protected revoke.
- Evidence presentation.

---

## 18. Post-revocation proof — REMAINING

Immediately repeat the formerly authorized request:

> Purchase $35 of compute.

UCII must perform a **fresh** authority evaluation.

Expected result:

- Identity: VERIFIED
- Credential: VERIFIED
- Authentication: VALID
- Authority: REVOKED
- Decision: DENY
- Execution: NONE

This demonstrates the core property:

> **Identity survives revocation. Authority does not.**

---

## 19. Final proof UI and judge experience — PARTIAL

The foundation exists.

Final integration should let judges visibly follow:

- **WHO?** Brad / Voice Agent
- **WHAT?** `compute.purchase` / $35
- **AUTHORITY?** NONE → ACTIVE → REVOKED
- **STEP-UP?** VERIFIED
- **DECISION?** DENY → ALLOW → DENY
- **EXECUTION?** NO → YES → NO
- **EVIDENCE?** UCII cryptographic/provenance references

There must be no hard-coded security green lights. Every security status must derive from actual evidence.

---

## 20. Final end-to-end hackathon demonstration — FINAL TARGET

The north-star sequence remains:

1. **Voice requests compute with no delegated authority → DENY.**
2. **Brad grants bounded authority by voice → HUMAN step-up → UCII GRANT.**
3. **$35 compute request → authority ACTIVE + budget accepted → ALLOW.**
4. **$5,000 request → economic/bound policy fails → DENY.**
5. **Brad revokes authority → HUMAN step-up → UCII REVOKE.**
6. **Repeat $35 request → authority REVOKED → DENY.**

That is the finished Voice Authority proof.

---

# Current Project Snapshot

| Area | Status |
| --- | --- |
| Architecture | COMPLETE |
| AssemblyAI voice foundation | LARGELY BUILT |
| Voice UCII identity | COMPLETE |
| Cryptographic signer | COMPLETE |
| Protected custody | COMPLETE |
| Controller authority | COMPLETE |
| Entitlement | COMPLETE |
| Delegated ActionAuthority | COMPLETE |
| Lifecycle authorization | COMPLETE |
| HUMAN step-up machinery | COMPLETE |
| HUMAN lifecycle authorization | COMPLETE |
| First-HUMAN bootstrap | **CURRENT BLOCKER** |
| Voice GRANT integration | PARTIAL / REMAINING |
| Voice EXECUTE integration | PARTIAL / REMAINING |
| Amount/budget policy | REMAINING |
| Voice REVOKE integration | PARTIAL / REMAINING |
| Evidence UI | PARTIAL |
| Final E2E | REMAINING |

The project is **not halfway through** merely because several final integration lines remain. Most of the difficult security infrastructure beneath Voice Authority is already built and production-proven.

# Immediate Critical Path

**Unit 3G → implement legitimate domain bootstrap → establish Brad's Voice-domain HUMAN governance → return to Voice → GRANT → EXECUTE → amount-policy DENY → REVOKE → post-revoke DENY → polish evidence UI → FINAL DEMO.**

# Scope Discipline

Do **not** restart or unnecessarily reopen completed work:

- Voice identity/enrollment.
- Signer/custody.
- Dedicated Unix principals.
- Controller authority.
- Existing entitlement.
- Delegated execution core.
- Existing HUMAN step-up/lifecycle machinery.

Do **not** fabricate a HUMAN identity, factor, governance relationship, or alternate trust root merely to unblock the demonstration.

Do **not** turn Unit 3G into an unnecessary full UCII redesign. Its job is to inspect the existing trust boundary, identify the reusable lifecycle abstraction, and implement the smallest correct primitive needed now while preserving the path to succession, recovery, reset, generation safety, and cross-identity governance.

---

## Resume Point

**UNIT 3G — PROTECTED FIRST-HUMAN BOOTSTRAP REUSE BOUNDARY**
