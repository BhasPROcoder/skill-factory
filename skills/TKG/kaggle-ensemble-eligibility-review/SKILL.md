---
id: TKG-007
name: kaggle-ensemble-eligibility-review
domain: Kaggle Competition Workflows
subdomain: Experiments
version: 1.1
description: Create an ensemble candidate review from supplied evidence; use when preparing or reviewing ensemble candidate review decisions.
triggers: ["kaggle ensemble eligibility review", "help with an ensemble candidate review", "review my ensemble candidate review", "prepare an ensemble candidate review", "check the evidence for this ensemble candidate review"]
not_for: ["kaggle notebook rerun readiness [TKG-008]", "kaggle final submission selection [TKG-009]"]
requires: []
risk_level: medium
---

# Kaggle Ensemble Eligibility Review

## Purpose
Create an ensemble candidate review that another practitioner can use to make the stated decision. This skill handles the narrow task named above; its result must distinguish observed evidence, assumptions, and work that still needs to be performed.

## Inputs to collect
1. **Task and intended use** — identify the decision this deliverable supports; required, with no default when different uses would change the method.
2. **Task material** — collect candidate predictions, common row identifiers, validation evidence, current rules; required for a completed assessment, otherwise produce an explicitly provisional plan.
3. **Scope and environment** — obtain the applicable artifact versions, time window, data population, and technical environment; default to the supplied material only, without implying full-system coverage.
4. **Acceptance criterion** — obtain the user's success condition and tolerable failure behavior; default to identifying unresolved conditions rather than inventing a universal threshold.
5. **Constraints and owner** — collect access restrictions, budget, schedule, and the person who can approve the next action; default to analysis only with the owner marked unassigned.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Keep a missing source distinguishable from a source that was inspected and contained no relevant evidence.

## Procedure
1. State the boundary of an ensemble candidate review and name the source artifacts used; retain a version or observation date where available.
2. Confirm all candidate artifacts are allowed under the competition rules
3. Align predictions and target semantics across candidates
4. ⚠️ Compare ensemble choices on held-out evidence without fitting to final test labels. Do not silently replace missing evidence with an assumed successful outcome.
5. Record candidate provenance and the chosen combination rule
6. Apply the domain check: Keep local validation, public feedback, final selection, and rule compliance as separate evidence; never infer hidden labels or redistribute restricted competition material.
7. Verify the proposed result with this task-specific check: Verify row identity before recomputing the proposed weighted combination. If the check cannot be performed, label it pending and explain what evidence would complete it.
8. Produce the actual requested artifact: concrete contract fields, matrix rows, comparison values, script lines, or ordered plan steps as appropriate. A recommendation to create the artifact is not the artifact; use the example's concrete deliverable as a structural illustration while replacing its facts with the user's supplied material.
9. Populate the output template with the artifact, decision, evidence, and next action; separate instructions to execute from results already observed.

Domain context: Use the specific competition page, rules, data description, evaluation definition, and submission instructions as inputs. Check their current versions; do not assume that limits, external-data permissions, team rules, or notebook requirements match another competition. A conclusion only applies to the artifact, population, and conditions actually examined. Preserve enough input identifiers that another practitioner can repeat the review without relying on memory. When there are conflicting records, expose the conflict and select no preferred value without a stated reason.

The following offline fixture uses Python 3 and its standard language features. It is a runnable check of the example invariant, not a replacement for inspecting the real artifact. Save it as a temporary script and run it with the available Python 3 interpreter; successful completion means its assertions held. Change the fixture to include a failing case before relying on it. Record the interpreter version actually used; verify any additional package or platform behavior against its official documentation before adapting this check.

```python
a={'x':0.2,'y':0.8}; b={'y':0.6,'x':0.4}; blend={k:(a[k]+b[k])/2 for k in a}; assert abs(blend['x']-0.3)<1e-12
```

## Decision rules
- IF candidate rows or target meanings differ THEN repair alignment before combining BECAUSE arithmetic blending cannot fix semantic mismatches.
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
- **Title-only answer**: restating the request without producing an ensemble candidate review. Fix: fill every field of the output template with task evidence or an explicit open item.
- **Skipped branch**: ignoring the condition that candidate rows or target meanings differ. Fix: evaluate that condition before recommending the next action.
- **Evidence laundering**: presenting a proposed test as a successful result. Fix: label it pending until an actual observation exists.
- **Universal threshold**: inventing a cutoff that the user did not supply. Fix: request an acceptance criterion or show the decision as conditional.
- **Scope creep**: turning a bounded review into an unsolicited production change. Fix: return an actionable handoff with the execution boundary stated.

## Worked example
**Input:**
> Fictional team Cedar Lantern requests an ensemble candidate review. Two eligible models predict probabilities for the same target on the same rows; one file reverses row order. The team asks for an assessment only and supplies these facts as the complete example fixture.

**Output:**
```text
Deliverable: an ensemble candidate review
Scope: Cedar Lantern's supplied fictional fixture; analysis only.
Evidence: The files cannot be blended safely by row position.
Decision: Align identifiers and evaluate a declared combination on local held-out data.
Artifact: Identifier-aligned example: x predictions 0.2 and 0.4 → equal-weight mean 0.3; y predictions 0.8 and 0.6 → mean 0.7. This is a proposed combination, not a performance claim. Validate eligibility and held-out results before selecting weights.
Action: Team owner — Record candidate provenance and the chosen combination rule Completion condition: the task-specific verification is recorded.
Verification: The fixture supports the stated finding; real-environment check remains pending: Verify row identity before recomputing the proposed weighted combination.
Open items: Confirm artifact versions and authorized owner before applying the recommendation outside this fixture.
```

**Bad output:**
> Everything looks ready; proceed without checking candidate predictions, common row identifiers, validation evidence, current rules.

This fails because it omits the evidence-dependent branch, substitutes confidence for verification, and cannot show why the proposed action follows from the supplied fixture.

## Edge cases
- **Conflicting artifacts**: identify the conflicting versions, state which decision depends on the conflict, and request the authoritative source before resolving it.
- **No usable example or record**: deliver only the method and a list of required evidence; do not fabricate a representative result.
- **Partial completion**: preserve completed observations, mark the remaining checks pending, and avoid describing the whole deliverable as verified.
- **Unexpected branch condition**: when candidate rows or target meanings differ, apply the stated decision rule and document its consequence instead of continuing the default path.

## Test case
**Input:**
> Fictional team Cedar Lantern asks for an ensemble candidate review. Two eligible models predict probabilities for the same target on the same rows; one file reverses row order. Produce the assessment and identify what remains unverified.

**Assertions:**
1. The response uses all eight output fields in the specified order and Artifact contains concrete task output rather than only a recommendation to produce it.
2. It reflects this fixture-specific finding: The files cannot be blended safely by row position.
3. It preserves this task-specific conclusion: Align identifiers and evaluate a declared combination on local held-out data.
4. It includes the verification check or explicitly marks it pending: Verify row identity before recomputing the proposed weighted combination.
5. It does not claim to have executed a production change or checked material that was not supplied.
