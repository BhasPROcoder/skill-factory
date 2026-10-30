---
id: GRV-009
name: narrative-evidence-synthesis
domain: Evidence Review and Synthesis
subdomain: Analysis
version: 1.1
description: Prepare narrative evidence synthesis from supplied evidence; use when the request concerns extracted evidence.
triggers: ["narrative evidence synthesis", "prepare narrative evidence synthesis", "review my narrative evidence synthesis", "help me with narrative evidence synthesis", "turn extracted evidence into an actionable plan"]
not_for: ["Evidence review update watchlist [GRV-010]", "Literature search concept map [GRV-001]"]
requires: []
risk_level: medium
---

# Narrative evidence synthesis

## Purpose
Produce narrative evidence synthesis that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Extracted evidence** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Review question** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Study differences** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Group studies by the question or mechanism they address.
3. Describe the pattern within each group using evidence quality and relevance.
4. Explain important differences before combining conclusions.
5. Separate supported findings from plausible interpretations.
6. End with implications bounded by the included evidence.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Use a reproducible account of what was searched, included and excluded. A source reference must identify a real source that was supplied or actually retrieved; never fabricate authors, titles, dates, quotations or links. Distinguish an author claim from the evidence supporting it. Compare studies only after checking their populations, interventions or phenomena, outcomes, and methods. If evidence is incomplete, describe the bounded search and remaining uncertainty rather than claiming exhaustiveness. Preserve contradictory findings and avoid turning a count of positive studies into an unsupported estimate of effect.



## Decision rules
- IF studies are too heterogeneous for one summary THEN report structured subgroups BECAUSE a single conclusion would erase meaningful differences.
- IF only favorable findings are summarized THEN restore relevant contrary evidence BECAUSE selective synthesis misrepresents the record.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Evidence group | Observed pattern | Important difference | Bounded conclusion
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
- **Task-specific shortcut**: turning a collection of studies into a certainty stronger than any supported comparison. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional reviewer Lila has studies of two distinct service designs with different outcome definitions. Design A is described through qualitative accounts of access; Design B uses completion records.

**Output:**
```text
Scope: Prepare narrative evidence synthesis for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Evidence group | Observed pattern | Important difference | Bounded conclusion
Design A | Reported access experiences | Qualitative accounts | Describes user barriers
Design B | Completion records | Different outcome | Do not combine as one effect

Next action: The requester or assigned reviewer will complete this task-specific check: End with implications bounded by the included evidence. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Describes user barriers.
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
> Fictional test request: Fictional reviewer Eli asks for one confident conclusion despite incompatible outcome definitions.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
