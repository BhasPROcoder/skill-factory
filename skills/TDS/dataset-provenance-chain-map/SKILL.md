---
id: TDS-002
name: dataset-provenance-chain-map
domain: Dataset Intake and Documentation
subdomain: Provenance
version: 1.0
description: Produce a dataset provenance chain; use when the task is to dataset provenance chain map.
triggers: ["dataset provenance chain map", "help with a dataset provenance chain", "review my a dataset provenance chain", "prepare a dataset provenance chain", "check dataset provenance chain map evidence"]
not_for: ["dataset license evidence inventory [TDS-003]", "dataset data dictionary build [TDS-004]"]
requires: []
risk_level: medium
---

# Dataset Provenance Chain Map

## Purpose
Create a dataset provenance chain that another practitioner can use to make the stated decision. This skill handles the narrow task named above; its result must distinguish observed evidence, assumptions, and work that still needs to be performed.

## Inputs to collect
1. **Task and intended use** — identify the decision this deliverable supports; required, with no default when different uses would change the method.
2. **Task material** — collect source inventory, acquisition notes, transformation records, release identifiers; required for a completed assessment, otherwise produce an explicitly provisional plan.
3. **Scope and environment** — obtain the applicable artifact versions, time window, data population, and technical environment; default to the supplied material only, without implying full-system coverage.
4. **Acceptance criterion** — obtain the user's success condition and tolerable failure behavior; default to identifying unresolved conditions rather than inventing a universal threshold.
5. **Constraints and owner** — collect access restrictions, budget, schedule, and the person who can approve the next action; default to analysis only with the owner marked unassigned.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Keep a missing source distinguishable from a source that was inspected and contained no relevant evidence.

## Procedure
1. State the boundary of a dataset provenance chain and name the source artifacts used; retain a version or observation date where available.
2. List the original source for each acquired artifact
3. Connect derived artifacts to their immediate parents
4. ⚠️ Flag transformations with no recorded inputs or parameters Do not silently replace missing evidence with an assumed successful outcome.
5. Create a lineage table with unresolved links assigned to owners
6. Apply the domain check: Separate permission to access from permission to redistribute; retain acquisition and transformation provenance.
7. Verify the proposed result with this task-specific check: Trace every released artifact to a documented source or an explicit unresolved node. If the check cannot be performed, label it pending and explain what evidence would complete it.
8. Populate the output template with the decision, its evidence, and the next action; separate instructions to execute from results already observed.

Domain context: Dataset suitability is specific to a population, intended prediction or analysis, and collection process. A convenient download is not evidence of representative coverage. A conclusion only applies to the artifact, population, and conditions actually examined. Preserve enough input identifiers that another practitioner can repeat the review without relying on memory. When there are conflicting records, expose the conflict and select no preferred value without a stated reason.

The following offline fixture uses Python 3 and its standard language features. It is a runnable check of the example invariant, not a replacement for inspecting the real artifact. Save it as a temporary script and run it with the available Python 3 interpreter; successful completion means its assertions held. Change the fixture to include a failing case before relying on it. Record the interpreter version actually used; verify any additional package or platform behavior against its official documentation before adapting this check.

```python
parents={'C':'R','M':None}; assert parents['C']=='R' and parents['M'] is None
```

## Decision rules
- IF a derived file has no identifiable parent THEN mark its provenance incomplete BECAUSE a filename alone cannot establish derivation.
- IF the task-specific verification cannot run on the supplied evidence THEN return a provisional result and name the missing artifact BECAUSE an unperformed check is not a pass.
- IF the proposed next action changes data, access, a live service, or a submitted artifact THEN identify the authorized owner and reversible preparation step BECAUSE analysis alone does not establish execution permission.
- IF an external platform rule, library behavior, or organizational requirement is relevant THEN check the current value in the official documentation or supplied governing policy BECAUSE a remembered value may not match the active environment.

## Output template
```text
Deliverable: <name; one line>
Scope: <artifacts, population, environment; at most two sentences>
Evidence: <observations with input references; at most six bullets>
Decision: <supported conclusion or provisional status; at most two sentences>
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
- **Title-only answer**: restating the request without producing a dataset provenance chain. Fix: fill every field of the output template with task evidence or an explicit open item.
- **Skipped branch**: ignoring the condition that a derived file has no identifiable parent. Fix: evaluate that condition before recommending the next action.
- **Evidence laundering**: presenting a proposed test as a successful result. Fix: label it pending until an actual observation exists.
- **Universal threshold**: inventing a cutoff that the user did not supply. Fix: request an acceptance criterion or show the decision as conditional.
- **Scope creep**: turning a bounded review into an unsolicited production change. Fix: return an actionable handoff with the execution boundary stated.

## Worked example
**Input:**
> Fictional team Cedar Lantern requests a dataset provenance chain. Raw extract R becomes cleaned file C; model table M is present but has no recorded parent. The team asks for an assessment only and supplies these facts as the complete example fixture.

**Output:**
```text
Deliverable: a dataset provenance chain
Scope: Cedar Lantern's supplied fictional fixture; analysis only.
Evidence: The R-to-C link is documented; M has an unresolved parent.
Decision: Use C only within its documented scope and resolve M's lineage before relying on it.
Action: Team owner — Create a lineage table with unresolved links assigned to owners Completion condition: the task-specific verification is recorded.
Verification: The fixture supports the stated finding; real-environment check remains pending: Trace every released artifact to a documented source or an explicit unresolved node.
Open items: Confirm artifact versions and authorized owner before applying the recommendation outside this fixture.
```

**Bad output:**
> Everything looks ready; proceed without checking source inventory, acquisition notes, transformation records, release identifiers.

This fails because it omits the evidence-dependent branch, substitutes confidence for verification, and cannot show why the proposed action follows from the supplied fixture.

## Edge cases
- **Conflicting artifacts**: identify the conflicting versions, state which decision depends on the conflict, and request the authoritative source before resolving it.
- **No usable example or record**: deliver only the method and a list of required evidence; do not fabricate a representative result.
- **Partial completion**: preserve completed observations, mark the remaining checks pending, and avoid describing the whole deliverable as verified.
- **Unexpected branch condition**: when a derived file has no identifiable parent, apply the stated decision rule and document its consequence instead of continuing the default path.

## Test case
**Input:**
> Fictional team Cedar Lantern asks for a dataset provenance chain. Raw extract R becomes cleaned file C; model table M is present but has no recorded parent. Produce the assessment and identify what remains unverified.

**Assertions:**
1. The response uses all seven output fields in the specified order.
2. It reflects this fixture-specific finding: The R-to-C link is documented; M has an unresolved parent.
3. It preserves this task-specific conclusion: Use C only within its documented scope and resolve M's lineage before relying on it.
4. It includes the verification check or explicitly marks it pending: Trace every released artifact to a documented source or an explicit unresolved node.
5. It does not claim to have executed a production change or checked material that was not supplied.
