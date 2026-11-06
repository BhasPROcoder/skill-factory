---
id: EVT-002
name: alternate-playback-recovery-rehearsal
domain: Event Show Operations
subdomain: Playback recovery
version: 1.0
description: Build a rehearsal script for a failed presentation cue that identifies an approved alternate, the switch decision, and a verified rejoin point.
triggers: ["rehearse a failed presentation clip","plan fallback playback","test alternate show media","recover a missed projection cue","prevent duplicate playback after recovery"]
not_for: ["normal show calling sheet [EVT-001]","presentation visual quality review [CBG-006]","general system disaster recovery"]
requires: []
risk_level: low
---

# Alternate playback recovery rehearsal

## Purpose
Prepare a rehearsal that tests what the audience will see or hear when a specific presentation cue fails. The deliverable traces detection, an authorized alternate branch, and rejoining the program without replaying completed content or assuming a backup works.

## Inputs to collect
1. Intended cue and essential message: identify its asset revision, destination, starting marker, ending marker, and what must reach the audience. This establishes what a fallback has to preserve. Default to unresolved if the program owner has not identified essential content.
2. Failure symptom: obtain an observable audience-side symptom and the evidence available at the operator position. This determines how the team knows a failure occurred. Default to a proposed simulation, not a claim of actual failure.
3. Alternate paths: collect approved replacement media, spoken alternatives, or permission to omit content, with their dependencies and limitations. Default to no approved alternate.
4. Switch authority and roles: identify who may stop the original, run the alternate, speak to the audience, and release the next cue. Default to role placeholders and a blocked switch until authority is confirmed.
5. Test conditions: identify an isolated rehearsal setting, representative output monitor, time constraints, and who records observations. Default to a desk exercise; do not interrupt live program output.
6. Rejoin evidence: request the next approved program marker, including whether a partially delivered message must resume, restart, or be omitted. Default to holding the next release for the caller's decision.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Write the intended cue and define a success witness at the audience destination. Distinguish the operator's local preview from what the room or remote audience actually receives.
2. List the primary and alternate paths by their relevant dependencies. Two copies of the same file on the same failed playback device do not establish an independent route for a device outage.
3. Select a failure condition for the rehearsal and state how it will be simulated in the authorized test environment. A tabletop statement such as “the room display stays blank” is enough for a dialogue test; label it accordingly.
4. Define the decision point in terms of observable facts. Avoid arbitrary retry counts and timeout values unless the show owner supplied them. Distinguish no-start, mid-cue interruption, and unavailable confirmation.
5. ⚠️ Identify who prevents the primary from reappearing unexpectedly during the alternate. If stopping or isolating it cannot be confirmed, design a hold branch rather than layering new audio or visuals over an uncertain original.
6. Specify the caller's switch instruction and the operator's acknowledgment. Describe precisely which replacement material is permitted and which parts of the intended message it omits.
7. Record how the rehearsal observer distinguishes successful alternate delivery from a merely loaded backup. Verify the relevant destinations separately if venue and stream receive different feeds.
8. Choose an unambiguous rejoin marker after the affected segment. Establish whether the audience has already received the essential content. Decide what happens to any delayed automatic cue or operator waiting on the original end signal.
9. Exercise the branch on an authorized rehearsal setup if available, or execute a tabletop walkthrough. Record the method, actual observations, untested assumptions, and deviations from the plan.
10. Return the program to its agreed starting condition only when authority and actual restoration evidence exist. Preserve unresolved failures and assign a proposed retest; do not turn a paper exercise into permission for a live switch.

## Decision rules
- IF both options depend on the failed component THEN mark the alternate unavailable for that failure BECAUSE another filename alone does not remove a shared dependency.
- IF the original may still emit sound or video THEN hold overlapping replacement playback until the operator confirms isolation BECAUSE an apparent frozen picture does not establish that every output stopped.
- IF the substitute omits required information THEN request an approved way to deliver that information BECAUSE finishing on time is not evidence that the audience received the intended message.
- IF the affected segment is already complete at one destination THEN specify a destination-specific recovery or an approved common rejoin BECAUSE restarting everywhere can duplicate content.
- IF rehearsal evidence comes only from a written scenario THEN label operational readiness untested BECAUSE a decision walkthrough does not exercise media routing or equipment.

## Output template
```text
Cue under test: <asset, essential audience outcome, destinations; two lines>
Dependency check: <primary and alternate requirements; shared failure points>
Recovery script: <one row per decision step>
Condition | Caller decision | Operator or presenter action | Evidence before proceeding
Rejoin: <exact next marker, stale trigger disposition, content still owed>
Test record: <method, observed outcome, untested paths>
Disposition: <ready within tested scope / revise / blocked / untested; next action>
```

## Quality checklist
- [ ] A failure symptom is distinguished from an assumed technical cause.
- [ ] The proposed alternate is checked against the specified failure.
- [ ] The release authority and operator roles are identified or unresolved.
- [ ] The primary cannot silently reappear during substitute playback.
- [ ] Essential omitted information is accounted for in the decision.
- [ ] A precise rejoin marker replaces the original end trigger.
- [ ] The status describes the actual rehearsal method and observation limits.

## Anti-patterns
- **Backup by filename:** A spare file shares the broken route. Fix: identify the failed dependency before choosing the alternate.
- **Optimistic switch:** The operator sees the backup in preview and declares success. Fix: obtain the appropriate audience-side witness.
- **Replay by habit:** The team restarts an entire clip after most of it played. Fix: decide which message remains owed and use an approved rejoin.
- **Ghost cue:** The original delayed completion triggers the next segment a second time. Fix: retire that trigger explicitly and designate one new release.
- **Unapproved improvisation:** An operator chooses substitute material with different meaning. Fix: obtain content approval or hold.

## Worked example
**Input:**
> Fictional team Rowan runs a tabletop exercise. Their presentation should play clip Seed-C from player Lane to a room screen. Its essential message is that field notes stay with each sample. The exercise says the screen remains blank when called; nobody knows why. Caller Eve may authorize presenter Jo to read the producer-approved card “Keep field notes with each sample.” Operator Fen must confirm Lane stopped before Jo speaks. Eve hears Jo in the room. The next marker is “Questions open,” called only by Eve. No technical rehearsal occurs.

**Output:**
```text
Cue under test: Seed-C to room screen; audience must receive the field-note instruction.
Dependency check: Original uses Lane and room screen. Approved spoken card does not require clip playback or screen; audience audibility is a separate check.
Recovery script:
Condition | Caller decision | Operator or presenter action | Evidence before proceeding
Room remains blank at release | Eve holds the next cue and requests primary stop | Fen stops Lane in the exercise | Fen must acknowledge stop; otherwise remain held
Primary confirmed stopped | Eve calls spoken card | Jo reads “Keep field notes with each sample.” | Eve listens for the complete line; uncertain delivery remains unresolved
Line heard complete | Eve retires original clip-end trigger | Fen does not replay a delayed clip | Only Eve may release Questions open
Rejoin: Eve calls Questions open after the spoken line is heard; no clip restart. Field-note message is covered if the line is delivered.
Test record: Tabletop decision path only. Blank screen is a stipulated symptom, not a diagnosed failure. No playback stop, audibility, or output switch was physically tested.
Disposition: Untested operationally. Rehearse the stop acknowledgment, spoken delivery, and single rejoin on an authorized setup before calling the branch technically ready.
```
**Bad output:**
“Restart the video immediately, read the card at the same time, then continue once the computer says finished.”
This risks overlapping messages and releases the next cue from an unverified original signal.

## Edge cases
- **No approved alternate:** Provide the hold-and-escalate script with the next decision-maker; do not select an asset solely because it is available.
- **Partial delivery unknown:** Record the last confirmed audience marker, then ask the authorized caller which bounded restart or omission is acceptable.
- **Alternate cannot be monitored:** Mark delivery unconfirmed and specify the missing observation; a completed operator action does not prove reception.
- **Late recovery after rejoin:** Suppress the retired original cue under the approved plan; do not reinsert completed content without a new decision.

## Test case
**Input:**
> Fictional team Echo has two copies of a clip on one player, whose output is unavailable. It has no approved spoken substitute. The caller asks whether to claim the spare copy proves readiness.

**Assertions:**
1. The alternate is identified as sharing the unavailable player output.
2. No cause beyond the observed output problem is asserted.
3. The script holds and requests an authorized alternative instead of inventing one.
4. Operational readiness remains untested or blocked.
