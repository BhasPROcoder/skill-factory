---
id: RNT-001
name: rental-serial-allocation-reconciliation
domain: Rental Asset Operations
subdomain: Serial allocation
version: 1.0
description: Reconcile physical rental unit identities with class-level reservations when duplicate serial assignments or substitution constraints obscure fulfillment readiness.
triggers: ["resolve duplicate rental serial assignments","map rental units to reservations","check class versus serial allocation","one asset promised to two hires","reconcile a rental asset swap"]
not_for: ["appointment interval conflict analysis [SVC-001]","warehouse order pick shortages [WHS-002]","supplier equivalence evaluation [BID-002]"]
requires: []
risk_level: medium
---

# Rental serial allocation reconciliation

## Purpose
Produce an assignment ledger that distinguishes a promise for an equipment class from a verified allocation of a particular physical rental unit. Use it when class availability looks sufficient but serial records, held units or return dependencies prevent a reliable handover.

## Inputs to collect
1. **Reservation commitments:** Obtain reservation identifiers, required class, quantity and any promised exact unit. These define whether an assignment may be interchangeable. Default: no assumed right to substitute a serial-specific promise.
2. **Physical-unit register:** Obtain serial or unique asset identifiers, class membership and distinguishing labels. Required; a product-family name alone is not an individual unit.
3. **Assignment evidence:** Collect active allocations, provisional holds, canceled allocations and handover status. These reveal whether two records refer to one claim or competing claims. Default: ambiguous claims remain unresolved.
4. **Eligibility basis:** Obtain location, required readiness status, ownership restrictions and supplied interchangeability rules. Default: only evidenced eligibility counts; do not declare an asset usable from class membership alone.
5. **Time boundary:** Identify the relevant handover window and any preceding return dependency. Default: report the identity conflict without claiming that timing is feasible.
6. **Change authority:** Establish who may replace assignments or alter promises. Default: proposed reassignment only, with original commitments preserved.

If a required input lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Name the allocation snapshot and reservations being reconciled. Preserve the distinction between class-level demand and serial-specific commitments in separate fields.
2. Build a physical-unit identity crosswalk from supplied labels and serials. Flag two asset records that may describe the same object; do not create extra availability by counting aliases independently.
3. Associate each active allocation with its reservation, unit and status. Retain historical rows but exclude confirmed superseded assignments from the current assignment count.
4. ⚠️ Check uniqueness at the physical-object level. If an item has been relabeled, the old and new labels must not satisfy two simultaneous handovers simply because their strings differ.
5. Derive the eligible unit set for each reservation using its own constraints. A unit can be eligible for one use and prohibited for another; retain the requirement that causes the difference.
6. Mark already handed-over units separately from units merely reserved. A promised return provides a possible future source, not current possession or readiness.
7. Compare class-level demand with the union of distinct eligible physical units, then inspect actual assignment conflicts. A sufficient overall count does not prove that every constrained reservation can be satisfied.
8. Construct a proposed reassignment only from evidenced eligibility. Show the displaced reservation, replacement unit and unchanged customer promise; if the promise must change, route that as a separate decision.
9. ⚠️ Check the complete proposed assignment together. Moving a duplicate allocation away from one reservation can create a new duplicate or leave another reservation unassigned.
10. Deliver the allocation ledger and the exact confirmation needed before handover. Recheck current status before any authorized system mutation; do not turn a candidate assignment into a customer confirmation.

## Decision rules
- IF a reservation names an exact unit THEN preserve that promise unless an authorized change is supplied BECAUSE class equivalence alone does not erase a serial-specific commitment.
- IF two labels identify one physical object THEN count one candidate BECAUSE relabeling is not fleet growth.
- IF a replacement depends on an expected return THEN show that dependency explicitly BECAUSE a scheduled return is not an observed ready unit.
- IF all class counts balance but a constrained reservation lacks a candidate THEN retain the unsatisfied reservation BECAUSE aggregate totals can hide assignment infeasibility.
- IF assignments have already been handed over THEN route correction through the actual custody process BECAUSE editing a roster cannot retrieve an asset.

## Output template
```text
Boundary: <snapshot, reservations and handover scope; up to three lines>
Unit identity: <up to eight aliases, unique units and unresolved matches>
Assignment ledger:
Reservation | Promise | Current unit/status | Eligible alternatives | Conflict
<up to ten rows; attach full allocation if larger>
Proposed mapping: <explicit reservation-to-unit changes or no supported map>
Dependencies: <up to five readiness, return or authority checks>
Disposition: <feasible on supplied evidence / blocked / unresolved>
Execution note: <analysis versus actual assignment/handover actions>
```

## Quality checklist
- [ ] Class commitments and exact-unit promises are separated.
- [ ] Physical identity is not inferred solely from similar labels.
- [ ] Superseded and active assignments have distinct states.
- [ ] Eligibility is recorded per reservation.
- [ ] Expected returns are not counted as completed readiness.
- [ ] The proposed mapping contains no competing claim on the same unit.
- [ ] Every displaced reservation retains a supported outcome or explicit gap.
- [ ] No system change or customer confirmation is claimed without evidence.

## Anti-patterns
- **Class-count comfort:** sufficient inventory count is treated as complete allocation. Fix: check each constrained reservation's candidate set.
- **Alias multiplication:** old and new labels become two units. Fix: resolve physical identity before counting.
- **Return certainty:** a promised return is called available. Fix: retain custody and readiness dependencies.
- **Local repair:** one duplicate is moved without reviewing other claims. Fix: evaluate the entire proposed assignment.
- **Silent promise swap:** a named serial is replaced by a similar asset. Fix: obtain the required change authority.

## Worked example
**Input:** Fictional camera-rental studio Fern has two same-window reservations. A requires any blue display stand; B was promised exact stand S2. The fleet has distinct ready stands S1 and S2, both blue. The snapshot assigns S2 provisionally to both A and B; neither has been handed over. The manager may propose reassignment but no system edit has occurred.

**Output:**
```text
Boundary: Fern supplied snapshot; reservations A/B before handover.
Unit identity: S1 and S2 are distinct ready blue stands by supplied evidence.
Assignment ledger:
Reservation | Promise | Current unit/status | Eligible alternatives | Conflict
A | any blue stand | S2, provisional | S1 or S2 | competing S2 claim
B | exact S2 | S2, provisional | S2 only | competing S2 claim
Proposed mapping: Keep B->S2; propose A->S1. Both physical units used once.
Dependencies: Recheck current readiness and allocation; manager authorizes and records A's reassignment.
Disposition: Feasible on supplied evidence as a proposal; existing duplicate remains until authorized correction.
Execution note: Ledger prepared only; no unit assigned, handed over or customer notified.
```

**Bad output:** “Two stands and two bookings means both are already fulfilled.”
This ignores the duplicate serial allocation and mistakes a promise for handover.

## Edge cases
- A serial plate cannot be read: preserve the physical observation and request an approved identification method; do not invent a replacement serial.
- A pooled reservation allows several equivalent units: record the permitted pool and defer final serial choice until verified allocation.
- One asset appears at two locations: hold both location claims pending custody reconciliation instead of choosing the more convenient location.
- A proposed swap changes an accessory interface: reopen eligibility and handover-kit checks rather than assuming the base class guarantees completeness.

## Test case
**Input:**
> Fictional depot Grove has labels Old-R and New-R that its register explicitly identifies as one relabeled stand. Separate reservations each provisionally claim one label. No other stand is evidenced.

**Assertions:**
1. Counts one physical unit rather than two.
2. Identifies competing claims requiring a decision.
3. Does not invent another candidate or erase a reservation.
4. Makes no handover or assignment-change claim.
