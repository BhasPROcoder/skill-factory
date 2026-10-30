---
id: GRE-010
name: disagreement-crux-map
domain: Reasoning and Decision Clarity
subdomain: Analysis
version: 1.1
description: Prepare disagreement crux map from supplied evidence; use when the request concerns competing positions.
triggers: ["disagreement crux map", "prepare disagreement crux map", "review my disagreement crux map", "help me with disagreement crux map", "turn competing positions into an actionable plan"]
not_for: ["Argument premise map [GRE-001]", "Claim scope qualification [GRE-002]"]
requires: []
risk_level: low
---

# Disagreement crux map

## Purpose
Produce disagreement crux map that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Competing positions** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Reasons from each side** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Shared decision** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. Restate each position in wording its holder would recognize.
3. Separate factual disputes from value priorities and definition differences.
4. Identify a premise whose resolution could change a participant position.
5. Ask each participant whether the proposed crux is actually decision-relevant.
6. Plan a fair check or explicit tradeoff discussion.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Separate an argument structure from the truth of its premises. A valid-looking diagram does not verify an observation. Preserve the speaker exact claim before making it stronger or weaker. Define terms when their meaning changes the inference. Use counterexamples to test a stated generalization, not to dismiss a narrower claim it never made. Describe uncertainty in words when no defensible numerical probability model is supplied. These tasks support reasoning about ordinary decisions and do not substitute for professional judgment in consequential domains.



## Decision rules
- IF disagreement concerns values rather than a fact THEN make the tradeoff visible BECAUSE more data alone may not choose priorities.
- IF neither participant would change position if a premise changed THEN seek a different crux BECAUSE a debating point is not necessarily decisive.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Disagreement | Type | Potential crux | Resolution route
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
- **Task-specific shortcut**: assuming every disagreement can be settled by finding one fact. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional colleagues Noor and Bea choose between a quiet room and a central room; Noor prioritizes concentration and Bea prioritizes easy attendance.

**Output:**
```text
Scope: Prepare disagreement crux map for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Disagreement | Type | Potential crux | Resolution route
Room preference | Value priority | Which outcome matters more for this session? | Agree meeting purpose
Travel burden | Factual question | Does central location materially change attendance? | Ask affected attendees

Next action: The requester or assigned reviewer will complete this task-specific check: Plan a fair check or explicit tradeoff discussion. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Agree meeting purpose.
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
> Fictional test request: Fictional team argues about an option while disagreeing about the purpose the option should serve.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
