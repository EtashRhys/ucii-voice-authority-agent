# Human Authority Ceremony Contract

## Status

**FROZEN — OBJECTIVE 0D COMPLETE**

This document freezes the deterministic Human Authority Ceremony contract for
the UCII Voice Authority Agent.

The contract was semantically reviewed against the completed Objective 0C UCII
authority-chain proof before being marked frozen.

It is an application and UCII-integration contract.

It does not itself implement the missing UCII HUMAN lifecycle-governance runtime
primitive identified by Objective 0C.

It does not create authority.

It does not make AssemblyAI, an LLM, an out-of-band provider, payment, or
entitlement an authority source.

The governing separation is:

    Voice
        != Intent
        != Identity
        != Authentication
        != Step-Up Verification
        != Authority
        != Authorization
        != Entitlement
        != Payment
        != Execution

The central invariant is:

> Understanding a human request does not create authority to execute it.

---

## 1. Purpose

The Human Authority Ceremony Engine is the deterministic state machine between
a conversational request and a protected UCII lifecycle or execution decision.

Its responsibilities are to:

- accept only bounded structured operation proposals;
- bind a ceremony to the relevant principal, session, operation, and target;
- determine the applicable consequence class;
- require authentication where applicable;
- require independently established governance authority where applicable;
- require step-up evidence where applicable;
- issue and verify challenges deterministically;
- obtain fresh UCII lifecycle or execution authorization;
- invoke only the protected operation authorized by that decision;
- preserve attributable non-secret evidence; and
- fail closed when required facts cannot be established.

The engine is application code.

It is not an LLM policy prompt.

It must remain reusable independently of AssemblyAI.

---

## 2. Authority Sources and Non-Sources

A ceremony may consume evidence from multiple systems, but evidence is not
automatically authority.

The following do not independently create UCII lifecycle authority:

- voice;
- a transcript;
- intent classification;
- an LLM tool call;
- a structured proposal;
- authentication;
- human confirmation;
- possession of an email challenge;
- possession of an SMS challenge;
- successful challenge verification;
- payment;
- x402 settlement;
- first-party entitlement;
- technical access to a tool;
- possession of a public identifier;
- possession of a credential not explicitly authorized for the operation; or
- an external message.

The applicable UCII governance/lifecycle policy determines authority.

The challenge contributes factor evidence required by that policy.

---

## 3. Operation Vocabulary

The initial ceremony vocabulary is closed to five top-level operations.

### INSPECT

Read intentionally exposed non-secret identity, authority, lifecycle, decision,
or evidence state.

INSPECT must not mutate authority.

### GRANT

Create a bounded delegated authority.

GRANT must specify the exact governed identity, grantee/subject where
applicable, allowed operation scope, and other required bounded grant fields.

GRANT must not accept wildcard authority.

### REVOKE

Remove one exact delegated authority or another explicitly supported bounded
authority target.

REVOKE must identify the exact target and applicable reason.

### EXECUTE

Request a consequential action under already established authority.

EXECUTE does not create the authority required to execute.

### GOVERN

Request a controller, governance, recovery, succession, transfer,
factor-enrollment/change, or similarly critical lifecycle operation.

GOVERN is the highest-sensitivity class in the initial vocabulary.

Unsupported operations fail closed.

An LLM may not create additional operation types dynamically.

---

## 4. Structured Ceremony Request

Before a protected ceremony begins, conversational input must be converted into
a bounded structured proposal.

A security-relevant ceremony request must contain or deterministically resolve
the fields applicable to the requested operation.

The canonical envelope is conceptually:

    ceremony_id
    session_id
    operation
    principal_identity_id
    target_identity_id
    target_authority_id
    requested_scope
    requested_parameters
    consequence_class
    source_turn_reference
    created_at

Fields not applicable to a particular operation may be absent.

Fields required for the operation may not be guessed.

Security-relevant values must not be silently filled from conversational
assumption.

The ceremony engine must reject or request clarification when a required
security field remains ambiguous.

Ambiguity may narrow a request.

Ambiguity must never expand authority.

---

## 5. AssemblyAI Boundary

AssemblyAI is the conversational voice runtime.

AssemblyAI may:

- receive human speech;
- produce partial conversational information;
- produce a finalized user turn;
- maintain conversational context;
- produce a bounded structured tool/action proposal;
- transcribe a spoken challenge response;
- receive a deterministic tool result; and
- speak the resulting response.

Security-relevant ceremony creation must use a finalized user turn rather than
an unstable partial transcript.

AssemblyAI must not:

- decide that a HUMAN has lifecycle authority;
- decide that a challenge is close enough;
- grant delegated authority;
- revoke delegated authority;
- create governance membership;
- create recovery authority;
- bypass UCII authorization;
- treat conversational confirmation as authorization; or
- invoke the consequential executor through an alternate path.

Conversational interruption after a protected mutation commits must not silently
undo or falsify the committed UCII state.

---

## 6. Principal Binding

A protected ceremony must bind to the principal relevant to the operation.

Where HUMAN authentication is required, the principal must be resolved through
the supported UCII authentication and identity-binding path.

A caller-supplied identity identifier is not sufficient principal proof.

The ceremony must preserve the distinction:

    claimed identity
        !=
    authenticated identity

and:

    authenticated identity
        !=
    governance authority

For lifecycle-changing operations, the authenticated HUMAN principal must also
satisfy the applicable independently established UCII governance relationship
and lifecycle policy.

---

## 7. Session and Ceremony Binding

Each protected ceremony must have a unique ceremony identifier.

Where conversational/session continuity matters, it must also bind to the
active session.

Evidence from one ceremony must not satisfy another ceremony unless an explicit
policy permits that reuse.

A challenge issued for one ceremony must not be accepted for:

- another ceremony;
- another session where session binding applies;
- another principal;
- another operation;
- another target; or
- another authority scope.

Conversation history may provide context.

Conversation history is not authority.

---

## 8. Consequence Classes

The ceremony engine applies consequence-based assurance.

### LOW

Typical example:

    INSPECT

A low-consequence read may use an already established authenticated session
where policy permits.

It must not mutate protected authority.

### CONSEQUENTIAL

Typical example:

    EXECUTE

A consequential execution requires:

- the acting identity;
- the exact requested operation;
- existing matching delegated authority;
- current lifecycle validity;
- a fresh UCII execution authorization decision; and
- applicable economic determination.

Additional step-up may be required by policy.

### SENSITIVE

Typical examples:

    GRANT
    REVOKE

A sensitive lifecycle operation requires:

- authenticated HUMAN principal;
- applicable HUMAN governance relationship;
- operation-specific lifecycle authority;
- required step-up evidence;
- fresh lifecycle authorization;
- exact request binding; and
- protected lifecycle execution.

### CRITICAL

Typical examples:

    GOVERN
    recovery
    controller change
    recovery-factor change
    succession
    transfer
    bootstrap-policy change

A critical operation requires the strongest applicable UCII governance path.

A simple initial deployment may support only a bounded subset of GOVERN.

Unsupported critical operations fail closed rather than being downgraded to a
weaker ceremony.

---

## 9. Generic Ceremony State Model

The canonical protected ceremony progresses through explicit code-controlled
states.

A general lifecycle-changing path is:

    IDLE
        |
        v
    REQUEST_RECEIVED
        |
        v
    REQUEST_STRUCTURED
        |
        v
    PRINCIPAL_REQUIRED
        |
        v
    PRINCIPAL_AUTHENTICATED
        |
        v
    GOVERNANCE_EVALUATION
        |
        +--> DENIED
        |
        v
    STEP_UP_EVALUATION
        |
        +--> STEP_UP_NOT_REQUIRED
        |
        +--> STEP_UP_REQUIRED
                    |
                    v
              CHALLENGE_ISSUED
                    |
                    v
              CHALLENGE_PENDING
                    |
                    +--> EXPIRED
                    |
                    +--> DENIED
                    |
                    v
              CHALLENGE_VERIFIED
        |
        v
    FRESH_AUTHORIZATION_REQUIRED
        |
        v
    AUTHORIZATION_EVALUATED
        |
        +--> DENIED
        |
        v
    PROTECTED_OPERATION_READY
        |
        v
    PROTECTED_OPERATION_EXECUTED
        |
        v
    EVIDENCE_RECORDED
        |
        v
    COMPLETE

No state transition may be created merely because an LLM says that a previous
state was satisfied.

---

## 10. Terminal States

The ceremony engine must support explicit terminal outcomes.

At minimum:

    COMPLETE
    DENIED
    EXPIRED
    CANCELLED
    FAILED_CLOSED

A terminal outcome must preserve enough non-secret evidence to determine why
the ceremony ended.

A failed ceremony must not leave an implied authority state that was never
committed by UCII.

---

## 11. GRANT Ceremony

The canonical sensitive GRANT ceremony is:

    IDLE
        |
        v
    VOICE_REQUEST
        |
        v
    STRUCTURED_GRANT
        |
        v
    PRINCIPAL_AUTHENTICATED
        |
        v
    GOVERNANCE_AUTHORITY_EVALUATED
        |
        v
    STEP_UP_REQUIRED
        |
        v
    CHALLENGE_SENT
        |
        v
    CHALLENGE_VERIFIED
        |
        v
    FRESH_LIFECYCLE_AUTHORIZATION
        |
        v
    GRANT_EXECUTED
        |
        v
    COMPLETE

GRANT executes only if every required preceding state is established.

Challenge verification alone cannot transition directly to GRANT_EXECUTED.

Authentication alone cannot transition directly to GRANT_EXECUTED.

Human confirmation alone cannot transition directly to GRANT_EXECUTED.

---

## 12. REVOKE Ceremony

The canonical sensitive REVOKE ceremony is:

    IDLE
        |
        v
    VOICE_REQUEST
        |
        v
    STRUCTURED_REVOKE
        |
        v
    PRINCIPAL_AUTHENTICATED
        |
        v
    GOVERNANCE_AUTHORITY_EVALUATED
        |
        v
    STEP_UP_EVALUATED
        |
        v
    REQUIRED_STEP_UP_VERIFIED
        |
        v
    FRESH_LIFECYCLE_AUTHORIZATION
        |
        v
    EXACT_AUTHORITY_REVOKED
        |
        v
    COMPLETE

REVOKE must bind to the exact authority being revoked.

A revocation request must not silently broaden into revocation of unrelated
credentials, identities, or authority.

After revocation, subsequent execution must use fresh authoritative state.

Cached pre-revocation authority must not survive as execution permission.

---

## 13. EXECUTE Ceremony

The canonical EXECUTE path is:

    REQUEST_RECEIVED
        |
        v
    STRUCTURED_EXECUTION
        |
        v
    ACTING_IDENTITY_ESTABLISHED
        |
        v
    CREDENTIAL / IDENTITY PROOF VERIFIED
        |
        v
    DELEGATED_AUTHORITY_EVALUATED
        |
        v
    FRESH_EXECUTION_AUTHORIZATION
        |
        v
    ECONOMIC_REQUIREMENT_EVALUATED
        |
        +--> FIRST_PARTY_ENTITLEMENT
        |
        +--> X402_REQUIRED
        |        |
        |        v
        |    X402_SETTLED
        |
        +--> NO_PAYMENT_REQUIRED
        |
        v
    EXECUTOR_INVOKED
        |
        v
    RESULT_RECORDED

Economic success cannot repair failed authorization.

Authorization success cannot silently bypass an applicable economic
requirement.

Entitlement may waive payment only.

It never creates authority.

---

## 14. GOVERN Ceremony

GOVERN is an umbrella for the highest-sensitivity lifecycle operations.

Examples include:

- initial governance establishment;
- controller addition or removal;
- recovery-policy change;
- recovery-factor enrollment or replacement;
- controller recovery;
- succession;
- transfer; and
- other critical lifecycle changes.

A GOVERN request must resolve to an explicit supported governance subtype before
execution.

The generic word GOVERN is not itself sufficient execution scope.

Each supported subtype must define:

- exact principal requirements;
- exact governed identity;
- exact target;
- applicable governance policy;
- required independent assurance;
- required step-up;
- fresh lifecycle authorization;
- protected mutation;
- resulting authority;
- rollback/failure behavior; and
- evidence.

Unsupported governance subtypes fail closed.

---

## 15. Challenge Record

A step-up challenge must have a deterministic protected record.

The canonical record contains conceptually:

    challenge_id
    ceremony_id
    session_id
    principal_identity_id
    operation
    target_reference
    challenge_hash
    issued_at
    expires_at
    attempts
    max_attempts
    consumed_at
    status

Additional non-secret policy metadata may be included where necessary.

The plaintext challenge should be minimized and must not be retained merely for
convenience after protected verification no longer requires it.

The challenge must be:

- unpredictable;
- short-lived;
- single-use;
- ceremony-bound;
- principal-bound;
- operation-bound;
- target-bound where applicable;
- session-bound where applicable;
- attempt-limited;
- expiry-enforced;
- replay-protected; and
- consumed after successful use.

---

## 16. Challenge Delivery

Challenge delivery uses an abstraction:

    ChallengeService
        |
        v
    ChallengeDeliveryProvider
        |
        +--> Email
        |
        +--> SMS

The delivery provider transports challenge material.

The provider does not determine:

- HUMAN identity;
- governance membership;
- lifecycle authority;
- recovery authority;
- challenge correctness;
- execution authorization; or
- resulting UCII state.

A communication-provider compromise must not automatically become UCII
governance authority.

---

## 17. Spoken Challenge Verification

The human may read a delivered challenge aloud.

AssemblyAI may transcribe that spoken response.

Protected deterministic code verifies the response.

The LLM must not decide whether the response is sufficiently similar.

Normalization may be deterministic and deliberately bounded for expected speech
representation differences.

Normalization must not turn materially incorrect challenge content into a valid
response.

A valid challenge establishes only the factor evidence represented by that
challenge.

It does not independently establish lifecycle authority.

---

## 18. Challenge Failure

The challenge fails when applicable if:

- expired;
- already consumed;
- attempt limit exceeded;
- incorrect;
- wrong ceremony;
- wrong principal;
- wrong operation;
- wrong target;
- wrong session where session binding applies;
- malformed;
- missing authoritative challenge state; or
- otherwise inconsistent with its protected record.

Failure must not cause fallback to a weaker authority path.

A new challenge requires an explicit new issuance decision.

---

## 19. OOB Factor Enrollment and Change

An OOB destination cannot become a trusted factor merely because a caller
supplies an email address or telephone number during a sensitive ceremony.

Initial factor establishment belongs to bootstrap or another explicitly
authorized enrollment ceremony.

Later factor addition, replacement, or removal is a sensitive or critical
governance operation.

Policy may require:

- existing controller/governance authority;
- verification of the existing factor;
- verification of the new factor;
- additional independent assurance;
- delay;
- recovery authority; or
- another explicit control.

Factor replacement must not become a recovery bypass.

---

## 20. Bootstrap Ceremony

Bootstrap is a special GOVERN ceremony because no prior governance relationship
necessarily exists.

The conceptual bootstrap progression is:

    UNINITIALIZED
        |
        v
    BOOTSTRAP_REQUESTED
        |
        v
    INITIAL_HUMAN_IDENTITY_ESTABLISHED
        |
        v
    INITIAL_AUTHENTICATION_ESTABLISHED
        |
        v
    INDEPENDENT_OOB_FACTOR_ENROLLED
        |
        v
    OOB_FACTOR_VERIFIED
        |
        v
    BOOTSTRAP_POLICY_SATISFIED
        |
        v
    INITIAL_GOVERNANCE_RELATIONSHIP_ESTABLISHED
        |
        v
    PROTECTED_CONTROLLER_CAPABILITY_ESTABLISHED
        |
        v
    RECOVERY_POLICY_ESTABLISHED
        |
        v
    ACTIVE
        |
        v
    BOOTSTRAP_CLOSED

Bootstrap must not use:

- first-caller-wins forever;
- authentication alone;
- challenge possession alone;
- payment;
- entitlement;
- LLM judgment; or
- an ordinary delegated agent

as sufficient governance authority.

Once bootstrap is closed, ordinary callers must not be able to reopen the
initial bootstrap path.

The exact bootstrap authority implementation remains dependent on the reusable
UCII HUMAN lifecycle-governance runtime primitive identified by Objective 0C.

---

## 21. Recovery Ceremony

Recovery is a GOVERN subtype.

Recovery restores legitimate control.

It does not create privilege.

A recovery ceremony must independently establish recovery authority according
to the applicable UCII HUMAN recovery policy.

Possible evidence may include policy-authorized combinations of:

- another independently valid HUMAN credential;
- dedicated recovery credential;
- independently enrolled OOB factor;
- hardware or offline factor;
- authorized administrator/operator;
- quorum;
- delay;
- device/hardware attestation; or
- another explicitly authorized recovery mechanism.

Authentication may contribute evidence.

Authentication is not automatically recovery authority.

Payment and entitlement never create recovery authority.

A compromised credential must not be the sole authority for unrestricted
replacement of itself.

Replacement authority must not silently exceed the authority explicitly
granted by recovery policy.

If recovery authority cannot be established, recovery fails closed.

---

## 22. Governance Durability

The ceremony contract must preserve durable HUMAN governance.

A HUMAN identity is not equivalent to one device or credential.

Revoking one HUMAN credential must not inherently destroy the HUMAN identity.

The architecture must permit independently governed credentials and future
stronger governance profiles.

The initial implementation may use a simple supported governance profile.

It must not create an immortal root user.

It must not prevent future:

- additional controllers;
- independently scoped recovery credentials;
- controller removal;
- succession;
- transfer;
- quorum;
- delayed recovery; or
- organizational governance.

---

## 23. Fresh Authorization

Sensitive or consequential operations require a fresh authoritative decision at
the applicable boundary.

A previous successful authorization must not be reused after relevant state has
changed.

Relevant changes include:

- authority revocation;
- credential revocation;
- identity deactivation;
- policy change;
- challenge expiry;
- ceremony expiry;
- governance change; or
- another authoritative lifecycle transition.

The ceremony engine must not infer current authority from conversational memory.

---

## 24. Protected Operation Boundary

After authorization succeeds, the ceremony engine may invoke only the exact
protected operation represented by the authorized request.

The protected executor or lifecycle service must independently enforce its own
required boundary.

The ceremony engine must not provide a second unprotected route to the same
consequential mutation.

The LLM must not call the consequential executor directly.

The voice transport must not call the consequential executor directly.

---

## 25. Evidence Contract

The compact proof surface is:

    WHO
    HEARD
    REQUEST
    STEP-UP
    AUTHORITY
    DECISION
    RESULT

These fields are evidence views.

They are not authority sources.

The underlying ceremony evidence should preserve enough non-secret information
to determine, where applicable:

- ceremony identifier;
- session reference;
- authenticated principal;
- source finalized-turn reference;
- requested operation;
- exact target;
- requested scope;
- consequence class;
- governance-policy reference;
- step-up requirement;
- challenge identifier;
- challenge result;
- lifecycle-authorization reference;
- execution-authorization reference;
- economic determination;
- protected-operation result;
- resulting authority state;
- denial/failure reason;
- timestamps; and
- provenance references.

Evidence must not contain:

- raw controller authority;
- raw private keys;
- passwords;
- bearer tokens;
- reusable payment proofs;
- wallet secrets;
- plaintext recovery secrets; or
- other reusable protected material.

Provenance records what occurred.

Provenance does not create authority.

---

## 26. Fail-Closed Rules

A protected operation must not execute when any required security fact is
missing, expired, contradictory, ambiguous, revoked, or unverifiable.

Fail-closed conditions include, where applicable:

- unresolved principal;
- inactive identity;
- invalid credential proof;
- unresolved governance relationship;
- missing lifecycle authority;
- missing delegated authority;
- insufficient step-up;
- invalid challenge;
- expired challenge;
- replayed challenge;
- wrong ceremony binding;
- wrong operation binding;
- wrong target binding;
- stale authorization;
- revoked authority;
- unsupported operation;
- unsupported governance subtype;
- ambiguous authority scope;
- missing protected service result; or
- inconsistent resulting state.

Availability pressure does not create authority.

Conversational pressure does not create authority.

Demo pressure does not create authority.

---

## 27. Ambiguity Contract

The conversational layer may ask clarifying questions.

It may not resolve security ambiguity by selecting broader authority.

Examples:

    "let it buy compute"

may require clarification of:

- which agent;
- which compute operation;
- spending/resource limit;
- duration;
- target service; or
- other policy-required scope.

A clarification may narrow the request.

It may not silently transform:

    $50

into:

    unlimited

or:

    one hour

into:

    permanent

or:

    this agent

into:

    every agent

If security-relevant ambiguity remains unresolved, the ceremony does not
advance to protected execution.

---

## 28. Cancellation and Interruption

A human may cancel a pending ceremony where policy permits.

Cancellation must not itself broaden authority.

A conversational interruption may stop an uncommitted conversational flow.

Once a protected UCII mutation has committed, conversational interruption must
not represent the mutation as though it never happened.

The application must reconcile against authoritative UCII state after uncertain
transport or conversational failure around a consequential commit.

---

## 29. Adversarial Invariants

The implementation must test at least:

- voice/LLM self-authorization attempt;
- prompt-injection attempt to bypass the ceremony;
- unauthorized GRANT;
- unauthorized REVOKE;
- unauthorized GOVERN;
- wrong-principal challenge;
- wrong-ceremony challenge;
- wrong-session challenge where applicable;
- wrong-operation challenge;
- expired challenge;
- replayed challenge;
- attempt-limit exhaustion;
- challenge possession without governance authority;
- authentication without governance authority;
- payment without authority;
- entitlement without authority;
- stale authority after revocation;
- direct executor bypass attempt; and
- ambiguity that would broaden authority.

The safe outcome is DENY, clarification, cancellation, expiry, or fail-closed as
appropriate.

---

## 30. Objective 0C Runtime Dependency

Objective 0C proved that UCII already has:

- HUMAN identity;
- HUMAN authentication and identity binding;
- controller-authority capability;
- protected controller custody;
- controller verification;
- delegated action authority;
- protected delegated grant/revoke machinery;
- authorization;
- entitlement/x402 economic separation;
- provenance; and
- the authoritative HUMAN governance/recovery contract.

Objective 0C also established that the inspected runtime does not yet provide
the generalized policy-governed binding:

    authenticated HUMAN
        |
        v
    governance relationship
        |
        v
    operation-specific HUMAN lifecycle authority

Therefore this ceremony contract MUST NOT pretend that this runtime decision
already exists.

Implementation must either:

1. use an existing UCII primitive if later implementation inspection proves an
   applicable supported primitive already exists; or

2. make the smallest reusable UCII-core implementation required to realize the
   already-defined HUMAN lifecycle-governance contract.

It must not create a hackathon-only alternate trust root.

---

## 31. Guardian Reuse Boundary

Guardian is not a Voice Authority Agent dependency.

Generic protected lifecycle infrastructure developed during Guardian work may
be reused or promoted into UCII core where appropriate.

Potentially reusable infrastructure includes:

- protected controller-authority custody;
- exact lifecycle authorization;
- one-use authorization consumption;
- protected lifecycle client;
- privilege-separated lifecycle service/daemon; and
- controller verification before mutation.

Guardian-specific recovery composition, paths, UI, and product policy remain
Guardian-specific unless deliberately generalized as reusable UCII
infrastructure.

The target relationship is:

    Human
        |
        v
    Voice / AssemblyAI
        |
        v
    Human Authority Ceremony Engine
        |
        v
    UCII HUMAN lifecycle governance
        |
        v
    protected UCII controller lifecycle
        |
        v
    machine / agent authority

not:

    Voice -> Guardian -> UCII

---

## 32. Entitlement Boundary

The first-party Voice Authority Agent should use legitimate UCII entitlement
where applicable rather than paying UCII itself merely to exercise a
first-party economic path.

The ordering remains:

    Identity
        |
        v
    Authentication
        |
        v
    Authority
        |
        v
    Authorization
        |
        v
    Entitlement / payment determination
        |
        v
    Execution

The invariant is:

> Entitlement waives payment only. It never creates authority.

---

## 33. Minimum Supported Ceremony Profile

The minimum excellent hackathon profile should support:

1. finalized AssemblyAI voice request;
2. bounded structured proposal;
3. authenticated HUMAN identity where human governance is required;
4. UCII agent identity / credential verification;
5. no-authority execution DENY;
6. sensitive GRANT ceremony;
7. independently enrolled OOB challenge;
8. spoken challenge verification;
9. fresh HUMAN lifecycle-authority evaluation;
10. protected bounded delegated-authority grant;
11. authorized execution ALLOW;
12. unauthorized escalation DENY;
13. protected REVOKE ceremony;
14. post-revocation execution DENY;
15. compact proof surface; and
16. attributable provenance/evidence.

Full recovery, multi-controller governance, quorum, and succession may remain
stretch functionality provided the implementation does not violate or prevent
the frozen contract.

---

## 34. Acceptance Gate

Objective 0D is satisfied when the project has frozen:

- operation vocabulary;
- structured security-relevant request fields;
- principal binding;
- session/ceremony binding;
- consequence classes;
- deterministic ceremony states;
- terminal outcomes;
- GRANT progression;
- REVOKE progression;
- EXECUTE progression;
- GOVERN boundary;
- challenge record;
- challenge lifecycle;
- challenge delivery-provider boundary;
- spoken deterministic verification;
- factor enrollment/change boundary;
- bootstrap boundary;
- recovery boundary;
- governance durability;
- fresh authorization requirements;
- protected-operation boundary;
- evidence/provenance requirements;
- fail-closed rules;
- ambiguity rules;
- interruption/cancellation semantics;
- adversarial invariants;
- Objective 0C runtime dependency;
- Guardian reuse boundary; and
- entitlement/payment separation.

After this contract is reviewed, committed, synchronized, and explicitly marked
complete, implementation may begin from the smallest required primitive.

---

## Frozen North Star

> Ask by voice. Receive a challenge when necessary. Read it aloud. UCII verifies
> the human and the authority. The requested operation either happens or it
> does not.

And:

> Capability is not authority.
