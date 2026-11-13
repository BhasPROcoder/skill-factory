---
id: EVT-001
name: show-cue-and-standby-sheet
domain: Event Show Operations
subdomain: Cue calling
version: 1.0
description: Turn an event rundown into a callable sheet that separates standby, release, acknowledgment, and audience-visible completion.
triggers: ["turn this agenda into show cues","prepare a standby sheet","call the session transitions","coordinate presenter and playback handoffs","draft a show caller rundown"]
not_for: ["slide creation and visual review [CBG-006]","alternate playback rehearsal [EVT-002]","venue safety or technical installation"]
requires: []
risk_level: low
---

# Show cue and standby sheet

## Purpose
Turn a sequence of program segments into instructions that a caller and operators can use at the moment of transition. The result is a draft calling document: preparing a cue does not actually call it or establish that an operator can execute it.

## Inputs to collect
1. Program order and boundaries: collect segment names, intended starts, durations, and which end times are fixed. These determine timing exposure. Default to relative order without clock times if the producer has not assigned them.
2. Trigger evidence: obtain the exact line, gesture, observed display, or clock condition that releases each transition. Default to an unresolved release rather than inventing words a presenter has never agreed to say.
3. Roles and communication: identify who calls, who performs each action, how readiness is returned, and which channel the parties can actually use. Default to proposed roles, clearly unassigned.
4. Assets and destinations: record names and revisions for slides, media, or other program material, and where the audience should see or hear them. Default to a descriptive placeholder marked for confirmation.
5. Authority: ask who may hold, cut, reorder, or shorten the program. This determines which changes may be proposed versus executed. Default to maintaining the approved order and escalating timing conflicts.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Give the sheet a revision label and state which event session and time basis it covers. Keep the signed-off program order available for comparison.
2. Map each actual change the audience will experience to a cue identifier. A session called “Welcome” might need a title visible before doors open and a different cue when the host begins; the agenda item alone does not identify either action.
3. Identify the person or role that can observe each release trigger. If the caller cannot hear a presenter’s final line, specify an agreed relay or mark the cue blocked until one is arranged.
4. Write the standby instruction for each operator. State the target asset or action and the acknowledgment the caller needs. Use a warning tied to the previous reliable event when there is no dependable countdown.
5. ⚠️ Write the release instruction separately from standby. Acknowledging that a clip is loaded is not permission to play it. Do not release a dependent cue until its required evidence is available.
6. Choose one owner per action, including for cues that share a release. Record whether those actions must occur together or whether the second operator waits for the first observable result.
7. Give each cue an end witness that someone can observe. “Slide is visible on the audience screen” is a different witness from “operator pressed advance.” If no observer is assigned, mark the witness unconfirmed.
8. Check planned segment times against hard boundaries. Separate targets from elapsed times; do not turn a late start into permission to cut content. Include an exception branch for a missing acknowledgment or an expired slot.
9. Walk the caller through the rows in sequence with the supplied evidence. Flag ambiguous triggers, conflicting operator assignments, unavailable assets, and any change that still requires producer approval.
10. Issue a draft with its open checks and revision owner. If the program changes, replace affected dependencies as well as labels; an unchanged cue name can now point to a different presenter or asset.

## Decision rules
- IF a clock target arrives but its agreed verbal trigger has not occurred THEN hold the release and alert the caller BECAUSE scheduled time does not establish presenter readiness.
- IF an operator acknowledges standby but the audience result is not observed THEN retain separate ready and completion statuses BECAUSE loaded media may never reach the intended destination.
- IF several cues require the same operator at once THEN expose the conflict before publication BECAUSE simultaneous actions may exceed the operator’s confirmed capability.
- IF overrun threatens a fixed finish THEN show the timing conflict and ask the authorized producer for a disposition BECAUSE the caller cannot silently remove a segment.

## Output template
```text
Session: <revision, time basis, caller, status; two lines maximum>
Cue sheet: <one row per transition>
ID | Target | Standby and acknowledgment | Release trigger and call | Action owner and action | Completion witness
Hold rules: <up to four specific exceptions and responsible roles>
Timing: <planned intervals, fixed boundaries and unresolved conflicts>
Verification: <walkthrough performed or proposed; actual evidence>
Open checks: <up to three questions>
```

## Quality checklist
- [ ] Every transition has an identifier and an observable release condition.
- [ ] A named role owns each call and each resulting action.
- [ ] Standby wording cannot reasonably be mistaken for release wording.
- [ ] Dependencies distinguish acknowledgment from audience-visible completion.
- [ ] Time targets are marked as targets or hard boundaries.
- [ ] Unconfirmed changes are routed to the correct authority.
- [ ] Open technical or communication assumptions remain visible.

## Anti-patterns
- **Agenda with timestamps:** Segment names give operators nothing to execute. Fix: name the release, action, owner, and result.
- **Assumed communications:** A caller relies on a gesture they cannot see. Fix: establish an observable trigger or relay.
- **Automatic catch-up:** A late segment silently deletes the next item. Fix: show the resulting conflict and seek a decision.
- **Ambiguous call:** “Ready video” might mean load or start. Fix: separate preparation and release with distinct language.

## Worked example
**Input:**
> Fictional studio Hazel schedules a welcome from 10:00 to 10:04 local and a two-minute clip before a fixed 10:06 panel start. Caller Ren and operator Sol share an agreed voice channel. Ren sees the audience screen and hears host Ada. Ada opens on Ren’s call and ends with “Here is the field visit.” Sol has the approved clip Visit-B. Producer Kim alone can change the program. Panelist Bo enters on Ren’s call after the clip ends. No show or rehearsal has run.

**Output:**
```text
Session: Hazel panel opening, draft A, local program time. Caller Ren.
Cue sheet:
ID | Target | Standby and acknowledgment | Release trigger and call | Action owner and action | Completion witness
W | 10:00 | Ren asks Ada to confirm readiness before opening | At opening target with Ada ready, Ren: Welcome go | Ada begins welcome | Ren hears opening words
V | 10:04 target | During welcome, Ren: Standby Visit-B; Sol confirms loaded | On Ada's agreed final line and Sol ready, Ren: Visit-B go | Sol plays Visit-B | Ren sees clip on audience screen
P | 10:06 fixed | During clip, Ren requests Bo's ready acknowledgment | When clip ends and Bo ready, Ren: Panel go | Bo enters | Ren observes entrance
Hold rules: No clip acknowledgment or final line: hold V. If panel deadline threatened, Ren alerts Kim; do not shorten the clip or release Bo early without direction.
Timing: Welcome 4 minutes plus clip 2 minutes fills the 6-minute opening exactly. No transition allowance is supplied.
Verification: Desk timing check only. Voice channel and observation arrangements supplied, not tested.
Open checks: Can the crew meet the fixed start with no transition allowance? What does Kim authorize if acknowledgment is missing?
```
**Bad output:**
“At 10:04 play the video regardless. At 10:06 cut it and send Bo on.”
This ignores the agreed line, clip readiness, actual end, and producer authority.

## Edge cases
- **Unscripted finish:** Agree an observable handoff with the presenter; leave the release pending until the handoff is confirmed.
- **Repeated asset name:** Add revision and destination identifiers to distinguish the intended item before standby.
- **Reordered speaker:** Check the preceding standby opportunity and following release trigger as well as the changed row.
- **Two audiences:** Record a separate completion witness for each destination if their feeds differ; one visible screen does not prove both changed.

## Test case
**Input:**
> A fictional panel host improvises past the planned clip start. The operator reports loaded, but the host has not given the agreed signal. Only the producer may shorten the session. Write the relevant cue row and exception branch.

**Assertions:**
1. The row separates loaded acknowledgment from release.
2. The release remains on hold while the signal is missing.
3. The timing conflict goes to the producer without inventing an approved cut.
4. The output identifies the needed audience-side witness.
