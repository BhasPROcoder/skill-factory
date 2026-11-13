---
id: IXA-002
name: voice-turn-repair-confirmation-design
domain: Interaction Adaptation
subdomain: Conversational repair
version: 1.0
description: Design bounded voice-dialogue repair and confirmation turns when recognition uncertainty or corrections could change a user's intended action.
triggers: ["design voice error recovery", "confirm a spoken request", "handle misheard commands", "repair voice assistant turns", "preserve details during spoken correction", "handle silence in a voice flow"]
not_for: ["general workplace message drafting [GCO-001]", "general empty-state copy [MPU-002]", "speech recognition model implementation", "executing external actions or authenticating identity"]
requires: []
risk_level: medium
---

# Voice Turn Repair and Confirmation Design

## Purpose
Produce a dialogue contract that repairs ambiguous or corrected speech without discarding established details or treating silence as consent. It distinguishes what the recognizer suggested, what the user confirmed, and what an external system actually completed.

## Inputs to collect
1. **User task:** Identify the intended action, required fields, and material consequences. This defines what must be understood before proceeding. Default: none; no concrete action flow without a task.
2. **Recognized evidence:** Obtain the transcript, alternatives if supplied, and which parts are uncertain. This identifies the repair target. Default: uncertainty is unknown; do not invent recognition scores or alternative names.
3. **Dialogue context:** Collect previously accepted fields, explicit corrections, and the latest unanswered prompt. This prevents a local repair from erasing unrelated choices. Default: no established fields beyond the supplied conversation.
4. **Action contract:** Obtain prerequisites, confirmation requirements, cancellation behavior, and result evidence. This distinguishes a draft from an executable request. Default: propose only; no external authority is inferred from this design exercise.
5. **Channel constraints:** Identify speech-only or multimodal interaction, available controls, and privacy constraints. These shape repair options. Default: short spoken turns with no assumed screen or private listening environment.
6. **Recovery policy:** Obtain retry limits, timeout handling, and fallback routes. This bounds repeated failures. Default: propose a bounded policy for owner review rather than claiming a universal retry count.

If a required input is missing and has no safe default, ask in one message with at most 3 questions.

## Procedure
1. Extract the intended action and its required fields into a dialogue record, keeping recognized candidates separate from confirmed values.
2. Identify the smallest uncertain portion of the request. Ask about that portion instead of making the user repeat every already established detail.
3. ⚠️ Preserve ambiguity rather than choosing the most familiar entity. A supplied recognition score or repeated spelling does not establish that the user's intended recipient or object was correctly understood.
4. Write a repair prompt that exposes meaningful supplied alternatives or requests the missing field. Avoid suggesting unsupported options that may bias the user into accepting an invented interpretation.
5. Apply a correction only to the field the user changed, while checking whether that correction invalidates any dependent field. Retain unrelated accepted values and disclose any dependent information that must be collected again.
6. Choose confirmation depth from the supplied consequence and action contract. For a consequential action, read back the material fields and consequence before commitment; do not substitute a vague “Is that okay?” for an identifiable request.
7. Bind a positive response to the latest clear confirmation turn. If the user corrects a field, changes topic, or interrupts the readback, update the draft and issue a new relevant confirmation instead of reusing earlier consent.
8. ⚠️ Define silence, unrecognized speech, and explicit rejection as different events. None should silently commit the pending action; use the agreed retry or fallback policy and retain a recoverable draft where appropriate.
9. Separate request submission from completion feedback. Report “requested” or “pending” when the result is not known, and report success only from the action system's supplied result evidence.
10. Write ordinary, correction, rejection, timeout, and unavailable-result dialogues. Include cancellation or a supported alternative channel when repeated repair cannot establish intent.
11. Review prompts aloud or through an available speech interface when possible. Check whether the user can identify the disputed detail and consequence without relying on an unseen screen; otherwise label auditory testing pending.

Keep each turn focused on the immediate choice, with explicit names or values when they can be disclosed in the actual context. Do not read sensitive content aloud merely because it appears in the draft. Use the user's supplied privacy constraints; request clarification when spoken disclosure itself would be inappropriate. Verify any platform-specific recognition, interruption, or timeout behavior against current official documentation before implementation. The procedure defines dialogue behavior, not recognition accuracy or identity verification.

## Decision rules
- IF only one field is uncertain THEN repair that field while retaining accepted details BECAUSE full restarts increase the chance of losing correct context.
- IF the user corrects a material field after confirmation THEN require confirmation of the revised action BECAUSE earlier assent applied to a different request.
- IF silence follows a confirmation prompt THEN keep the action uncommitted BECAUSE absence of a response is not an affirmative instruction.
- IF recognition alternatives are absent THEN ask an open clarification BECAUSE fabricated choices can introduce an error rather than resolve it.
- IF the action result is unavailable THEN report the unresolved result BECAUSE recognizing or submitting a command does not prove completion.

## Output template
```text
Action boundary: <task, consequence, and authority; up to two lines>
Dialogue record: <field | candidate | confirmed status; up to eight rows>
Turn contract:
Event | Spoken response | Draft update | Commit permission
<four to eight rows>
Example exchange: <four to eight labeled turns>
Recovery limit: <supplied policy or proposal awaiting agreement>
Verification: <text review and performed or pending auditory/action checks>
Open dependencies: <up to three grouped questions>
```

## Quality checklist
- [ ] Recognized candidates and confirmed values remain separate.
- [ ] Repair prompts target the uncertain field rather than restarting unnecessarily.
- [ ] Corrections preserve unrelated values and revisit dependent fields.
- [ ] Confirmation names the material action and consequence.
- [ ] New material corrections invalidate earlier confirmation.
- [ ] Silence and recognition failure cannot commit an action.
- [ ] Pending submission and completed result have different messages.
- [ ] Privacy and fallback assumptions are disclosed rather than invented.

## Anti-patterns
- **Familiar-name substitution:** Selecting a known contact when a name is ambiguous. Fix: request a distinguishing identifier supported by available context.
- **Global reset:** Restarting the whole request after a single correction. Fix: retain accepted fields and repair only affected dependencies.
- **Floating yes:** Applying assent to an earlier draft after a correction. Fix: bind confirmation to the latest explicitly read-back action.
- **Silence means proceed:** Submitting on timeout. Fix: leave uncommitted and use the agreed recovery path.
- **Success by speech:** Saying an action completed immediately after recognizing it. Fix: wait for actual result evidence or state that it is pending.

## Worked example
**Input:**
Fictional room-booking prototype Cedar has a draft for Room Elm tomorrow afternoon. User Lea says, “Actually Room Ash.” The supplied action contract requires explicit confirmation of the room and time before a booking request. Both rooms are supported names; availability is not supplied. The prototype may retain a draft but cannot submit anything in this exercise. No retry policy or speech engine is supplied.

**Output:**
```text
Action boundary: Prepare a room-booking dialogue; no booking request may be submitted in this exercise.
Dialogue record: room | Ash after explicit correction | user-selected, action not confirmed
time | tomorrow afternoon | retained, exact booking interval unresolved
availability | unknown | not confirmed
Turn contract:
Room correction | Room Ash, keeping tomorrow afternoon. What exact time interval do you need? | update room; retain time context | none
Time supplied | Read back Room Ash and the supplied interval before requesting booking | update interval | none until required confirmation and prerequisites
Rejection | What would you like to change? | retain draft | none
Silence | No booking request has been sent | keep draft or end per agreed policy | none
Result unavailable | Booking result is not known | preserve pending status only if actually submitted | no success claim
Example exchange: Lea: Actually Room Ash.
Assistant: Room Ash, keeping tomorrow afternoon. What exact time interval do you need?
Lea: I need to check my schedule first.
Assistant: The draft remains unsubmitted. Tell me the interval when you are ready.
Recovery limit: Retry and timeout policy not supplied; agree a bounded recovery and cancellation path before implementation.
Verification: Text design only; no speech engine, availability lookup, or booking action tested.
Open dependencies: What exact interval and date context apply? How is room availability checked? What retry, cancellation, and privacy rules govern this channel?
```

**Bad output:**
“Room Ash is booked; I kept the old confirmation and assumed the usual afternoon slot.”
This invents a time, reuses assent for a changed action, and claims external completion without evidence.

## Edge cases
- The user interrupts readback: stop treating the readback as complete, identify the correction, and confirm the revised material fields.
- Two people speak: keep speaker intent unresolved rather than combining their statements into one authorized request.
- An alternative channel is unavailable: state that limitation and preserve or cancel the draft according to the agreed policy instead of promising a transfer.
- A response arrives after the dialogue expired: establish the current draft and prompt context before applying it to any pending action.

## Test case
**Input:**
> Fictional kiosk Oak asks whether to request Room Pine for a supplied interval. The user says “No, Room Birch,” then remains silent. The room update is recognized, but availability and submission result are absent. Design the next turns.

**Assertions:**
1. Updates the room while retaining the supplied interval.
2. Does not treat the earlier confirmation prompt or later silence as assent to Birch.
3. Keeps availability and action completion unresolved.
4. Provides a bounded recovery or requests the missing policy without inventing a successful booking.
