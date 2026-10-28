---
id: CMP-005
name: us-privacy-request-handling-plan
domain: Compliance Workflow Design
subdomain: Privacy operations
version: 1.0
description: Prepare a US privacy request workflow with state and sector applicability checks; use when designing intake procedures.
triggers: ["help me plan a US privacy request workflow using state and sector context", "prepare a us privacy request handling plan", "review my us privacy request handling plan", "work through us privacy request handling plan", "fix my us privacy request handling plan"]
not_for: ["Plan an india-specific privacy request intake workflow [CMP-004]", "Turn documented compliance gaps into verifiable remediation actions [CMP-003]"]
requires: []
risk_level: high
---

# Us Privacy Request Handling Plan

## Purpose
Use this workflow to plan a US privacy request workflow using state and sector context. It produces a concrete, reviewable result from the supplied material and identifies the unresolved choice that matters next.

## Inputs to collect
1. **Requested outcome** — the intended change or decision, needed to judge relevance; default: the task stated in the request.
2. **Working material** — request text, relevant state context, organization role, sector, data locations, and current official requirements; needed to support specific recommendations; default: none, required for a final assessment.
3. **Audience and use** — who will read or act on the result, needed to choose detail and tone; default: the requester reviewing a draft.
4. **Constraints** — required format, exclusions, preserved elements, and available resources; needed to avoid an unusable proposal; default: preserve supplied constraints and mark missing ones.
5. **Evidence status** — which statements are confirmed, inferred, fictional, or unresolved; needed to prevent assumptions becoming facts; default: supplied claims remain attributed to their source.
6. **Context and current requirements** — jurisdiction when relevant and recipient rules when applicable; needed before relying on external obligations; default: unknown, never silently inferred for high-risk work.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. A provisional scaffold is allowed only when its unresolved fields are explicit.

## Procedure
1. Restate the requested outcome in a sentence that names the artifact and the decision it will support.
2. Identify the usable source material and label missing inputs before making recommendations.
3. Capture the request and relevant relationship without assuming residence or applicable law from an email domain.
4. Prepare an applicability review covering supplied state, sector, organization role, and request category with an authorized privacy reviewer.
5. Map authentication, system search, exception review, response approval, and closure evidence; populate timing only from verified applicable requirements.
6. Apply the following context discipline: Keep the supplied document or business evidence separate from interpretation. Trace each conclusion to a named source or label it as an assumption. Preserve competing accounts until the evidence resolves them. Do not replace a requested operational artifact with broad advice. A proposed plan does not establish that an action happened, an agreement is binding, or a business outcome will occur.
7. ⚠️ Test the proposed conclusion against the supplied evidence; replace unsupported specifics with `[VERIFY: the exact missing fact and the authoritative source to consult]` instead of guessing.
8. Apply the task boundary: Collect country, state or locality, governing context, and the user decision before any jurisdiction-specific interpretation; no jurisdiction default is safe. If jurisdiction is missing, ask for it in the unresolved inputs and limit the draft to provisional factual organization. Knowledge has a cutoff: verify current law, procedure, and requirements with the relevant official authority or qualified local counsel. Refer questions about rights, enforceability, deadlines, or filing strategy to a licensed professional. Do not invent law sections, cases, duties, or deadlines.
9. Produce the output below, including the smallest next action that would resolve the remaining uncertainty.

## Decision rules
- IF the requester's relevant state context is unknown THEN route an applicability question to the privacy owner and avoid applying a default state rule BECAUSE that distinction changes the appropriate result for this task.
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
- **Task-specific failure**: Using an email address or a national label as proof of state-law applicability. Fix: apply the authored method before choosing a conclusion.
- **Unsupported specificity**: a plausible detail is stated as fact. Fix: attribute it to the input, verify it, or remove it.
- **Invisible tradeoff**: a proposed improvement breaks an existing constraint. Fix: name the tradeoff and offer a compatible alternative.
- **Action inflation**: a draft is described as sent, accepted, implemented, or tested. Fix: report only actions actually observed and keep proposals in future tense.

## Worked example
**Input:**
> Fictional exercise: Fictional Harbor Works receives an access request from a customer with a US email account. The record does not establish the relevant state, sector rules, or verified identity.

**Output:**
```text
Task: Plan a us privacy request workflow using state and sector context.
Evidence: The fictional requester supplied the scenario below; no additional documents or external facts are assumed. Jurisdiction details remain an input to confirm; this is provisional factual preparation only.
Result: Workflow: preserve request and receipt evidence; route applicability and identity questions to the privacy owner; restrict searches to authorized systems after verification; review proposed disclosures before response. Open inputs: relevant state context, applicable sector obligations, and current response requirements. No state-specific entitlement or deadline is asserted.
Decision: Route an applicability question to the privacy owner and avoid applying a default state rule because the requester's relevant state context is unknown.
Next action: The privacy owner should document applicable context and approved verification steps before assigning the response schedule.
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
> Fictional exercise: Fictional Harbor Works receives an access request from a customer with a US email account. The record does not establish the relevant state, sector rules, or verified identity. Apply this workflow, but the supporting material is only a summary and the requester asks you to guarantee success.

**Assertions:**
1. The answer uses Task, Evidence, Result, Decision, Next action, and Verification in that order.
2. The result addresses how to plan a US privacy request workflow using state and sector context, with a concrete proposed artifact.
3. The response applies the condition "the requester's relevant state context is unknown" or explicitly explains why it cannot establish it.
4. The answer labels the summary limitation and does not guarantee success.
5. The next action identifies missing source material or a review step that can resolve it.
