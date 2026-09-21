# UCII Human Governance Authority Chain

## Status

Objective 0C establishes the factual UCII authority and governance baseline that
must be understood before the Voice Authority Agent freezes its Human Authority
Ceremony contract or implements consequential authority-changing operations.

This record is based on read-only inspection of the UCII repository at:

    c13e555b4a58eed965b2c6b915279ac9197f179b

No production database state, controller secret, credential secret, protected
service state, or other secret material was accessed during this inspection.

This document records architecture and implementation findings only.

It does not create new authority.

It does not modify UCII core.

It does not authorize deployment.

---

## 1. Governing Separation

The Voice Authority Agent preserves the following separation:

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

The central rule remains:

> Understanding a human request does not create authority to execute it.

AssemblyAI may understand speech and propose a bounded operation.

AssemblyAI does not determine UCII authority.

An LLM does not determine UCII authority.

An email or SMS challenge does not create UCII authority.

Successful authentication does not automatically create lifecycle authority.

Successful payment does not create lifecycle authority.

A first-party entitlement does not create lifecycle authority.

---

## 2. Existing UCII Machine / Agent Authority Chain

The existing UCII architecture already provides the machine and autonomous-agent
authority foundation required by this project.

The established chain is conceptually:

    UCII identity
        |
        v
    credential
        |
        v
    authentication / verification
        |
        v
    identity binding
        |
        v
    delegated action authority
        |
        v
    UCII authorization
        |
        v
    applicable economic policy
        |
        +--> first-party entitlement where legitimately applicable
        |
        +--> x402 settlement where legitimately applicable
        |
        v
    protected execution

No earlier state manufactures a later state.

In particular:

    authentication != authorization

    verification != authorization

    authorization != payment authority

    payment != controller authority

    settlement != execution authority

    entitlement != controller authority

This existing machine/agent authority architecture is not being replaced by the
Voice Authority Agent.

The Voice project adds a legitimate human-facing governance path above it.

---

## 3. Existing UCII Human Authentication Foundation

UCII already has a real HUMAN identity and authentication foundation.

An authentication User is bound to an independently provisioned UCII identity.

Authenticated context resolves the authenticated user to the corresponding
active UCII identity rather than trusting an arbitrary caller-supplied identity
claim.

This provides an important primitive:

    authenticated HUMAN
        |
        v
    authenticated UCII identity context

However:

    authenticated HUMAN
        != lifecycle controller

and:

    authenticated HUMAN
        != recovery authority

Authentication establishes who successfully authenticated.

It does not by itself establish what lifecycle or governance operations that
human is authorized to perform.

---

## 4. Existing Controller Authority Primitive

UCII already implements an identity-scoped controller-authority primitive.

The inspected implementation establishes:

- one IdentityControllerAuthority record per identity;
- a freshly generated controller-authority secret;
- hash-only persistence of that secret;
- exact identity binding;
- constant-time verification of presented authority;
- duplicate initial issuance rejection;
- controller-authority replacement / recovery;
- rotated-at lifecycle evidence; and
- transaction-composable issuance and replacement.

The raw controller-authority secret is not stored in the UCII database.

The currently implemented core primitive represents one currently valid
controller secret for an identity.

Replacement rotates that authority on the same durable identity-bound record.

This primitive is strong controller-capability machinery.

It is not, by itself, a generalized multi-human governance model.

---

## 5. Existing Initial Controller Bootstrap Modes

Inspection established two important initial provisioning patterns.

### 5.1 Public Identity Provisioning

The public identity creation route currently creates a new identity and issues
its initial controller authority.

At the inspected source boundary:

- the identity creation route is described as public;
- authentication and authorization are not attached to that route;
- a successful caller receives the newly created identity's controller
  authority exactly once;
- only the digest is persisted; and
- later ordinary GET/LIST responses do not disclose the controller authority.

This does not establish authority over an existing identity.

It does mean that public creation of a new identity is not, by itself, proof of
a durable human governance relationship.

Therefore the Voice Authority Agent MUST NOT treat:

    caller can create identity

as equivalent to:

    caller is a legitimate HUMAN lifecycle controller

### 5.2 Protected First-Party Provisioning

UCII also contains protected first-party operator provisioning machinery.

That path can:

    create identity transactionally
        |
        v
    issue controller authority transactionally
        |
        v
    stage protected controller-authority custody
        |
        v
    commit authoritative database state
        |
        v
    finalize protected controller-authority custody
        |
        v
    provision protected operational signing credentials

Successful provisioning does not expose raw controller authority to the
autonomous runtime.

This is valuable reusable infrastructure.

It still does not, by itself, define the human governance relationship that
legitimates the initial operator decision.

---

## 6. Existing Protected Lifecycle Machinery

UCII contains protected controller-lifecycle machinery developed during the
Guardian work that is architecturally reusable beyond Guardian.

The generic protected chain includes:

    exact lifecycle authorization
        |
        v
    durable one-use consumption
        |
        v
    protected lifecycle client
        |
        v
    privilege-separated lifecycle service / daemon
        |
        v
    protected controller-authority credential
        |
        v
    controller-authority verification
        |
        v
    exact bounded lifecycle mutation

The inspected lifecycle authorization vocabulary currently supports exact
delegated-authority operations for:

- GRANT_DELEGATED_AUTHORITY
- REVOKE_DELEGATED_AUTHORITY

The authorization artifacts are:

- operation-specific;
- identity-bound;
- target/scope-bound where applicable;
- explicitly time-bounded;
- one-use;
- wildcard-resistant; and
- replay-resistant through durable consumption evidence.

The protected lifecycle service keeps the controller authority outside the
ordinary API process.

This machinery should be preserved.

The Voice Authority Agent MUST NOT create a second controller secret path or an
alternate lifecycle trust root merely because its interface is conversational.

---

## 7. Current Lifecycle Authorization Origin

The inspected delegated grant/revoke routes rely on a separately established
root-controlled lifecycle authorization.

At the inspected layer, authorization artifact authenticity is established by
protected host/filesystem properties including:

- absolute path requirements;
- regular-file requirements;
- root ownership;
- rejection of group/world writable state;
- exact schema;
- exact operation and identity binding;
- bounded timing; and
- one-use consumption.

No production authoring mechanism was located that establishes:

    authenticated HUMAN
        |
        v
    legitimate governance decision
        |
        v
    protected lifecycle authorization artifact

Therefore the existing protected lifecycle machinery strongly answers:

> How can UCII safely execute an already-established bounded lifecycle decision?

It does not yet provide the generalized runtime answer to:

> Which authenticated human was legitimately allowed to originate that
> lifecycle decision, and under what governance policy?

That is the principal implementation seam exposed by Objective 0C.

---

## 8. Existing Controller Recovery Primitive

UCII contains a protected controller-authority replacement primitive.

The inspected Guardian recovery composition:

    locate exact existing active identity
        |
        v
    create replacement controller authority transactionally
        |
        v
    stage replacement into protected encrypted custody
        |
        v
    commit authoritative digest
        |
        v
    promote protected replacement custody

The raw replacement authority is not returned to the caller.

Failure behavior is designed to fail closed around custody and authoritative
database state.

However, the inspected Guardian-specific recovery function does not itself
receive or verify:

- an authenticated HUMAN principal;
- an existing controller proof;
- a dedicated recovery credential;
- a governance membership;
- a recovery-policy decision;
- a quorum approval; or
- another independent recovery-authority proof.

No production public route, SDK recovery operation, or independent production
recovery ceremony was located during the inspection.

Therefore:

> Protected replacement mechanics exist, but generalized HUMAN recovery
> authorization is not currently connected to those mechanics.

Guardian-specific recovery code MUST NOT become a Voice dependency.

Reusable protected primitives may instead be promoted or generalized in UCII
core.

---

## 9. Authoritative HUMAN Governance and Recovery Contract

UCII's existing engineering contract already defines the intended HUMAN
governance semantics.

The Voice project does not need to invent a new governance philosophy.

The established contract requires that HUMAN recovery authority be
independently established according to policy.

Permitted policy mechanisms may include:

- another independently valid HUMAN credential;
- a dedicated recovery credential;
- a hardware recovery token;
- an offline recovery factor;
- multiple independently controlled recovery factors;
- an authorized organization administrator;
- an authorized human recovery operator;
- quorum approval;
- delayed recovery;
- device or hardware attestation;
- previously established recovery policy;
- out-of-band confirmation; or
- another explicitly authorized recovery mechanism.

The contract explicitly establishes:

    identity identifier != recovery authority

    authentication token != recovery authority

    authentication != recovery authority

    payment != recovery authority

    existing credential != unrestricted lifecycle authority

The governing HUMAN recovery rule is:

> Recovery restores legitimate control. It does not create privilege.

---

## 10. Durable HUMAN Identity and Multiple Credentials

The UCII contract defines a HUMAN identity as durable independently of any
single credential, private key, device, or custody mechanism.

One HUMAN identity may possess multiple independently governed credentials.

For example, policy may legitimately permit:

    phone credential       REVOKED
    laptop credential      ACTIVE
    hardware credential    ACTIVE
    recovery credential    ACTIVE

Revocation of one HUMAN credential does not silently revoke unrelated
credentials unless broader containment is independently justified.

Loss or compromise of one credential therefore does not inherently destroy the
HUMAN identity.

This contract is essential to the Voice project's governance design.

The project MUST NOT create an immortal creator credential or permanent
single-human root merely for implementation convenience.

---

## 11. Multi-Party and Organizational Governance

UCII's existing contract permits stronger governance profiles where required.

Examples include:

- two administrators;
- administrator plus security officer;
- 2-of-3 governance members;
- recovery committee approval;
- offline plus online approval; and
- another explicitly governed quorum.

Quorum approval establishes only the lifecycle authority permitted by the
governing policy.

It does not transfer the approving principals' unrelated authority to the
resulting credential.

The existing pre-D.2 hardening record explicitly treats threshold cryptography
and 2-of-3 organizational recovery as higher-assurance work that the core
architecture must accommodate but does not need to impose universally.

Therefore the Voice Authority Agent does not need to implement a full threshold
governance system for its minimum excellent submission.

It MUST avoid designing a core model that prevents such governance later.

---

## 12. Out-of-Band Challenge Role

The existing HUMAN recovery contract explicitly permits out-of-band
confirmation as part of stronger recovery assurance.

This supports the Voice project's email/SMS spoken-challenge design.

The challenge has one narrow role:

    prove possession / completion of an enrolled step-up factor

It does not establish governance authority by itself.

The correct relationship is:

    authenticated HUMAN
        |
        v
    requested consequential lifecycle operation
        |
        v
    applicable governance / lifecycle policy
        |
        v
    step-up required
        |
        v
    OOB challenge issued
        |
        v
    challenge possession verified
        |
        v
    fresh governance authority evaluation
        |
        v
    ALLOW or DENY
        |
        v
    protected lifecycle execution if allowed

Therefore:

    correct SMS code != controller authority

    correct email code != recovery authority

    spoken challenge != authorization

The challenge contributes evidence required by policy.

UCII remains the authority decision point.

---

## 13. Missing Runtime Primitive

Objective 0C establishes a specific implementation gap between the existing
UCII governance contract and the currently inspected runtime.

UCII already has:

- HUMAN identities;
- authentication;
- identity binding;
- credentials;
- controller-authority capability;
- controller-authority verification;
- protected controller custody;
- controller-authority replacement mechanics;
- delegated action authority;
- authorization;
- protected delegated grant/revoke machinery;
- lifecycle evidence;
- x402 economic authorization;
- first-party service entitlement; and
- a detailed HUMAN governance/recovery contract.

The missing reusable runtime primitive is:

> A policy-governed relationship that establishes which authenticated HUMAN
> principals and independently enrolled factors are authorized to originate
> specific lifecycle/governance operations for a UCII identity.

Conceptually:

    authenticated HUMAN principal
        |
        v
    governance relationship / membership
        |
        v
    operation-specific lifecycle policy
        |
        v
    required independent assurance / step-up factors
        |
        v
    HUMAN lifecycle authority established
        |
        v
    bounded protected lifecycle decision
        |
        v
    existing protected controller lifecycle machinery

This capability belongs in reusable UCII infrastructure.

It MUST NOT be implemented as an AssemblyAI-specific authority mechanism.

It MUST NOT be implemented as a Guardian dependency.

It MUST NOT be implemented as an LLM decision.

---

## 14. Smallest Reusable UCII-Core Direction

The implementation direction to evaluate after the Voice ceremony contract is
frozen is a reusable HUMAN lifecycle-governance layer.

The layer should be capable of representing, at minimum:

- the governed UCII identity;
- the HUMAN principal authorized to participate in governance;
- the governance/lifecycle role or explicitly permitted operations;
- current lifecycle state;
- applicable step-up policy;
- independently enrolled factor references;
- creation and revocation state;
- attributable provenance; and
- fail-closed authority evaluation.

It should support a simple initial profile without preventing stronger future
profiles.

A simple profile may permit one independently authenticated HUMAN controller
plus an independently enrolled OOB factor.

Higher-assurance profiles may later permit:

- multiple HUMAN controllers;
- independent recovery credentials;
- controller addition/removal;
- succession;
- transfer;
- quorum;
- delayed recovery;
- hardware-backed factors; or
- organizational governance.

The existing protected controller authority should remain the low-level
capability used to perform protected lifecycle mutations.

The new HUMAN governance layer should determine whether the lifecycle decision
is legitimate.

---

## 15. Bootstrap Requirement

Initial HUMAN governance bootstrap requires special treatment because no prior
governance membership necessarily exists.

The Voice project MUST NOT solve bootstrap with:

    first caller wins forever

or:

    authenticated account automatically becomes controller

or:

    successful OOB challenge automatically becomes controller

or:

    payment creates controller

or:

    entitlement creates controller

or:

    LLM decides who seems legitimate

The bootstrap ceremony must establish the initial HUMAN governance relationship
under an explicit bootstrap policy.

Conceptually:

    UNINITIALIZED
        |
        v
    bootstrap requested
        |
        v
    initial HUMAN identity established
        |
        v
    initial authentication established
        |
        v
    independent OOB factor enrolled and verified
        |
        v
    bootstrap policy satisfied
        |
        v
    initial governance relationship established
        |
        v
    protected controller capability established
        |
        v
    recovery policy established
        |
        v
    ACTIVE
        |
        v
    bootstrap path CLOSED

After activation, ordinary callers MUST NOT be able to reopen initial bootstrap
and claim controller authority.

---

## 16. Voice Authority Agent Target Chain

The target human-to-machine authority chain is:

    HUMAN SPEECH
        |
        v
    AssemblyAI finalized conversational turn
        |
        v
    bounded structured operation proposal
        |
        v
    Human Authority Ceremony Engine
        |
        v
    authenticated HUMAN identity
        |
        v
    existing HUMAN governance relationship / bootstrap policy
        |
        v
    consequence-based step-up policy
        |
        v
    OOB challenge where required
        |
        v
    deterministic challenge verification
        |
        v
    fresh HUMAN lifecycle authority evaluation
        |
        v
    bounded lifecycle authorization
        |
        v
    protected UCII controller lifecycle machinery
        |
        v
    delegated machine / agent authority
        |
        v
    UCII authorization
        |
        v
    entitlement or x402 determination where applicable
        |
        v
    protected execution
        |
        v
    attributable provenance

At every boundary:

> No earlier state manufactures a later state.

---

## 17. First-Party Entitlement Boundary

The Voice Authority Agent is a first-party UCII system.

Where UCII's economic policy legitimately permits first-party entitlement, the
project should use that entitlement rather than paying UCII itself through
x402.

The invariant is:

> Entitlement waives payment only. It never creates authority.

Therefore:

    authorized operation
        |
        v
    economic requirement evaluated
        |
        +--> valid first-party entitlement
        |        |
        |        v
        |    payment requirement satisfied / waived
        |
        +--> x402 required
                 |
                 v
             settlement required
        |
        v
    execution may proceed only if every other applicable boundary is satisfied

Entitlement MUST NOT create:

- HUMAN identity authority;
- controller authority;
- governance membership;
- recovery authority;
- delegated action authority;
- credential lifecycle authority; or
- permission to execute an otherwise unauthorized action.

---

## 18. Reuse Boundary

The implementation must distinguish three categories.

### UCII Core — Preserve

Preserve and reuse:

- identity;
- HUMAN authentication;
- credential lifecycle;
- controller-authority primitive;
- delegated action authority;
- authorization;
- economic separation;
- provenance; and
- the existing HUMAN governance/recovery contract.

### Generic Protected Lifecycle Infrastructure — Reuse / Promote

Evaluate promotion or generalization of:

- protected controller-authority custody;
- lifecycle authorization;
- one-use lifecycle authorization consumption;
- protected lifecycle client;
- privilege-separated lifecycle service/daemon; and
- controller-authority verification before mutation.

These capabilities were developed during Guardian work but are not inherently
Guardian concepts.

### Guardian-Specific — Do Not Couple

Keep Guardian-specific:

- Guardian-specific custody destinations;
- Guardian-specific recovery composition;
- Guardian-specific UI or operator behavior;
- Guardian-specific policy assumptions; and
- other Guardian product semantics.

Voice MUST NOT depend on Guardian to establish HUMAN authority.

---

## 19. Objective 0C Factual Determination

The Objective 0C acceptance question was:

> Who has authority to grant it, why UCII trusts that grant, how that authority
> can later be revoked or transferred, and how legitimate governance survives
> loss or revocation of an individual controller without creating an immortal
> root user?

The factual answer is:

1. Existing UCII can strongly enforce machine/agent authority after a legitimate
   lifecycle decision has been established.

2. Existing UCII has a protected identity-scoped controller capability and
   protected lifecycle execution machinery.

3. Existing HUMAN authentication establishes an authenticated UCII identity but
   does not automatically establish lifecycle governance authority.

4. Existing UCII engineering contracts already require HUMAN lifecycle and
   recovery authority to be independently established according to policy.

5. Those contracts already support multiple independently governed HUMAN
   credentials, OOB confirmation, recovery credentials, administrators,
   stronger factors, quorum, managed and unmanaged identities, and fail-closed
   recovery.

6. The inspected runtime does not yet provide the generalized policy-governed
   HUMAN-principal-to-lifecycle-authority relationship described by that
   contract.

7. Therefore the Voice project exposes a reusable UCII-core implementation seam:
   HUMAN lifecycle governance must be connected to the existing protected
   controller lifecycle machinery.

8. Initial bootstrap must explicitly establish the first legitimate HUMAN
   governance relationship and then close the bootstrap path.

9. Later grant, revoke, recovery, transfer, and succession decisions must derive
   from independently established governance authority rather than from voice,
   authentication, payment, entitlement, or possession of one arbitrary
   credential alone.

10. Loss or revocation of one HUMAN credential must not inherently destroy the
    durable identity or require an immortal root user.

---

## 20. Objective 0C Completion Boundary

Objective 0C establishes the factual architecture and the missing reusable
runtime primitive.

It does not implement that primitive.

It does not modify UCII production behavior.

It does not create a new controller.

It does not grant delegated authority.

It does not perform recovery.

It does not create an OOB challenge.

It does not integrate AssemblyAI.

The next engineering objective is Objective 0D:

> Freeze the Human Authority Ceremony contract using the proven UCII authority
> boundaries before implementation begins.

Only after that contract is frozen should implementation changes be evaluated.

---

## Objective 0C Result

    EXISTING MACHINE / AGENT AUTHORITY: ESTABLISHED

    HUMAN AUTHENTICATION FOUNDATION: ESTABLISHED

    CONTROLLER CAPABILITY: ESTABLISHED

    PROTECTED CONTROLLER CUSTODY: ESTABLISHED

    PROTECTED DELEGATED GRANT / REVOKE: ESTABLISHED

    HUMAN GOVERNANCE / RECOVERY CONTRACT: ESTABLISHED

    HUMAN PRINCIPAL -> GOVERNANCE AUTHORITY RUNTIME BINDING:
        NOT YET ESTABLISHED

    ENTITLEMENT / PAYMENT -> AUTHORITY:
        PROHIBITED

    VOICE / LLM -> AUTHORITY:
        PROHIBITED

    REQUIRED REUSABLE IMPROVEMENT:
        HUMAN LIFECYCLE GOVERNANCE AUTHORITY LAYER

    NEXT:
        OBJECTIVE 0D — FREEZE HUMAN AUTHORITY CEREMONY CONTRACT

---

## 2026-09-20 — Final Authority Lifecycle Pre-3G Checkpoint

### Current project position

The AssemblyAI Voice Authority Agent has completed the production infrastructure
and cryptographic activation work required before the final authority lifecycle
demonstration.

The project remains governed by the core separation:

    VOICE
        != INTENT
        != IDENTITY
        != AUTHENTICATION
        != STEP-UP
        != AUTHORITY
        != AUTHORIZATION
        != ENTITLEMENT
        != PAYMENT
        != EXECUTION

AssemblyAI supplies the conversational/transcription interface. It is not a UCII
authority source.

### Production gates completed

The following deployment gates are complete:

1. dedicated Voice Unix principals;
2. protected custody runtime generation;
3. dedicated Voice signer service;
4. production signing credential and first-party entitlement bound to the
   existing Voice identity;
5. real protected ML-DSA-65 signing proof against the registered UCII public
   credential.

The existing production objects are durable and MUST NOT be recreated:

Voice identity:

    9df0ff8a-25d0-4340-be32-05e8263f1277

Signing credential:

    fca03fa4-32c6-49fe-87b2-4b9e56453a66

Service entitlement:

    0522e726-035e-4254-a131-63a042a9fbbc

The protected signer is operational and the Voice application does not receive
the private signing material.

### Remaining original demonstration gate

The remaining original deployment gate is the final authority lifecycle proof:

    no delegated authority
        -> DENY
        -> legitimate HUMAN-governed GRANT
        -> bounded authorized execution
        -> out-of-policy request DENY
        -> legitimate REVOKE
        -> same formerly authorized request DENY

Every consequential execution must use a fresh authority decision.

The current target operation is:

    compute.purchase

The UCII ActionAuthority record scopes exact operations. It does not itself
encode monetary value. The final USD 35 versus USD 5,000 demonstration therefore
requires a separately verified real economic/budget policy seam and must not
attribute that distinction to ActionAuthority unless such a bound is actually
implemented there.

### Units 3A through 3F result

The final-lifecycle investigation established that UCII now has the generic
delegated execution contract and the reusable HUMAN ceremony components needed
after governance exists.

It also established a previously unresolved prerequisite.

Production currently contains:

    HUMAN identities: 0

There is therefore no existing production HUMAN principal/factor/governance
relationship that can legitimately authorize the Voice Authority grant/revoke
ceremony.

The available HUMAN governance relationship service cannot solve this by
itself. It deliberately requires its caller to establish authorization
independently.

The available step-up machinery also cannot manufacture that authorization.

This means the project has exposed a real UCII-core gap:

> UCII currently lacks an implemented production first-HUMAN governance
> bootstrap path.

This is the missing first link required before the ordinary HUMAN lifecycle
ceremony can legitimately operate.

### Why the project stops here instead of bypassing the gap

The demo MUST NOT be completed by creating fake or alternate authority.

Specifically, do not:

- manufacture a HUMAN row directly;
- manufacture an ACTIVE factor directly;
- manufacture a governance relationship directly;
- make AssemblyAI or the LLM an authority source;
- make entitlement an authority source;
- make payment an authority source;
- expose raw controller authority to the Voice runtime;
- use a Voice-specific bypass that would not be valid reusable UCII behavior.

The final lifecycle remains fail-closed until UCII has a legitimate bootstrap
path.

### Adoption hypothesis discovered during investigation

The missing first-HUMAN bootstrap may also be relevant to UCII's observed zero
completed adoption.

It is a confirmed blocker to completing any path that reaches a HUMAN-governed
authority boundary without an already established HUMAN governance root.

It is NOT yet proven to be the reason no external AI agent or human has adopted
UCII.

The distinction is important:

- if Ambassador interactions reached explicit opt-in/onboarding intent and then
  stopped at unresolved authority, this defect may explain failed completion;
- if interactions never reached adoption interest, explicit opt-in, or
  onboarding intent, the principal friction is upstream.

The real Ambassador adoption history should therefore be inspected after this
checkpoint is safely committed, rather than assuming causation.

### Exact resume point

Do not restart signer, custody, credential, entitlement, identity, enrollment,
or delegated-execution work.

Resume at:

    UNIT 3G — PROTECTED FIRST-HUMAN BOOTSTRAP REUSE BOUNDARY

Unit 3G must first inspect the existing protected controller lifecycle
authorization pattern and determine whether it can safely anchor the smallest
reusable UCII first-HUMAN bootstrap primitive.

After the first-HUMAN governance prerequisite is resolved, return directly to
the final Voice Authority lifecycle proof.

The Ambassador adoption-funnel investigation remains a separate evidence task
and must not replace completion of the Voice Authority hackathon path.


---

## 2026-09-20 — Domain Bootstrap, Recovery, Succession, and Factory-Reset Requirements

### Clarification: the first HUMAN is domain-scoped

The first-HUMAN governance problem discovered during the Voice Authority
lifecycle investigation is NOT a requirement to make Brad, UCII Labs, or any
other person the permanent supreme authority for all UCII.

It is the requirement to establish the first legitimate HUMAN governance
authority for a particular adopter's governance domain.

Conceptually:

    new adopter / uninitialized domain
        -> protected first-HUMAN bootstrap
        -> adopter's initial HUMAN governance authority
        -> bootstrap closes
        -> normal governance

Separate adopters and governance domains must remain authority-isolated.

Participation in bootstrap MUST NOT give UCII Labs, an operator, or the first
HUMAN a hidden universal authority over unrelated domains.

### The first HUMAN cannot be a permanent single point of failure

The initial HUMAN governance principal must not become an immortal controller
whose loss permanently kills access to the governed domain.

The architecture must distinguish:

    normal succession / replacement
        !=
    recovery
        !=
    factory reset

Normal succession applies when valid governance remains available and can
legitimately add, replace, or remove controllers.

Recovery applies when ordinary governance is unavailable or unsafe, including
lost credentials, compromise, incapacity, departure, or other lockout
conditions.

Factory reset is the destructive option for intentionally terminating the
existing governance domain state and returning that domain to a new
initialization boundary.

### Recovery must not depend on the lost authority

A recovery design that depends only on the first HUMAN's everyday credential or
factor does not solve loss of that credential or factor.

The recovery mechanism therefore must be independently established and
protected.

It must not turn UCII Labs or the Voice application into a master recovery
authority.

Recovery must be attributable, fail closed, and capable of invalidating
compromised governance authority before normal governance resumes.

### Factory reset is not ordinary revocation

Factory reset must not be implemented as merely deleting the original HUMAN or
revoking one relationship.

A true reset must terminate the old governance generation and invalidate the
authority-bearing state that could otherwise survive into a fresh bootstrap.

The exact implementation remains a UCII-core design task, but the contract must
cover, as applicable:

- HUMAN governance relationships;
- delegated authorities;
- credentials;
- sessions and refresh state;
- step-up factors/challenges/evidence;
- lifecycle authorizations;
- recovery material;
- controller authority;
- domain-scoped entitlements;
- outstanding economic/execution authority; and
- other stale capabilities tied to the terminated governance generation.

Required immutable provenance/audit evidence should remain available according
to its retention contract. Resetting authority is not permission to falsify or
erase historical evidence.

### Governance generation / epoch

The UCII-core design should evaluate an explicit governance generation or
equivalent epoch mechanism.

The desired invariant is:

    generation N
        -> protected destructive reset
        -> generation N terminated
        -> protected first-HUMAN bootstrap
        -> generation N+1

Authority issued solely under generation N must not resurrect in generation
N+1.

This includes stale credentials, sessions, delegated authority, lifecycle
authorizations, recovery artifacts, or other capabilities that would otherwise
reintroduce the destroyed authority state.

### Bootstrap must close

First-HUMAN bootstrap is a special ceremony available only to a legitimately
uninitialized governance domain.

After initialization it must close.

It must not be reopened by:

- voice;
- an LLM;
- successful authentication;
- possession of a normal step-up factor;
- entitlement;
- x402 payment;
- agent identity;
- ordinary application credentials; or
- a caller merely claiming to be the owner.

Subsequent governance changes must use ordinary governance, independently
protected recovery, or explicitly authorized destructive reset.

### Voice Authority implication

For the current Voice Authority deployment, Brad may become the first
legitimate HUMAN governance principal for this specific Voice Authority
governance domain once the reusable UCII bootstrap primitive exists.

That must not imply authority over every UCII adopter or unrelated governance
domain.

The Voice project must consume the reusable UCII lifecycle rather than invent a
Voice-specific root.

### Expanded acceptance requirements before first-HUMAN implementation

The next UCII-core design work must account for the complete lifecycle:

1. establish the first HUMAN legitimately;
2. close bootstrap after initialization;
3. support normal controller succession/replacement;
4. prevent the first HUMAN from becoming an immortal root;
5. provide independent recovery from loss or compromise;
6. avoid permanent domain lockout;
7. provide an explicitly protected destructive factory-reset path;
8. invalidate old authority across reset using a generation/epoch or equivalent
   boundary;
9. retain required immutable provenance;
10. prevent UCII Labs/operator infrastructure from becoming a hidden skeleton
    key.

UNIT 3G remains read-only first. It must inspect whether the existing protected
controller lifecycle trust boundary can anchor these requirements before any new
UCII-core primitive is implemented.

The frozen Human Authority Ceremony contract remains historical/frozen and is
not modified by this checkpoint. These newly discovered lifecycle requirements
are recorded here as the current governing implementation constraint.


### Cross-identity lifecycle requirement

The Voice Authority discovery also raises a UCII-wide machine/agent lifecycle
question that must be included in Unit 3G.

UCII already supports real cryptographic enrollment and operation for
non-HUMAN identities. That is not the same as proving a complete governance,
recovery, succession, and destructive-reset lifecycle for those identities.

The design must preserve:

    machine identity != governance authority

An AI agent, robot, device, or service proving possession of its own credential
must not automatically gain ultimate ownership/governance authority over
itself.

Unit 3G must inspect how UCII currently handles machine-side credential loss,
credential/controller compromise, controller replacement, authority
revocation, recovery, transfer of legitimate control, destructive reset, and
stale-authority invalidation.

Where possible, UCII should prefer one reusable governance-domain lifecycle
rather than independent HUMAN, AI_AGENT, ROBOT, DEVICE, SERVICE, and
ORGANIZATION bootstrap/reset systems.

The Voice implementation must remain narrowly scoped to what the demo needs,
but the UCII-core primitive it consumes must not create a HUMAN-only dead end
that later requires parallel trust roots for machines.

Accordingly, Unit 3G must determine whether governance generation/epoch,
recovery, succession, and destructive reset belong at a shared governance-domain
layer and identify which machine-side guarantees already exist versus which
remain future UCII-core work.

This requirement does not assert that machine-side recovery or factory reset is
currently missing in full. That conclusion requires the read-only Unit 3G
inspection.
