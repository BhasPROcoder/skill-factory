---
id: CBG-005
name: document-structure-and-render-review
domain: General Business and Artifact Workflows
subdomain: Analysis
version: 1.1
description: Prepare structured document creation and editing from supplied evidence; use when the request concerns document draft and content hierarchy.
triggers: ["structured document creation and editing", "prepare structured document creation and editing", "review my structured document creation and editing", "help me with structured document creation and editing", "turn document draft and content hierarchy into an actionable plan"]
not_for: ["Presentation creation editing and delivery [CBG-006]", "PDF creation editing and integrity verification [CBG-007]"]
requires: []
risk_level: medium
---

# Structured document creation and editing

## Purpose
Produce structured document creation and editing that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Document draft and content hierarchy** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Recipient format requirements** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Rendered pages** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Organize supplied content into a section outline and identify edits or missing material without inventing facts.
3. Create or edit the requested document using structural heading styles, appropriate lists, tables and deliberate section boundaries.
4. Set page layout, headers, footers and navigation to the recipient requirements while preserving content and requested revision tracking.
5. Save and render the document, inspect page breaks, clipping, table continuation and reading order, then repair the source.
6. Reopen the final file, verify the requested content and format, and deliver the artifact with remaining limitations.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Treat this as an operational method, not a promise of commercial success. Separate observed evidence from an interpretation, estimate, or proposed design. Choose criteria from the actual user objective instead of importing a universal benchmark. Preserve original source files while preparing a separate output, and change external systems only within the user authorization. Verify changing recipient, application, platform, or jurisdiction requirements in their official documentation before relying on them. A qualitative review can identify a defect without proving every other aspect is correct. State exactly which artifact, sample, and conditions were checked.



## Decision rules
- IF a heading is visually large but not structural THEN apply the proper heading role BECAUSE appearance alone does not support navigation.
- IF a table splits across pages THEN check headers and row readability BECAUSE a correct source table can become unclear in pagination.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Element | Observed issue | Repair | Verification
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
- **Task-specific shortcut**: claiming a document is print-ready without viewing rendered pages. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional editor Lila has a report whose section title is manually enlarged and whose rendered table loses its column labels on a continuation page.

**Output:**
```text
Scope: Prepare structured document creation and editing for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Element | Observed issue | Repair | Verification
Section title | Manual formatting only | Apply heading style | Check navigation
Continued table | Labels absent | Repeat header row where supported | Rerender continuation

Artifact: Revision brief: Make the section title a structural heading while preserving its intended level. Configure the table header to repeat on continuation pages using the target editor supported setting. Rerender, inspect the title placement and every continued table page, and verify reading order. Keep the original source and save the revised document separately until acceptance. Proposed document structure: Heading1=Findings; body=The supplied evidence is summarized below; table=the supplied findings with their original labels. Preserve the actual data and save the editable document before rendering. No final binary file is claimed by this text example.
Next action: The requester or assigned reviewer will complete this task-specific check: Reopen the final file, verify the requested content and format, and deliver the artifact with remaining limitations. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Check navigation.
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
> Fictional test request: Fictional editor asks to deliver a source document whose table overflows the rendered page.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
