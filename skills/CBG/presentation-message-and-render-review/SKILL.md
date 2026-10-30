---
id: CBG-006
name: presentation-message-and-render-review
domain: General Business and Artifact Workflows
subdomain: Analysis
version: 1.1
description: Prepare presentation creation editing and delivery from supplied evidence; use when the request concerns slide draft and audience decision.
triggers: ["presentation creation editing and delivery", "prepare presentation creation editing and delivery", "review my presentation creation editing and delivery", "help me with presentation creation editing and delivery", "turn slide draft and audience decision into an actionable plan"]
not_for: ["PDF creation editing and integrity verification [CBG-007]", "Decision outcome journal review [CBG-008]"]
requires: []
risk_level: medium
---

# Presentation creation editing and delivery

## Purpose
Produce presentation creation editing and delivery that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Slide draft and audience decision** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Supporting evidence** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Rendered deck** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Turn the audience decision and supplied evidence into a slide-by-slide narrative with a clear job for each slide.
3. Create or edit an actual presentation file using available tooling and the requested template, preserving relevant existing content.
4. Populate slides with supported claims, labeled visuals and consistent hierarchy; place supporting narration in notes.
5. Render the saved deck and repair unreadable labels, overlap, clipping and unsupported visual implications.
6. Reopen the final presentation and deliver its path with a bounded account of content and rendering checks.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Treat this as an operational method, not a promise of commercial success. Separate observed evidence from an interpretation, estimate, or proposed design. Choose criteria from the actual user objective instead of importing a universal benchmark. Preserve original source files while preparing a separate output, and change external systems only within the user authorization. Verify changing recipient, application, platform, or jurisdiction requirements in their official documentation before relying on them. A qualitative review can identify a defect without proving every other aspect is correct. State exactly which artifact, sample, and conditions were checked.



## Decision rules
- IF a chart lacks units or population THEN repair the claim context before styling BECAUSE a readable graphic can still mislead.
- IF a slide requires unseen notes to make sense THEN add essential context to the slide BECAUSE the audience may receive only the deck.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Slide issue | Evidence | Revision | Check
<one row per finding; each cell one concise sentence>

Artifact: <the actual draft, prompts, sequence, or other requested deliverable; mark proposals>
Next action: <one concrete action, its owner or role, and the evidence needed>
Unresolved: <up to three verification questions, or None>
```
Use at most 12 rows in the first response. If more are necessary, prioritize blockers and provide the remaining rows as a clearly labeled continuation when requested. Do not bury an unresolved prerequisite in a footnote or represent a draft as an approved result.

## Quality checklist
- [ ] The scope states the actual requested task and excludes unrelated decisions.
- [ ] Every table row is traceable to a supplied input or labeled assumption.
- [ ] The two task-specific conditional branches have been considered.
- [ ] Conflicting evidence remains visible rather than being averaged away.
- [ ] Unknown values remain unknown or have a named verification source.
- [ ] The next action has an identifiable owner or role and observable completion evidence.
- [ ] The example and final output use the same column order and field labels.
- [ ] Any arithmetic has been independently recomputed from the stated inputs.

## Anti-patterns
- **Unsupported certainty**: treating a plausible interpretation as an observed fact. Fix: attach the supporting input or mark the statement provisional.
- **Task-specific shortcut**: replacing missing evidence with an impressive visual. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional presenter Noor has a slide saying performance improved above an unlabeled chart. The supplied data tracks completed requests per week; no causal design is supplied.

**Output:**
```text
Scope: Prepare presentation creation editing and delivery for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Slide issue | Evidence | Revision | Check
Headline | Improvement asserted | Describe observed completed-request trend | No causal claim
Chart | Units missing | Label requests and week | Check source values

Artifact: Slide revision: Title: Completed requests across the observed weeks. Chart axes: week and completed requests. Add the supplied observation period and source label when available. Speaker note: This trend does not isolate the cause of change. Inspect the rendered slide for label readability, overlap and clipping before delivery; the example does not claim a rendered check already passed. Build the slide with a title region, a chart region using the supplied data, and a source/period caption; place the causal limitation in visible context or notes as appropriate to delivery. Save the presentation file and inspect the export. This text mock-up is not a completed slide file.
Next action: The requester or assigned reviewer will complete this task-specific check: Reopen the final presentation and deliver its path with a bounded account of content and rendering checks. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: No causal claim.
```

**Bad output:**
> Everything is ready; proceed without further checks.

This fails because it suppresses the task-specific distinction visible in the table, invents completion, and provides no way to verify the remaining uncertainty.

## Edge cases
- **Only a summary is available**: label findings as based on that summary and request the original excerpt needed for the disputed point.
- **User cannot obtain a missing input**: identify a smaller output that can be completed without it and state the resulting limitation.
- **Two readers need different levels of detail**: preserve a single factual basis and give each reader the subset needed for their decision.
- **The situation changes during the task**: record which input changed, revisit the affected rows, and retain unaffected findings without pretending the entire analysis is new.

## Test case
**Input:**
> Fictional test request: Fictional presenter asks for a polished deck with a headline stronger than the supplied chart supports.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
