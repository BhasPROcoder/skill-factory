---
id: BPL-005
name: business-contingency-action-plan
domain: Business Planning
subdomain: Contingency planning
version: 1.0
description: Define scenario signals and corresponding business actions with owners and reversibility checks; use when preparing for uncertain operating conditions.
triggers: ["help me define observable scenario signals and owned contingency actions", "prepare a business contingency action plan", "review my business contingency action plan", "work through business contingency action plan", "fix my business contingency action plan"]
not_for: ["Design an operating review that leads to owned decisions [BPL-004]", "Compare planned work with supplied capacity and explicit tradeoffs [BPL-003]"]
requires: []
risk_level: medium
---

# Business Contingency Action Plan

## Purpose
Use this workflow to define observable scenario signals and owned contingency actions. It produces a concrete, reviewable result from the supplied material and identifies the unresolved choice that matters next.

## Inputs to collect
1. **Requested outcome** — the intended change or decision, needed to judge relevance; default: the task stated in the request.
2. **Working material** — critical dependencies, plausible disruptions, response options, owners, and reversibility limits; needed to support specific recommendations; default: none, required for a final assessment.
3. **Audience and use** — who will read or act on the result, needed to choose detail and tone; default: the requester reviewing a draft.
4. **Constraints** — required format, exclusions, preserved elements, and available resources; needed to avoid an unusable proposal; default: preserve supplied constraints and mark missing ones.
5. **Evidence status** — which statements are confirmed, inferred, fictional, or unresolved; needed to prevent assumptions becoming facts; default: supplied claims remain attributed to their source.
6. **Context and current requirements** — jurisdiction when relevant and recipient rules when applicable; needed before relying on external obligations; default: unknown, never silently inferred for high-risk work.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. A provisional scaffold is allowed only when its unresolved fields are explicit.

## Procedure
1. Restate the requested outcome in a sentence that names the artifact and the decision it will support.
2. Identify the usable source material and label missing inputs before making recommendations.
3. Describe each scenario in operational terms and separate early signals from confirmation that the scenario has occurred.
4. Pair signals with staged actions, decision authority, resource needs, and a rollback or review condition.
5. Test the plan against a false alarm and a delayed response so the escalation path does not depend on perfect prediction.
6. Apply the following context discipline: Keep the supplied document or business evidence separate from interpretation. Trace each conclusion to a named source or label it as an assumption. Preserve competing accounts until the evidence resolves them. Do not replace a requested operational artifact with broad advice. A proposed plan does not establish that an action happened, an agreement is binding, or a business outcome will occur.
7. ⚠️ Test the proposed conclusion against the supplied evidence; replace unsupported specifics with `[VERIFY: the exact missing fact and the authoritative source to consult]` instead of guessing.
8. Apply the task boundary: Use current recipient or platform requirements only when the task depends on them. Obtain those requirements from the official owner documentation and record what remains unchecked. If no external rule is involved, state that this is an editorial or planning judgment rather than adding irrelevant compliance steps.
9. Produce the output below, including the smallest next action that would resolve the remaining uncertainty.

## Decision rules
- IF an early signal is ambiguous and the proposed response is difficult to reverse THEN use a reversible preparation step and seek stronger confirmation before committing BECAUSE that distinction changes the appropriate result for this task.
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
- **Task-specific failure**: Triggering an irreversible response from an ambiguous early-warning signal. Fix: apply the authored method before choosing a conclusion.
- **Unsupported specificity**: a plausible detail is stated as fact. Fix: attribute it to the input, verify it, or remove it.
- **Invisible tradeoff**: a proposed improvement breaks an existing constraint. Fix: name the tradeoff and offer a compatible alternative.
- **Action inflation**: a draft is described as sent, accepted, implemented, or tested. Fix: report only actions actually observed and keep proposals in future tense.

## Worked example
**Input:**
> Fictional exercise: Fictional Cedar Studio hears that its regular print supplier may pause service. The rumor is unconfirmed, and the proposed response is to cancel all pending work immediately.

**Output:**
```text
Task: Define observable scenario signals and owned contingency actions.
Evidence: The fictional requester supplied the scenario below; no additional documents or external facts are assumed. 
Result: Signal: unconfirmed supplier interruption report. Reversible preparation: identify authorized alternatives and check current order exposure. Confirmation task: obtain an attributable supplier update. Escalation: the operations owner decides on rerouting affected work after checking delivery needs and switching consequences. Immediate blanket cancellation is not assumed necessary.
Decision: Use a reversible preparation step and seek stronger confirmation before committing because an early signal is ambiguous and the proposed response is difficult to reverse.
Next action: The operations owner should confirm supplier status and document which orders, if any, need rerouting.
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
> Fictional exercise: Fictional Cedar Studio hears that its regular print supplier may pause service. The rumor is unconfirmed, and the proposed response is to cancel all pending work immediately. Apply this workflow, but the supporting material is only a summary and the requester asks you to guarantee success.

**Assertions:**
1. The answer uses Task, Evidence, Result, Decision, Next action, and Verification in that order.
2. The result addresses how to define observable scenario signals and owned contingency actions, with a concrete proposed artifact.
3. The response applies the condition "an early signal is ambiguous and the proposed response is difficult to reverse" or explicitly explains why it cannot establish it.
4. The answer labels the summary limitation and does not guarantee success.
5. The next action identifies missing source material or a review step that can resolve it.
