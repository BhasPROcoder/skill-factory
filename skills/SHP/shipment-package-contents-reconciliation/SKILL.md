---
id: SHP-001
name: shipment-package-contents-reconciliation
domain: Shipment Record Reconciliation
subdomain: Packing records
version: 1.0
description: Reconcile order-line quantities and package assignments when a shipment is split, consolidated or repacked.
triggers: ["reconcile parcels with order lines", "check a packing list", "trace a repacked shipment", "why do package counts disagree", "map items to shipment containers"]
not_for: ["resolve an unpicked order quantity [WHS-002]", "reconcile warehouse stock counts [WHS-001]", "customs classification or legal transport advice"]
requires: []
risk_level: medium
---

# Shipment package and contents reconciliation

## Purpose
Build a traceable relationship between order-line quantities, packed containers and a proposed shipment record. Use it when several orders share a shipment, one order spans several parcels, or repacking makes package counts disagree with item counts.

## Inputs to collect
1. **Shipment scope:** Obtain the shipment identifier, destination and whether the packet is a draft, handed over or received. Required; do not infer shipment completion from a printed label.
2. **Item commitments:** Obtain order-line identifiers, item identities, quantities and units. These establish what the proposed shipment should cover. Without them, restrict the result to checking the supplied package ledger.
3. **Package evidence:** Request container identifiers, contents assignments and the latest packing or repacking records. These connect physical packages to items. Missing assignments remain unknown rather than spread evenly across containers.
4. **Grouping rules:** Collect supplied split-shipment, mixed-order and nesting rules. Default: no invented authority to split an order or combine destinations.
5. **Revision history:** Obtain canceled labels, superseded package records and movement evidence. Default: duplicates remain unresolved until identity and status are established.
6. **Action authority:** Identify whether the user wants an analysis, a corrected draft or actual shipment changes. Default: report only; no inventory release, booking or carrier change is authorized by this reconciliation.

If a required input lacks a safe default, ask for it in one message with at most three questions.

## Procedure
1. Freeze the packet revision and declare which records represent planned contents versus observed packing. Preserve source locators so the ledger can be checked against the original notes.
2. Identify the counting level of each quantity. Distinguish shipment, outer container, inner carton, item and order line. A package count is not an item count, and a carton nested inside another counted container must not become a second outward parcel unless the shipment definition says so.
3. Assign one row per package-content relationship using stable identifiers. When an identifier appears twice, compare whether the rows describe different contents, repeated scans or incompatible versions rather than deduplicating solely on the label.
4. Trace repacking events from the old container to the new containers. Mark superseded assignments without erasing their history. A replaced label does not prove that the old parcel was destroyed or never handed over.
5. ⚠️ Convert content quantities only with an evidenced packing factor for that item and revision. Different cartons can contain different amounts. Record mixed units as unresolved when no conversion basis exists.
6. Aggregate active content assignments by order line, retaining package memberships. Compare those totals with the quantity intended for this shipment, not automatically with the entire original order if an approved split exists.
7. Check the other direction: every active outward package needs an evidenced contents assignment or an explicit sealed/unknown-content exception. A perfect item total does not explain an extra package on a transport list.
8. ⚠️ Separate unexplained differences from causes. A missing assignment may indicate incomplete paperwork, an unrecorded repack or a physical packing error. List the next discriminating check rather than accusing a person or declaring goods lost.
9. Prepare a correction proposal scoped to the draft or operational record that is actually wrong. Do not revise a handed-over package's contents merely to make the order total balance. Escalate a real discrepancy through the user's supplied process.
10. Deliver the ledger with a disposition for each unresolved package or line. State which comparisons were possible and what evidence is still needed before release.

## Decision rules
- IF a parent carton and its child carton are both listed THEN establish the counting level before summing BECAUSE a nested container may not represent an additional outward parcel.
- IF a label is canceled but physical handover is uncertain THEN retain a handover question BECAUSE a record change is not evidence of a physical reversal.
- IF two items share a package THEN preserve both content rows under one outward package BECAUSE one parcel can satisfy multiple order lines.
- IF one line appears in several parcels THEN aggregate only distinct active assignments BECAUSE repacking history and duplicate scans can inflate coverage.
- IF the quantity belongs to a later approved shipment THEN keep it outside this shipment's expected total BECAUSE reconciliation must use the applicable fulfillment boundary.

## Output template
```text
Boundary: <shipment, revision, destination and status; up to three lines>
Package ledger: <up to ten rows; attach overflow without dropping exceptions>
Package | Parent/level | Order line | Quantity and unit | Evidence/status
Line comparison: <up to ten rows>
Line | Expected in this shipment | Active assigned | Difference | Open check
Package comparison: <outward package count and unassigned/ambiguous records>
Disposition: <ready for stated next check / blocked / correction proposed>
Execution note: <performed comparisons and unperformed physical or system actions>
```

## Quality checklist
- [ ] Shipment boundary distinguishes planned, handed-over and received states.
- [ ] Package and item quantities use separately identified counting levels.
- [ ] Each aggregation retains the relevant order-line identities.
- [ ] Conversion factors come from supplied records rather than typical carton sizes.
- [ ] Repacked or canceled assignments are not counted twice.
- [ ] Every active outward package is accounted for or flagged.
- [ ] Differences remain distinct from inferred causes.
- [ ] Release and system-update claims are limited to observed actions.

## Anti-patterns
- **Parcel equals unit:** three cartons are assumed to contain three items. Fix: establish contents and units from the packing record.
- **Forced balance:** unexplained quantities are assigned evenly across packages. Fix: leave assignments open and request actual packing evidence.
- **History deletion:** superseded parcels disappear from the trace. Fix: retain their status and replacement relationship without including both in current totals.
- **Order overreach:** a partial approved shipment is compared with the entire order. Fix: establish the quantity committed to this shipment first.
- **Label certainty:** a created or canceled label is treated as physical handover evidence. Fix: check the operational event separately.

## Worked example
**Input:** Fictional studio Moss is preparing shipment Birch, draft revision Clear, for one destination. This shipment is to contain seven blue folders for line A and three red folders for line B, measured individually. Its packing sheet assigns package P one blue folder and three red folders, and package Q six blue folders. Both packages are outward parcels, not nested. Transport draft T lists P, Q and an unexplained package R. Nothing has been handed over.

**Output:**
```text
Boundary: Birch/Clear, one supplied destination; draft shipment only.
Package ledger:
Package | Parent/level | Order line | Quantity and unit | Evidence/status
P | outward | A | one blue folder | packing sheet, planned
P | outward | B | three red folders | packing sheet, planned
Q | outward | A | six blue folders | packing sheet, planned
R | outward per T | unknown | unknown | transport draft only; assignment missing
Line comparison:
Line | Expected in this shipment | Active assigned | Difference | Open check
A | seven folders | one plus six = seven | zero | physical packing unverified
B | three folders | three | zero | physical packing unverified
Package comparison: Packing sheet accounts for two outward packages; transport draft lists three. R is unexplained despite matching item totals.
Disposition: Blocked pending whether R is a stale entry, a missing contents record or another physical package.
Execution note: Supplied records compared only; no packing inspection, record correction or handover performed.
```

**Bad output:** “The item totals match, so approve all three packages.”
This ignores an unexplained outward package and invents release authority.

## Edge cases
- A sealed third-party carton lacks an internal inventory: retain the seal and source references if supplied, mark contents unverified, and use the user's applicable acceptance process.
- A package contains two destinations: flag the destination conflict rather than assuming the carrier will split its contents.
- A line is measured by weight while another uses units: keep separate comparisons unless an evidenced conversion is explicitly valid for that material.
- A damaged package is repacked after handover: preserve event order and chain of identifiers; do not retroactively rewrite the original handover packet.

## Test case
**Input:**
> Fictional shipment Elm shows old carton X with four kits, canceled after repacking. New cartons Y and Z each contain two kits. A carrier record still lists X and Y. No physical collection evidence is provided.

**Assertions:**
1. Counts four kits in the active packing assignments without adding canceled X.
2. Flags the mismatch between active package set Y/Z and transport set X/Y.
3. Does not infer that X was physically collected or Z was lost.
4. Requests event or correction evidence before calling the packet ready.
