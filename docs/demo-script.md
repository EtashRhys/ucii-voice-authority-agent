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

## Scene 2 — Protected human grant ceremony

The legitimate human controller requests a narrowly constrained delegation by voice, for example:

> Allow this agent to purchase up to 50 units of compute for the next hour.

AssemblyAI should establish the finalized spoken request and produce a bounded structured `GRANT` proposal.

Conceptually, the proposed delegation contains:

    agent: <verified UCII identity>
    operation: compute.purchase
    maximum: 50 units or equivalent bounded limit
    expiry: short-lived demo window
    scope: exact demo resource/category

Expected visible proof before the grant:

- `WHO`: legitimate human principal identified through the supported UCII path;
- `HEARD`: spoken request finalized by AssemblyAI;
- `REQUEST`: bounded `GRANT` proposal displayed;
- `STEP-UP`: REQUIRED;
- lifecycle authority has not yet been exercised;
- delegation does not yet exist.

Narrative point:

> Understanding my request does not give the voice system authority to grant it. This is a protected authority change.

### Scene 2A — Out-of-band step-up

Because the request changes authority, the ceremony requires independently enrolled step-up verification.

A short-lived, single-use challenge is delivered through the enrolled email or SMS channel, for example:

> UCII verification: ORBIT 381

The human reads the challenge aloud to the voice agent:

> ORBIT 381.

Expected visible proof:

- challenge bound to the active ceremony and requested operation;
- challenge delivered through the enrolled out-of-band channel;
- AssemblyAI transcribes the spoken response;
- deterministic protected code verifies the challenge;
- challenge status becomes VERIFIED / CONSUMED;
- replay of the challenge is not permitted.

Narrative point:

> The spoken challenge proves possession of an enrolled factor. It does not itself create authority.

### Scene 2B — Fresh lifecycle authorization and grant

After successful step-up, UCII performs a fresh lifecycle-authority check for the exact `GRANT`.

Expected visible proof:

- authenticated principal established;
- required step-up evidence established;
- fresh lifecycle authorization: ALLOW;
- bounded delegation created through the legitimate UCII lifecycle;
- delegation scope displayed clearly;
- agent identity remains unchanged;
- provenance/evidence recorded.

The protected relationship is:

    authenticated legitimate principal
            +
    required step-up evidence
            +
    fresh UCII lifecycle authorization
            |
            v
    bounded authority grant

Narrative point:

> The email or text did not grant authority. My voice did not grant authority. AssemblyAI did not grant authority. UCII verified the legitimate human authority before the delegation could be created.

## Scene 3 — Same agent request, now authorized

Repeat the original consequential agent request:

> Purchase 20 units of compute for this workload.

Expected visible proof:

- `WHO`: same UCII agent identity;
- `HEARD`: request recognized correctly;
- `REQUEST`: `compute.purchase`, 20 units;
- `STEP-UP`: not applicable to ordinary execution under existing delegation unless policy requires otherwise;
- identity: VERIFIED;
- bounded delegated authority: ACTIVE;
- fresh execution authorization: ALLOW;
- deterministic executor: EXECUTED;
- provenance/evidence recorded.

Narrative point:

> Nothing about the agent's identity or technical capability changed. A legitimate bounded authority now exists for this exact action.

## Scene 4 — Unauthorized authority escalation

A principal without the required lifecycle authority asks the voice system to expand the delegation, for example:

> Increase this agent's compute purchasing authority to 5,000 units.

AssemblyAI should understand the request correctly.

Expected visible proof:

- `HEARD`: escalation request recognized correctly;
- `REQUEST`: structured authority-changing request produced;
- requested scope is visibly larger than the active delegation;
- legitimate lifecycle authority for the requesting principal: NOT ESTABLISHED;
- lifecycle authorization: DENY;
- existing delegation remains unchanged;
- no expanded authority is created;
- execution: NOT PERFORMED.

If the requesting principal can satisfy an out-of-band factor challenge but still lacks the required UCII lifecycle authority, the result remains `DENY`.

Narrative point:

> Authentication, confirmation, or possession of a verification factor cannot manufacture governance authority. The request can be perfectly understood and still be denied.

## Scene 5 — Protected revocation ceremony

The legitimate controller requests revocation by voice:

> Revoke this agent's compute purchasing authority.

AssemblyAI produces the bounded `REVOKE` proposal.

Because revocation changes authority, execute the applicable protected human ceremony:

- establish the legitimate human principal;
- require step-up according to consequence policy;
- deliver a fresh short-lived out-of-band challenge where required;
- verify the spoken challenge deterministically;
- perform a fresh lifecycle-authority check for the exact revocation;
- execute revocation only after lifecycle authorization returns `ALLOW`.

Expected visible proof:

- `WHO`: legitimate controller;
- `HEARD`: revoke request recognized;
- `REQUEST`: exact bounded `REVOKE`;
- `STEP-UP`: VERIFIED where required;
- fresh lifecycle authorization: ALLOW;
- authority: REVOKED;
- agent identity remains VERIFIED;
- provenance/evidence recorded.

Narrative point:

> Revocation changes what the agent may do. It does not erase the agent's identity.

## Scene 6 — Same request after revocation

Repeat the exact original agent request:

> Purchase 20 units of compute for this workload.

Expected visible proof:

- request understood;
- same identity: VERIFIED;
- technical capability still exists;
- authority: REVOKED;
- fresh execution authorization: DENY;
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
