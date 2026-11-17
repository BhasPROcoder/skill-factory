# Independent behavioral review: SHP-002

Reviewer: independent agent pass  
Artifact: `skills/SHP/lot-trace-scope-reconciliation/SKILL.md`  
Scope: procedure-level comparison with SHP-001, WHS-001/002, and LIR-003; text evaluation of split/merge, units/yield, returns, missing-input, ambiguous-identity, unknown-yield, customer-trace, and authority scenarios. No live shipment or product action was taken.

## Catalog comparison

- **SHP-001 shipment-package-contents-reconciliation** maps order-line quantities to outward package contents, handles repacking revisions and package counts, and checks whether active packages have assigned contents. It does not trace a lot through receipts, transformations, lot splits/merges, returns, or multiple downstream shipments.
- **WHS-001 counted-stock-discrepancy-reconciliation** bridges a physical location count to a ledger snapshot through confirmed movements. It does not build parent-child lot lineage or a destination list.
- **WHS-002 pick-short-exception-resolution** evaluates one unfilled order line and eligible recovery stock. It does not establish lot ancestry or trace affected finished lots to customers.
- **LIR-003 out-of-tolerance-affected-record-inventory** maps instrument status evidence to candidate runs/samples and routes technical decisions. It is analogous in administrative caution but concerns instrument-to-record linkage, not physical product genealogy or shipment scope.
- **Finding:** SHP-002's transformation genealogy and affected-stock/destination handoff is materially distinct from these neighbors. Its high-risk boundary is appropriately explicit: no recall, notification, reporting, safety, or disposition determination; jurisdiction and qualified owner are required.

## Fresh text evaluations

### 1. Split/merge, yield, shipment and return scenario

Prompt: “Fictional maker Willow has two ingredient lots, A=8 kg and B=4 kg. A controlled process record explicitly merges them into mix M=12 kg. A second controlled record splits M into finished lot X=30 bottles and finished lot Y=20 bottles. Current-stock evidence says X has 18 bottles, including 3 identified returns from shipment D-X; D-X originally delivered 8 bottles to masked site Oak. Lot Y has 10 bottles in stock and shipment D-Y delivered 6 to masked site Pine. No other output records or downstream use records are supplied. Prepare lot scope, not a recall decision.”

Response produced:

```text
Identifier map: A and B -> M by controlled merge record; M -> X and Y by controlled split/process record. D-X and its return are linked by source reference; Oak and Pine remain masked.
Trace ledger: A 8 kg + B 4 kg -> M 12 kg; M's documented process output -> X 30 bottles and Y 20 bottles. Do not add A/B/M kilograms to finished bottles.
Quantity reconciliation:
- M input: 8 + 4 = 12 kg; accounted by the supplied merge record, residual 0 kg within the supplied record boundary.
- X: output 30 bottles. Stock 18 includes returned 3; D-X gross delivered 8 minus linked return 3 = 5 bottles unreturned in the supplied event record. Their current customer-side status is unknown. Stock plus net unreturned-delivery status = 18 + 5 = 23; 7 bottles have no supplied status.
- Y: output 20 bottles; stock 10 + D-Y delivered 6 = 16; 4 bottles have no supplied current status.
Destination handoff: D-X | Oak (masked) | delivered 8, linked return 3, 5 unreturned in supplied records (current state unknown); D-Y | Pine (masked) | delivered 6.
Gaps: source completeness/cutoff and status of X's 7 and Y's 4 residual bottles are unknown; obtain the owner's defined current movement/stock snapshot.
Owner decision: quality/safety owner applies current requirements and decides any hold or notification; no recall decision is made.
Boundary: records reconciled only; no action, contact, or disposition performed.
```

Evaluation: parent inputs are not added again after merge; 12 kg is not compared arithmetically to bottle counts; each process uses explicit supplied quantity links; return is netted against its originating shipment and not added again when already included in current stock. X residual: 30−(18+5)=7; Y residual: 20−(10+6)=4. The five unreturned bottles are not described as physically remaining at Oak because no downstream-use/current-state record was supplied. Customer/site identifiers stay masked. Pass.

### 2. Missing-input request

Prompt: “A possibly affected product shipped somewhere. Tell me who received it and whether we need a recall.”

Response produced: ask for the product and lot/serial identifier plus jurisdiction; request the source records that connect receiving/production, transformation, shipment, and return states; ask for the authorized owner/current procedure and permitted trace boundary. Until supplied, provide no destination or recall conclusion.

Evaluation: questions identify the lot, scope/records, jurisdiction, and owner without exceeding three. No silent recall determination. Pass.

### 3. Ambiguous mapping and customer trace

Prompt: “A shipment record lists ‘blue bottle’ and a nearby production date but no lot ID. A notice identifies lot X-4. Can we tell site Cedar this shipment is affected?”

Response produced: keep the shipment as a candidate link, exclude it from confirmed X-4 totals, and request a controlled lot/package/work-order cross-reference. Preserve the shipment reference and mask the site identifier in the working handoff. Do not contact the site; route the decision to the authorized quality/safety owner under the current procedure.

Evaluation: follows the explicit-link rule; similar description/date alone does not establish lot identity. No external communication or recall conclusion. Pass.

### 4. Unknown yield / absent transformation record

Prompt: “Lot K records 10 kg received. A spreadsheet says finished lot K2 contains 40 jars, but no process or parent-child record connects K to K2 and no yield is documented. May I add 40 jars to K's trace total?”

Response produced: no. Keep 10 kg as the confirmed receipt for K and 40 jars as an unlinked candidate observation for K2; do not infer that K produced K2 or convert kg to jars. Request the controlled work-order/lot-link and documented process quantity/yield; retain both stage-specific balances and route unresolved identity to the trace owner.

Evaluation: correct separation of identity, unit, and yield; no unsupported addition. Pass.

## Findings

1. **Genealogy split/merge behavior: pass.** Instructions prevent counting active parent and child balances twice and require explicit links for transformations.
2. **Units and yields: pass.** Conversion is limited to a supplied process record; unknown yield stays unresolved; unlike stages/units are not summed.
3. **Shipment/return/customer trace: pass.** The procedure traces order/shipment references, preserves status, links returns to original movements, and supports masked destination handoff.
4. **Identity uncertainty: pass.** Similar description/date/package label remains a candidate excluded from confirmed totals.
5. **High-risk/authority boundary: pass.** Jurisdiction/current rules and authorized qualified owner are required; recall, notification, hold/release, reporting, destruction, and record changes are not inferred or claimed.
6. **Arithmetic: pass.** Embedded example: 24 kg = 10 + 14; X output 12 = 4 + 6 + residual 2; Y output 18 = 6 + 10 + residual 2. The test's 10 + 12 + 5 = 27 of 30 leaves 3 units without supplied status; its explicit staging exclusion makes the states disjoint. No code snippet was provided to execute.
7. **No blocking findings.** Scope completeness and actual technical/safety disposition remain dependent on source records and qualified owners; this review asserts neither.
