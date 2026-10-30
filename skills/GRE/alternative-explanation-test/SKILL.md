---
id: GRE-003
name: alternative-explanation-test
domain: Reasoning and Decision Clarity
subdomain: Analysis
version: 1.1
description: Prepare alternative explanation test from supplied evidence; use when the request concerns observation.
triggers: ["alternative explanation test", "prepare alternative explanation test", "review my alternative explanation test", "help me with alternative explanation test", "turn observation into an actionable plan"]
not_for: ["Definition disambiguation [GRE-004]", "Counterexample generalization check [GRE-005]"]
requires: []
risk_level: low
---

# Alternative explanation test

## Purpose
Produce alternative explanation test that another person can use without guessing which evidence supports each action. Keep the request bounded to this task and distinguish an observed fact, a working interpretation, and an unresolved question.

## Inputs to collect
1. **Observation** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
2. **Preferred explanation** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
3. **Contextual changes** — supply the relevant original material or describe what is unavailable; it determines the scope of the analysis. Default: unknown, never invented.
4. **Intended use and constraints** — identify the reader, available effort, and decision this output supports. Default: a private working draft using only supplied information.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Continue only the parts that do not depend on the missing answer; label any provisional work as provisional.

## Procedure
1. Restate the requested outcome in one sentence and identify the smallest useful deliverable; do not expand into adjacent advice merely because the input mentions it.
2. State the observation separately from the explanation.
3. Generate plausible alternatives tied to supplied context rather than arbitrary speculation.
4. Identify observations that would differ if each explanation were correct.
5. Choose a feasible discriminating check.
6. Retain unresolved alternatives until that check provides evidence.
7. ⚠️ Trace every proposed action back to an input or an explicitly stated condition; when support is missing, replace the conclusion with a verification question instead of filling the gap from memory.
8. Populate the output table with the task-specific findings, retaining disagreements or missing information as visible rows rather than silently dropping them.
9. Check the completed worked logic against an alternative explanation or a changed input; state what would have to change for the recommended next action to change.
10. Run the checklist below and revise any failed item before presenting the deliverable.

Separate an argument structure from the truth of its premises. A valid-looking diagram does not verify an observation. Preserve the speaker exact claim before making it stronger or weaker. Define terms when their meaning changes the inference. Use counterexamples to test a stated generalization, not to dismiss a narrower claim it never made. Describe uncertainty in words when no defensible numerical probability model is supplied. These tasks support reasoning about ordinary decisions and do not substitute for professional judgment in consequential domains.



## Decision rules
- IF alternatives predict the same observed fact THEN seek a different discriminating observation BECAUSE repeating the original fact cannot decide between them.
- IF an alternative is merely imaginable THEN label it speculative BECAUSE logical possibility alone does not make it equally supported.
- IF source material conflicts THEN preserve both versions and identify the fact needed to resolve the conflict BECAUSE silently choosing a convenient version hides uncertainty.
- IF a requested conclusion depends on unavailable evidence THEN give a conditional next step and name the missing evidence BECAUSE an actionable question is preferable to an unsupported answer.

## Output template
```text
Scope: <one sentence defining this task and its boundaries>
Basis: <up to three supplied inputs; distinguish unknowns>
Explanation | Predicted difference | Available evidence | Discriminating check
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
- **Task-specific shortcut**: listing many explanations without identifying how to distinguish them. Fix: apply the relevant procedural check before selecting a next action.
- **Missing decision owner**: giving advice that nobody can carry out. Fix: name the role responsible and the artifact that confirms completion.
- **Unbounded expansion**: solving every adjacent problem mentioned in the inputs. Fix: finish the declared scope and list a separate follow-up only when needed.

## Worked example
**Input:**
> Fictional scenario: Fictional organizer Tara sees fewer late arrivals after changing reminders and also moving the meeting time.

**Output:**
```text
Scope: Prepare alternative explanation test for the fictional case, limited to the supplied facts.
Basis: The fictional scenario above; missing supporting material remains unverified.
Explanation | Predicted difference | Available evidence | Discriminating check
Reminder effect | People saw reminder and adjusted | Not recorded | Ask about reminder use
Time effect | New time removes conflict | Not recorded | Check prior scheduling conflicts

Next action: The requester or assigned reviewer will complete this task-specific check: Retain unresolved alternatives until that check provides evidence. Retain the resulting revision or evidence record; do not describe the proposed action as already completed.
Unresolved: Resolve or confirm the first row's verification issue: Ask about reminder use.
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
> Fictional test request: Fictional manager Ivo attributes an improvement to one change while another relevant condition changed simultaneously.

**Assertions:**
1. The answer uses Scope, Basis, the specified table columns, Next action, and Unresolved in that order.
2. It applies the task-specific operations to the supplied case rather than returning a generic advice list.
3. It identifies the missing or conflicting input before presenting a dependent conclusion as settled.
4. It gives a next action with a responsible role and observable evidence of completion.
