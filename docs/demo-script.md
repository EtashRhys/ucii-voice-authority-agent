# Demo Script

This is the working demonstration contract. Exact wording and tool details may be refined after implementation.

## Opening

Explain in one sentence:

> This agent can understand my voice and has access to a consequential tool, but neither voice understanding nor tool access gives it authority to act.

## Scene 1 — Request without authority

Human speaks a consequential request, for example:

> Purchase 20 units of compute for this workload.

Expected visible proof:

- AssemblyAI voice request recognized;
- structured proposed action displayed;
- UCII agent identity: VERIFIED;
- delegated authority: NONE / NOT APPLICABLE;
- authorization: DENY;
- execution: NOT PERFORMED.

Narrative point:

> The agent is real and verified. The request is understood. The capability exists. It still cannot execute because identity is not authority.

## Scene 2 — Bounded human grant

Create a narrowly constrained delegation, conceptually similar to:

```text
agent: <verified UCII identity>
operation: compute.purchase
maximum: 50 units or equivalent bounded limit
expiry: short-lived demo window
scope: exact demo resource/category
```

Expected visible proof:

- authority created by the authorized human/control path, not the voice model;
- delegation scope shown clearly;
- identity unchanged.

## Scene 3 — Same request, now authorized

Repeat the exact spoken request.

Expected visible proof:

- AssemblyAI recognizes the request again;
- same agent identity: VERIFIED;
- bounded authority: ACTIVE;
- fresh authorization: ALLOW;
- deterministic executor: EXECUTED;
- provenance/evidence recorded.

Narrative point:

> Nothing about the agent's identity or technical capability changed. A valid bounded authority now exists for this action.

## Scene 4 — Revoke

Revoke the exact delegation.

Expected visible proof:

- authority: REVOKED;
- agent identity remains VERIFIED.

## Scene 5 — Same request after revocation

Repeat the exact spoken request a third time.

Expected visible proof:

- request understood;
- same identity: VERIFIED;
- authority: REVOKED;
- fresh authorization: DENY;
- execution: NOT PERFORMED.

Closing line:

> Same voice capability. Same cryptographically verified agent. Different authority state, different execution outcome. Capability is not authority.

## Demo integrity requirements

- Do not fake UCII verification or authority transitions for the final proof.
- Do not let the LLM create its own authority.
- Do not pre-authorize the denied scenes.
- Require a fresh authority decision after grant and after revocation.
- Make denied execution visibly distinguishable from an application error.
- Preserve provenance/evidence for the meaningful transitions.
