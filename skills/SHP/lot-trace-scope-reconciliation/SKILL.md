---
id: SHP-002
name: lot-trace-scope-reconciliation
domain: Shipment Record Reconciliation
subdomain: Lot trace scope
version: 1.0
description: Trace a specified product lot through supplied inventory, transformation, shipment, and return records to prepare a bounded affected-stock and destination handoff.
triggers: ["trace where this product lot went", "prepare a lot traceability record", "identify shipments linked to an affected batch", "reconcile lot stock and customer destinations", "map returned and quarantined lot units"]
not_for: ["decide whether a recall is legally required", "reconcile package contents for one shipment [SHP-001]", "reconcile one warehouse stock count [WHS-001]", "reconcile an inbound receipt variance [WHS-003]", "contact customers or release or destroy stock"]
requires: []
risk_level: high
---

# Lot Trace Scope Reconciliation

## Purpose
Trace a defined lot across supplied receiving, transformation, inventory, shipment, and return records. Separate confirmed links, candidates, and unknown quantities for an owner handoff. This administrative record does not decide whether recall, notification, reporting, or product disposition is required.

## Inputs to collect
1. **Scope** — product/lot IDs, aliases, concern, jurisdiction, and trace boundary. Why: IDs and obligations vary. Default: ask for missing identity/context; do not presume a recall.
2. **Authority** — incident owner, current trace/hold procedure, and permitted actions. Why: owners decide containment. Default: evidence trace only.
3. **Records** — receiving, transformation, inventory, shipment, return, and correction records with revisions and times. Why: each shows a state change. Default: use supplied evidence and list missing record types.
4. **Quantity basis** — item, unit, conversion, scrap/consumption, and cumulative vs incremental rule. Why: unlike bases cannot be summed. Default: keep conversion unresolved.
5. **Destinations/privacy** — order/shipment and customer/site references, access and masking limits. Why: minimize data exposure. Default: use only identifiers needed by the authorized owner.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

Verify current safety, legal, or regulatory requirements in authoritative sources; do not rely on model memory. Refer recall, reporting, notification, and product-safety decisions to the responsible qualified professional; seek licensed legal counsel when interpreting legal obligations.

## Procedure
1. Freeze source IDs, revisions, times/time zones where supplied, and trace boundary.
2. Map explicit lot, serial, item, and transformation links; keep unverified aliases as candidates.
3. Trace backward to receipt/production and forward through inventory, transformations, shipments, returns, and current locations.
4. Record one row per evidenced movement/state with source, unit, event/record time, location, and status; maintain separate balances by item, lot stage, and unit.
5. ⚠️ Do not infer lot identity from similar descriptions, dates, or package labels; mark candidates and request a controlled cross-reference.
6. Distinguish received, available, held, transformed, shipped, returned, and unknown only when evidenced; a planned move is not completed.
7. For splits, count child quantities as a partition only when records show they are mutually exclusive. For merges, retain each parent contribution without adding the merged output to the same-stage input balance.
8. Link changed items/units through process records. Use only documented conversion/yield; unknown yield stays unresolved and unlike units stay in separate balances.
9. Reconcile same-item, same-unit stages after checking duplicate scans, reversals, scrap, and returns. Show confirmed, candidate, and residual amounts; never assign residuals to an unknown destination.
10. List shipment/order references with masked destinations and status. Return the gaps to the authorized owner; take no hold, release, contact, destruction, reporting, or record-change action without explicit authorization.

## Decision rules
- IF a controlled record explicitly links a lot to a movement THEN mark that link confirmed within the source scope BECAUSE the record supplies the relationship.
- IF identity rests only on similar description, date, or label THEN mark it candidate and exclude it from confirmed totals BECAUSE resemblance is not lot evidence.
- IF parent/child lots appear after a split or merge THEN keep stage balances separate and count only mutually exclusive states BECAUSE adding both generations double-counts material.
- IF item or unit changes, or yield is unknown THEN use separate balances and mark downstream scope unresolved BECAUSE unlike units cannot be added without a documented process basis.
- IF a shipment has only a created label or plan THEN do not call it shipped/delivered BECAUSE preparation is not handover evidence.
- IF a return or reversal exists THEN link it to the original event before netting BECAUSE it may describe the same units at another state.
- IF a balance has a residual THEN report it and the next discriminating record; do not assign a cause BECAUSE residuals do not identify a destination.
- IF recall, notification, release, or reporting is requested THEN prepare evidence only and refer the decision to the qualified owner using current guidance BECAUSE trace scope does not establish the obligation.
- IF jurisdiction, unit basis, source completeness, or authority is missing THEN state the limit and ask before dependent conclusions BECAUSE no safe default is established.

## Output template
```text
Scope: <product/lot identifiers, jurisdiction, source snapshot and boundary; up to 3 lines>
Identifier map: <confirmed links and candidate aliases with source references>
Trace ledger:
| Event/source | Lot or linked ID | From/to | Quantity/unit at this stage | Status | Confirmed/candidate | Evidence |
|---|---|---|---:|---|---|---|
Quantity reconciliation: <one row per item/lot stage/unit; source total | confirmed accounted | candidate/unresolved | residual; show arithmetic; never add unlike units>
Destination handoff: <shipment/order reference | masked customer/site | status | source>
Gaps: <missing records or identity links and next discriminating check>
Owner decision: <authorized owner and current-source questions; do not decide recall duty>
Boundary: <analysis performed; unperformed hold, release, notification, reporting, destruction, or record change>
```

## Quality checklist
- [ ] Lot identity is linked through explicit source records or marked candidate
- [ ] Source versions and event/record time distinctions are preserved where supplied
- [ ] Units and conversion basis remain visible and compatible before arithmetic
- [ ] Planned, moved, shipped, delivered, returned, and current-stock states are not conflated
- [ ] Split/merged parent-child links and transformation yields use supplied evidence
- [ ] Quantity totals show confirmed amount, unresolved amount, and residual separately
- [ ] Destination list uses the minimum identifying detail needed for authorized follow-up
- [ ] No recall, notification, safety, legal, or regulatory conclusion is inferred from the trace
- [ ] Current requirements are checked with authoritative sources or left open
- [ ] No external or inventory action is reported as performed without evidence

## Anti-patterns
- **Fuzzy lot join**: link similar names/dates. Fix: require a controlled ID or retain a candidate.
- **Planned equals shipped**: treat a label as delivery evidence. Fix: use the actual movement record.
- **Residual assignment**: allocate untraced units to a convenient destination. Fix: report the gap and request records.
- **Double-counted genealogy**: sum parent and child lots or incompatible units. Fix: separate stage balances and use documented yields only.
- **Trace equals recall**: infer a recall decision from the destination list. Fix: route evidence to the authorized qualified owner.
- **Overexposed recipient list**: include unnecessary customer details. Fix: mask identifiers to the follow-up need.

## Worked example
**Input:** Fictional maker Alder received 24 kg of ingredient lot L-7. Process records link 10 kg to finished lot Q (12 bottles) and 14 kg to lot R (18 bottles). A stock snapshot lists 4 Q and 6 R bottles. Shipment records link 6 Q bottles to masked site Cedar and 10 R bottles to masked site Pine; both are delivered. No other output status is supplied. The owner asks for trace scope, not a recall decision.

**Output:**
```text
Scope: Alder L-7; jurisdiction not supplied; supplied receipt, process, stock, and shipment records only.
Identifier map: process records link L-7 to finished lots Q and R.
Trace ledger:
| Event/source | Lot or linked ID | From/to | Quantity/unit at this stage | Status | Confirmed/candidate | Evidence |
| Receipt R-1 | L-7 | supplier to Alder | 24 kg | received | confirmed | R-1 |
| Process T-1 | L-7 → Q | 10 kg input → Q | 12 bottles output | transformed | confirmed genealogy | T-1 |
| Process T-2 | L-7 → R | 14 kg input → R | 18 bottles output | transformed | confirmed genealogy | T-2 |
| Stock S-1 | Q | Alder stock | 4 bottles | current stock | confirmed | S-1 |
| Stock S-1 | R | Alder stock | 6 bottles | current stock | confirmed | S-1 |
| Shipment D-1 | Q | Alder to masked Cedar via O-1 | 6 bottles | delivered | confirmed | D-1 |
| Shipment D-2 | R | Alder to masked Pine via O-2 | 10 bottles | delivered | confirmed | D-2 |
Quantity reconciliation: L-7 input: 10 + 14 = 24 kg consumed; residual 0 kg. Q: 12 bottles output = 4 stock + 6 delivered + 2 unknown. R: 18 bottles output = 6 stock + 10 delivered + 2 unknown. Keep ingredient kg separate from finished bottles.
Destination handoff: O-1 | Cedar | 6 Q bottles delivered | D-1; O-2 | Pine | 10 R bottles delivered | D-2.
Gaps: Four bottles have no supplied status (two Q, two R); later movements and source cutoff remain unverified. Request the current lot movement export through the owner's cutoff.
Owner decision: Responsible quality/safety owner decides applicable containment and notification steps using current requirements; jurisdiction and authorization were not supplied.
Boundary: Supplied records reconciled; no hold, release, notification, reporting, destruction, or record change performed.
```

**Bad output:** “All finished units are accounted for, so no recall is needed.”

Fails because the ledger only covers supplied records, and trace completeness does not determine whether a safety or legal action is required.

## Edge cases
- **A transformation changes the lot identifier**: link parent and child only through the supplied process record; do not infer yield or equivalence.
- **A destination is a distributor or internal site**: record that immediate destination and mark onward distribution unresolved until downstream records are supplied.
- **A shipment is canceled after label creation**: retain the planned shipment row but do not count it as delivered or subtract it from stock without movement evidence.
- **A returned unit has no lot reference**: keep it outside confirmed lot totals and request the return authorization or inspection cross-reference.
- **A source export is incomplete or ends at an unknown cutoff**: label the trace as provisional and state the exact missing period or record class.

## Test case
**Input:**
> Birch received 30 units of batch B-4. A complete stock count records 10 units and excludes staging. Shipment records link 12 units to delivered order Oak. A separate staging record identifies 5 picked units for another order; its label exists but no handover is evidenced. Prepare a trace scope, not a recall decision.

**Assertions:**
1. Confirms only the 10 current-stock units and 12 delivered units; the 5 labeled units remain planned or shipment-status unresolved.
2. Reconciles 10 current-stock + 12 delivered + 5 separately staged = 27 units and shows 3 units with no supplied status; it does not count the label as shipment or delivery evidence.
3. Keeps the customer/site identifier masked and identifies a current source cutoff as a limitation.
4. Makes no recall, notification, safety, legal, or regulatory determination.
5. Reports no hold, release, destruction, notification, or record change as performed.
