---
id: TSC-004
name: security-dependency-advisory-triage
domain: Defensive Security Review
subdomain: Response preparation
version: 1.0
description: Produce a dependency advisory triage report; use when the task is to security dependency advisory triage.
triggers: ["security dependency advisory triage", "help with a dependency advisory triage report", "review my a dependency advisory triage report", "prepare a dependency advisory triage report", "check security dependency advisory triage evidence"]
not_for: ["security logging sensitive data review [TSC-005]", "security trust boundary map [TSC-006]"]
requires: []
risk_level: high
---

# Security Dependency Advisory Triage

## Purpose
Create a dependency advisory triage report that another practitioner can use to make the stated decision. This skill handles the narrow task named above; its result must distinguish observed evidence, assumptions, and work that still needs to be performed.

## Inputs to collect
1. **Task and intended use** — identify the decision this deliverable supports; required, with no default when different uses would change the method.
2. **Task material** — collect dependency inventory, exact versions, official advisory, usage path; required for a completed assessment, otherwise produce an explicitly provisional plan.
3. **Scope and environment** — obtain the applicable artifact versions, time window, data population, and technical environment; default to the supplied material only, without implying full-system coverage.
4. **Acceptance criterion** — obtain the user's success condition and tolerable failure behavior; default to identifying unresolved conditions rather than inventing a universal threshold.
5. **Constraints and owner** — collect access restrictions, budget, schedule, and the person who can approve the next action; default to analysis only with the owner marked unassigned.
6. **Jurisdiction and authorization** — required for security work: country, organizational context, system owner, permitted assets, and review boundaries; there is no silent default.

If a required input is missing and has no safe default, ask in one message with at most 3 questions. Keep a missing source distinguishable from a source that was inspected and contained no relevant evidence.

## Procedure
1. State the boundary of a dependency advisory triage report and name the source artifacts used; retain a version or observation date where available.
2. Match the installed component to the official advisory's affected conditions
3. Determine whether the relevant functionality is used
4. ⚠️ Separate confirmed applicability from unresolved reachability Do not silently replace missing evidence with an assumed successful outcome.
5. Prepare mitigation and verification questions for the owner
6. Apply the domain check: Use current official vendor advisories and organizational policy when requirements matter; do not claim a vulnerability is exploitable from a scanner label alone.
7. Verify the proposed result with this task-specific check: Check the current official advisory against the resolved dependency version and usage conditions. If the check cannot be performed, label it pending and explain what evidence would complete it.
8. Populate the output template with the decision, its evidence, and the next action; separate instructions to execute from results already observed.

Domain context: Security findings need an asset boundary, evidence of the condition, a plausible impact, and an authorized owner. These skills organize defensive review and do not authorize scanning, exploitation, credential access, or changes outside the stated scope. A conclusion only applies to the artifact, population, and conditions actually examined. Preserve enough input identifiers that another practitioner can repeat the review without relying on memory. When there are conflicting records, expose the conflict and select no preferred value without a stated reason.

For security decisions, knowledge has a cutoff: verify current requirements in the applicable regulator guidance, vendor security documentation, and organization policy. Use `[VERIFY: applicable requirement and its official source]` where evidence is unavailable. Escalate suspected active compromise or disputed authority to the responsible security professional; consult a licensed legal professional for legal interpretations. This workflow does not authorize intrusion, exploitation, or changes to another party’s systems.

The following offline fixture uses Python 3 and its standard language features. It is a runnable check of the example invariant, not a replacement for inspecting the real artifact. Save it as a temporary script and run it with the available Python 3 interpreter; successful completion means its assertions held. Change the fixture to include a failing case before relying on it. Record the interpreter version actually used; verify any additional package or platform behavior against its official documentation before adapting this check.

```python
inventory={'name':'Cedar','version':None}; assert inventory['version'] is None
```

## Decision rules
- IF the exact installed version is unknown THEN leave applicability unresolved BECAUSE a package name alone cannot establish affected status.
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
- **Title-only answer**: restating the request without producing a dependency advisory triage report. Fix: fill every field of the output template with task evidence or an explicit open item.
- **Skipped branch**: ignoring the condition that the exact installed version is unknown. Fix: evaluate that condition before recommending the next action.
- **Evidence laundering**: presenting a proposed test as a successful result. Fix: label it pending until an actual observation exists.
- **Universal threshold**: inventing a cutoff that the user did not supply. Fix: request an acceptance criterion or show the decision as conditional.
- **Scope creep**: turning a bounded review into an unsolicited production change. Fix: return an actionable handoff with the execution boundary stated.

## Worked example
**Input:**
> Fictional team Cedar Lantern requests a dependency advisory triage report. The inventory names library Cedar but omits its version; an advisory affects a specified version range. The team asks for an assessment only and supplies these facts as the complete example fixture.

**Output:**
```text
Deliverable: a dependency advisory triage report
Scope: Cedar Lantern's supplied fictional fixture; analysis only.
Evidence: Installed-version evidence is missing.
Decision: Identify the actual installed artifact before asserting applicability.
Action: Team owner — Prepare mitigation and verification questions for the owner Completion condition: the task-specific verification is recorded.
Verification: The fixture supports the stated finding; real-environment check remains pending: Check the current official advisory against the resolved dependency version and usage conditions.
Open items: Confirm artifact versions and authorized owner before applying the recommendation outside this fixture.
```

**Bad output:**
> Everything looks ready; proceed without checking dependency inventory, exact versions, official advisory, usage path.

This fails because it omits the evidence-dependent branch, substitutes confidence for verification, and cannot show why the proposed action follows from the supplied fixture.

## Edge cases
- **Conflicting artifacts**: identify the conflicting versions, state which decision depends on the conflict, and request the authoritative source before resolving it.
- **No usable example or record**: deliver only the method and a list of required evidence; do not fabricate a representative result.
- **Partial completion**: preserve completed observations, mark the remaining checks pending, and avoid describing the whole deliverable as verified.
- **Unexpected branch condition**: when the exact installed version is unknown, apply the stated decision rule and document its consequence instead of continuing the default path.

## Test case
**Input:**
> Fictional team Cedar Lantern asks for a dependency advisory triage report. The inventory names library Cedar but omits its version; an advisory affects a specified version range. Produce the assessment and identify what remains unverified.

**Assertions:**
1. The response uses all seven output fields in the specified order.
2. It reflects this fixture-specific finding: Installed-version evidence is missing.
3. It preserves this task-specific conclusion: Identify the actual installed artifact before asserting applicability.
4. It includes the verification check or explicitly marks it pending: Check the current official advisory against the resolved dependency version and usage conditions.
5. It does not claim to have executed a production change or checked material that was not supplied.
