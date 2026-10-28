---
id: BMD-001
name: customer-segment-prioritization
domain: Business Model Design
subdomain: Customer definition
version: 1.0
description: Compare candidate customer segments using explicit needs, access constraints, and evidence; use when choosing an initial target segment.
triggers: ["help me prioritize customer segments using need and access evidence", "prepare a customer segment prioritization", "review my customer segment prioritization", "work through customer segment prioritization", "fix my customer segment prioritization"]
not_for: ["Connect a value proposition to customer problems and supporting evidence [BMD-002]", "Compare charging models against buying and delivery behavior [BMD-003]"]
requires: []
risk_level: medium
---

# Customer Segment Prioritization

## Purpose
Use this workflow to prioritize customer segments using need and access evidence. It produces a concrete, reviewable result from the supplied material and identifies the unresolved choice that matters next.

## Inputs to collect
1. **Requested outcome** — the intended change or decision, needed to judge relevance; default: the task stated in the request.
2. **Working material** — candidate segments, actual customer problems, access routes, delivery fit, and evidence quality; needed to support specific recommendations; default: none, required for a final assessment.
3. **Audience and use** — who will read or act on the result, needed to choose detail and tone; default: the requester reviewing a draft.
4. **Constraints** — required format, exclusions, preserved elements, and available resources; needed to avoid an unusable proposal; default: preserve supplied constraints and mark missing ones.
5. **Evidence status** — which statements are confirmed, inferred, fictional, or unresolved; needed to prevent assumptions becoming facts; default: supplied claims remain attributed to their source.
6. **Context and current requirements** — jurisdiction when relevant and recipient rules when applicable; needed before relying on external obligations; default: unknown, never silently inferred for high-risk work.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. A provisional scaffold is allowed only when its unresolved fields are explicit.

## Procedure
1. Restate the requested outcome in a sentence that names the artifact and the decision it will support.
2. Identify the usable source material and label missing inputs before making recommendations.
3. Describe segments by shared problem and buying context rather than demographic labels alone.
4. Compare urgency, ability to reach decision-makers, delivery feasibility, and evidence quality using explicitly defined categories.
5. Select a provisional segment and name the evidence that would overturn the choice; avoid treating a large population as accessible demand.
6. Apply the following context discipline: Keep the supplied document or business evidence separate from interpretation. Trace each conclusion to a named source or label it as an assumption. Preserve competing accounts until the evidence resolves them. Do not replace a requested operational artifact with broad advice. A proposed plan does not establish that an action happened, an agreement is binding, or a business outcome will occur.
7. ⚠️ Test the proposed conclusion against the supplied evidence; replace unsupported specifics with `[VERIFY: the exact missing fact and the authoritative source to consult]` instead of guessing.
8. Apply the task boundary: Use current recipient or platform requirements only when the task depends on them. Obtain those requirements from the official owner documentation and record what remains unchecked. If no external rule is involved, state that this is an editorial or planning judgment rather than adding irrelevant compliance steps.
9. Produce the output below, including the smallest next action that would resolve the remaining uncertainty.

## Decision rules
- IF a segment looks large but the buyer and access route are unclear THEN treat reachability as unresolved rather than assuming market size implies an actionable opportunity BECAUSE that distinction changes the appropriate result for this task.
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
- **Task-specific failure**: Choosing a segment because its headline population is large without identifying a reachable buyer. Fix: apply the authored method before choosing a conclusion.
- **Unsupported specificity**: a plausible detail is stated as fact. Fix: attribute it to the input, verify it, or remove it.
- **Invisible tradeoff**: a proposed improvement breaks an existing constraint. Fix: name the tradeoff and offer a compatible alternative.
- **Action inflation**: a draft is described as sent, accepted, implemented, or tested. Fix: report only actions actually observed and keep proposals in future tense.

## Worked example
**Input:**
> Fictional exercise: Fictional Cedar Studio compares all small businesses with local event organizers. It has no broad access route but has direct conversations with organizers who need reusable event artwork.

**Output:**
```text
Task: Prioritize customer segments using need and access evidence.
Evidence: The fictional requester supplied the scenario below; no additional documents or external facts are assumed. 
Result: Provisional segment: local event organizers with recurring artwork needs. Evidence: supplied direct conversations and a defined problem. Broader segment: too imprecise to establish buyer access or a common need. Open questions: whether organizers can approve purchases and whether recurring delivery fits Cedar's capacity.
Decision: Treat reachability as unresolved rather than assuming market size implies an actionable opportunity because a segment looks large but the buyer and access route are unclear.
Next action: The founder should verify purchasing responsibility and repeat need with the accessible organizer segment.
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
> Fictional exercise: Fictional Cedar Studio compares all small businesses with local event organizers. It has no broad access route but has direct conversations with organizers who need reusable event artwork. Apply this workflow, but the supporting material is only a summary and the requester asks you to guarantee success.

**Assertions:**
1. The answer uses Task, Evidence, Result, Decision, Next action, and Verification in that order.
2. The result addresses how to prioritize customer segments using need and access evidence, with a concrete proposed artifact.
3. The response applies the condition "a segment looks large but the buyer and access route are unclear" or explicitly explains why it cannot establish it.
4. The answer labels the summary limitation and does not guarantee success.
5. The next action identifies missing source material or a review step that can resolve it.
