# Voice Authority Proof UI — Functional Requirements

## Status and implementation gate

**FROZEN PRODUCT REQUIREMENTS — IMPLEMENT ONLY AFTER THE CORE AUTHORITY PATH AND REAL ASSEMBLYAI AUDIO PATH ARE WORKING CORRECTLY.**

This file complements `docs/proof-ui-spec.md` and the preferred visual concept at `docs/assets/ucii-voice-authority-ui-concept.svg`.

The UI is not decoration. Every state, waveform, transcript, metric, control, decision, countdown, playback function, and evidence field that appears operational in the production interface must be driven by real application data or explicitly shown as unavailable. No fake waveform, fake confidence, fake latency, fake security state, fake authority transition, fake recording state, or fabricated evidence is permitted.

Implementation order is intentionally strict:

1. finish the required UCII HUMAN lifecycle conversion boundary;
2. leave UCII core;
3. establish and verify the real AssemblyAI microphone/session/finalized-turn/output-audio path;
4. establish bounded structured operation handling;
5. connect the real UCII identity/governance/step-up/authority/execution path;
6. only then implement these UI capabilities against real runtime events and retained audio;
7. verify every interactive control and displayed state end to end;
8. adversarially validate that UI state can never imply authority or execution that the underlying system did not establish.

The preferred SVG is a visual north star, not permission to simulate functionality.

## 1. Real-time HUMAN waveform — mandatory

The **YOUR VOICE — INPUT** graph is a functional audio instrument, not a decorative animation.

Requirements:

- driven continuously by the actual microphone stream while capture is active;
- visibly responds to the user's real amplitude and/or frequency-domain audio data;
- updates in real time with sufficiently low latency to feel coupled to speech;
- becomes idle when microphone capture is idle;
- never plays a canned, looping, randomized, mirrored, or fabricated waveform;
- exposes clear `LISTENING`, `SPEAKING`, `TRANSCRIBING`, and `FINALIZED` states derived from real runtime events;
- provides a microphone input-level indication so a user can verify the microphone is receiving useful signal before speaking;
- reports unavailable/unsupported rather than drawing fake data if the required browser/runtime audio data cannot be obtained.

The implementation should use the actual browser audio pipeline (for example, Web Audio analysis primitives where appropriate) while preserving the audio format required by the verified AssemblyAI integration.

## 2. Real-time UCII/agent output waveform — mandatory

The **UCII VOICE — OUTPUT** graph is equally functional.

Requirements:

- driven by the actual returned/playback audio stream;
- updates in real time while the agent is speaking;
- remains independent from the HUMAN input waveform;
- never mirrors, reuses, randomizes, or decoratively synthesizes the HUMAN waveform;
- exposes real `PREPARING`, `RESPONDING`, `INTERRUPTED` where supported, and `COMPLETE` states;
- settles to idle when playback ends;
- reports unavailable rather than fabricating a trace when the playback pipeline cannot expose real analysis data.

The two graphs must visually communicate two independent audio directions.

## 3. Audio retention and per-turn playback

Where session recording is intentionally enabled and permitted, retain HUMAN input and UCII output audio as independently addressable source material.

Every finalized HUMAN transcript turn with retained audio should provide a compact **Play/Pause** control. Every finalized UCII response with retained audio should provide its own **Play/Pause** control.

Per-turn playback should support, where practical:

- play/pause;
- seek/scrub;
- elapsed and total duration;
- skip backward/forward approximately 10 seconds for longer segments;
- playback speed options such as 0.75x, 1x, 1.25x, and 1.5x;
- timestamp of the original turn;
- clear indication of whether the audio is HUMAN or UCII output.

Partial/unfinalized transcript fragments must not pretend to have finalized per-turn playback semantics.

## 4. Waveform/transcript synchronization

Where technically practical, finalized audio and finalized transcript should be synchronized.

Desired interaction:

- playback position is visible on the corresponding waveform;
- clicking/seeking the waveform changes audio playback position;
- transcript text or the current transcript segment highlights as its audio plays when reliable timing data is available;
- clicking a finalized conversation turn selects its audio and associated evidence;
- do not fabricate word-level timing when the real integration does not provide enough evidence to support it.

## 5. Conversation timeline and history

The Live Transcript experience should expand into a chronological conversation history rather than losing previous turns.

Each finalized turn should retain links to the real information available for that turn, including as applicable:

- HUMAN transcript and audio;
- UCII response transcript and audio;
- timestamp and duration;
- finalized/partial state;
- `HEARD` representation;
- `UNDERSTOOD` interpretation;
- bounded `REQUEST`;
- identity involved;
- step-up state;
- authority decision;
- execution outcome;
- non-secret evidence/provenance references.

Selecting a historical turn should restore the relevant proof context without changing historical truth or current authority state.

## 6. Transcript convenience controls

Finalized HUMAN and UCII transcript entries should support lightweight convenience actions:

- copy transcript/response;
- play associated audio when retained;
- inspect associated proof/evidence;
- identify timestamp and speaker/source.

These controls must remain subordinate to the security state and should not clutter the primary view.

## 7. Clarification / Say Again state

Ambiguity must be visible and fail closed.

When a consequential request is incomplete, low-confidence in a security-relevant field, internally inconsistent, or missing required bounded fields, the UI should show a clear **CLARIFICATION REQUIRED** or **SAY AGAIN** state rather than implying an authorization decision.

Examples include an unclear monetary amount, target, operation, duration, or other required scope field.

The UI should identify the specific field requiring clarification where the deterministic application layer can do so safely.

Clarification is not DENY, ALLOW, authentication, step-up, or authority. It is a distinct conversational state.

## 8. Microphone, speaker, recording, and device controls

Provide a compact settings/control surface for the real media pipeline, including where supported:

- microphone selection;
- speaker/output selection;
- microphone input-level meter;
- mute/unmute;
- recording enabled/disabled state;
- explicit recording indicator when session audio is being retained;
- clear handling of browser permission failure or missing devices.

Recording state must be truthful and must not be inferred merely from an active AssemblyAI session.

## 9. Authority countdown and expiry

When bounded authority has a real expiry, display a live remaining-time countdown derived from the authoritative expiry timestamp.

Example:

`AUTHORITY: ACTIVE — EXPIRES IN 47:21`

The countdown must not itself decide expiration. UCII remains authoritative. When the authoritative state changes to expired/revoked/not established, the UI must update accordingly.

## 10. Decision history

Provide a compact chronological decision trail derived from real decisions/provenance, for example:

`DENY -> GRANT -> ALLOW -> REVOKE -> DENY`

Each entry should include a timestamp and should be selectable to inspect its associated non-secret evidence.

Historical DENY/ALLOW/GRANT/REVOKE outcomes must not be rewritten when later state changes.

## 11. Identity-versus-authority transition

Revocation is a key visual proof moment.

When delegated authority changes from ACTIVE to REVOKED, the UI should visibly animate or otherwise emphasize the transition while leaving the cryptographic identity state unchanged when it remains valid.

Canonical proof:

`IDENTITY: VERIFIED` remains visible.

`AUTHORITY: ACTIVE -> REVOKED` changes visibly.

A subsequent identical action should then show a fresh authority check and `DENY`, with execution not invoked.

## 12. Export drawer and complete session package

`Export` should open an explicit selection surface rather than silently downloading an unspecified artifact.

Selectable export components should include where available and intentionally retained:

- HUMAN transcript;
- UCII response transcript;
- combined conversation transcript;
- HUMAN source audio;
- UCII source audio;
- combined conversation audio;
- non-secret security/provenance evidence;
- session metadata;
- complete session package containing the selected safe artifacts.

Audio quality profiles remain:

- **ARCHIVAL / NATIVE** — preserve the highest genuine native quality available from the implemented source path;
- **HIGH QUALITY** — high-quality compressed convenience export;
- **STANDARD** — balanced size/quality;
- **COMPACT** — smaller-file export.

Do not invent stereo as a quality upgrade. If HUMAN and UCII are independently retained mono sources, a derived two-channel conversation export may place HUMAN on one channel and UCII on the other. It must be labeled as a **derived two-channel conversation**, not native AssemblyAI stereo.

Exact codecs, sample rates, bitrates, containers, and channel layouts are frozen only after the real implemented audio paths are inspected.

## 13. Export and privacy safety

Export is user-triggered and explicit about contents.

Never export reusable authority, controller secrets, challenge secrets, challenge hashes, private keys, wallet secrets, reusable payment proofs, protected credentials, or other custody material.

A compact privacy/security indicator may communicate that exported evidence is non-secret proof rather than portable authority.

## 14. Keyboard and interaction convenience

Where it improves the real desktop experience, support documented keyboard controls such as:

- hold/toggle microphone interaction;
- play/pause selected retained audio;
- escape/cancel a noncommitted conversational operation where safe;
- mute/unmute agent playback.

Keyboard controls must never bypass ceremony, authority, confirmation, or protected execution requirements.

## 15. Demo Mode

A **Demo Mode** may simplify presentation without changing system behavior.

Demo Mode may enlarge or emphasize the real:

`VOICE -> INTENT -> IDENTITY -> STEP-UP -> AUTHORITY -> DECISION -> EXECUTION`

chain and hide secondary controls, but it must consume exactly the same runtime state as the normal UI.

Demo Mode must never inject scripted ALLOW/DENY states, fake metrics, prerecorded security outcomes, fake evidence, or alternate authority logic.

## 16. System health strip

Provide a compact real health/status surface for critical dependencies where actual status can be measured, such as:

- AssemblyAI connection;
- UCII API/control-plane reachability;
- microphone capture;
- output audio/playback;
- secure application session.

A failed or unknown dependency should be shown as failed/unknown rather than green by default.

This is especially important for live demonstration diagnosis.

## 17. Visual density rule

The preferred futuristic dashboard should remain clean. New functionality should use compact contextual controls, drawers, hover/focus details, selected-turn views, and progressive disclosure rather than filling the primary console with permanent buttons.

The primary five-second hierarchy remains:

**Speak -> See what was heard -> See what was understood -> See who is acting -> See whether authority exists -> See ALLOW/DENY -> See whether anything actually happened.**

## 18. Functional acceptance criteria

The UI work is not complete because it visually resembles the SVG. It is complete only when the relevant visible features work against real runtime state.

At minimum verify end to end that:

1. HUMAN waveform visibly follows real microphone audio in real time;
2. UCII output waveform visibly follows real returned/playback audio in real time;
3. the two waveforms are independently sourced;
4. partial and finalized transcripts are correctly distinguished;
5. retained finalized HUMAN audio can be replayed from its transcript turn;
6. retained finalized UCII audio can be replayed from its response turn;
7. playback seeking/synchronization works to the level supported by real timing data;
8. conversation history preserves prior turns and outcomes;
9. ambiguous consequential requests enter clarification rather than silently expanding scope;
10. device/recording indicators reflect actual media state;
11. authority countdown reflects real expiry without becoming the authority source;
12. decision history reflects real historical decisions/provenance;
13. revocation visibly changes authority without falsely invalidating identity;
14. export produces the selected real artifacts at the selected supported quality;
15. no export contains reusable authority or protected secrets;
16. Demo Mode renders real state only;
17. health indicators report actual measured/known status;
18. no decorative fallback can be mistaken for live audio, authority, evidence, execution, or runtime metrics.

## 19. Non-negotiable product rule

> **Nothing that looks operational is merely decorative.**

Visual polish is encouraged, but animation and presentation must be projections of real audio, real conversation state, real UCII state, real evidence, or clearly identified non-operational visual atmosphere. In particular, the two voice wave graphs are functional real-time audio visualizers and are mandatory product behavior.
