---
id: BST-005
name: strategy-assumption-test-plan
domain: Business Strategy
subdomain: Decision design
version: 1.1
description: Prioritize strategic assumptions and design evidence-gathering tests with decision criteria; use before committing to a chosen direction.
triggers: ["help me design tests for assumptions that determine a strategy choice", "prepare a strategy assumption test plan", "review my strategy assumption test plan", "work through strategy assumption test plan", "fix my strategy assumption test plan"]
not_for: ["Design the detailed intervention and comparison for one already-selected business-model assumption [BMD-005]", "Map dependencies across the business model before choosing a critical assumption [BMD-004]"]
requires: []
risk_level: medium
---

# Strategy Assumption Test Plan

## Purpose
Use this workflow to design tests for assumptions that determine a strategy choice. It produces a concrete, reviewable result from the supplied material and identifies the unresolved choice that matters next.

## Inputs to collect
1. **Requested outcome** — the intended change or decision, needed to judge relevance; default: the task stated in the request.
2. **Working material** — the proposed strategy, dependency assumptions, existing evidence, and decision constraints; needed to support specific recommendations; default: none, required for a final assessment.
3. **Audience and use** — who will read or act on the result, needed to choose detail and tone; default: the requester reviewing a draft.
4. **Constraints** — required format, exclusions, preserved elements, and available resources; needed to avoid an unusable proposal; default: preserve supplied constraints and mark missing ones.
5. **Evidence status** — which statements are confirmed, inferred, fictional, or unresolved; needed to prevent assumptions becoming facts; default: supplied claims remain attributed to their source.
6. **Context and current requirements** — jurisdiction when relevant and recipient rules when applicable; needed before relying on external obligations; default: unknown, never silently inferred for high-risk work.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. A provisional scaffold is allowed only when its unresolved fields are explicit.

## Procedure
1. Restate the requested outcome in a sentence that names the artifact and the decision it will support.
2. Identify the usable source material and label missing inputs before making recommendations.
3. Express each assumption as an observable proposition whose failure would change a decision.
4. Prioritize assumptions by decision consequence and uncertainty, keeping cheap-to-test but irrelevant questions out of the critical path.
5. Define the evidence collection method, disconfirming result, interpretation limits, and next decision before collecting data.
6. Apply the following context discipline: Keep the supplied document or business evidence separate from interpretation. Trace each conclusion to a named source or label it as an assumption. Preserve competing accounts until the evidence resolves them. Do not replace a requested operational artifact with broad advice. A proposed plan does not establish that an action happened, an agreement is binding, or a business outcome will occur.
7. ⚠️ Test the proposed conclusion against the supplied evidence; replace unsupported specifics with `[VERIFY: the exact missing fact and the authoritative source to consult]` instead of guessing.
8. Apply the task boundary: Use current recipient or platform requirements only when the task depends on them. Obtain those requirements from the official owner documentation and record what remains unchecked. If no external rule is involved, state that this is an editorial or planning judgment rather than adding irrelevant compliance steps.
9. Produce the output below, including the smallest next action that would resolve the remaining uncertainty.

## Decision rules
- IF the proposed test measures interest but the strategy depends on adoption behavior THEN redesign the test around the relevant behavior or label the evidence as insufficient BECAUSE that distinction changes the appropriate result for this task.
- IF the working material does not support a requested conclusion THEN label the conclusion unresolved and name the missing evidence BECAUSE a complete-looking answer must not imply certainty.
- IF a proposed revision conflicts with a supplied constraint THEN show the conflict and a compliant alternative BECAUSE the user's intended use determines whether the result is usable.
- IF several changes are possible THEN prioritize the change that directly advances the stated outcome and retain reversible alternatives BECAUSE unrelated improvements can obscure the decision.

## Output template
```text
Task: <one sentence>
Evidence: <material used and its limitation; up to 3 sentences>
Result: <concrete task artifact; up to 350 words>
Decision: <selected approach and task-specific reason; up to 3 sentences>
Next action: <owner or requester action plus completion evidence; up to 2 sentences>
Verification: <unresolved fact and source, or no external factual claim required>
```

## Quality checklist
- [ ] The result addresses the named task rather than an adjacent workflow.
- [ ] Each recommendation can be traced to supplied material or is labeled a proposal.
- [ ] The task-specific decision rule is applied to the actual condition.
- [ ] Preserved constraints are visible in the result or its decision explanation.
- [ ] Unknown facts are paired with a concrete verification source category.
- [ ] The next action has an observable completion condition.
- [ ] The response uses every output-template label in order.
- [ ] Any numbers are derived from supplied data and recomputed before delivery.

## Anti-patterns
- **Task-specific failure**: Using favorable opinions as proof of the behavior required for the strategy. Fix: apply the authored method before choosing a conclusion.
- **Unsupported specificity**: a plausible detail is stated as fact. Fix: attribute it to the input, verify it, or remove it.
- **Invisible tradeoff**: a proposed improvement breaks an existing constraint. Fix: name the tradeoff and offer a compatible alternative.
- **Action inflation**: a draft is described as sent, accepted, implemented, or tested. Fix: report only actions actually observed and keep proposals in future tense.

## Worked example
**Input:**
> Fictional exercise: Fictional Cedar Studio plans a self-service design intake. Its strategy depends on clients completing intake without assistance, but the proposed survey only asks whether they like the idea.

**Output:**
```text
Task: Design tests for assumptions that determine a strategy choice.
Evidence: The fictional requester supplied the scenario below; no additional documents or external facts are assumed. 
Result: Critical assumption: clients can complete a realistic intake independently. Test: give consenting representative users the proposed intake and observe completion barriers without coaching. Evidence: completed fields, requests for help, and misunderstood instructions. Decision rule: revise or narrow the workflow when observed barriers prevent the intended independent completion; do not equate liking with adoption.
Decision: Redesign the test around the relevant behavior or label the evidence as insufficient because the proposed test measures interest but the strategy depends on adoption behavior.
Next action: The strategy owner should approve observable completion criteria before running the intake exercise.
Verification: No external factual claim is required for this fictional exercise; verify any later recipient-specific requirements with that recipient.
```

**Bad output:**
> Everything looks fine; proceed without changing anything.

This fails because it contains no task artifact, does not apply the distinguishing decision rule, and supplies no evidence-based next action.

## Edge cases
- **Only a summary is supplied**: produce a provisional plan and list the exact source material needed before making detailed findings.
- **Inputs contradict one another**: keep both accounts labeled and identify which decision depends on resolving the conflict.
- **The requested action exceeds the scope**: deliver the reviewable draft, then identify the additional authorization or expertise needed for execution.
- **The user rejects the proposed approach**: retain the original material, ask which constraint changed, and revise the decision rather than insisting on the initial preference.

## Test case
**Input:**
> Fictional exercise: Fictional Cedar Studio plans a self-service design intake. Its strategy depends on clients completing intake without assistance, but the proposed survey only asks whether they like the idea. Apply this workflow, but the supporting material is only a summary and the requester asks you to guarantee success.

**Assertions:**
1. The answer uses Task, Evidence, Result, Decision, Next action, and Verification in that order.
2. The result addresses how to design tests for assumptions that determine a strategy choice, with a concrete proposed artifact.
3. The response applies the condition "the proposed test measures interest but the strategy depends on adoption behavior" or explicitly explains why it cannot establish it.
4. The answer labels the summary limitation and does not guarantee success.
5. The next action identifies missing source material or a review step that can resolve it.
