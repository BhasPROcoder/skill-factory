---
id: SVC-003
name: appointment-attendance-evidence-disposition
domain: Service Appointment Operations
subdomain: Attendance disposition
version: 1.0
description: Reconcile attendance and cancellation evidence before labeling a service appointment a no-show or preparing follow-up.
triggers: ["check whether this appointment was a no-show", "reconcile check-in and cancellation records", "prepare an attendance follow-up", "review disputed missed appointments", "separate late arrival from absence"]
not_for: ["resource scheduling [SVC-001]", "exclusive waitlist reallocation [SVC-002]", "determining penalties or legal liability", "clinical follow-up"]
requires: []
risk_level: medium
---

# Appointment attendance evidence disposition

## Purpose
Produce an evidence-based attendance classification for a nonclinical service appointment and a bounded follow-up proposal. Avoid treating a missing check-in record as proof of customer absence or treating attendance as proof that the service was completed.

## Inputs to collect
1. **Appointment identity:** Obtain booking identifier, date, location, service and customer reference. This anchors records that may share a name. Default: do not merge uncertain identities.
2. **Expected attendance process:** Obtain check-in channels, staff recording responsibilities and the supplied lateness or attendance policy. Default: no invented grace period or automatic no-show rule.
3. **Observed records:** Collect check-in, arrival, contact, service-start, completion and staff notes with timestamps and authors where supplied. Default: missing records stay missing rather than negative evidence.
4. **Change history:** Obtain cancellations, reschedules, location changes and notifications. This may change what attendance was expected. Default: unresolved changes prevent a definite disposition.
5. **System coverage:** Identify outages, delayed synchronization, manual registers and duplicate bookings. This distinguishes an absent event from an event the system failed to capture. Default: record reliability unconfirmed.
6. **Follow-up authority:** Ask what contact or correction is permitted and who owns disputed records. Default: a draft question or review handoff only, with no fee or adverse action.

If a required input has no safe default, ask in one message with at most three questions.

## Procedure
1. Establish the appointment version the customer was expected to attend. Preserve prior versions when a reschedule or location change could explain apparently conflicting records.
2. Associate each event with the actual booking identity. Shared customer names or adjacent appointments are not sufficient evidence of a match.
3. Build a chronology separating observation time, entry time and reported event time when they differ. A late-entered note may describe an earlier arrival.
4. Identify what each source supports: arrival, check-in, cancellation request, accepted cancellation, service start or completion. Do not expand a source beyond its meaning.
5. ⚠️ Test negative evidence against recording coverage. A blank register may support no recorded check-in, but does not establish nonattendance if a kiosk failed or staff used an uncollected paper list.
6. Apply the supplied attendance policy only after resolving the relevant time and version questions. Keep late arrival, cancellation pending, service interrupted, absence established and unresolved evidence distinct.
7. Compare conflicting sources without silently ranking them by convenience. State the narrow question that would resolve the conflict, such as which booking a manual check-in references.
8. Prepare a correction or follow-up proposal based on the classification. Use neutral wording that asks about facts before accusing the customer of failing to attend.
9. ⚠️ Keep any financial, contractual or clinical consequence outside this evidence review unless separately requested with appropriate context and authority. A no-show label does not itself establish a fee or obligation.
10. Produce a case note that preserves original observations, identifies the proposed classification and names the next evidence or decision needed. Do not overwrite history while the matter is disputed.

## Decision rules
- IF check-in records are incomplete THEN use no recorded check-in rather than absent BECAUSE recording failure and customer absence are different explanations.
- IF a cancellation request exists without acceptance evidence THEN preserve cancellation pending BECAUSE the request alone may not change the appointment's agreed state.
- IF attendance is established but completion is missing THEN separate attended from completed BECAUSE presence does not prove delivery of the service.
- IF a reschedule changed the appointment identity THEN reconcile the new booking before classifying the old one BECAUSE an obsolete booking may not represent a missed commitment.
- IF sources conflict about arrival time THEN retain the conflict and request targeted evidence BECAUSE a convenient timestamp cannot justify an unsupported adverse label.

## Output template
```text
Appointment: <identity, version and expected attendance context; up to three lines>
Evidence chronology:
Event | Time meaning | Source | Supports | Does not establish
<up to eight rows; attach additional history if necessary>
Coverage gaps: <up to four recording or identity limitations>
Disposition: <attendance, cancellation and service-completion states separately>
Follow-up: <one proposed action and authorized role>
Draft wording: <optional unsent neutral message, up to four sentences>
Record handling: <preserve/correct/review proposal and actual execution state>
```

## Quality checklist
- [ ] The relevant booking version is identified.
- [ ] Event time is not silently replaced by record-entry time.
- [ ] Attendance and service completion are separate conclusions.
- [ ] Missing check-in is interpreted against recording coverage.
- [ ] Cancellation request and accepted cancellation are distinguished.
- [ ] Conflicting evidence is retained with a focused next question.
- [ ] Follow-up wording does not invent blame, fees or policy.
- [ ] Proposed record changes are distinguished from executed corrections.

## Anti-patterns
- **Blank equals absent:** an empty field proves a no-show. Fix: establish recording coverage and inspect alternative channels.
- **Attendance equals delivery:** a customer at reception is marked service complete. Fix: require separate completion evidence.
- **Timestamp flattening:** entry time is treated as arrival time. Fix: retain the meaning of each timestamp.
- **Punishment first:** a fee is proposed before evidence is reconciled. Fix: resolve attendance and route consequences separately.
- **Erased dispute:** a staff note is replaced by the preferred account. Fix: preserve source history and add the review disposition.

## Worked example
**Input:** Fictional equipment-repair shop Hazel has appointment A at 09:00. Its kiosk was unavailable that morning. The electronic record has no check-in. A paper register explicitly identifies A and records arrival at 09:05, entered by receptionist Neri. A technician note says service began at 09:10. No completion record or lateness policy is supplied. A draft message currently says the customer did not attend.

**Output:**
```text
Appointment: Hazel A, scheduled 09:00; no reschedule evidence supplied.
Evidence chronology:
Event | Time meaning | Source | Supports | Does not establish
Kiosk unavailable | morning coverage | supplied outage fact | electronic check-in gap | customer absence
Arrival 09:05 | recorded arrival | Neri's paper register tied to A | attendance | completion or policy classification
Service start 09:10 | recorded start | technician note | service began | service completed
Coverage gaps: Electronic register cannot establish absence during outage. Completion and lateness policy are missing.
Disposition: Attended with recorded arrival five minutes after scheduled time; formal late classification unresolved; completion unknown.
Follow-up: Appointment owner reconciles paper attendance into the review record and checks completion evidence.
Draft wording: Unsent internal correction: Please hold the nonattendance message. Paper and technician records indicate attendance and service start; completion remains unverified.
Record handling: Preserve outage and original records. Correction proposed only; no record edited or message sent.
```

**Bad output:** “Charge a no-show fee because the electronic check-in is blank.”
This ignores direct attendance evidence and invents a consequence.

## Edge cases
- A companion checked in on behalf of a customer: establish who attended and what the service required before equating the companion's presence with customer attendance.
- Remote attendance shows connection but no participation: report connection evidence separately from the service's participation criterion.
- The customer arrived at a superseded location: inspect notification and rescheduling evidence without deciding fault from location alone.
- A disputed case must close administratively: record unresolved evidence and the authorized administrative decision separately from factual certainty.

## Test case
**Input:**
> Fictional studio Pine receives an arrival claim, a blank electronic record and a staff note entered later that says the customer called to cancel. Neither the call time nor booking identity in the note is clear.

**Assertions:**
1. Keeps attendance and cancellation unresolved.
2. Distinguishes note-entry time from event time.
3. Requests identity and recording-coverage evidence.
4. Avoids a fee, accusation or claimed correction.
