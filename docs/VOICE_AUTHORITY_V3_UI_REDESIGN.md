# Voice Authority Console — Post-Demo UI Redesign

Status: APPROVED CONCEPT / NOT IMPLEMENTED. Record and preserve the proven hackathon demo before changing the live console. Design reference: `src/voice_authority/assets/voice-authority-v3-concept.png` (asset to be added separately). Concept is visual direction, not a screenshot of working software.

## Non-negotiable requirements

- The UI must be **100% real and usable**: every displayed live identity, cryptographic-proof status, delegated-authority decision, timestamp, connection state, audio count, transcript, response and evidence item must be derived from actual application data. No fabricated metrics, identities, successful grants, transactions or sample logs in production UI.
- Keep real UCII authority checks independent from AssemblyAI interpretation. Voice is never authorization. Do not change backend trust boundaries or introduce new execution paths as part of a presentation redesign.
- DEMO GRANT / EXECUTE / REVOKE remain visibly and persistently marked **SIMULATION ONLY**; they must never imply a real UCII grant, authorization or execution. Real UCII DENIED must remain unmistakable.
- Do not replace `console-v2.html` or alter the verified live workflow until the minimum hackathon video is safely recorded. Build an isolated V3 candidate and retain an easy rollback to synchronized checkpoint `4e4e320`.
- The concept image contains illustrative identity labels, dates, event logs and a speculative price; **none are product specifications or approved factual claims**. Never hardcode them into the application.

## Visual direction

Use the approved dark mission-control aesthetic: navy/black surfaces, crisp cyan live-system accents, green cryptographic verification, red denial, gold **demo-only** accents. Preserve the UCII/AssemblyAI branding, glowing globe and large central microphone. Reduce visual crowding, maintain clear status hierarchy and make live-versus-demo boundaries impossible to confuse. The central voice interaction is the visual hero; the globe must never obscure transcription or response.

## Implementation backlog (after first video is secured)

1. **Information hierarchy:** Keep agent identity, proof status and latest real UCII decision always visible. Collapse secondary Identity & Access details and explanatory copy. Consolidate connection metadata. Consider tabs for Interpreted Request / Agent Response / Evidence, but ensure evidence and decision remain accessible during recording.
2. **Voice UX:** Make connection prerequisites obvious; show distinct MIC OFF, LISTENING, PROCESSING and RESPONSE states with accessible text and optional waveform. Connect action explicitly indicates a paid session; confirm before starting, display session timer and an accurate cost only if fetched from a verified rate source. Disconnect must be prominent. No automatic paid connections.
3. **Trust-state clarity:** Use labeled badges and icons, not color alone. Distinguish verified identity, authenticated session, authorized/denied operation and demo simulation. Never translate credential verification into an authorization claim.
4. **Evidence and console:** Auto-scroll, optional All / Error / Warning / Info filters, clear timestamps and export. Log actual events only; never use illustrative console rows. Retain provenance and no-execution evidence for denied requests.
5. **Responsive and accessible:** Desktop recording layout first, then Android/tablet single-column reflow and sticky critical status. Test real mobile microphone audio separately; frame counts alone do not prove usable audio. Keyboard focus, accessible labels, contrast and reduced-motion behavior.
6. **Polish:** Consistent cards, padding, radius and border weights; shorter microcopy; progressive-disclosure tooltips. Animate globe/rings subtly only when relevant and disable animation when reduced motion is requested.

## Functional acceptance gates

- Desktop and Android UI render without overflow; no controls are hidden or unusable.
- Every interactive button/tab/filter/toggle has real behavior and tested disabled states; no decorative fake controls.
- The existing live desktop flow remains intact: spoken inspection → real AssemblyAI transcription → validated `compute.inspect` proposal → signer-backed UCII delegated check → true DENIED or AUTHORIZED result → on-screen response and provenance. Browser spoken response must be audibly tested; until then it is implemented but unverified.
- A verified identity with DENIED authority must show both facts simultaneously. No real execution or authority grant is implied by simulated controls.
- Session costs, timers and speech indicators are driven by real measured data or explicitly labeled estimates; do not copy illustrative values from the concept.
- Tests cover DOM IDs/JS contracts, backend requests, no-authorization failure cases, reconnect/disconnect, accessibility, mobile responsiveness and a real browser rehearsal.
- Compare V3 against V2, verify diff and rollback, then switch only after the preserved demo is secure and V3 has passed end-to-end tests.

## Scope and scheduling

Current demo checkpoint: `4e4e320`, prior to documentation-only changes. First: test browser speech, rehearse, record live voice commands and preserve a complete minimum submission. Afterward, build V3 in isolation. Only replace the recorded version if V3 is demonstrably better and fully verified before the September 30, 2026 deadline. First-human bootstrap and new security operations remain separate projects; this document authorizes no production governance or execution changes.

## Reference asset

User-selected exact V3 image (1536 × 1024 PNG; no substitutes or regenerated variants). Filename: `src/voice_authority/assets/voice-authority-v3-concept.png`.
SHA-256: `9b3817f695631daa3d0d03013e6a05679c1ea618dbc6ac7468a4f368a95a0a4c`.
The image must be committed as a **design reference only**, never served as a substitute for the functional UI.
