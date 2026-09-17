# AssemblyAI Runtime Technical Contract

## Status

**OBJECTIVE 0B — RUNTIME CONTRACT ESTABLISHED**

Verified against current AssemblyAI technical material on 2026-09-17.

This document freezes the initial AssemblyAI runtime integration boundary for
the UCII Voice Authority Agent.

It does not make AssemblyAI an identity, authentication, authority,
authorization, governance, or execution trust root.

Competition/submission requirements remain a separate Objective 0B verification
gate.

---

## 1. Selected Runtime

The initial implementation will use the AssemblyAI Voice Agent API as the
genuine conversational voice runtime.

The Voice Agent API provides a managed voice pipeline behind a WebSocket,
including:

- streaming speech recognition;
- turn detection;
- conversational / LLM reasoning;
- text-to-speech;
- session management;
- interruption / barge-in behavior; and
- tool calling.

UCII remains independently authoritative for protected identity and authority
decisions.

---

## 2. Browser / Server Architecture

The selected initial architecture is:

    Browser microphone
        |
        v
    AssemblyAI Voice Agent WebSocket
        |
        +--> live transcript events ---------> UI only
        |
        +--> finalized user turn
        |        |
        |        v
        |    bounded proposal / tool request
        |        |
        |        v
        |    UCII application backend
        |        |
        |        v
        |    Human Authority Ceremony Engine
        |        |
        |        v
        |    UCII public / protected boundary
        |        |
        |        v
        |    deterministic result
        |
        +<-- tool result / conversational result
        |
        v
    AssemblyAI response audio
        |
        v
    Browser speaker + proof UI

The browser must not contain the long-lived AssemblyAI API key.

A backend endpoint will mint a short-lived AssemblyAI browser token.

The browser will use that temporary token to establish the Voice Agent
WebSocket.

AssemblyAI temporary-token possession creates AssemblyAI session access only.

It does not create UCII authority.

---

## 3. Voice Agent WebSocket

The current Voice Agent API uses the WebSocket endpoint:

    wss://agents.assemblyai.com/v1/ws

Server-side integrations may authenticate with the AssemblyAI API key through
the supported Bearer mechanism.

Browser integrations must not expose that long-lived key.

The selected browser architecture therefore uses a temporary token minted by
the application backend.

---

## 4. Audio Contract

The default browser voice path uses:

    PCM16
    24,000 Hz
    mono
    base64 encoded in JSON events

Microphone capture should use the browser audio stack and an AudioWorklet or
equivalent supported mechanism appropriate for reliable real-time PCM capture.

Browser microphone configuration should use available acoustic echo
cancellation because agent output may otherwise be re-detected as user speech.

The proof UI may visualize input and output audio, but waveform visualization
is evidence/presentation only.

It is not authority.

---

## 5. Session Establishment

The application configures the Voice Agent session through `session.update`.

The application waits for `session.ready` before treating the session as ready
for microphone audio.

The returned AssemblyAI session identifier should be retained as attributable
runtime evidence.

An AssemblyAI session identifier is not a UCII identity.

---

## 6. User Transcript Events

The Voice Agent protocol distinguishes live/partial transcript information from
the finalized user turn.

The relevant events include:

    transcript.user.delta
    transcript.user

`transcript.user.delta` may drive the live-transcript presentation.

It must not initiate a protected UCII ceremony.

`transcript.user` is the finalized user turn and is the earliest AssemblyAI
transcript event permitted to become source input for security-relevant
structured-request creation.

Therefore:

    partial transcript
        !=
    finalized turn
        !=
    structured request
        !=
    authority

---

## 7. Agent Response Events

Relevant response events include:

    reply.started
    reply.audio
    transcript.agent
    reply.done

`reply.audio` supplies generated response audio for playback.

`transcript.agent` supplies the resulting agent transcript.

These events may drive the UCII response panel and output waveform in the proof
UI.

They do not create or modify UCII authority.

---

## 8. Tool Calling

AssemblyAI Voice Agent sessions support registered tools.

The Voice Agent may emit:

    tool.call

A tool call contains a tool name, call identifier, and structured arguments.

For this project:

    AssemblyAI tool.call
        =
    proposed application operation

It does NOT mean:

    AssemblyAI tool.call
        =
    authorized UCII operation

A security-relevant tool proposal must pass through:

    bounded request validation
        ->
    principal binding
        ->
    Human Authority Ceremony Engine
        ->
    fresh UCII authorization
        ->
    protected operation

where applicable.

The LLM must not receive an alternate path to a consequential executor.

---

## 9. Tool Result Ordering

The Voice Agent protocol requires tool-result handling to respect the
conversation/reply lifecycle.

Tool calls may be accumulated while the reply is active.

Applicable tool results are returned according to the supported `tool.result`
protocol after the corresponding reply lifecycle reaches the required point.

If an AssemblyAI reply is interrupted before a pending conversational tool
result is committed to that reply flow, pending conversational results must be
handled according to the Voice Agent interruption contract rather than blindly
replayed.

This conversational rule must not reverse a protected UCII mutation that has
already committed.

UCII authoritative state wins.

---

## 10. Interruption / Barge-In

The Voice Agent API supports interruption / barge-in.

Relevant runtime evidence includes speech-start / speech-stop events and an
interrupted reply outcome.

The browser must stop stale response playback when the applicable reply is
interrupted.

For protected ceremonies:

    interruption before protected commit

may cancel or interrupt an uncommitted conversational flow where ceremony
policy permits.

But:

    interruption after protected UCII commit

must not silently undo, falsify, or reinterpret the committed authoritative
state.

The next conversational turn must reconcile with authoritative UCII state.

---

## 11. Session Resume

Current Voice Agent behavior supports short-lived session resumption after a
connection loss.

Session resumption is a transport/conversation continuity feature.

It is not proof that a previously established UCII authorization remains valid.

Consequential operations still require the applicable fresh authoritative
decision.

---

## 12. Proof UI Event Mapping

The attached UCII Voice Console visual target can be driven by real runtime
evidence.

Conceptual mapping:

    YOUR VOICE waveform
        <- browser microphone PCM

    LIVE TRANSCRIPT
        <- transcript.user.delta
        <- transcript.user

    UCII VOICE OUTPUT waveform
        <- reply.audio

    UCII RESPONSE
        <- transcript.agent

    SESSION INFO
        <- session.ready / session lifecycle

    UNDERSTANDING
        <- finalized AssemblyAI turn
        <- bounded proposal state

    WHO
        <- UCII principal / identity evidence

    REQUEST
        <- deterministic bounded request

    STEP-UP
        <- Human Authority Ceremony Engine

    AUTHORITY
        <- UCII authoritative state

    DECISION
        <- fresh UCII authorization

    RESULT
        <- protected operation result

    EVIDENCE
        <- attributable AssemblyAI + UCII references

No visual status may be hard-coded as proof in the final demonstration.

---

## 13. Security Boundary

AssemblyAI is trusted for the voice-runtime facts it actually establishes.

Those facts may include:

- session state;
- received speech;
- transcript state;
- finalized conversational turns;
- model-generated proposals;
- tool-call proposals;
- generated response audio; and
- interruption state.

AssemblyAI is not authoritative for:

- UCII identity;
- HUMAN governance membership;
- controller authority;
- delegated authority;
- lifecycle authorization;
- challenge correctness;
- recovery authority;
- entitlement validity;
- x402 authority;
- protected mutation; or
- execution permission.

The governing separation remains:

    Voice
        !=
    Intent
        !=
    Identity
        !=
    Authentication
        !=
    Step-Up Verification
        !=
    Authority
        !=
    Authorization
        !=
    Entitlement
        !=
    Payment
        !=
    Execution

---

## 14. Initial Implementation Decision

The first executable project objective after prerequisite inspection will use:

- browser microphone input;
- AssemblyAI Voice Agent API;
- backend-minted temporary browser token;
- Voice Agent WebSocket;
- 24 kHz mono PCM16 audio;
- live partial transcript presentation;
- finalized user-turn boundary;
- AssemblyAI response audio;
- explicit interruption handling; and
- no consequential UCII execution.

That first proof establishes:

    microphone
        ->
    AssemblyAI
        ->
    finalized spoken turn
        ->
    application

before authority-changing behavior is introduced.

---

## 15. Remaining Objective 0B Gate

This runtime contract does not by itself complete Objective 0B.

Before Objective 0B is marked complete, independently verify and record the
current competition requirements, including:

- required AssemblyAI technology usage;
- eligibility;
- team rules;
- submission deadline and timezone;
- repository/source requirements;
- prototype/demo requirements;
- video/pitch requirements;
- product-feedback requirements;
- judging criteria;
- prize categories; and
- sponsor-specific technical constraints.

Only after that verification may Objective 0B be closed.
