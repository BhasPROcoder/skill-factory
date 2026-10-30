---
id: TDQ-001
name: dataset-key-uniqueness-check
domain: Dataset Quality Diagnostics
subdomain: Schema
version: 1.1
description: Create a key uniqueness report from supplied evidence; use when preparing or reviewing key uniqueness report decisions.
triggers: ["dataset key uniqueness check", "help with a key uniqueness report", "review my key uniqueness report", "prepare a key uniqueness report", "check the evidence for this key uniqueness report"]
not_for: ["dataset missingness pattern review [TDQ-002]", "dataset category normalization map [TDQ-003]"]
requires: []
risk_level: medium
---

# Dataset Key Uniqueness Check

## Purpose
Create a key uniqueness report that another practitioner can use to make the stated decision. This skill handles the narrow task named above; its result must distinguish observed evidence, assumptions, and work that still needs to be performed.

## Inputs to collect
1. **Task and intended use** — identify the decision this deliverable supports; required, with no default when different uses would change the method.
2. **Task material** — collect candidate key fields, records, intended row meaning; required for a completed assessment, otherwise produce an explicitly provisional plan.
3. **Scope and environment** — obtain the applicable artifact versions, time window, data population, and technical environment; default to the supplied material only, without implying full-system coverage.
4. **Acceptance criterion** — obtain the user's success condition and tolerable failure behavior; default to identifying unresolved conditions rather than inventing a universal threshold.
5. **Constraints and owner** — collect access restrictions, budget, schedule, and the person who can approve the next action; default to analysis only with the owner marked unassigned.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Keep a missing source distinguishable from a source that was inspected and contained no relevant evidence.

## Procedure
1. State the boundary of a key uniqueness report and name the source artifacts used; retain a version or observation date where available.
2. Define what one row represents
3. Group records by the candidate key
4. ⚠️ Distinguish repeated observations from accidental duplicates. Do not silently replace missing evidence with an assumed successful outcome.
5. Propose a corrected key or documented deduplication rule
6. Apply the domain check: Report counts with denominators and compare values under explicit normalization rules; never silently drop inconvenient records.
7. Verify the proposed result with this task-specific check: Check uniqueness on the declared compound key and preserve all legitimate rows. If the check cannot be performed, label it pending and explain what evidence would complete it.
8. Produce the actual requested artifact: concrete contract fields, matrix rows, comparison values, script lines, or ordered plan steps as appropriate. A recommendation to create the artifact is not the artifact; use the example's concrete deliverable as a structural illustration while replacing its facts with the user's supplied material.
9. Populate the output template with the artifact, decision, evidence, and next action; separate instructions to execute from results already observed.

Domain context: Quality checks must reflect the intended observation unit and business meaning. A repair can change the estimand or hide a collection defect, so retain the unmodified input and explain consequences. A conclusion only applies to the artifact, population, and conditions actually examined. Preserve enough input identifiers that another practitioner can repeat the review without relying on memory. When there are conflicting records, expose the conflict and select no preferred value without a stated reason.

The following offline fixture uses Python 3 and its standard language features. It is a runnable check of the example invariant, not a replacement for inspecting the real artifact. Save it as a temporary script and run it with the available Python 3 interpreter; successful completion means its assertions held. Change the fixture to include a failing case before relying on it. Record the interpreter version actually used; verify any additional package or platform behavior against its official documentation before adapting this check.

```python
rows=[('o1','l1'),('o1','l2')]; assert len(set(rows))==2 and len({r[0] for r in rows})==1
```

## Decision rules
- IF duplicate keys represent legitimate repeated events THEN extend the key rather than delete rows BECAUSE key failure is not proof of duplicate data.
- IF the task-specific verification cannot run on the supplied evidence THEN return a provisional result and name the missing artifact BECAUSE an unperformed check is not a pass.
- IF the proposed next action changes data, access, a live service, or a submitted artifact THEN identify the authorized owner and reversible preparation step BECAUSE analysis alone does not establish execution permission.
- IF an external platform rule, library behavior, or organizational requirement is relevant THEN check the current value in the official documentation or supplied governing policy BECAUSE a remembered value may not match the active environment.

## Output template
```text
Deliverable: <name; one line>
Scope: <artifacts, population, environment; at most two sentences>
Evidence: <observations with input references; at most six bullets>
Decision: <supported conclusion or provisional status; at most two sentences>
Artifact: <the concrete requested deliverable, with actual fields, entries, or draft text; at most 300 words>
Action: <owner, concrete next step, completion condition; at most three bullets>
Verification: <performed checks and results, or explicitly pending checks; at most three bullets>
Open items: <missing information or current-source checks; at most three bullets, or none>
```

## Quality checklist
- [ ] The deliverable is limited to the named task rather than a general domain tutorial.
- [ ] Each factual observation can be traced to supplied material or an explicitly fictional fixture.
- [ ] The task-specific branch condition is evaluated, or the missing evidence is identified.
- [ ] The decision states its scope and does not imply an unseen system was checked.
- [ ] The next action includes a completion condition and an owner or an unassigned marker.
- [ ] Verification distinguishes performed checks from proposed checks.
- [ ] Every external rule or changing requirement has a current-source check instead of a remembered constant.
- [ ] The example arithmetic and executable assertions agree with the stated conclusion.

## Anti-patterns
- **Title-only answer**: restating the request without producing a key uniqueness report. Fix: fill every field of the output template with task evidence or an explicit open item.
- **Skipped branch**: ignoring the condition that duplicate keys represent legitimate repeated events. Fix: evaluate that condition before recommending the next action.
- **Evidence laundering**: presenting a proposed test as a successful result. Fix: label it pending until an actual observation exists.
- **Universal threshold**: inventing a cutoff that the user did not supply. Fix: request an acceptance criterion or show the decision as conditional.
- **Scope creep**: turning a bounded review into an unsolicited production change. Fix: return an actionable handoff with the execution boundary stated.

## Worked example
**Input:**
> Fictional team Cedar Lantern requests a key uniqueness report. Order o1 has line items l1 and l2; order ID alone is proposed as the key. The team asks for an assessment only and supplies these facts as the complete example fixture.

**Output:**
```text
Deliverable: a key uniqueness report
Scope: Cedar Lantern's supplied fictional fixture; analysis only.
Evidence: Order ID repeats while the order-plus-line pair is unique.
Decision: Use the compound key if each row is an order line.
Artifact: Row meaning: order line item. Candidate key order_id fails for o1 because l1 and l2 are distinct legitimate lines. Proposed key: order_id plus line_item_id, subject to full-data uniqueness verification. Do not delete the second legitimate line as a duplicate.
Action: Team owner — Propose a corrected key or documented deduplication rule Completion condition: the task-specific verification is recorded.
Verification: The fixture supports the stated finding; real-environment check remains pending: Check uniqueness on the declared compound key and preserve all legitimate rows.
Open items: Confirm artifact versions and authorized owner before applying the recommendation outside this fixture.
```

**Bad output:**
> Everything looks ready; proceed without checking candidate key fields, records, intended row meaning.

This fails because it omits the evidence-dependent branch, substitutes confidence for verification, and cannot show why the proposed action follows from the supplied fixture.

## Edge cases
- **Conflicting artifacts**: identify the conflicting versions, state which decision depends on the conflict, and request the authoritative source before resolving it.
- **No usable example or record**: deliver only the method and a list of required evidence; do not fabricate a representative result.
- **Partial completion**: preserve completed observations, mark the remaining checks pending, and avoid describing the whole deliverable as verified.
- **Unexpected branch condition**: when duplicate keys represent legitimate repeated events, apply the stated decision rule and document its consequence instead of continuing the default path.

## Test case
**Input:**
> Fictional team Cedar Lantern asks for a key uniqueness report. Order o1 has line items l1 and l2; order ID alone is proposed as the key. Produce the assessment and identify what remains unverified.

**Assertions:**
1. The response uses all eight output fields in the specified order and Artifact contains concrete task output rather than only a recommendation to produce it.
2. It reflects this fixture-specific finding: Order ID repeats while the order-plus-line pair is unique.
3. It preserves this task-specific conclusion: Use the compound key if each row is an order line.
4. It includes the verification check or explicitly marks it pending: Check uniqueness on the declared compound key and preserve all legitimate rows.
5. It does not claim to have executed a production change or checked material that was not supplied.
