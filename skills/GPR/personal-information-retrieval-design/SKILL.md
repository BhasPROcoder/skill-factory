---
id: GPR-009
name: personal-information-retrieval-design
domain: Personal Work Organization
subdomain: Analysis
version: 1.1
description: Prepare personal information retrieval design from supplied evidence; use when the request concerns frequently needed information.
triggers: ["personal information retrieval design", "prepare personal information retrieval design", "review my personal information retrieval design", "help me with personal information retrieval design", "turn frequently needed information into an actionable plan"]
not_for: ["Overdue commitment recovery plan [GPR-010]", "Task inbox triage [GPR-001]"]
requires: []
risk_level: low
---

# Personal information retrieval design

## Purpose
Produce personal information retrieval design that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Frequently needed information** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Current storage locations** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Search habits** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Identify the questions the person repeatedly needs to answer.
3. Choose a stable naming or indexing convention tied to those questions.
4. Separate reference material from active tasks.
5. Test retrieval using realistic examples.
6. Remove redundant categories that do not help find information.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Use the person actual commitments and constraints rather than an idealized day. Distinguish a desired outcome, a project, and the next action that can be performed. Keep external promises separate from private intentions, and avoid silently moving a commitment that affects someone else. A plan should show what will be deferred when capacity is insufficient. Treat a routine as an experiment with observable results, not a universal productivity law. Do not turn ordinary organization requests into psychological diagnoses or medical advice.



## Decision rules
- IF categories overlap heavily THEN use clearer labels or cross-references BECAUSE uncertain filing slows retrieval.
- IF a document has several uses THEN retain one source with links BECAUSE multiple uncontrolled copies can diverge.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Information type | Retrieval question | Organization choice | Test
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
- **Task-specific shortcut**: designing an elaborate folder tree before testing retrieval. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional user Sora stores meeting decisions in several folders and cannot find the latest one.

**Output:**
```text
Scope: Prepare personal information retrieval design for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Information type | Retrieval question | Organization choice | Test
Decision note | What was agreed? | Index by project and meeting reference | Find current decision
Source file | Where is original? | Keep one canonical location | Link from index

Next action: The requester or assigned reviewer will complete this task-specific check: Remove redundant categories that do not help find information. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Find current decision.
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
> Fictional test request: Fictional user Max wants a new category for every possible future topic.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
