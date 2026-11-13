---
id: SVC-001
name: appointment-resource-conflict-reconciliation
domain: Service Appointment Operations
subdomain: Resource occupancy
version: 1.0
description: Reconcile overlapping service bookings against shared resource occupancy when appointment times alone do not establish feasibility.
triggers: ["resolve overlapping appointments", "check room and staff double booking", "reconcile a booking conflict", "include setup in appointment occupancy", "find a feasible service slot"]
not_for: ["aggregate service capacity planning [MOP-008]", "personal weekly planning [GPR-002]", "clinical triage or emergency scheduling"]
requires: []
risk_level: medium
---

# Appointment resource conflict reconciliation

## Purpose
Build an occupancy comparison that explains whether specific bookings can coexist on the supplied resource roster. Separate appointment promises from setup, reset and resource constraints before proposing a change to anyone's booking.

## Inputs to collect
1. **Booking identities and states:** Obtain identifiers, service types, confirmed or tentative status and current owner. These prevent duplicate records becoming two commitments. Default: unidentified records remain unresolved.
2. **Time semantics:** Obtain dates, timezone, start and end meaning, and the supplied boundary convention. These make comparisons meaningful. Default: no assumption that matching clock labels denote the same instant.
3. **Resource assignments:** Obtain staff, rooms, equipment and any sharing limits. A free room does not establish that its operator is free. Default: only supplied resources are checked.
4. **Occupancy requirements:** Request preparation, travel, reset and protected break rules. These may extend resource use beyond the customer-facing appointment. Default: mark missing buffers unknown rather than inventing customary values.
5. **Permitted remedies:** Identify which resources are interchangeable and who may move, cancel or reassign bookings. Default: suggestions only; preserve existing commitments.
6. **Freshness of records:** Obtain the roster snapshot and any pending holds or edits. Default: stale or incomplete records cannot support a current availability promise.

If a required input has no safe default, ask in one message with at most three questions.

## Procedure
1. Define the exact comparison window and list the bookings being reconciled. Keep canceled, tentative, confirmed and uncertain entries distinguishable.
2. Resolve duplicate identities against authoritative booking records. Two exports of one booking are not necessarily two resource claims.
3. Normalize time labels into a common comparison context using supplied timezone and date evidence. Keep ambiguous local times unresolved.
4. Expand each booking into one occupancy interval per resource, retaining the source of every extension. A room reset and a staff break may have different boundaries.
5. ⚠️ Compare intervals on the same resource using the supplied endpoint rule. Under a proposed end-exclusive convention, one interval ending when another starts does not overlap; disclose that convention rather than silently applying it to an unknown system.
6. Identify the shared portion of each conflict and distinguish definite overlap from uncertain feasibility caused by missing buffers or assignments.
7. Test a proposed remedy against every affected resource, not just the resource that first revealed the conflict. Reassigning a room does not solve a shared operator collision.
8. Preserve the original booking promises in a before-and-after record. Show who would be affected, which approvals are missing, and what evidence makes an alternative feasible.
9. ⚠️ Recheck live availability immediately before an authorized change. A proposal based on a snapshot is not a reserved slot and must not be announced as confirmed.
10. Deliver the occupancy ledger and a bounded disposition: feasible under supplied rules, conflict established, or unresolved. State explicitly whether anything was changed.

## Decision rules
- IF customer appointment times do not overlap but resource reset intervals do THEN report a resource conflict BECAUSE the resource remains occupied after the customer leaves.
- IF an alternate room exists but the same required operator overlaps THEN retain the conflict BECAUSE resources must be jointly feasible.
- IF resource sharing is unspecified THEN request the actual sharing rule BECAUSE a quantity of bookings is not proof of capacity.
- IF records are stale or a hold is unresolved THEN label availability conditional BECAUSE another commitment may already occupy the candidate interval.
- IF moving an appointment requires agreement THEN produce a proposal and affected-party list BECAUSE diagnosis does not supply permission to change a commitment.

## Output template
```text
Scope: <window, comparison convention and snapshot; up to three lines>
Occupancy:
Booking | Resource | Occupied interval | Basis | State
<up to ten rows; attach continuation for additional resources>
Conflict: <shared resource, overlapping portion or unresolved condition>
Remedies: <up to three options with dependencies and affected bookings>
Decision: <feasible / conflict / unresolved, with bounded reason>
Before change: <freshness, authority and confirmation checks; up to four lines>
Execution status: <what was actually inspected or changed>
```

## Quality checklist
- [ ] Booking identity is separate from exported record identity.
- [ ] Dates and timezone meanings are comparable or explicitly unresolved.
- [ ] Each required resource has its own occupancy interval.
- [ ] Setup and reset durations are supplied rather than assumed.
- [ ] Endpoint treatment is explicit.
- [ ] Every remedy checks all relevant resources.
- [ ] Proposed availability is not described as a reservation.
- [ ] No booking alteration or notification is implied without evidence.

## Anti-patterns
- **Calendar-only proof:** nonoverlapping customer blocks are called feasible. Fix: compare resource occupancy including supplied preparation and reset.
- **One-resource repair:** a room changes while staff remain double-booked. Fix: repeat the comparison for every required resource.
- **Snapshot promise:** yesterday's empty slot is offered as confirmed. Fix: recheck before any commitment.
- **Silent reschedule:** a solver chooses who should move without authority. Fix: identify impact and obtain the required decision.
- **Habitual buffer:** a familiar duration is inserted as policy. Fix: request the actual service rule and mark uncertainty.

## Worked example
**Input:** Fictional studio Larch supplies one room, one operator and two confirmed portrait sessions on the same local date. A occupies both from 10:00 to 10:30. Its supplied room-reset rule uses the room until 10:40; the operator is free at 10:30. B begins at 10:35 and ends at 11:00 using the same room and operator. The studio uses end-exclusive intervals. No alternate room or permission to move bookings is supplied.

**Output:**
```text
Scope: Larch's supplied local-date roster; end-exclusive intervals; currentness unverified.
Occupancy:
Booking | Resource | Occupied interval | Basis | State
A | room | 10:00–10:40 | session plus supplied reset | confirmed claim
A | operator | 10:00–10:30 | supplied operator release | confirmed claim
B | room | 10:35–11:00 | supplied session | confirmed claim
B | operator | 10:35–11:00 | supplied session | confirmed claim
Conflict: Room overlap is 10:35–10:40, five minutes. Operator intervals do not overlap.
Remedies: Propose B starting no earlier than 10:40 only if its duration, downstream resource availability and customer agreement are confirmed. An alternate room would require evidence of suitability and availability.
Decision: Conflict established for the room; no authorized remedy selected.
Before change: Recheck roster and all downstream occupancy. Obtain studio and customer agreement where required.
Execution status: Desk comparison only; no booking edited or message sent.
```

**Bad output:** “The operator is free, so both appointments are confirmed feasible.”
This ignores the room's supplied reset occupancy.

## Edge cases
- A booking spans midnight: retain the actual dates for both endpoints before comparing clock times.
- A resource supports concurrent use: apply its supplied capacity rule and count concurrent occupancy, not merely pairwise conflicts.
- The customer duration is flexible: propose a bounded alternative only when the permissible duration and service outcome are supplied.
- A reset may happen elsewhere: request the documented resource handoff before shortening the original resource claim.

## Test case
**Input:**
> Fictional salon Elm has two entries with the same booking identifier but different rooms. The operator overlaps another confirmed service. No current authoritative roster is available.

**Assertions:**
1. Treats the duplicate identifier as a reconciliation question rather than two established appointments.
2. Retains the operator conflict even if an alternate room is considered.
3. Requests current assignment and roster evidence.
4. Does not claim a booking was moved.
