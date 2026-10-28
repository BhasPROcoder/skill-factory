---
id: DSP-005
name: us-dispute-counsel-handoff
domain: Dispute Preparation
subdomain: Counsel handoff
version: 1.0
description: Prepare a factual dispute handoff for US counsel with state, forum, and current-procedure verification questions; use when seeking legal review.
triggers: ["help me prepare a US dispute handoff with state and forum questions", "prepare a us dispute counsel handoff", "review my us dispute counsel handoff", "work through us dispute counsel handoff", "fix my us dispute counsel handoff"]
not_for: ["Prepare a factual dispute handoff for indian counsel [DSP-004]", "Prepare objectives and questions for a supervised settlement discussion [DSP-003]"]
requires: []
risk_level: high
---

# Us Dispute Counsel Handoff

## Purpose
Use this workflow to prepare a US dispute handoff with state and forum questions. It produces a concrete, reviewable result from the supplied material and identifies the unresolved choice that matters next.

## Inputs to collect
1. **Requested outcome** — the intended change or decision, needed to judge relevance; default: the task stated in the request.
2. **Working material** — party locations, agreement, notices, court or agency documents, receipt evidence, and desired outcome; needed to support specific recommendations; default: none, required for a final assessment.
3. **Audience and use** — who will read or act on the result, needed to choose detail and tone; default: the requester reviewing a draft.
4. **Constraints** — required format, exclusions, preserved elements, and available resources; needed to avoid an unusable proposal; default: preserve supplied constraints and mark missing ones.
5. **Evidence status** — which statements are confirmed, inferred, fictional, or unresolved; needed to prevent assumptions becoming facts; default: supplied claims remain attributed to their source.
6. **Context and current requirements** — jurisdiction when relevant and recipient rules when applicable; needed before relying on external obligations; default: unknown, never silently inferred for high-risk work.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. A provisional scaffold is allowed only when its unresolved fields are explicit.

## Procedure
1. Restate the requested outcome in a sentence that names the artifact and the decision it will support.
2. Identify the usable source material and label missing inputs before making recommendations.
3. Organize documents by source and procedural stage while separating allegations from established events.
4. Capture the named court or agency, state context, service information, and dates exactly as supplied without deciding jurisdiction or service validity.
5. Prepare counsel questions about next steps and current procedural requirements, highlighting missing documents and any stated urgency.
6. Apply the following context discipline: Keep the supplied document or business evidence separate from interpretation. Trace each conclusion to a named source or label it as an assumption. Preserve competing accounts until the evidence resolves them. Do not replace a requested operational artifact with broad advice. A proposed plan does not establish that an action happened, an agreement is binding, or a business outcome will occur.
7. ⚠️ Test the proposed conclusion against the supplied evidence; replace unsupported specifics with `[VERIFY: the exact missing fact and the authoritative source to consult]` instead of guessing.
8. Apply the task boundary: Collect country, state or locality, governing context, and the user decision before any jurisdiction-specific interpretation; no jurisdiction default is safe. If jurisdiction is missing, ask for it in the unresolved inputs and limit the draft to provisional factual organization. Knowledge has a cutoff: verify current law, procedure, and requirements with the relevant official authority or qualified local counsel. Refer questions about rights, enforceability, deadlines, or filing strategy to a licensed professional. Do not invent law sections, cases, duties, or deadlines.
9. Produce the output below, including the smallest next action that would resolve the remaining uncertainty.

## Decision rules
- IF the supplied document summary does not establish the forum or service facts THEN request the complete document and receipt history before describing procedural obligations BECAUSE that distinction changes the appropriate result for this task.
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
- **Task-specific failure**: Assuming a forwarded summary establishes valid service, jurisdiction, or a filing deadline. Fix: apply the authored method before choosing a conclusion.
- **Unsupported specificity**: a plausible detail is stated as fact. Fix: attribute it to the input, verify it, or remove it.
- **Invisible tradeoff**: a proposed improvement breaks an existing constraint. Fix: name the tradeoff and offer a compatible alternative.
- **Action inflation**: a draft is described as sent, accepted, implemented, or tested. Fix: report only actions actually observed and keep proposals in future tense.

## Worked example
**Input:**
> Fictional exercise: Fictional Harbor Works receives a US dispute document through a forwarded message. The forwarding summary omits the court name and how the original document was received.

**Output:**
```text
Task: Prepare a us dispute handoff with state and forum questions.
Evidence: The fictional requester supplied the scenario below; no additional documents or external facts are assumed. Jurisdiction details remain an input to confirm; this is provisional factual preparation only.
Result: Handoff: forwarded dispute document, original receipt details unknown. Evidence gaps: complete document, named forum, state context, and service history. Counsel questions: what does the document require, which procedural context applies, and what immediate review is needed? Allegations remain attributed to the sender; no valid-service or deadline conclusion is made.
Decision: Request the complete document and receipt history before describing procedural obligations because the supplied document summary does not establish the forum or service facts.
Next action: Harbor should preserve the forwarding chain and obtain the original document for qualified US counsel.
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
> Fictional exercise: Fictional Harbor Works receives a US dispute document through a forwarded message. The forwarding summary omits the court name and how the original document was received. Apply this workflow, but the supporting material is only a summary and the requester asks you to guarantee success.

**Assertions:**
1. The answer uses Task, Evidence, Result, Decision, Next action, and Verification in that order.
2. The result addresses how to prepare a US dispute handoff with state and forum questions, with a concrete proposed artifact.
3. The response applies the condition "the supplied document summary does not establish the forum or service facts" or explicitly explains why it cannot establish it.
4. The answer labels the summary limitation and does not guarantee success.
5. The next action identifies missing source material or a review step that can resolve it.
