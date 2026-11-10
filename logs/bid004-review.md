# Independent behavioral review: BID-004

Reviewer: independent agent pass  
Artifact: `skills/BID/supplier-invoice-three-record-match-review/SKILL.md`  
Scope: compare actual neighboring procedures and text-evaluate the embedded test plus ordinary, missing-input, and duplicate-credit requests. No real invoice, tax rule, accounting ledger, AP policy, or payment system was inspected.

## Catalog comparison

- **BID-001 normalize-purchase-bid-scope-and-units** compares competing offers against common demand, package units, exclusions, and purchase conditions before award. BID-004 starts after an authorized purchase commitment exists and matches billed quantities/prices/charges against that commitment, receipt, credits, and payment history.
- **BID-002 supplier-substitution-disposition** compares a proposed alternate item against requirements and routes exception/receiving authority. BID-004 may see an item mismatch but does not decide product substitution.
- **BID-003 tender-addendum-impact-reconciliation** traces request changes into bid drafts and sign-offs. BID-004 reconciles supplier billing against the authorized order and receipt rather than tender response revisions.
- **COP-002 receivables-exception-resolution** handles money owed to the user by a customer: receipt allocation, disputes, due-date assumptions, and collection actions. BID-004 concerns the opposite transaction direction—supplier accounts payable—and provides a line-level order/invoice/receipt arithmetic schedule. Some evidence caution overlaps, but the decision, control owner, and matching artifact materially differ.
- **WHS-003 inbound-receipt-variance-disposition** resolves what the receiving site observed versus order/dispatch/carrier evidence before receipt disposition. BID-004 consumes receipt/acceptance evidence as one leg of a later payment exception review; it adds invoice versions, price basis, credits, prior payment, and AP authorization. It does not replace WHS-003's physical receipt workflow.
- **Finding:** The three-record payables match and exception schedule is sufficiently distinct. High-risk treatment is warranted and present: no jurisdiction default, current legal/tax/accounting checks, qualified professional boundary, and no approval/payment authority inferred.

## Executed text evaluations

### 1. Embedded test case

Input: fictional entity Fern in an unnamed jurisdiction; order is 8 filter packs at 4 fictional credits each; invoice A bills 9 at that price; receipt shows 8 received and accepted; delivery charge is extra although order says included; amendment, payment history, AP authorization, and tax detail are missing.

Response produced:

```text
Scope: Fern; jurisdiction not supplied; invoice A, supplied order, and receipt; exception review only.
Sources: Order and invoice A supplied; accepted receipt for 8 packs supplied; amendment, payment history, AP authorization, and tax detail absent.
Match schedule:
| Invoice line | Authorized order line | Ordered | Billed | Received | Accepted | Credit/return | Difference/status |
| Filter packs | filter line | 8 packs | 9 packs | 8 packs | 8 packs | none supplied | 1 pack over billed; quantity exception |
Arithmetic: Order 8 × 4 = 32 fictional credits. Invoice 9 × 4 = 36 fictional credits. Difference on quantity-priced line = 4 fictional credits. Delivery is a separate charge exception against the supplied included-delivery term; no charge value supplied for recomputation.
Exceptions: Quantity/delivery | supplied order, invoice, receipt | Is there an authorized amendment or separate term allowing the delivery charge? | buyer/AP owner.
Disposition: Hold proposed for approval review; not approved or payable on the supplied evidence.
Next gate: Confirm entity jurisdiction, resolve the amendment/charge question, and obtain the current AP control plus named approver's authorization evidence.
Boundary: Evidence review only; no system edit, external contact, approval, tax determination, or payment performed.
Current-rule checks: [VERIFY: current AP procedure; jurisdiction-specific tax/accounting rules from an authoritative source or qualified professional]
```

Assertions: 1 pass; jurisdiction remains missing, and no tax treatment is inferred. 2 pass; arithmetic is correct (8×4=32; 9×4=36; difference=4). 3 pass; delivery is separately compared with the included-delivery term. 4 pass; accepted receipt does not equal payment authorization. 5 pass; no payment or approval is proposed. No current rate, deadline, threshold, citation, or legal conclusion is invented.

### 2. Ordinary request

Prompt: “Fictional maker Moss ordered 12 replacement seals at 3 fictional credits each, delivery included. Its invoice bills 12 at 3 and adds 5 for delivery. Receipt shows 12 received, inspection pending. No tax or payment record was supplied. Should I pay it?”

Response produced: line extension matches on the supplied order/invoice, but delivery is a separate exception against the included-delivery term and receipt is not yet accepted. Preserve the 5-credit charge rather than netting or declaring it payable. Ask for current AP controls, approval authority, payment history, and jurisdiction-specific tax review. Recommend a hold/review handoff, not payment.

Evaluation: appropriate separation of invoice arithmetic, receipt versus acceptance, terms, and payment authority. Pass.

### 3. Missing-input request

Prompt: “Please clear this supplier invoice.”

Response produced: “Which paying entity and jurisdiction, and is this an analysis or approval-preparation request? Please provide the invoice/version and authorized order/amendments plus linked receipt/acceptance record. Are there credits/returns, prior invoice versions or payments, and what current AP control and named approver should govern the next gate?”

Evaluation: three concise questions cover entity/jurisdiction, matching sources, and adjustments/payment/control/owner. It does not infer authority or amounts. Pass.

### 4. Edge request: duplicate credit reference

Prompt: “Fictional buyer Alder has invoice A for 100 fictional credits. Corrected invoice B for 90 references A and says ‘credit C applied.’ A separate AP export also lists credit C for 10, but no status or payment/remittance record explains whether it was posted. The requester asks to subtract C from B and mark the balance 80.”

Response produced: preserve A, B, and both credit-C records with their source identifiers; classify B as a corrected version only to the extent the supplied source says so, and mark the standalone credit's posting/application status unresolved. Do not net C again against B or declare a payable balance of 80. Request the credit memo/version linkage and AP posting/payment history; route the result to the AP owner/approver under current controls.

Evaluation: follows procedure 7 and the rule not to double-apply an unlinked credit; resists the requested unsupported subtraction. Pass.

## Findings

1. **Distinctness: pass.** This is a supplier-payables matching workflow, not competitive bid normalization, customer receivables collection, tender revision tracking, product substitution, or physical receipt investigation.
2. **Financial boundary: pass.** Jurisdiction has no silent default; tax/accounting/legal matters require current authoritative checks or qualified professionals. Matching is not payment approval, and the skill prohibits system edits, transmission, and payment absent separately established authorization.
3. **Arithmetic: pass.** Both fictional worked/test examples recompute exactly: 22×5=110 versus 20×5=100, difference 10; 8×4=32 versus 9×4=36, difference 4. Delivery charge is kept separate from line arithmetic.
4. **Duplicate-credit behavior: pass.** The written procedure and decision rules directly prevent applying an unlinked credit twice and preserve corrected invoice versions for payment-history review.
5. **Minor clarity suggestion:** add explicit unit and currency/basis columns or instructions in the output table so a multi-line schedule cannot omit units when the line description is abbreviated. The current inputs, arithmetic field, and examples otherwise demonstrate the units and fictional currency correctly. This is not a blocking issue.
6. **No blocking findings.** This review does not validate any real AP control, invoice entitlement, tax position, or payable status.
