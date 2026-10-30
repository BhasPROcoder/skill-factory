---
id: COP-002
name: receivables-exception-resolution
domain: Venture Operations Preparation
subdomain: Operating records
version: 1.0
description: Prepare a receivables exception resolution from supplied evidence when the decision concerns invoice and delivery evidence.
triggers: ["receivables exception resolution", "prepare receivables exception resolution", "review my receivables exception resolution", "help with receivables exception resolution", "organize invoice and delivery evidence"]
not_for: ["Map payment obligations from contract wording [CTR-002]", "Prepare a contract negotiation issue list [CTR-003]"]
requires: []
risk_level: high
---

# Receivables exception resolution

## Purpose
Produce a receivables exception resolution that supports a bounded decision from traceable evidence. Separate a proposed action from an approved commitment and from a completed outcome, so the requester can use the artifact without assuming that missing steps already happened.

## Inputs to collect
1. **Working evidence** — collect invoice and delivery evidence; agreed payment terms; payment and credit records; customer dispute or remittance message; these determine what can be established. Default: unavailable items remain unknown rather than being reconstructed from memory.
2. **Decision and recipient** — identify who uses the output and what they can decide. Default: the requester reviewing a private draft, without authority to bind another party.
3. **Constraints and context** — collect the scope, jurisdiction where relevant, current stage, timing constraints, and authorized access. Default: no external action and no invented urgency.
4. **Completion evidence** — ask what would demonstrate that the task is complete rather than merely attempted. Default: a reviewable artifact and a visible list of unresolved prerequisites.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only independent preparation; label any dependent conclusion provisional and identify what would resolve it.

## Procedure
1. State the requested decision and the evidence boundary in a sentence before interpreting the records.
2. Reconcile the invoice against delivery, credits, receipts, and the customer reference.
3. Classify the unpaid item as timing, missing paperwork, disputed delivery, allocation uncertainty, or another evidenced cause.
4. Separate an actual overdue obligation from an unverified due-date assumption.
5. Identify the person who can resolve the specific exception and prepare a factual request.
6. Compare any proposed suspension, interest, or collection action with the supplied agreement and current applicable requirements.
7. Record a resolution only when the payment allocation or agreed dispute outcome is evidenced.
8. ⚠️ Trace each statement in the proposed artifact to an input, an explicitly labeled proposal, or a verification question; remove unsupported facts rather than making the draft sound more complete.
9. Apply the task boundary below before presenting a recommendation that depends on external requirements.
10. Produce the concrete artifact and identify its next decision owner; retain missing evidence and disagreement instead of presenting a neat but false conclusion.

Collect the jurisdiction, relevant entities, transaction stage, and governing context before interpreting legal, tax, financial, or privacy requirements; there is no silent default. Model knowledge has a cutoff. Check current law and requirements with the responsible official authority and the applicable authoritative records. Use `[VERIFY: the exact requirement and responsible official source]` when that check is unavailable. Refer individualized legal or tax conclusions to a licensed professional qualified in the jurisdiction, and financial decisions to an appropriately qualified adviser. Do not invent citations, deadlines, tax rates, entitlement, enforceability, or approval probabilities.

Use evidence labels that another reader can locate in the supplied materials. If a source is only a summary, preserve that limitation; do not represent an inferred original document as inspected. Distinguish the dates of events, records, and your review when they differ. A later message may change the state without erasing the earlier record. Where quantities matter, keep the unit, period, and denominator visible and recompute calculations from the actual inputs before saving. No benchmark, rate, threshold, or customary term is introduced merely because it sounds familiar.

## Decision rules
- IF a receipt cannot be matched to an invoice THEN hold the item as allocation unresolved BECAUSE an unmatched receipt does not prove that a particular invoice is unpaid.
- IF the customer disputes acceptance THEN route the acceptance evidence before threatening enforcement BECAUSE a payment reminder does not resolve the underlying dispute.
- IF two records conflict THEN preserve both and name the evidence needed to reconcile them BECAUSE silently preferring one can change the decision without justification.
- IF the requester wants an external action THEN distinguish this preparation artifact from execution and check the actual authority BECAUSE a proposed workflow does not itself authorize disclosure, payment, filing, or commitment.

## Output template
```text
Scope: <one sentence naming the decision and boundaries>
Evidence: <up to four supplied records and their limitations>
Decision: <supported disposition, with uncertainty stated>
Artifact: <the actual register, draft, comparison, or protocol; up to twelve concise entries>
Next action: <owner role, concrete action, and completion evidence>
Unresolved: <up to three questions or current-source checks>
```
Keep the first response within the requested scope. Use enough detail to carry out the next action, but do not replace missing source material with a long generic checklist. If the evidence supports only preparation, name the output a draft or provisional review. Present sensitive identifiers as masked references when full values are unnecessary for review.

## Quality checklist
- [ ] The scope identifies a decision rather than only a broad topic.
- [ ] Each factual statement is traceable to supplied evidence.
- [ ] Proposed steps and completed events have different labels.
- [ ] The task-specific conditional branches are reflected in the disposition.
- [ ] Any current external requirement has a source check or remains unresolved.
- [ ] The artifact contains usable content rather than a promise to create it later.
- [ ] The next action identifies a role and observable completion evidence.
- [ ] Any arithmetic uses the supplied units, period, and denominator.

## Anti-patterns
- **Shortcut**: treating every outstanding ledger row as deliberate refusal to pay. Fix: apply the task-specific evidence check before choosing the action.
- **False completion**: treating a prepared record as received, accepted, or approved. Fix: retain the actual state and required confirmation.
- **Borrowed certainty**: copying a source workflow's numbers or local custom as a universal rule. Fix: replace it with a contextual input or current-source verification.
- **Unowned next step**: listing actions without a responsible role. Fix: identify who can resolve the particular gap and what evidence closes it.
- **Hidden expansion**: moving from organization of evidence into unauthorized commitment or transmission. Fix: separate the draft from the decision and execution steps.

## Worked example
**Input:**
> Fictional Finch Studio has an invoice with a supplied due date that has passed. Its bank record shows a receipt with an unclear reference. The customer says payment was sent, and no suspension clause is provided.

**Output:**
```text
Scope: Prepare receivables exception resolution for this fictional case using only the supplied facts.
Evidence: The fictional input above; omitted records and current external requirements remain unverified.
Decision: Use the bounded disposition in the artifact; do not treat unresolved prerequisites as satisfied.
Artifact: Exception: allocation unresolved, not confirmed nonpayment. Evidence: overdue invoice plus unmatched bank receipt and customer statement.
Draft request: Please confirm the invoice reference covered by your transfer so we can reconcile our records. We have a receipt that may relate to it and do not want to duplicate the request.
Owner: accounts reviewer matches the remittance to the invoice and records any remaining balance. No penalty or service suspension is proposed without verified authority.
Next action: The responsible requester reviews the artifact, obtains the specifically identified missing evidence, and records the resulting decision before any external execution.
Unresolved: Confirm the current authoritative requirements and any missing permissions identified in the artifact; do not substitute a remembered default.
```

**Bad output:**
> All requirements are satisfied; proceed immediately using standard terms.

This fails because the input does not establish complete evidence or authority. It bypasses the task-specific uncertainty and converts an organizing draft into an unsupported approval.

## Edge cases
- **Incomplete original records**: use the supplied excerpts for provisional organization and request the missing passage that controls the decision.
- **An urgent request**: identify the smallest safe preparation step and the unresolved blocker; urgency does not prove authority or change an unknown fact.
- **A source changes during review**: record the new version, revisit affected conclusions, and preserve the earlier decision history without silently overwriting it.
- **The user cannot resolve a gap**: state which limited artifact remains useful and which conclusion cannot responsibly be reached.

## Test case
**Input:**
> Fictional supplier sees a late invoice and a possible duplicate receipt, then asks for a threatening final notice; resolve the allocation question first.

**Assertions:**
1. The response uses Scope, Evidence, Decision, Artifact, Next action, and Unresolved in that order.
2. It applies the task-specific evidence distinction rather than returning only generic advice.
3. It produces the concrete draft or record while preserving the missing prerequisite.
4. It does not invent current requirements, approval, external execution, or a completed result.
