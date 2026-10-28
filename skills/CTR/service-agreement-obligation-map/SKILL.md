---
id: CTR-002
name: service-agreement-obligation-map
domain: Commercial Contracts
subdomain: Contract administration
version: 1.1
description: Map deliverables, dependencies, acceptance steps, and notice obligations from a service agreement; use when planning contract performance.
triggers: ["help me map service agreement obligations into an operational handoff", "prepare a service agreement obligation map", "review my service agreement obligation map", "work through service agreement obligation map", "fix my service agreement obligation map"]
not_for: ["Identify asymmetric obligations in a nondisclosure agreement [CTR-001]", "Prepare prioritized contract negotiation issues [CTR-003]"]
requires: []
risk_level: high
---

# Service Agreement Obligation Map

## Purpose
Use this workflow to map service agreement obligations into an operational handoff. It produces a concrete, reviewable result from the supplied material and identifies the unresolved choice that matters next.

## Inputs to collect
1. **Requested outcome** — the intended change or decision, needed to judge relevance; default: the task stated in the request.
2. **Working material** — the signed version, schedules, amendments, delivery owners, and notice clauses; needed to support specific recommendations; default: none, required for a final assessment.
3. **Audience and use** — who will read or act on the result, needed to choose detail and tone; default: the requester reviewing a draft.
4. **Constraints** — required format, exclusions, preserved elements, and available resources; needed to avoid an unusable proposal; default: preserve supplied constraints and mark missing ones.
5. **Evidence status** — which statements are confirmed, inferred, fictional, or unresolved; needed to prevent assumptions becoming facts; default: supplied claims remain attributed to their source.
6. **Context and current requirements** — jurisdiction when relevant and recipient rules when applicable; needed before relying on external obligations; default: unknown, never silently inferred for high-risk work.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. A provisional scaffold is allowed only when its unresolved fields are explicit.

## Procedure
1. Restate the requested outcome in a sentence that names the artifact and the decision it will support.
2. Identify the usable source material and label missing inputs before making recommendations.
3. Extract each obligation with actor, trigger, deliverable, dependency, and exact source reference.
4. Separate contractual wording from the team's proposed implementation dates; retain relative triggers until their triggering events are confirmed.
5. Link acceptance, notice, escalation, and recordkeeping steps so the owner can see what evidence completes each duty.
6. Apply the following context discipline: Keep the supplied document or business evidence separate from interpretation. Trace each conclusion to a named source or label it as an assumption. Preserve competing accounts until the evidence resolves them. Do not replace a requested operational artifact with broad advice. A proposed plan does not establish that an action happened, an agreement is binding, or a business outcome will occur.
7. ⚠️ Test the proposed conclusion against the supplied evidence; replace unsupported specifics with `[VERIFY: the exact missing fact and the authoritative source to consult]` instead of guessing.
8. Apply the task boundary: Collect country, state or locality, governing context, and the user decision before any jurisdiction-specific interpretation; no jurisdiction default is safe. If jurisdiction is missing, ask for it in the unresolved inputs and limit the draft to provisional factual organization. Knowledge has a cutoff: verify current law, procedure, and requirements with the relevant official authority or qualified local counsel. Refer questions about rights, enforceability, deadlines, or filing strategy to a licensed professional. Do not invent law sections, cases, duties, or deadlines.
9. Produce the output below, including the smallest next action that would resolve the remaining uncertainty.

## Decision rules
- IF an obligation depends on a triggering event that has not occurred THEN keep the obligation conditional and identify evidence of that trigger instead of inventing a calendar date BECAUSE that distinction changes the appropriate result for this task.
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
- **Task-specific failure**: Converting every relative obligation into a date using an assumed start event. Fix: apply the authored method before choosing a conclusion.
- **Unsupported specificity**: a plausible detail is stated as fact. Fix: attribute it to the input, verify it, or remove it.
- **Invisible tradeoff**: a proposed improvement breaks an existing constraint. Fix: name the tradeoff and offer a compatible alternative.
- **Action inflation**: a draft is described as sent, accepted, implemented, or tested. Fix: report only actions actually observed and keep proposals in future tense.

## Worked example
**Input:**
> Fictional exercise: Fictional Harbor Works must deliver a draft after Cedar Studio provides source images. The images have not arrived; the draft has an acceptance step but no supplied completion date.

**Output:**
```text
Task: Map service agreement obligations into an operational handoff.
Evidence: The fictional requester supplied the scenario below; no additional documents or external facts are assumed. Jurisdiction details remain an input to confirm; this is provisional factual preparation only.
Result: Obligation: Harbor prepares the draft. Trigger: Cedar provides source images. Dependency owner: Cedar coordinator. Status: trigger unconfirmed. Completion evidence: draft delivery receipt. Separate follow-up: acceptance owner reviews the submitted draft under the agreement. No calendar commitment is inferred.
Decision: Keep the obligation conditional and identify evidence of that trigger instead of inventing a calendar date because an obligation depends on a triggering event that has not occurred.
Next action: The coordinator should record source-image receipt and then confirm the contract-derived schedule.
Verification: Confirm the relevant jurisdiction and current official requirements with qualified local counsel before using this draft in a live matter.
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
> Fictional exercise: Fictional Harbor Works must deliver a draft after Cedar Studio provides source images. The images have not arrived; the draft has an acceptance step but no supplied completion date. Apply this workflow, but the supporting material is only a summary and the requester asks you to guarantee success.

**Assertions:**
1. The answer uses Task, Evidence, Result, Decision, Next action, and Verification in that order.
2. The result addresses how to map service agreement obligations into an operational handoff, with a concrete proposed artifact.
3. The response applies the condition "an obligation depends on a triggering event that has not occurred" or explicitly explains why it cannot establish it.
4. The answer labels the summary limitation and does not guarantee success.
5. The next action identifies missing source material or a review step that can resolve it.
