# Hackathon Requirements

## Event

AssemblyAI Voice Agent Hackathon, hosted through lablab.ai together with
AssemblyAI.

- Format: online, month-long hackathon
- Build window: September 1-30, 2026
- Submission deadline: September 30, 2026 at 11:00 AM Eastern Daylight Time
- Published prize pool: $10,000
- Published awards: five winners, each receiving $1,000 cash plus $1,000
  in AssemblyAI API credits

Prize eligibility, availability, distribution, and other award terms remain
subject to the event and lablab.ai terms.

## Project status

- Participant: Brad Phee / EtashRhys
- Team: `UCII Labs`
- Team model: closed solo team
- Repository: `EtashRhys/ucii-voice-authority-agent`
- Project: UCII Voice Authority Agent
- Build status: documentation/foundation only
- Submission status: not submitted

## Challenge technology contract

The challenge requires building a voice agent using AssemblyAI's real-time
voice AI technology.

The event provides two principal implementation paths:

1. AssemblyAI Voice Agent API
2. AssemblyAI Realtime Speech-to-Text API with participant-controlled
   orchestration

This project selects the AssemblyAI Voice Agent API path.

The event describes that path as an end-to-end voice-agent connection with
speech-to-text, LLM routing and voice output, turn-taking and voice activity
detection, and JSON-Schema tool calling.

AssemblyAI must therefore be a genuine runtime component of the working
voice-agent experience rather than a decorative or incidental dependency.

The detailed runtime architecture is frozen separately in
`docs/assemblyai-technical-contract.md`.

## UCII authority boundary

AssemblyAI provides the voice interaction surface.

UCII independently provides the identity and authority control plane.

The governing separation remains:

VOICE != INTENT != IDENTITY != AUTHENTICATION != STEP-UP != AUTHORITY
!= AUTHORIZATION != ENTITLEMENT != PAYMENT != EXECUTION

Understanding a request does not create authority to execute it.

AssemblyAI transcription, conversation state, tool-call proposals, model
output, or successful voice understanding cannot independently create UCII
identity, governance authority, delegated authority, authorization,
entitlement, payment authority, or execution authority.

## Participation and team rules

The event is online and welcomes participants regardless of previous AI or
coding experience.

The event-specific team size is 1-6 people.

Participants register through lablab.ai. The event also directs participants
to the lablab.ai Discord community.

The current solo `UCII Labs` team is within the published team-size boundary.

## Required submission package

The event page requires the following submission material.

### Basic information

- Project title
- Short description
- Long description
- Technology and category tags

### Media and presentation

- Cover image
- Video presentation
- Slide presentation

### Application and source

- Public GitHub repository
- Demo application platform
- Application URL

The final submission therefore requires a publicly reachable working
application and public source repository; a local-only proof is not the
intended final submission surface.

## Originality and repository requirements

The event states that submissions must be original and MIT-compliant.

For this project:

- the hackathon repository remains independently identifiable;
- AssemblyAI voice-agent integration is implemented as hackathon work;
- reused UCII infrastructure is disclosed accurately rather than represented
  as newly created during the event;
- third-party dependencies are identified accurately;
- the public repository must not expose production secrets, API keys,
  private keys, controller or recovery secrets, reusable authentication
  material, wallet secrets, or reusable payment proofs.

Use of existing UCII infrastructure does not change the requirement that the
submitted Voice Authority Agent itself be an original hackathon project.

## Current planned submission artifact

The working project will demonstrate:

- real spoken input;
- real AssemblyAI-powered voice interaction;
- finalized conversational turns;
- bounded structured proposed consequential action;
- real UCII identity/authentication binding through the supported public
  boundary;
- explicit UCII authority evaluation;
- denial when authority is absent;
- protected human authority ceremony where required;
- bounded delegated authority;
- successful execution while authority is valid;
- revocation;
- denial after revocation while identity remains verified;
- verifiable provenance/evidence;
- judge-facing visual proof backed by actual runtime state.

The UI must not hardcode successful security states or claim security
properties that the implementation has not established.

## Judging criteria

The event publishes four judging criteria.

### Application of Technology

How effectively the selected technology is integrated into the solution.

For this project, AssemblyAI must be visibly and materially involved in the
real working voice path.

### Presentation

Clarity and effectiveness of the project presentation.

The demonstration should make the distinction between understanding a
request and possessing authority to execute it observable rather than merely
described.

### Business Value

Impact and practical value, including fit within business areas.

The project should demonstrate why bounded and revocable authority matters
when voice agents can initiate consequential real-world actions.

### Originality

Uniqueness and creativity of the solution, including demonstrated behaviors.

The project should demonstrate its authority architecture through real
contrasting states and outcomes.

These project implications guide implementation and presentation scope. They
do not modify UCII security semantics.

## Prize structure

The published prize pool is $10,000.

Five winners are listed, each receiving:

- $1,000 cash
- $1,000 in AssemblyAI API credits

No separate sponsor-specific prize track is established by the event material
reviewed for this Objective 0B gate.

## Product feedback requirement

The event material reviewed for this gate does not establish a separate
mandatory product-feedback submission artifact.

Product feedback may still be useful to AssemblyAI and may be recorded by the
project, but it must not be represented as a mandatory competition
requirement without additional authoritative event guidance.

## Sponsor-specific technical constraints

The material reviewed establishes AssemblyAI real-time voice AI as the
required challenge technology.

No additional sponsor-specific authority, payment, entitlement, custody, or
identity requirement was established by the event material reviewed for this
gate.

AssemblyAI API credits are an economic resource only and cannot create UCII
authority.

## Competition readiness checklist

- [x] AssemblyAI technology usage verified
- [x] general eligibility verified
- [x] team-size rule verified
- [x] submission deadline and timezone verified
- [x] public GitHub repository requirement verified
- [x] demo application/platform and application URL requirement verified
- [x] video presentation requirement verified
- [x] slide presentation requirement verified
- [x] product feedback checked; no separate mandatory artifact established
- [x] judging criteria verified
- [x] prize structure verified
- [x] sponsor-specific technical boundary reviewed

## Final submission revalidation gate

Requirements can change or be clarified during an active event.

Immediately before submission, re-check the live authoritative event and
submission surfaces for:

- deadline and timezone;
- participant/team registration;
- submission-field limits;
- media format and duration constraints;
- public repository and licensing requirements;
- demo reachability;
- application URL;
- any newly published AssemblyAI technical requirement;
- any newly published sponsor requirement;
- any newly published eligibility or prize restriction.

If a live authoritative requirement conflicts with this document, the current
official requirement controls.

## Objective 0B completion boundary

Objective 0B consists of two verified contracts:

1. `docs/assemblyai-technical-contract.md`
2. `docs/hackathon-requirements.md`

Together they establish the technical and competition boundary required
before application implementation begins.

AssemblyAI provides the real voice interaction surface.

UCII independently provides the identity and authority control plane.

After this requirements update is reviewed, committed, synchronized, and
repository parity is proven, implementation may advance to Objective 1:

MICROPHONE -> ASSEMBLYAI -> FINALIZED TURN -> APPLICATION

Objective 1 does not introduce consequential UCII execution.
