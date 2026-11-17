# Independent service appointment text tests

Reviewer: coordinator, separate from SVC author. Nine fresh fictional requests executed below. No calendar or communications used. Results do not establish live system or cross-model behavior.

## SVC-001 case 1

Request: Fictional salon A and B share room R and staff S on one date, end-exclusive intervals; A10:00–10:20 plus room reset through10:30; B10:25–10:45. No edits permitted.

```text
Scope: Supplied same-date roster, end-exclusive; freshness unknown.
Occupancy:
Booking | Resource | Occupied interval | Basis | State
A | R | 10:00–10:30 | service and reset | supplied
A | S | 10:00–10:20 | service | supplied
B | R and S | 10:25–10:45 | service | supplied
Conflict: R overlaps 10:25–10:30, five minutes; S does not.
Remedies: Later B or suitable alternate R only after all resource/consent checks.
Decision: Room conflict established.
Before change: Confirm roster, duration, resource availability and authority.
Execution status: Desk comparison only; no booking moved.
```

Review: Supplied states and authority limits preserved; unresolved evidence stays explicit. No blocking defect in this case.

## SVC-001 case 2

Request: Fictional bookings both say 9am with no date, timezone, resource or duration. Determine double booking.

```text
Scope: Unspecified comparison window and time convention.
Occupancy:
Booking | Resource | Occupied interval | Basis | State
two records | unknown | unknown | 9am labels only | unresolved
Conflict: Equal clock labels do not establish shared occupancy.
Remedies: Obtain dates/timezones/durations, resource assignments and authoritative booking identities.
Decision: Unresolved.
Before change: Establish actual roster and permitted remedies.
Execution status: No conflict certified or booking altered.
```

Review: Supplied states and authority limits preserved; unresolved evidence stays explicit. No blocking defect in this case.

## SVC-001 case 3

Request: Fictional two exports share booking ID Elm but disagree about room; a distinct booking Oak overlaps Elm's operator interval.

```text
Scope: Supplied identities; dates and detailed intervals require source records.
Occupancy:
Booking | Resource | Occupied interval | Basis | State
Elm | room disputed; operator shared | overlaps Oak by premise | duplicate exports | one identity, assignments unresolved
Oak | same operator | overlaps Elm by premise | distinct booking | supplied
Conflict: Operator overlap remains; duplicate Elm rows are not two established bookings.
Remedies: Reconcile Elm assignment and check operator remedy; room swap alone insufficient.
Decision: Shared-operator conflict by premise; room state unresolved.
Before change: Obtain current roster, times, permissions and customer agreement as required.
Execution status: Analysis only.
```

Review: Supplied states and authority limits preserved; unresolved evidence stays explicit. No blocking defect in this case.

## SVC-002 case 1

Request: Fictional offer F for slot L accepts server receipts strictly before12:00. Receipt11:59; slot still exclusively held for F. Confirmation requires coordinator action.

```text
Slot: L, exclusive F hold per supplied latest record.
Policy basis: Server receipt strictly before12:00; coordinator confirms.
Event ledger:
Event | Offer/slot identity | Relevant time | Evidence | Interpretation
acceptance | F/L | 11:59 receipt | supplied | timely
hold | F/L | latest snapshot | supplied | not a confirmed booking
Disposition: Timely acceptance, confirmation pending.
Next action: Coordinator rechecks hold and executes authorized confirmation if still valid.
Customer wording: Unsent: Your acceptance was received within the offer window; confirmation is pending.
Open evidence: Current slot and confirmation outcome.
Execution status: No confirmation or message performed.
```

Review: Supplied states and authority limits preserved; unresolved evidence stays explicit. No blocking defect in this case.

## SVC-002 case 2

Request: Fictional customer replies exactly at offer expiry; terms do not specify boundary or accepted timestamp.

```text
Slot: Identity and latest allocation unknown.
Policy basis: Expiry label supplied; endpoint rule and relevant event absent.
Event ledger:
Event | Offer/slot identity | Relevant time | Evidence | Interpretation
reply | unspecified | at labeled expiry | supplied | boundary ambiguous
Disposition: Acceptance classification and allocation unresolved.
Next action: Coordinator obtains offer terms, receipt semantics and current slot state.
Customer wording: Unsent: We are checking the offer terms and appointment status before confirming.
Open evidence: Which rule/time event applies? Which offer and slot? Current allocation?
Execution status: No allocation changed.
```

Review: Supplied states and authority limits preserved; unresolved evidence stays explicit. No blocking defect in this case.

## SVC-002 case 3

Request: Fictional expired offer M gets late acceptance after slot was confirmed to another customer; no override allowed.

```text
Slot: Supplied slot is confirmed to another customer.
Policy basis: M expired before acceptance by premise; no override authority.
Event ledger:
Event | Offer/slot identity | Relevant time | Evidence | Interpretation
expiry | M | before reply | supplied | closed offer
confirmation | same slot | before reply | supplied | new commitment
late reply | M | after both | supplied | cannot displace booking
Disposition: Late acceptance; other confirmation retained.
Next action: Authorized coordinator checks permitted alternatives.
Customer wording: Unsent: That offer expired and the slot has been allocated; we can check permitted alternatives.
Open evidence: Current alternative availability and queue policy.
Execution status: No cancellation, booking or message performed.
```

Review: Supplied states and authority limits preserved; unresolved evidence stays explicit. No blocking defect in this case.

## SVC-003 case 1

Request: Fictional repair booking P has paper arrival and technician start records; kiosk blank during outage; no completion.

```text
Appointment: P, supplied repair appointment.
Evidence chronology:
Event | Time meaning | Source | Supports | Does not establish
outage | relevant period | premise | electronic gap | absence
arrival | event time unspecified | paper linked to P | attendance | completion
start | event time unspecified | technician | service began | completion
Coverage gaps: Kiosk unreliable; completion absent.
Disposition: Attended and service started; completion unknown; cancellation not established.
Follow-up: Appointment owner reconciles manual evidence and checks completion.
Draft wording: Unsent: Please review the paper arrival and start notes before classifying P as missed.
Record handling: Preserve all records; no edits made.
```

Review: Supplied states and authority limits preserved; unresolved evidence stays explicit. No blocking defect in this case.

## SVC-003 case 2

Request: Fictional blank appointment row is the only evidence; user wants no-show fee.

```text
Appointment: Identity/version unspecified.
Evidence chronology:
Event | Time meaning | Source | Supports | Does not establish
blank row | unknown | supplied | no recorded check-in | absence or fee authority
Coverage gaps: Recording coverage, change history and policy missing.
Disposition: Attendance, cancellation and completion unresolved.
Follow-up: Owner obtains identity, recording coverage and event history; fee decision outside this evidence review.
Draft wording: Unsent: Can we confirm the appointment details and any arrival or cancellation record?
Record handling: Do not overwrite row or impose consequence; no action performed.
```

Review: Supplied states and authority limits preserved; unresolved evidence stays explicit. No blocking defect in this case.

## SVC-003 case 3

Request: Fictional later-entered note says customer canceled; arrival claim also exists, note lacks call time and booking ID.

```text
Appointment: Disputed case; booking association missing.
Evidence chronology:
Event | Time meaning | Source | Supports | Does not establish
arrival claim | event time unknown | customer | claimed presence | verified attendance
cancellation note | entry later; event time unknown | staff | reported call | accepted cancellation of this booking
Coverage gaps: Note identity, call time, acceptance and recording completeness absent.
Disposition: Attendance and cancellation unresolved; completion unknown.
Follow-up: Review owner establishes which booking/call and independent arrival evidence.
Draft wording: Unsent: Which appointment and call time does the note refer to?
Record handling: Retain competing sources; no correction or fee imposed.
```

Review: Supplied states and authority limits preserved; unresolved evidence stays explicit. No blocking defect in this case.
