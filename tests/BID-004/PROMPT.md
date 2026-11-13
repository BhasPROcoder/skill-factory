Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: BID-004
name: supplier-invoice-three-record-match-review
domain: Procurement Evidence Decisions
subdomain: Supplier invoice matching
version: 1.0
description: Compare a supplier invoice with the authorized purchase order and receipt evidence to prepare a traceable payment exception handoff before approval.
triggers: ["match a supplier invoice to the purchase order", "check this vendor bill against receipt records", "prepare an accounts payable exception", "review an invoice quantity mismatch", "find duplicate supplier invoices", "reconcile a supplier credit against a bill"]
not_for: ["compare bids before purchase [BID-001]", "decide whether to accept a substitute item [BID-002]", "reconcile physical inbound receipt differences [WHS-003]", "customer receivables disputes [COP-002]", "tax or legal advice"]
requires: []
risk_level: high
---

# Supplier Invoice Three-Record Match Review

## Purpose
Prepare a traceable exception review by comparing a supplier invoice with the authorized purchase commitment and the receiving evidence that supports the billed goods or services. Keep invoice arithmetic, order authorization, receipt status, credits, and payment status separate so a match recommendation does not become an approval or payment. This skill organizes evidence; it does not determine tax treatment, legal rights, accounting policy, or payment authorization.

## Inputs to collect
1. **Entity and context** — paying entity, jurisdiction, relevant period, and whether this is analysis or approval preparation. Why: requirements vary. Default: ask; assume no jurisdiction or authority.
2. **Supplier invoice set** — source invoice, identifier, date/version, lines, units, prices, charges, credits, and currency. Why: establishes billing claims. Default: missing fields and revision links stay unknown.
3. **Authorized purchase record** — approved order, amendments, line identity, unit, price basis, and supplied terms. Why: defines authorized scope. Default: a quote or draft is not approval.
4. **Receipt and acceptance evidence** — transaction state, quantity, inspection/acceptance status, date, and linked line. Why: distinguishes received from accepted. Default: dispatch records alone do not prove acceptance.
5. **Adjustments and payments** — credits, returns, prior invoice versions, payments, and remittance allocations. Why: prevents duplicate charges or offsets. Default: absent evidence is unresolved, not zero.
6. **Current controls and owner** — accounts-payable procedure, authorization limits, hold rules, and approver. Why: determines release authority. Default: recommend review only.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

Do not rely on model memory for current legal, tax, or financial requirements; check authoritative current sources because requirements may have changed. Refer individualized accounting, tax, or legal conclusions to a qualified professional.

## Procedure
1. State the entity, jurisdiction, invoice set, purchase commitment, and receipt period; preserve identifiers and source versions.
2. Compare repeated invoice identifiers and supplier, date, currency, amount, and line references; flag possible duplicates for owner review.
3. Match invoice lines to authorized purchase lines by identity, amendment, unit, and price basis; leave ambiguous mappings unresolved.
4. Compare billed quantities with same-line receipt evidence; keep ordered, billed, received, accepted, returned, and uninspected states distinct.
5. Recompute line extensions and subtotals from supplied quantities/prices; preserve supplier figures and do not invent tolerances.
6. Compare fees, freight, discounts, and credits with supplied order terms and evidence; do not assume customary charges.
7. Link credits, returns, and corrections to their invoice version; do not double-apply a credit or erase prior records.
8. Classify each item as matched, quantity/price exception, receipt unresolved, possible duplicate, credit unresolved, arithmetic difference, or not comparable.
9. ⚠️ Before recommending payment release, check the current AP control and confirm the named approver and evidence of authorization. If absent, prepare a hold/review handoff and do not state that the invoice is payable.
10. Prepare the exception schedule, recomputable calculations, source references, unresolved decisions, and the next owner action. Do not edit the accounting system, approve, transmit, or pay unless the user separately authorizes the action and the authorized workflow is established.

## Decision rules
- IF the invoice refers to a draft order or unapproved change THEN mark the related amount unauthorized or unresolved on the supplied record and route it to the buyer BECAUSE a supplier invoice cannot itself amend the purchase commitment.
- IF billed quantity exceeds accepted receipt quantity THEN show billed, received, accepted, and pending quantities separately and consult supplied partial-payment controls BECAUSE the difference may be an inspection or receipt-state issue rather than proof of supplier error.
- IF a receipt cannot be linked to the invoiced line THEN leave the match open and request an identifier or owner confirmation BECAUSE similar descriptions do not establish that the delivery satisfies this bill.
- IF two invoice records may refer to the same charge THEN preserve both source references and mark a possible duplicate until the responsible reviewer compares status and payment history BECAUSE deleting one could conceal a corrected version or separate shipment.
- IF a credit or return has no reliable link to an invoice line THEN show it as unallocated and do not net it against a convenient balance BECAUSE the amount may belong to another transaction.
- IF an invoice arithmetic difference appears THEN recompute only from the supplied quantity, price basis, and stated charges; label any user-provided tolerance rather than creating a universal threshold BECAUSE false tolerances can hide unauthorized spend.
- IF tax, accounting treatment, contractual entitlement, statutory timing, or legal collection rights affect the decision THEN write `[VERIFY: current rule in the relevant jurisdiction and authoritative tax/accounting/legal source]` and refer individualized conclusions to a qualified accountant, tax professional, or lawyer BECAUSE those requirements are context-dependent and can change.
- IF payment authority or current AP controls are missing THEN return a review handoff, not an approval or payment instruction BECAUSE matching evidence is not payment authorization.

## Output template
```text
Scope: <entity, jurisdiction, invoice/order/receipt versions, and period; up to 3 lines>
Sources: <invoice, authorized order/amendment, receipt/acceptance, adjustments, payment evidence; identify missing records>
Match schedule:
| Invoice line | Authorized order line | Ordered | Billed | Received | Accepted | Credit/return | Difference/status |
|---|---|---:|---:|---:|---:|---:|---|
Arithmetic: <recomputed line extensions and stated subtotal; identify any difference>
Exceptions: <issue | evidence | unresolved question | owner role>
Disposition: <matched for next approval review / hold proposed / unresolved; never imply approval without evidence>
Next gate: <current control or approval needed and completion evidence>
Boundary: <analysis completed; unperformed approval, system edit, transmission, or payment>
Current-rule checks: <[VERIFY: ...] items, or none identified>
```

## Quality checklist
- [ ] Entity and jurisdiction are supplied or explicitly requested
- [ ] Invoice, order amendment, receipt, and adjustment sources are identified by version or status
- [ ] Each billed line is matched to an authorized order line or marked unresolved
- [ ] Billed, ordered, received, accepted, returned, and credited amounts remain distinguishable
- [ ] Arithmetic can be recomputed from displayed quantities and price basis
- [ ] Possible duplicate invoices are preserved for review, not silently removed
- [ ] No tax rate, deadline, tolerance, or accounting treatment is invented
- [ ] A match recommendation is separate from approver authorization and payment execution
- [ ] Current AP controls and applicable professional review are named where needed

## Anti-patterns
- **Receipt equals approval**: treat a warehouse receipt as permission to pay the invoice. Fix: verify acceptance status and current AP authorization separately.
- **Invoice equals order**: let billed quantity, price, or charges replace an authorized purchase line. Fix: preserve the billed value and show the variance against the controlling order record.
- **Net by convenience**: apply an unlinked credit to the nearest open invoice. Fix: keep it unallocated until evidence links it.
- **Duplicate deletion**: remove a repeated invoice without checking versions and payment history. Fix: retain both for owner review.
- **Payment by arithmetic**: mark a correctly summed invoice approved. Fix: route the match schedule to the authorized approver and report payment as unperformed.

## Worked example
**Input:** Fictional workshop Cedar's authorized order line F calls for 20 filter packs at 5 fictional credits per pack, with delivery included. The supplier invoice version A bills 22 packs at 5 credits each and adds 6 credits for delivery. The receipt record shows 20 packs received and accepted. No amendment, credit, duplicate-payment check, tax breakdown, or payment approval is supplied.

**Output:**
```text
Scope: Cedar, jurisdiction not supplied, invoice A versus order F and the supplied receipt record; approval review only.
Sources: Invoice A; authorized order F; receipt record for 20 accepted packs. Amendment, credit, duplicate/payment history, tax detail, and current AP controls are absent.
Match schedule:
| Invoice line | Authorized order line | Ordered | Billed | Received | Accepted | Credit/return | Difference/status |
| Filter packs | F | 20 | 22 | 20 | 20 | none supplied | 2 extra billed packs; quantity exception |
Arithmetic: Invoice line 22 × 5 = 110 credits. Order line 20 × 5 = 100 credits. Difference before other treatment: 10 credits for the extra two packs. Invoice also lists 6 credits delivery while supplied order says delivery included; charge exception, not silently netted.
Exceptions: Quantity and delivery charge | order, invoice, and receipt records above | Was an authorized amendment issued and is the delivery charge permitted under the controlling terms? | buyer/AP approver
Disposition: Hold proposed pending order-term and amendment review; no payment approval evidenced.
Next gate: Authorized buyer confirms any amendment and AP owner checks current payment controls; record approval evidence before release.
Boundary: Records compared only; no accounting system edit, supplier contact, approval, tax determination, or payment performed.
Current-rule checks: [VERIFY: Cedar's current AP controls and any jurisdiction-specific tax/accounting treatment before payment processing]
```

**Bad output:** “Pay 116 credits because the invoice total is 22 × 5 plus 6.”

Fails because it ignores the order quantity and included-delivery term, omits the receipt match, and treats arithmetic as payment authority.

## Edge cases
- **Several partial receipts**: keep each receipt event and version separate, then aggregate only quantities that refer to the same authorized line and unit.
- **Corrected invoice arrives**: retain both versions, identify which one the supplier says supersedes the other, and check whether the earlier version was already approved or paid.
- **Invoice groups multiple orders**: split the match schedule by order and line; leave any unallocated charge visible rather than distributing it without a supplied basis.
- **Goods are received but inspection is pending**: keep receipt and acceptance separate; ask the owner to apply the current hold rule.
- **Foreign currency or uncertain tax line**: preserve the source currency and amount; request the approved comparison basis and qualified review.

## Test case
**Input:**
> Fictional entity Fern in a jurisdiction I have not named ordered 8 filter packs at 4 fictional credits each. Its supplier invoice version A bills 9 packs at that price. The receipt record shows 8 received, with inspection complete and accepted. Delivery is listed as an extra charge, while the supplied order says delivery included. No amendment, payment history, AP authorization, or tax details are provided. Prepare an exception review.

**Assertions:**
1. The result asks for or explicitly records the missing entity jurisdiction and does not infer tax treatment.
2. It computes the order line as 8 × 4 = 32 credits and invoice line as 9 × 4 = 36 credits, showing a 4-credit quantity difference.
3. It treats delivery as a separate exception against the supplied included-delivery term.
4. It keeps accepted receipt evidence separate from invoice match and payment authorization.
5. It proposes no approval or payment and names the current AP owner/control as the next gate.
</skill>

<user_request>
Fictional entity Fern in a jurisdiction I have not named ordered 8 filter packs at 4 fictional credits each. Its supplier invoice version A bills 9 packs at that price. The receipt record shows 8 received, with inspection complete and accepted. Delivery is listed as an extra charge, while the supplied order says delivery included. No amendment, payment history, AP authorization, or tax details are provided. Prepare an exception review.
</user_request>
