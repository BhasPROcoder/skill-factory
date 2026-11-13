---
id: WHS-002
name: pick-short-exception-resolution
domain: Warehouse Stock Operations
subdomain: Order picking exceptions
version: 1.0
description: Prepare a fulfillment decision for a short pick when confirmed picked quantities, eligible alternatives and order constraints must be reconciled.
triggers: ["a picker cannot complete this order line","resolve a short pick","which inventory can cover this unfilled quantity","prepare a picking exception handoff","compare hold split and substitution options"]
not_for: ["explaining a bin-count discrepancy [WHS-001]","designing storefront out-of-stock behavior [MEC-009]","drafting a post-purchase message [MEC-008]"]
requires: []
risk_level: medium
---

# Resolve a short pick without losing the order balance

## Purpose
Give a fulfillment operator a decision record for an order line whose pick could not be completed as instructed. Determine what remains open, which stock could actually satisfy that line, and which release decision still needs permission; avoid converting an operational shortage into a false shipment or an unauthorized replacement.

## Inputs to collect
1. **Line commitment.** Collect the item, variant, unit, requested quantity, and approved changes to the order. This sets the demand to satisfy. If the line or unit is ambiguous, keep its quantity unresolved.
2. **Pick evidence.** Collect confirmed pick events, quantities in the order tote, prior fulfilled units, cancellations and reversals. Ask whether the reported counts are cumulative or incremental. Default: a task assignment is not a completed pick.
3. **Candidate stock.** For each alternative location request item identity, unit, quantity, reservations, holds, lot or other eligibility restrictions, and time of the check. Default: a location lead, not available supply.
4. **Order conditions.** Obtain partial-release, split, backorder, substitution, and timing rules from the current order and applicable operating instructions. Default: no permission to change the customer's commitment.
5. **Execution boundary.** Identify what the operator can verify or authorize, whether any pick is already in progress, and which system evidence would establish success. Default: propose a disposition without reserving, releasing or messaging.

If required information lacks a safe default, ask in one message with at most three questions.

## Procedure
1. Identify the exact order line and the remaining commitment. Record any approved cancellation separately so it is not mistaken for a pick.
2. Reconstruct confirmed coverage in mutually exclusive buckets. For example, units already fulfilled and units picked but not yet shipped may cover different portions. If a cumulative pick count already includes shipped units, do not add that full count to shipped units again.
3. Compute the open pick quantity as the active commitment less confirmed coverage. Also show which covered units still await release. Picking and shipping have different completion boundaries.
4. ⚠️ Inspect duplicate scans, reversals and open pick tasks before proposing a replacement pick. A second task for the same shortage must not authorize a second physical fulfillment.
5. Build a candidate list in the line's unit. Identify restrictions before arithmetic: matching product alone is insufficient if ownership, allocation, condition or order-specific requirements differ. Do not deduct the same held units twice when reservation and hold categories overlap.
6. Assign each candidate a usable quantity supported by the supplied evidence, a confirmed exclusion, or a pending check. A nearby location with unknown reservations may be worth checking but contributes no confirmed coverage yet.
7. Draft alternative dispositions that respect the actual permissions. Consider an exact-item recovery from an eligible bin, a hold pending replenishment, partial release if allowed, or a separately approved substitution. Do not call a candidate quantity picked until the necessary operation has occurred.
8. Compare the options using the user's constraints. If partial release is forbidden, do not infer that the already picked units may ship. If a customer approval is required, identify what must be proposed and keep the line unchanged while awaiting it.
9. Name the next owner and trigger. An operator may need to recheck availability immediately before assignment, confirm a physical pick, close a superseded task, or obtain a release decision. Describe each as a pending step unless evidence shows it occurred.
10. Report the post-action quantity as a conditional projection alongside the current open quantity. Mention stock reconciliation separately when the bin record itself may be wrong.

## Decision rules
- IF a possible replacement is already reserved for another order THEN exclude it from confirmed recoverable quantity BECAUSE stock on a shelf is not necessarily available to this line.
- IF the candidate is a different variant THEN require the relevant substitution authorization BECAUSE similarity alone cannot change the original commitment.
- IF a pick event may duplicate another event THEN preserve both references and defer the disputed quantity BECAUSE summing duplicate coverage can hide a short line.
- IF the available exact item covers only part of the shortage THEN show the residual after a hypothetical successful pick BECAUSE that recovery does not independently authorize a partial shipment.
- IF a prior pick attempt is still active THEN reconcile its status before creating another instruction BECAUSE parallel attempts may both finish against the same demand.

## Output template
```text
Line: <order line, item, unit, active commitment and supplied constraints>
Coverage: <confirmed nonoverlapping quantities and open pick quantity>
Candidate checks: <one row per location or alternative: identity, eligibility, usable or pending>
Options: <permitted recovery paths and quantities still open after each>
Decision: <recommended next step, authority and any unresolved gate>
Closeout evidence: <what would establish recovery, release or escalation>
Current status: <what is actually confirmed; maximum two sentences>
```

## Quality checklist
- [ ] The active commitment matches the supplied order in one verified unit.
- [ ] Shipped and picked coverage are not double-counted.
- [ ] Assigned and proposed picks remain separate from confirmed quantities.
- [ ] Each candidate's restrictions are checked or explicitly unresolved.
- [ ] Current and conditional remaining quantities are separately labeled.
- [ ] A partial release or substitution follows explicit permission.
- [ ] Duplicate or superseded tasks have a reconciliation step.
- [ ] No unobserved customer notification, reservation or shipment is claimed.

## Anti-patterns
- **System balance as promise:** A stock screen displays enough units, so the customer is promised delivery. Fix: verify current eligibility and successful completion before making a commitment.
- **Counting tasks as units:** A reassigned pick is treated as a second completed pick. Fix: trace confirmations to line, destination and reversal history.
- **Quiet substitution:** A similar item is used to close a short line. Fix: preserve original demand and require the documented decision for a different item.
- **Partial by default:** Shipping what is ready despite a complete-line requirement. Fix: retain picked goods as awaiting release and identify the permitted recovery path.
- **Closing the root cause:** A recovered order is treated as proof the original bin record is correct. Fix: route the count difference for separate investigation.

## Worked example
**Input:**
> Fictional shop Tamarind has an active line for nine blue journals, to ship together without substitution. Four blue journals are confirmed in the tote, none shipped, and there are no other pick tasks. Bin B has three matching journals checked as eligible and unreserved. Bin C has two matching journals already reserved for another order. The supervisor can request another exact-item pick but no new pick has been performed.

**Output:**
```text
Line: Nine blue journals for one line; ship together, no substitutes.
Coverage: Four picked in tote; none shipped. Nine minus four = five still to pick.
Candidate checks: B: three exact, eligible and unreserved at check time. C: two exact but reserved elsewhere; zero usable for this line.
Options: Recheck and request three from B: if confirmed, seven would be picked and two still open. Hold the complete shipment pending the remaining two. No permitted partial release or substitution.
Decision: Supervisor rechecks B before assigning the recovery pick and seeks another eligible source for the residual. Preserve the four already in the tote.
Closeout evidence: Confirm each new pick against the order line and tote; verify the full nine are covered and the release conditions still hold before any shipment decision.
Current status: Four picked, five still open, none shipped. B's three are a recovery proposal only.
```

**Bad output:** “B and C have five more; mark the line complete.” This uses another order's reservation and counts prospective picks as completed.

## Edge cases
- Units in another bin are in cartons: confirm the pack conversion and permission to break the carton; otherwise leave the candidate pending.
- A picked unit is damaged before release: verify its current status and any reversal before reducing covered quantity; record it separately from the unfilled demand.
- A late pick confirmation arrives during reassignment: reconcile both task identities before additional work and recalculate the residual from confirmed nonduplicate units.
- Customer changes the quantity while recovery is pending: obtain the effective revised commitment, preserve the previous decision record and recheck any open tasks against the new balance.

## Test case
**Input:**
> A fictional order needs eight identical units. A cumulative pick record shows six, of which two already shipped. Two alternatives of the correct type exist, but both are on hold. The user asks whether the line is complete.

**Assertions:**
1. Treats the six cumulative picks as six units of coverage, including the two shipped.
2. Reports four picked but not shipped and two units still to pick.
3. Excludes held alternatives from confirmed recovery unless the holds are resolved by an authorized decision.
4. Does not claim completion or shipment of the remaining units.
