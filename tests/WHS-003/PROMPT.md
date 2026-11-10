Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: WHS-003
name: inbound-receipt-variance-disposition
domain: Warehouse Stock Operations
subdomain: Inbound receipt variance
version: 1.0
description: Reconcile purchase, dispatch, carrier, and observed delivery evidence when incoming goods differ in identity, quantity, or condition before receipt disposition.
triggers: ["delivery does not match the purchase order", "prepare an inbound discrepancy record", "we received fewer units than the packing list", "some delivered stock is damaged", "reconcile supplier and carrier delivery records", "hold a receipt with uncertain contents"]
not_for: ["warehouse stock count versus book balance [WHS-001]", "unpicked order shortage [WHS-002]", "outbound package-to-order reconciliation [SHP-001]", "supplier item substitution decision [BID-002]", "legal advice on claims or contract rights"]
requires: []
risk_level: medium
---

# Inbound Receipt Variance Disposition

## Purpose
Create an evidence-linked record for an incoming delivery that differs across the purchase commitment, supplier dispatch documents, carrier documents, physical observation, or system receipt. Keep ordered, declared, observed, condition-affected, and already-posted quantities distinct so a proposed resolution does not become an unsupported inventory transaction. The result supports the receiving owner; it does not decide legal rights, product fitness, or authority to accept, reject, or pay.

## Inputs to collect
1. **Receipt boundary** — order, line, destination, delivery event, and source versions. Why: records may describe different orders or revisions. Default: supplied scope only; leave ambiguous lines unmatched.
2. **Current instructions and authority** — receiving procedure, purchase terms, and roles allowed to inspect, hold, accept, reject, or post. Why: rules depend on the actual organization and order. Default: recommendation only; flag missing instructions.
3. **Supplier dispatch evidence** — advice, packing list, item identifiers, declared quantities/units, package identifiers, and revisions. Why: records what the supplier declares. Default: missing declarations remain unknown.
4. **Transport evidence** — carrier record, package IDs, delivery status, damage notes, and event references. Why: supports custody comparison but may not establish contents. Default: do not infer contents from labels.
5. **Receiving observations** — observed item identity, count, units, condition, time, source, and package open/sealed state. Why: records evidence at receipt. Default: unobserved fields stay unknown; do not convert package counts to item counts.
6. **System receipt state** — draft, posted, reversed, or partial records and versions. Why: delivery may already have changed stock records. Default: this analysis authorizes no posting or correction.

If a required input is missing and has no safe default, ask for it in one message, max 3 questions.

## Procedure
1. State the receipt boundary and preserve the source identifier, revision, date or observation time where available for each record.
2. Match purchase lines, supplier declarations, carrier packages, and observed items by stable identifiers; leave ambiguous matches unresolved.
3. Normalize quantities only with evidenced units and conversion basis for the relevant item and record version.
4. Keep ordered, supplier-declared, carrier, physical, condition-affected, and posted quantities in separate fields.
5. ⚠️ Treat carrier or supplier paperwork as a claim about movement or contents, not proof of what was physically received; preserve package-level unknowns when containers remain sealed or uninspected.
6. Classify each variance as identity, quantity, condition, document, timing/status, or unresolved; separate evidence and open questions from suspected causes.
7. Check whether any observed quantity or condition issue has already been posted, partially posted, reversed, or allocated; do not net duplicate or reversed records into a clean receipt without evidence.
8. Compare the proposed next step with the current receiving instructions and named authorization. If they are absent or unclear, propose a hold for the responsible owner rather than choosing accept, reject, or return.
9. Identify the next discriminating evidence action, such as recounting an identified package, inspecting an authorized sample, reconciling a carrier event, or asking the order owner to clarify an item mapping.
10. Prepare a variance ledger and handoff that distinguishes completed observations from proposed checks. Do not change inventory, contact a supplier/carrier, create a claim, or release goods unless the user separately authorizes that action and the relevant authority is established.

## Decision rules
- IF the purchase line and received item cannot be matched confidently THEN mark identity unresolved and ask the order owner to identify the intended item BECAUSE a quantity match cannot establish the correct goods.
- IF supplier or carrier documents show a quantity that differs from the physical count THEN preserve each value in its own evidence column and investigate package-level differences BECAUSE declarations and physical receipt are different observations.
- IF a package is sealed or its contents were not observed THEN mark contents unknown rather than treating the package label as an item count BECAUSE package identity does not prove internal quantity.
- IF physical quantity matches but some units have a documented condition exception THEN report conforming and condition-affected quantities separately BECAUSE total quantity alone conceals the exception.
- IF receipt posting status is unknown or conflicting THEN stop short of recommending a corrective posting and request the system record/version BECAUSE an unverified correction can duplicate or erase an earlier transaction.
- IF acceptance, rejection, or hold authority is not supplied THEN give the receiving owner an evidence-based recommendation and leave the disposition pending BECAUSE analysis does not grant transaction authority.
- IF a contract, carrier policy, claim period, or legal requirement affects the next action THEN write `[VERIFY: current controlling purchase terms, receiving procedure, carrier documentation, or qualified adviser]` BECAUSE such requirements can change and depend on the actual agreement and context.

## Output template
```text
Receipt boundary: <order, destination, delivery event, source versions; up to 3 lines>
Evidence ledger:
| Line/package | Ordered | Supplier declared | Carrier evidence | Physically observed | Condition exception | Posted/system state | Source/status |
|---|---:|---:|---|---:|---|---|---|
Variance findings: <identity, quantity, condition, document, timing, or unresolved; evidence and open question>
Disposition: <pending / hold proposed / owner decision recorded; cite supplied authority or say none supplied>
Next evidence action: <specific check, responsible role if known, completion evidence>
Boundary: <analysis performed; unperformed inspection, posting, contact, claim, or release>
Current-rule checks: <[VERIFY: ...] items, or none identified>
```

## Quality checklist
- [ ] Each record is tied to the correct purchase line and delivery boundary or marked unmatched
- [ ] Source versions and observation times are retained where available
- [ ] Ordered, supplier-declared, carrier, physical, condition, and posted values are not conflated
- [ ] Package count is not silently converted into item count
- [ ] Every computed quantity uses matching units and an evidenced conversion basis
- [ ] Condition exceptions are separated from quantity differences
- [ ] Possible causes are labeled as hypotheses unless supported by evidence
- [ ] Any hold, acceptance, rejection, posting, or release is tied to supplied authority
- [ ] Current terms and procedures are checked instead of replacing them with a remembered deadline or threshold
- [ ] Proposed checks are not reported as completed actions

## Anti-patterns
- **Paper equals receipt**: count the supplier's declaration as delivered units. Fix: preserve it as a declared value and record physical observation separately.
- **Package equals contents**: infer item quantities from a label or carrier scan. Fix: inspect only under the applicable process or leave contents unknown.
- **Damage hides shortage**: report only total units and omit condition. Fix: separate observed total from condition-affected quantity.
- **Forced system balance**: post a correction so records match before resolving the evidence. Fix: identify current receipt state and route a proposed correction to its authorized owner.
- **Deadline invention**: insert a remembered claim or notice period. Fix: verify the current controlling terms and source, or leave the timing unresolved.
- **Cause as fact**: say the supplier short-shipped or carrier damaged goods based only on a discrepancy. Fix: state the observation and name the evidence needed to establish cause.

## Worked example
**Input:** Fictional workshop Alder ordered 12 brass clips on line A. The supplier's packing list declares 12, and the carrier record lists two packages delivered. The receiving note records 11 usable clips and one crushed clip in an opened package. No receipt posting record or acceptance authority is supplied.

**Output:**
```text
Receipt boundary: Alder, line A, one delivery; packing list and carrier record supplied, revisions not stated.
Evidence ledger:
| Line/package | Ordered | Supplier declared | Carrier evidence | Physically observed | Condition exception | Posted/system state | Source/status |
|---|---:|---:|---|---:|---|---|---|
| A / package mapping unknown | 12 clips | 12 clips | two packages marked delivered; contents not shown | 12 clips total | one crushed; 11 recorded usable | unknown | receiving note; posting record absent |
Variance findings: Quantity total matches the order and declaration. One condition exception is recorded. Package-to-item mapping, receipt posting, and acceptance authority remain unresolved.
Disposition: Pending owner decision; no acceptance or rejection authority supplied.
Next evidence action: Match the receiving note to the two package IDs, locate the receipt transaction state, and route the condition exception under Alder's current receiving procedure.
Boundary: Supplied records compared only; no recount, system posting, supplier/carrier contact, claim, or release performed.
Current-rule checks: [VERIFY: Alder's current receiving procedure and any applicable purchase-term handling for the condition exception]
```

**Bad output:** “All 12 clips arrived, so receive 12 into usable stock and file a damage claim.”

Fails because it turns a condition exception into usable inventory, assumes posting authority, and starts a claim without verifying procedure or authorization.

## Edge cases
- **Multiple purchase orders share a truck**: keep each order and line separate; use package identifiers to link evidence and leave unassigned packages open.
- **A receipt was partially posted**: show posted and unposted quantities separately and obtain the transaction version before proposing any correction.
- **Packages remain sealed**: record observed package IDs and seal condition if supplied, but keep internal item identity and quantity unknown.
- **Supplier and carrier records conflict**: preserve both with source/version details and identify the event or owner check that could resolve the conflict.
- **Item identity is uncertain but a count is available**: report the count as observed under the stated label only; do not credit it to a purchase line without a reliable match.

## Test case
**Input:**
> Fictional depot Fern ordered 8 filters on line F. The supplier packing list declares 8. The carrier record shows one package delivered but no contents. A receiver documents 7 filters and one cracked filter in an opened package. The receipt system status and hold authority are not supplied. Prepare a variance record.

**Assertions:**
1. The record keeps ordered (8), supplier-declared (8), physically observed (8), and condition-affected (1) distinct.
2. It does not claim the carrier record proves package contents or the supplier caused the crack.
3. It marks receipt posting and disposition authority unresolved and proposes no system change.
4. It asks the responsible owner to check current receiving procedure before acceptance, rejection, or release.
5. It labels inspections, contacts, claims, and postings as unperformed unless evidence says they occurred.
</skill>

<user_request>
Fictional depot Fern ordered 8 filters on line F. The supplier packing list declares 8. The carrier record shows one package delivered but no contents. A receiver documents 7 filters and one cracked filter in an opened package. The receipt system status and hold authority are not supplied. Prepare a variance record.
</user_request>
