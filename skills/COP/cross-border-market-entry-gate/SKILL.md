---
id: COP-011
name: cross-border-market-entry-gate
domain: Venture Operations Preparation
subdomain: Transaction preparation
version: 1.0
description: Prepare a cross-border market-entry gate from supplied evidence when the decision concerns target customer evidence.
triggers: ["cross-border market-entry gate", "prepare cross-border market-entry gate", "review my cross-border market-entry gate", "help with cross border market entry gate", "organize target customer evidence"]
not_for: ["Map campaign audience and messages [MCA-002]", "Review operational capacity [BPL-003]"]
requires: []
risk_level: high
---

# Cross-border market-entry gate

## Purpose
Produce a cross-border market-entry gate that supports a bounded decision from traceable evidence. Separate a proposed action from an approved commitment and from a completed outcome, so the requester can use the artifact without assuming that missing steps already happened.

## Inputs to collect
1. **Working evidence** — collect target customer evidence; delivery and support model; operating jurisdictions; payment and compliance constraints; these determine what can be established. Default: unavailable items remain unknown rather than being reconstructed from memory.
2. **Decision and recipient** — identify who uses the output and what they can decide. Default: the requester reviewing a private draft, without authority to bind another party.
3. **Constraints and context** — collect the scope, jurisdiction where relevant, current stage, timing constraints, and authorized access. Default: no external action and no invented urgency.
4. **Completion evidence** — ask what would demonstrate that the task is complete rather than merely attempted. Default: a reviewable artifact and a visible list of unresolved prerequisites.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only independent preparation; label any dependent conclusion provisional and identify what would resolve it.

## Procedure
1. State the requested decision and the evidence boundary in a sentence before interpreting the records.
2. Define the specific destination segment and evidence of its need instead of assuming foreign demand.
3. Map the complete customer journey across discovery, contracting, delivery, support, billing, and exit.
4. Identify where language, time zones, data handling, payment availability, and local requirements change the operating model.
5. Separate demand tests from obligations that must be resolved before live delivery.
6. Compare a bounded market pilot with the capacity and verified constraints of the current operation.
7. Write a go, revise, or defer gate with evidence needed to revisit it.
8. ⚠️ Trace each statement in the proposed artifact to an input, an explicitly labeled proposal, or a verification question; remove unsupported facts rather than making the draft sound more complete.
9. Apply the task boundary below before presenting a recommendation that depends on external requirements.
10. Produce the concrete artifact and identify its next decision owner; retain missing evidence and disagreement instead of presenting a neat but false conclusion.

Collect the jurisdiction, relevant entities, transaction stage, and governing context before interpreting legal, tax, financial, or privacy requirements; there is no silent default. Model knowledge has a cutoff. Check current law and requirements with the responsible official authority and the applicable authoritative records. Use `[VERIFY: the exact requirement and responsible official source]` when that check is unavailable. Refer individualized legal or tax conclusions to a licensed professional qualified in the jurisdiction, and financial decisions to an appropriately qualified adviser. Do not invent citations, deadlines, tax rates, entitlement, enforceability, or approval probabilities.

Use evidence labels that another reader can locate in the supplied materials. If a source is only a summary, preserve that limitation; do not represent an inferred original document as inspected. Distinguish the dates of events, records, and your review when they differ. A later message may change the state without erasing the earlier record. Where quantities matter, keep the unit, period, and denominator visible and recompute calculations from the actual inputs before saving. No benchmark, rate, threshold, or customary term is introduced merely because it sounds familiar.

## Decision rules
- IF demand evidence is absent THEN plan a bounded learning step before a full launch BECAUSE a higher advertised price does not establish a viable market.
- IF support coverage depends on unavailable staff THEN revise delivery promises BECAUSE geographic reach does not create service capacity.
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
- **Shortcut**: treating currency differences as guaranteed margin without considering delivery obligations. Fix: apply the task-specific evidence check before choosing the action.
- **False completion**: treating a prepared record as received, accepted, or approved. Fix: retain the actual state and required confirmation.
- **Borrowed certainty**: copying a source workflow's numbers or local custom as a universal rule. Fix: replace it with a contextual input or current-source verification.
- **Unowned next step**: listing actions without a responsible role. Fix: identify who can resolve the particular gap and what evidence closes it.
- **Hidden expansion**: moving from organization of evidence into unauthorized commitment or transmission. Fix: separate the draft from the decision and execution steps.

## Worked example
**Input:**
> Fictional Elm Support has an inquiry from a customer abroad but cannot cover the customer preferred live-support hours. Payment-provider eligibility and data-transfer requirements are unverified.

**Output:**
```text
Scope: Prepare cross-border market-entry gate for this fictional case using only the supplied facts.
Evidence: The fictional input above; omitted records and current external requirements remain unverified.
Decision: Use the bounded disposition in the artifact; do not treat unresolved prerequisites as satisfied.
Artifact: Gate: revise before live commitment. Demand: one inquiry, not proven segment demand. Delivery option: propose explicitly agreed asynchronous support and test whether it meets the customer need.
Blocking checks: provider eligibility for the actual parties; applicable contracting and data-handling requirements; owner approval of support promises.
Pilot success evidence: customer accepts the revised service model and the verified prerequisites are satisfied. No universal destination or price is recommended.
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
> Fictional agency wants to promise continuous support in a new market without staff coverage or verified payment eligibility.

**Assertions:**
1. The response uses Scope, Evidence, Decision, Artifact, Next action, and Unresolved in that order.
2. It applies the task-specific evidence distinction rather than returning only generic advice.
3. It produces the concrete draft or record while preserving the missing prerequisite.
4. It does not invent current requirements, approval, external execution, or a completed result.
