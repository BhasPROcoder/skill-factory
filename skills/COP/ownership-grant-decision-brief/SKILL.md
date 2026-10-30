---
id: COP-004
name: ownership-grant-decision-brief
domain: Venture Operations Preparation
subdomain: Transaction preparation
version: 1.0
description: Prepare a ownership grant decision brief from supplied evidence when the decision concerns proposed recipient and contribution.
triggers: ["ownership grant decision brief", "prepare ownership grant decision brief", "review my ownership grant decision brief", "help with ownership grant decision brief", "organize proposed recipient and contribution"]
not_for: ["Compare general strategic options [BST-004]", "Review negotiated contract clauses [CTR-003]"]
requires: []
risk_level: high
---

# Ownership grant decision brief

## Purpose
Produce a ownership grant decision brief that supports a bounded decision from traceable evidence. Separate a proposed action from an approved commitment and from a completed outcome, so the requester can use the artifact without assuming that missing steps already happened.

## Inputs to collect
1. **Working evidence** — collect proposed recipient and contribution; current ownership records; intended instrument; approval and jurisdiction context; these determine what can be established. Default: unavailable items remain unknown rather than being reconstructed from memory.
2. **Decision and recipient** — identify who uses the output and what they can decide. Default: the requester reviewing a private draft, without authority to bind another party.
3. **Constraints and context** — collect the scope, jurisdiction where relevant, current stage, timing constraints, and authorized access. Default: no external action and no invented urgency.
4. **Completion evidence** — ask what would demonstrate that the task is complete rather than merely attempted. Default: a reviewable artifact and a visible list of unresolved prerequisites.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only independent preparation; label any dependent conclusion provisional and identify what would resolve it.

## Procedure
1. State the requested decision and the evidence boundary in a sentence before interpreting the records.
2. Separate the commercial reason for a proposed grant from the legal instrument used to implement it.
3. Record existing ownership, reserved interests, and unresolved capitalization records before discussing dilution.
4. Describe expected contribution and evidence of performance without converting a subjective score into a legal entitlement.
5. Compare staged commitment, cash compensation, or a proposed ownership grant against the actual purpose.
6. List vesting, departure, transfer, exercise, approval, and tax questions for qualified advisers using current source requirements.
7. Write a decision brief that distinguishes negotiated intentions from authorized and executed grants.
8. ⚠️ Trace each statement in the proposed artifact to an input, an explicitly labeled proposal, or a verification question; remove unsupported facts rather than making the draft sound more complete.
9. Apply the task boundary below before presenting a recommendation that depends on external requirements.
10. Produce the concrete artifact and identify its next decision owner; retain missing evidence and disagreement instead of presenting a neat but false conclusion.

Collect the jurisdiction, relevant entities, transaction stage, and governing context before interpreting legal, tax, financial, or privacy requirements; there is no silent default. Model knowledge has a cutoff. Check current law and requirements with the responsible official authority and the applicable authoritative records. Use `[VERIFY: the exact requirement and responsible official source]` when that check is unavailable. Refer individualized legal or tax conclusions to a licensed professional qualified in the jurisdiction, and financial decisions to an appropriately qualified adviser. Do not invent citations, deadlines, tax rates, entitlement, enforceability, or approval probabilities.

Use evidence labels that another reader can locate in the supplied materials. If a source is only a summary, preserve that limitation; do not represent an inferred original document as inspected. Distinguish the dates of events, records, and your review when they differ. A later message may change the state without erasing the earlier record. Where quantities matter, keep the unit, period, and denominator visible and recompute calculations from the actual inputs before saving. No benchmark, rate, threshold, or customary term is introduced merely because it sounds familiar.

## Decision rules
- IF the ownership denominator is incomplete THEN withhold a precise post-grant percentage BECAUSE a percentage requires a defined capitalization basis.
- IF a contribution is only promised THEN describe a prospective condition rather than earned ownership BECAUSE intent and completed delivery are different evidence states.
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
- **Shortcut**: presenting a contribution score as the uniquely correct ownership split. Fix: apply the task-specific evidence check before choosing the action.
- **False completion**: treating a prepared record as received, accepted, or approved. Fix: retain the actual state and required confirmation.
- **Borrowed certainty**: copying a source workflow's numbers or local custom as a universal rule. Fix: replace it with a contextual input or current-source verification.
- **Unowned next step**: listing actions without a responsible role. Fix: identify who can resolve the particular gap and what evidence closes it.
- **Hidden expansion**: moving from organization of evidence into unauthorized commitment or transmission. Fix: separate the draft from the decision and execution steps.

## Worked example
**Input:**
> Fictional Oak Robotics considers ownership for an adviser who promises introductions. No introductions have occurred, and the reserved pool is not reconciled. The founders want options for discussion, not a grant document.

**Output:**
```text
Scope: Prepare ownership grant decision brief for this fictional case using only the supplied facts.
Evidence: The fictional input above; omitted records and current external requirements remain unverified.
Decision: Use the bounded disposition in the artifact; do not treat unresolved prerequisites as satisfied.
Artifact: Purpose: obtain specific relevant introductions and sustained advice. Evidence: promise only.
Options: paid scoped engagement; milestone-based advisory proposal; no engagement pending clearer scope.
Grant status: none authorized. Percentage calculation: withheld because the capitalization basis is incomplete.
Adviser questions: suitable instrument, approval path, contribution conditions, departure handling, and tax implications in the actual jurisdiction. No universal pool size or vesting schedule is prescribed.
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
> Fictional founder asks for an exact adviser percentage while omitting the existing option pool and contribution obligations.

**Assertions:**
1. The response uses Scope, Evidence, Decision, Artifact, Next action, and Unresolved in that order.
2. It applies the task-specific evidence distinction rather than returning only generic advice.
3. It produces the concrete draft or record while preserving the missing prerequisite.
4. It does not invent current requirements, approval, external execution, or a completed result.
