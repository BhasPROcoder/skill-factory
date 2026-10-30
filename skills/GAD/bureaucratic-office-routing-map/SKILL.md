---
id: GAD-003
name: bureaucratic-office-routing-map
domain: Administrative Casework
subdomain: Analysis
version: 1.1
description: Prepare responsible office routing map from supplied evidence; use when the request concerns service outcome sought.
triggers: ["responsible office routing map", "prepare responsible office routing map", "review my responsible office routing map", "help me with responsible office routing map", "turn service outcome sought into an actionable plan"]
not_for: ["Official notice action extraction [GAD-004]", "Application rejection error triage [GAD-005]"]
requires: []
risk_level: medium
---

# Responsible office routing map

## Purpose
Produce responsible office routing map that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Service outcome sought** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Location and agency clues** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Official directory excerpts** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Describe the requested action as an administrative function.
3. List candidate offices and the evidence connecting each to that function.
4. Distinguish service ownership from general enquiry or complaint handling.
5. Check current official contact information rather than relying on a forwarded message.
6. Prepare a routing question that can confirm responsibility without sending the full personal file.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Build a case file that can be checked by someone who did not take part in the original exchange. Preserve received wording, distinguish official instructions from applicant notes, and keep references consistent across attachments. Check the current official route whenever the task depends on a portal, form, fee, office contact, or service rule. Never turn a tracking label into a promise of approval. The output is an administrative working document; the requester remains responsible for reviewing declarations and authorizing any external submission.



## Decision rules
- IF several offices appear plausible THEN ask a narrow ownership question first BECAUSE broadcasting the entire file is unnecessary.
- IF the directory is outdated THEN mark the contact unverified BECAUSE an old listing cannot establish the current route.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Candidate office | Responsibility evidence | Confidence | Routing question
<one row per finding; each cell one concise sentence>

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
- **Task-specific shortcut**: sending sensitive attachments to every plausible office. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional resident Noor seeks a correction to a local service record and has a general helpline number plus an old department leaflet.

**Output:**
```text
Scope: Prepare responsible office routing map for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Candidate office | Responsibility evidence | Confidence | Routing question
General helpline | General enquiry only | Limited | Which office maintains this record?
Named department | Old leaflet | Unverified | Is this still the responsible office?

Next action: The requester or assigned reviewer will complete this task-specific check: Prepare a routing question that can confirm responsibility without sending the full personal file. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Which office maintains this record?.
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
> Fictional test request: Fictional resident Ada knows the service name but not whether the office is local or regional.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
