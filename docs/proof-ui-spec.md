# Voice Authority Proof UI Specification

## Status

**DESIGN CONTRACT — IMPLEMENT AFTER THE REAL ASSEMBLYAI VOICE PATH IS ESTABLISHED**

This document defines the judge-facing and user-facing proof UI for the UCII Voice Authority Agent. The UI is not decorative evidence and must not manufacture security state. It renders real AssemblyAI conversation events and real UCII identity, step-up, governance, lifecycle-authorization, delegation, revocation, execution, and provenance state.

Core visual thesis:

> **AssemblyAI hears and understands the human. UCII determines whether what the human asked for is allowed to happen.**

Core security thesis:

> **Understanding a human request does not create authority to execute it.**

The interface should make the separation visible:

`Voice != Intent != Identity != Authentication != Step-Up != Authority != Decision != Execution`

## 1. Visual direction

The application should look like a near-future technical control plane rather than a generic SaaS dashboard.

Design language:

- deep black / navy base;
- restrained glass-like technical panels;
- fine borders and grid details;
- subtle depth, particles, traces, and motion where they communicate live system state;
- electric cyan for HUMAN / microphone / input state;
- violet or magenta for UCII Voice Agent / output state;
- green reserved for verified / established / ALLOW states;
- amber reserved for step-up, clarification, pending, and attention-required states;
- red reserved primarily for DENY, REVOKED, failed verification, and security failure;
- high legibility and strong contrast over visual spectacle;
- AssemblyAI branding/integration attribution clearly visible because AssemblyAI is a central runtime component of the project;
- UCII branding and authority role clearly visible without visually implying that AssemblyAI itself is the authority source.

Motion must communicate real state. Avoid fake security animations, fake waveforms, fake confidence, or fabricated evidence.

## 2. Dual real-time voice tracers

The primary voice console should contain two visually separate waveform / frequency-trace surfaces.

### 2.1 HUMAN voice input tracer

Label:

**YOUR VOICE — INPUT**

Visual identity: electric cyan.

The visualization should be driven by the actual microphone audio stream, not a decorative looping animation. Where browser/runtime support allows, use actual amplitude and/or frequency-domain information from the live audio path.

State progression should be visible:

`LISTENING -> SPEAKING -> TRANSCRIBING -> FINALIZED`

The waveform should respond to the human's real speech. When the turn is finalized, the active trace may settle/fade while the finalized transcript remains visible.

### 2.2 Agent voice output tracer

Label:

**UCII VOICE — OUTPUT**

Visual identity: violet / magenta.

The visualization should be driven by the actual returned/playback audio stream where technically available. It should not mirror the input waveform or use a fake repeated animation.

State progression should be visible where supported:

`PREPARING -> RESPONDING -> COMPLETE`

The two traces must remain visually and semantically distinct so a viewer immediately understands the two communication directions.

## 3. Live transcript and finalized transcript

A prominent transcript surface should sit near the HUMAN input waveform.

Label:

**LIVE TRANSCRIPT — YOU**

The UI should display partial AssemblyAI transcription progressively while the human is speaking where the supported event contract provides it.

Partial/unfinalized transcript text should be visually distinguishable from finalized transcript text, for example through lower emphasis. Security-relevant interpretation must never rely on partial transcript state.

When AssemblyAI finalizes the human turn, the transcript should visibly transition to a stable finalized state.

This serves two purposes:

1. usability — the human can see what the system believes it heard and can restate or clarify when needed;
2. proof — judges can distinguish speech recognition from the later UCII authority decision.

The agent response should have a corresponding visible text surface:

**UCII RESPONSE**

This should allow the spoken response to be read as well as heard.

## 4. HEARD / UNDERSTOOD / REQUEST separation

The interface should explicitly distinguish three layers:

- **HEARD** — finalized human transcript;
- **UNDERSTOOD** — AssemblyAI/application interpretation;
- **REQUEST** — bounded structured operation proposed to the deterministic authority/application layer.

For a consequential request, the structured operation display should show only the fields actually established by the application contract, for example:

`GRANT / target agent / compute purchase / $50 limit / 1 hour`

No model confidence score, transcript, or semantic interpretation may be rendered as UCII authorization.

## 5. Live Authority Chain

A central proof component should visualize the security progression in real time:

`VOICE -> INTENT -> IDENTITY -> STEP-UP -> AUTHORITY -> DECISION -> EXECUTION`

Each stage should illuminate only when the corresponding real system state is established.

Example legitimate sensitive GRANT progression:

1. spoken request finalized — `VOICE` established;
2. bounded operation parsed — `INTENT` established;
3. authenticated HUMAN principal established — `IDENTITY` established;
4. consequence policy requires independent factor proof — `STEP-UP REQUIRED`;
5. enrolled factor challenge verified and durable evidence established — `STEP-UP` established;
6. UCII freshly establishes the required HUMAN lifecycle governance authority — `AUTHORITY` established;
7. UCII returns the applicable decision — `ALLOW`;
8. protected lifecycle operation succeeds — `EXECUTION` established.

The UI must not skip intermediate states merely to make the demo faster.

## 6. DENY as a first-class proof state

DENY is a primary demonstration outcome, not an error screen.

A powerful adversarial demo is a perfectly understood unauthorized request, for example an unauthorized principal asking to increase an agent's purchasing authority.

The interface should be capable of showing simultaneously:

- `VOICE` — established;
- `INTENT` — established;
- `IDENTITY` — established where applicable;
- `AUTHORITY` — **NOT ESTABLISHED**;
- `DECISION` — **DENY**;
- `EXECUTION` — **NOT INVOKED**.

A concise reason should be shown from deterministic application/UCII evidence, for example:

**Lifecycle authority not established.**

The visual point is that AssemblyAI can understand the request correctly while UCII still refuses the state transition.

## 7. Current Authority panel

Keep the selected agent's current security state visible during the demonstration.

Useful fields, when genuinely available, include:

- agent display label;
- UCII identity verification state;
- delegated authority state;
- allowed operation/resource;
- bounded scope or monetary limit;
- expiry / remaining lifetime;
- controlling HUMAN/governance state at an appropriate non-secret level.

The revocation demonstration must preserve the distinction between identity and authority.

Before revocation, the UI may show:

`IDENTITY: VERIFIED`

`AUTHORITY: ACTIVE`

After revocation, the same agent should visibly remain:

`IDENTITY: VERIFIED`

`AUTHORITY: REVOKED`

The interface must not imply that revoking delegated authority destroys or invalidates the agent's cryptographic identity.

## 8. Consequence-based step-up presentation

When a sensitive operation requires step-up, the UI should visibly enter a pending state rather than appearing frozen.

Example:

**STEP-UP REQUIRED**

**Verification sent through enrolled EMAIL factor**

The interface may show challenge lifetime / expiry and bounded ceremony status, but must not expose stored challenge hashes, secrets, reusable credentials, or protected controller material.

Successful challenge verification should be rendered as factor-possession evidence only. It must never be labeled as authority.

## 9. UCII state / orb visualization

A central UCII visualization may provide a strong futuristic focal point if it remains subordinate to the factual proof UI.

Suggested state language:

- blue/cyan — authenticated / normal secure state;
- amber — clarification or step-up pending;
- green — current operation authorized;
- red — denied / revoked / security failure.

The visualization may react to voice and state transitions, but must derive its state from the actual application state machine rather than independently deciding outcomes.

## 10. AssemblyAI-visible runtime metrics

Because AssemblyAI is a central hackathon technology, the interface should visibly expose useful AssemblyAI/runtime evidence where the supported API provides it.

Potential fields:

- session connection state;
- transcription/finalization state;
- STT confidence where actually supplied;
- STT latency where accurately measurable;
- response / TTS latency where accurately measurable;
- language / session configuration;
- interruption state where relevant.

Do not invent metrics merely to fill the interface.

## 11. Security Evidence drawer

The main interface should remain readable, while a secondary expandable evidence view gives technical judges deeper proof.

Where non-secret and actually available, it may expose:

- session ID;
- ceremony ID;
- UCII identity ID or safe abbreviated representation;
- governance relationship reference;
- step-up evidence ID;
- lifecycle authorization ID;
- delegated authority ID;
- operation and bounded scope;
- relevant timestamps / expiry;
- authorization decision reference;
- execution/provenance reference.

Secrets, challenge plaintext after use, challenge hashes, controller secrets, reusable credentials, wallet secrets, payment proofs, private keys, and protected custody material must never be exported or displayed.

## 12. Session information and controls

Useful controls may include:

- clear/reset conversation for demo preparation;
- mute/unmute agent audio;
- end session;
- export session/transcript/audio/evidence;
- optional evidence-detail toggle.

Controls must not bypass the Human Authority Ceremony Engine or UCII authority checks.

## 13. Export system

Export is a real product feature, not just a screenshot/download button.

The export surface should support distinct artifacts where practical:

- human transcript;
- agent transcript;
- combined conversation transcript;
- non-secret security/provenance evidence;
- human/input audio where recording is permitted and intentionally enabled;
- agent/output audio where recording is permitted and intentionally enabled;
- combined conversation audio where technically practical.

### 13.1 Audio quality profiles

The export UI should offer a high-quality archival option and smaller-file options.

The highest-quality option should preserve the **highest native audio quality actually available from the selected AssemblyAI/session audio contract and our browser/audio pipeline**. Do not claim stereo merely because stereo sounds higher quality.

The currently selected AssemblyAI voice integration contract uses 24 kHz mono PCM16 by default. If the actual implemented AssemblyAI path remains mono, the archival export should preserve that native mono signal rather than artificially duplicating it into fake stereo.

If a supported AssemblyAI/session path later provides genuine independent stereo channels or higher native sample rate/bit depth, the archival profile should preserve that supported native quality.

Recommended user-facing profiles:

- **ARCHIVAL / NATIVE** — lossless or minimally transformed export preserving the highest genuine native sample rate, bit depth, and channel layout available from the implemented input/output paths;
- **HIGH QUALITY** — high-quality compressed audio for convenient playback/sharing;
- **STANDARD** — balanced quality and file size;
- **COMPACT** — lower bitrate/quality for small files.

Exact codecs, bitrates, sample rates, and container formats should be frozen only after the real browser + AssemblyAI audio paths are implemented and inspected. Prefer broadly playable formats for user convenience while retaining a native/lossless archival path where practical.

### 13.2 Separate versus combined channels

Where technically practical, retain HUMAN input and agent output as separate source tracks so they can be exported independently.

For a combined conversation export, if the sources are independently available, we may offer a true two-channel presentation with HUMAN and agent audio placed on separate channels for analysis/demo playback. This is a derived presentation format and must not be described as native AssemblyAI stereo if the source streams themselves are mono.

A simpler mixed mono/stereo convenience export may also be offered, but the archival originals should remain available at their genuine source quality.

### 13.3 Export privacy and security

Export must be intentional and user-triggered. The product should make clear what is included.

Never include protected secrets or reusable authority material in an export. Evidence export is proof of what happened, not a portable authority token.

## 14. Suggested layout

A strong desktop judge/demo layout:

### Header

- UCII Voice Authority Agent branding;
- concise authority thesis;
- AssemblyAI attribution;
- current session/security state.

### Main upper region

Two side-by-side voice panels:

- HUMAN input waveform + live/final transcript;
- UCII Voice output waveform + response text.

### Main middle region

- Live Authority Chain;
- structured `HEARD / UNDERSTOOD / REQUEST` proof;
- current operation decision.

### Main lower region

- Current Authority panel;
- UCII identity state;
- step-up / ceremony state;
- provenance/evidence summary.

### Secondary side region

- session information;
- AssemblyAI/runtime metrics;
- export and demo controls;
- expandable technical evidence.

The layout must remain usable at narrower widths by reflowing panels rather than hiding security state.

## 15. Judge-facing canonical transitions

The UI should make the north-star demonstration visually obvious:

### Initial request without authority

`UNDERSTOOD -> IDENTITY VERIFIED -> AUTHORITY NOT ESTABLISHED -> DENY -> EXECUTOR NOT INVOKED`

### Legitimate HUMAN grant ceremony

`VOICE REQUEST -> AUTHENTICATED HUMAN -> STEP-UP REQUIRED -> EMAIL FACTOR VERIFIED -> FRESH LIFECYCLE AUTHORIZATION -> PROTECTED GRANT -> ACTIVE BOUNDED AUTHORITY`

### Authorized action

`SAME AGENT -> SAME IDENTITY -> SAME CAPABILITY -> FRESH AUTHORITY CHECK -> ALLOW -> EXECUTE`

### Unauthorized escalation

`REQUEST UNDERSTOOD -> PRINCIPAL LACKS REQUIRED LIFECYCLE AUTHORITY -> DENY`

### Legitimate revocation

`AUTHENTICATED HUMAN -> STEP-UP -> FRESH LIFECYCLE AUTHORIZATION -> PROTECTED REVOKE -> AUTHORITY REVOKED`

### Post-revocation replay

`SAME AGENT -> IDENTITY STILL VERIFIED -> AUTHORITY REVOKED -> DENY -> EXECUTOR NOT INVOKED`

This is the visual expression of:

> **Capability is not authority.**

## 16. Implementation boundary

Do not implement this UI by inventing placeholder authority decisions and later trying to retrofit the security model.

Engineering order remains:

1. finish the genuinely required UCII HUMAN lifecycle conversion boundary;
2. leave UCII core;
3. establish the real AssemblyAI microphone/session/finalized-turn/output-audio path;
4. establish bounded structured operation handling;
5. connect the real UCII identity/authority/ceremony path;
6. render the proof UI from real events and real evidence;
7. add export profiles against the actual implemented audio formats;
8. adversarially validate that the UI cannot imply ALLOW when the underlying authority/execution state is DENY or unknown.

The UI is a projection of the security system, never an authority source.

## 17. Acceptance criteria

The proof UI is complete when a judge can understand, without reading source code, all of the following:

- what the human actually said;
- what AssemblyAI transcribed;
- whether the turn is partial or finalized;
- what structured operation the application understood;
- which UCII identity is involved;
- whether step-up is required and whether factor evidence was established;
- whether lifecycle/action authority is actually established;
- why the decision is ALLOW or DENY;
- whether execution actually occurred;
- whether authority is active, expired, or revoked;
- that identity can remain verified after authority is revoked;
- where non-secret technical evidence can be inspected;
- that AssemblyAI provides the conversational runtime while UCII remains the authority control plane;
- that exported audio can preserve genuine native quality or intentionally trade quality for smaller file size; and
- that exported evidence cannot be reused as authority.

The desired five-second comprehension test is:

> **AssemblyAI hears and understands the human. UCII determines whether what the human asked for is allowed to happen.**
