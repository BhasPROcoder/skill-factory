---
id: EXP-005
name: exhibit-alternate-route-interpretation-parity
domain: Exhibition Interpretation Operations
subdomain: Route interpretation
version: 1.0
description: Compare the interpretive sequence available on different exhibit routes when visitors bypass a room, medium or physical feature.
triggers: ["compare alternate exhibition routes", "preserve the story on a bypass route", "check interpretation after a gallery closure", "review a non-audio exhibit path", "map essential content across visitor paths"]
not_for: ["certifying building access or evacuation safety", "translating individual panels [EXP-002]", "general customer arrival directions [MSL-010]"]
requires: []
risk_level: medium
---

# Exhibit alternate route interpretation parity

## Purpose
Map what a visitor can understand on each supplied exhibition route, including the context needed to interpret later objects. Propose equivalent access to essential interpretation when a route bypasses a space or medium, while leaving physical access certification and safety decisions to their appropriate processes.

## Inputs to collect
1. **Interpretive goals:** Obtain the central propositions, necessary qualifications and intended connections between objects. Required; distinguish essential meaning from optional examples with the interpretation owner.
2. **Route records:** Obtain the actual or proposed paths, entry points, bypasses and rejoining points. Required; do not assume that a drawn connection is physically available to visitors.
3. **Content inventory:** List panels, objects, audio, interactive stations and their relevant content. Default: supplied inventory only, with uninspected content marked unknown.
4. **Route constraints:** Identify the stated reason for each alternative, such as a closed room or unavailable audio. Default: evaluate only the stated constraints rather than inventing a visitor's abilities or preferences.
5. **Delivery capabilities:** Obtain confirmed places and media where replacement interpretation could be offered. Default: proposals only; do not assume devices, staff assistance or network access are available.
6. **Review evidence:** Collect a walkthrough record or route-specific prototype when available. Default: desk comparison, with actual navigation and delivery untested.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Name each route and its boundary from arrival at the exhibition to departure or a stated rejoining point. Keep route choices separate from visitors' inferred identities; the same person may choose different paths at different times.
2. Break the interpretive goals into essential propositions and dependencies. For example, a later comparison may require an earlier explanation of what is being compared, while another object can be understood independently.
3. Map each proposition to the places or media that communicate it. Include caveats and source distinctions, not merely subject headings or the number of objects encountered.
4. Trace each route in order, noting which information is available before it is needed. A caveat encountered only after the relevant claim does not necessarily serve the same interpretive function.
5. ⚠️ Identify gaps as missing meaning, missing prerequisite, unavailable medium or ambiguous navigation. Do not label a route inferior just because it contains fewer objects or takes less time.
6. Propose the smallest content or sequence change that preserves the essential understanding. A concise contextual panel at a rejoining point may suffice; an unrelated extra object does not replace a missing explanation.
7. Check that the proposed alternate is usable under the route's stated constraint. Replacing unavailable audio with another audio station does not resolve a non-audio path, and a link is not a confirmed delivery method without the required access.
8. Preserve the distinction between original experience and alternate interpretation. A description can communicate a work's premise without being represented as the same sensory experience or a complete substitute for every feature.
9. Define a route-specific comprehension check using the supplied interpretive goals. Ask whether the visitor can identify the central relationship and its uncertainty from that route alone; do not invent a universal score or claim actual visitor testing occurred.
10. Deliver the parity map, prioritized changes and evidence boundary. Identify which content decisions need editorial approval and which route-availability questions require the venue's responsible staff.

For current physical access criteria, refer to [VERIFY: the venue's approved access plan and applicable local requirements with its responsible access professional]. This skill does not provide dimensions, compliance thresholds or emergency routes.

## Decision rules
- IF a later claim depends on skipped context THEN place the necessary context before that claim on the alternate route BECAUSE sequence affects interpretation.
- IF a route omits only an optional example THEN record the difference without inventing an essential gap BECAUSE parity concerns the agreed learning goals rather than identical object counts.
- IF a proposed substitute relies on the unavailable medium THEN reject it as a solution to that constraint BECAUSE it reproduces the original barrier.
- IF physical availability is unverified THEN label the route proposed BECAUSE a narrative map does not establish that visitors can traverse it.
- IF an alternate communicates meaning but changes the sensory experience THEN describe that limitation BECAUSE equivalence of one interpretive goal is not identity of experience.

## Output template
```text
Boundary: <routes, constraints and evidence reviewed; up to four lines>
Essential interpretation: <up to six propositions and their prerequisites>
Route matrix: <one row per essential proposition; attach larger matrices>
Proposition | Main-route encounter | Alternate-route encounter | Gap type | Proposed remedy
Rejoining context: <what must be understood before each shared segment; up to four lines>
Delivery checks: <confirmed capabilities and unresolved dependencies; up to five lines>
Validation plan: <up to four route-specific comprehension or walkthrough checks>
Limit: <editorial, physical and experience claims still unverified; up to three lines>
```

## Quality checklist
- [ ] Essential interpretation is agreed or visibly provisional.
- [ ] Each route has a stated entry, order and boundary.
- [ ] Necessary context appears before dependent interpretation.
- [ ] Missing meaning is distinguished from omitted optional examples.
- [ ] Proposed remedies work under the route's stated constraint.
- [ ] Digital or staff-mediated alternatives have confirmed dependencies or remain proposed.
- [ ] Different sensory experiences are not declared identical.
- [ ] Physical access and actual visitor testing are not inferred from desk review.

## Anti-patterns
- **Equal-object counting:** parity is judged by the number of exhibits seen. Fix: compare essential propositions and prerequisites.
- **Late caveat:** uncertainty appears only after a confident downstream conclusion. Fix: move the qualification to the relevant reading point.
- **Barrier repetition:** unavailable audio is replaced with an audio link. Fix: choose a medium compatible with the stated constraint.
- **Invented route:** a line on a diagram is declared an available passage. Fix: obtain venue confirmation of the actual path.
- **Experience equivalence:** a textual description is called identical to a sensory work. Fix: specify which interpretation it conveys and what differs.

## Worked example
**Input:** Fictional exhibition Alder has a main route through Rooms Origin and Comparison. A closure bypass goes directly to Comparison. Origin explains that the displayed patterns are reconstructed hypotheses; Comparison asks visitors to compare those patterns. The interpretation owner calls that qualification essential. A blank text panel at the bypass rejoining point is available. No walkthrough has occurred.

**Output:**
```text
Boundary: Alder main route and proposed closure bypass; supplied content and route descriptions only.
Essential interpretation: Patterns are reconstructed hypotheses; this qualification is needed before comparing the patterns.
Route matrix:
Proposition | Main-route encounter | Alternate-route encounter | Gap type | Proposed remedy
Reconstruction is hypothetical | Origin before Comparison | absent before Comparison | missing prerequisite | approved contextual text on available rejoining panel
Compare the displayed patterns | Comparison after qualification | Comparison without qualification | dependent meaning distorted | retain comparison after adding prerequisite
Rejoining context: Before the shared Comparison segment, explain that the patterns are reconstructed hypotheses.
Delivery checks: Text panel availability supplied; exact copy and installation approval pending. Actual bypass availability requires venue confirmation.
Validation plan: Trace bypass entry to panel to comparison; check that a reader can state the hypothesis qualification before making the comparison.
Limit: Desk proposal only; no physical walkthrough, visitor comprehension test or access certification performed.
```

**Bad output:** “Add another object to the bypass so both routes are equivalent.”
Equalizing object counts leaves the missing qualification unresolved.

## Edge cases
- Visitors enter midway: evaluate that entry as a separate route boundary and identify the minimum orientation needed there.
- A route intentionally supports a different theme: assess it against its approved goals and disclose the difference instead of forcing identical interpretation.
- A temporary closure changes repeatedly: version the route map and retire outdated navigation with the venue owner rather than treating one review as permanent.
- Essential meaning depends on a tactile or auditory experience: involve the interpretation and access specialists in the alternate design and avoid claiming full equivalence from a summary alone.

## Test case
**Input:**
> Fictional exhibit Larch offers a non-audio path. The only explanation of whether a displayed scene is factual or imagined is an audio introduction. A proposed remedy links to that same audio.

**Assertions:**
1. Identifies the factual-versus-imagined distinction as a potential essential gap requiring the interpretation owner's decision.
2. Explains why the audio link does not resolve the stated non-audio constraint.
3. Proposes a compatible content route subject to actual delivery capabilities.
4. Does not certify physical access or identical sensory experience.
