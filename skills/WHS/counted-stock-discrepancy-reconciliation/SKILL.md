---
id: WHS-001
name: counted-stock-discrepancy-reconciliation
domain: Warehouse Stock Operations
subdomain: Stock count reconciliation
version: 1.0
description: Reconcile an observed warehouse count with a recorded quantity when location, stock identity or movement timing could explain the difference.
triggers: ["resolve a warehouse count variance","reconcile this bin count","explain a physical inventory difference","check which stock movements belong before the count","prepare a recount investigation"]
not_for: ["recovering an individual short order [WHS-002]","reconciling dataset control totals [TDQ-010]","valuing an inventory adjustment"]
requires: []
risk_level: medium
---

# Reconcile a counted stock discrepancy

## Purpose
Prepare an evidence-backed comparison between physical units counted in a specified place and the units the records say should have been there at that moment. Give the person investigating the variance a reproducible calculation, a separation of known movements from hypotheses, and the next check that would change the disposition.

## Inputs to collect
1. **Count identity.** Ask for item, variant, unit, bin, ownership or lot distinctions where used, and stock condition. These define what belongs in the comparison. Without them, label the scope unresolved rather than combining similar items.
2. **Physical evidence.** Obtain the original count sheet, quantity, count time or interval, and any independent recount. Preserve an uncounted location as unknown; a recorded zero requires evidence that the location was checked.
3. **Reference balance.** Request the balance for that scope and the precise point it represents, including which movements are already reflected. A live dashboard without a reference time is not a sufficient comparison by itself.
4. **Movement evidence.** Collect receipts, picks, transfers, returns, and relevant status changes spanning the comparison window. Obtain quantities, reference identifiers, actual movement times and recording times where available. Default: unexplained movement coverage.
5. **Review authority.** Ask who can recount, check event records, or authorize a correction. Without a supplied role, propose a follow-up for the inventory owner; do not claim an adjustment was posted.

If a required input has no safe default, ask in one message with at most three questions.

## Procedure
1. Define a comparison key that can be applied to both the count and ledger: same unit, item, physical boundary, ownership and included conditions. State whether a neighboring bin is inside or outside it.
2. Establish the count cutoff. For an interval rather than an instant, identify movements during counting and whether the affected units were counted before or after each movement.
3. Preserve each original observation separately. Keep original quantity and unit even when you translate to a common comparison unit.
4. Convert packs to units only when their actual contents and item identity are established. Treat an opened carton as separately counted loose units unless its contents are evidenced.
5. Build a movement bridge from the reference point to the count cutoff. Add confirmed entries into the boundary, subtract confirmed exits, and leave movement wholly inside the boundary at net zero. For a snapshot later than the count, reverse only the confirmed movements between count and snapshot.
6. ⚠️ Check which movements the reference balance already includes. A record's entry time may differ from the time goods moved. Record a reason for including, excluding, or deferring each candidate rather than counting the same event twice.
7. Compute expected units at the cutoff, then subtract expected units from counted units. Label the sign explicitly: negative means fewer were counted than expected. If a needed value is unknown, retain a symbolic bridge or competing cases rather than forcing a single residual.
8. List explanations supported by evidence separately from explanations that still need tests. A difference in a nearby bin may justify checking a transfer, but an offsetting number alone does not establish item identity or a common cause.
9. Choose the smallest discriminating check: an independent recount, an event identifier match, a location scan, or confirmation of carton contents. Where feasible under the site's process, ask the recounting person to record observations before seeing the expected total.
10. Set a disposition for the evidence packet. Matched within the defined boundary, unresolved variance, and not comparable are different findings. An explained timing difference may still require a recording correction by the authorized owner.

## Decision rules
- IF the stock keys or units cannot be aligned THEN withhold a numerical variance BECAUSE subtraction across unlike units or stock categories has no clear interpretation.
- IF a transfer crosses only part of the chosen boundary THEN record its effect on each affected location BECAUSE a site total can match while individual bins disagree.
- IF two records could describe the same movement THEN match event identifiers and physical evidence before including both BECAUSE duplicate records can manufacture a variance.
- IF the bridge explains only part of the difference THEN report the remaining signed quantity BECAUSE an evidenced cause does not explain unrelated missing units.
- IF the physical count and reference balance agree THEN limit the conclusion to that time and scope BECAUSE agreement does not verify ownership, valuation or other locations.

## Output template
```text
Scope: <one line: item, unit, location, conditions, cutoff>
Sources: <one line per count, balance, or movement record>
Bridge: <reference plus/minus included movements; exclusions and unknowns>
Result: <counted, expected, signed difference; or not comparable with reason>
Evidence assessment: <confirmed explanation; unresolved alternatives>
Next check: <discriminating check and responsible role if known>
Disposition: <matched / unresolved / not comparable; proposed action only>
```

## Quality checklist
- [ ] Count and balance use the same physical and item boundary.
- [ ] Cutoff timing and included stock conditions are explicit.
- [ ] Original units and any conversion basis remain traceable.
- [ ] Each included movement has a reference and direction.
- [ ] Movements already included in the balance are not reapplied.
- [ ] Signed difference can be recomputed or a missing input prevents it.
- [ ] Suggested causes are distinguished from established movements.
- [ ] Proposed correction is separate from a posted adjustment.

## Anti-patterns
- **Counting a label:** Assuming an unopened-looking package contains its nominal quantity. Fix: verify the basis for using the pack count or keep it unresolved.
- **Treating a pending record as movement:** A draft transfer may not have occurred. Fix: separate request, physical movement and recording evidence.
- **Balancing by assumption:** Adding an unexplained loss until the count matches. Fix: show the residual and a check that could distinguish explanations.
- **Netting unrelated bins:** Two opposite differences cancel across unlike lots. Fix: compare keyed balances first and aggregate only within a justified boundary.

## Worked example
**Input:**
> Fictional depot Mallow records 40 loose blue clips in bin P at opening. The opening balance includes no later movements. Receipt R confirms six loose blue clips physically entered P after opening and before the count. Transfer T confirms four left P in the same interval. Count sheet C records 41 loose blue clips in P after T. No other movement records, recount, or adjustment authority are supplied.

**Output:**
```text
Scope: Blue clips, loose units in bin P, at count C after transfer T.
Sources: Opening record: 40. R: six physically received. T: four physically transferred out. C: 41 counted.
Bridge: 40 + 6 - 4 = 42 expected from supplied records. Movement completeness is unconfirmed.
Result: 41 counted minus 42 expected = -1 clip; one fewer counted than expected.
Evidence assessment: R and T explain the change from opening to expected stock. Neither explains the remaining one-clip discrepancy; count error and an unrecorded movement are untested possibilities.
Next check: Request an independent recount of P and check the movement sequence around C against source documents.
Disposition: Unresolved; no adjustment posted or authorized.
```

**Bad output:** “A clip was stolen; reduce the balance by one.” A residual is not evidence of theft or authorization to change a record.

## Edge cases
- Count completed while a picker was removing units: establish whether those units entered the physical count; if timing cannot be reconstructed, request a controlled recount.
- Count mixes sealed cases and loose stock: verify each relevant pack size and count loose stock separately before aggregation.
- Recount disagrees with the initial count: preserve both observations with times and intervening events; do not silently select the value closer to the ledger.
- Correct bins but wrong stock condition: compare condition buckets separately and investigate any status change rather than assuming the goods are available to pick.

## Test case
**Input:**
> A fictional site supplies a later snapshot of 15 units and documentation that a three-unit receipt after the count is included in it. No other movements occurred. The earlier count was 12 units of the same item in the same bin. Prepare the comparison.

**Assertions:**
1. Reverses the later receipt to obtain 12 expected units at the count.
2. Reports zero signed difference for the specified boundary.
3. Distinguishes the matched result from any broader assurance about stock.
4. Does not propose or claim a posted correction.
