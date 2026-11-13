---
id: TST-011
name: regression-revision-boundary-isolation
domain: Software Verification Design
subdomain: Revision boundary isolation
version: 1.0
description: Narrow a reproducible regression to an evidenced revision boundary while preserving inconclusive builds and contradictory observations; use when a known working revision precedes a failing revision.
triggers: ["bisect a regression", "find the first failing revision", "isolate when this behavior changed", "handle unbuildable revisions during regression search", "narrow a regression commit range"]
not_for: ["minimizing a failing input [TST-004]", "diagnosing intermittent test behavior [TST-007]", "proving a code change is the root cause", "deploying a rollback"]
requires: []
risk_level: medium
---

# Regression Revision Boundary Isolation

## Purpose
Find the smallest supported revision interval containing a change in one reproducible behavior. Preserve inconclusive revisions and separate locating an observed transition from proving its causal mechanism.

## Inputs to collect
1. **Behavior oracle** — expected output, exact failure signature, fixture, and invocation. Why: an unrelated crash cannot stand in for the regression. Default: required; clarify an imprecise symptom before searching.
2. **Revision history** — immutable revision identities, known working and failing endpoints, and chosen ancestry path. Why: calendar order does not establish ancestry. Default: inspect supplied history; never invent a linear sequence through unrelated branches.
3. **Execution environment** — language/runtime versions, dependency resolution, configuration, services, and reset instructions. Why: environment drift can mimic code changes. Default: unresolved dependencies are recorded as blockers.
4. **Run authority and isolation** — permitted local commands, disposable checkout or equivalent isolation, and protected user work. Why: revision switching may overwrite files or run side effects. Default: analysis only until an authorized isolated execution path exists.
5. **Repeatability and stopping criteria** — agreed repeat checks, available resources, and acceptable interval width. Why: a passing retry does not settle intermittent behavior. Default: stop on inconsistent classifications or exhausted access, report the remaining interval.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Preserve the user's current checkout state and select an authorized isolated workspace for historical builds.
2. Define an oracle with separate outcomes: good means the target behavior satisfies the contract; bad means the exact target failure is reproduced; inconclusive means it was not evaluated reliably.
3. Reproduce both endpoints using the same fixture and comparable environment, recording actual commands, artifact identity, and logs.
4. Enumerate the chosen ancestry path between the endpoints and identify merges, reverts, or evidence of multiple behavior transitions.
5. State the working single-transition assumption: along this path the behavior changes from good to bad once. If evidence contradicts it, partition into supported intervals or investigate nonmonotonic behavior before continuing.
6. Select an untested revision near the middle of the remaining candidate interval, taking known unbuildable revisions into account.
7. Build and run the selected revision under its evidenced dependency/configuration requirements without modifying its relevant behavior.
8. ⚠️ Classify build errors, missing dependencies, timeouts before the oracle, and unrelated test failures as inconclusive; retain their reasons instead of labeling them bad.
9. Update the boundary only from good or bad results; retain skipped revisions inside the candidate set and choose another usable interior revision.
10. Recheck the final good and bad boundaries under the same oracle and compare their effective environments before reporting a unique introducing revision.
11. Inspect the boundary difference to propose a causal hypothesis and a discriminating follow-up; do not claim proof from temporal coincidence alone.
12. Save the run ledger and restore the original workspace state through the repository's normal non-destructive workflow.

Use the current version-control tool documentation to verify selection, skipped-revision handling, exit codes, and cleanup commands before automation. Do not hardcode remembered command semantics. Record the actual runtime version used for reference code.

This Python 3 reference checks candidate transitions in a supplied linear history. It does not run builds or prove the single-transition assumption. Each returned identity could be the first bad revision consistent with the observations; empty output signals inconsistent endpoints or observations.

```python
def candidates(ids, observations):
    if len(ids) != len(observations) or len(set(ids)) != len(ids):
        raise ValueError("aligned unique revision identities required")
    if any(x not in {"good", "bad", "unknown"} for x in observations):
        raise ValueError("invalid observation")
    if len(ids) < 2 or observations[0] != "good" or observations[-1] != "bad":
        return []
    return [ids[k] for k in range(1, len(ids))
            if all(x == "unknown" or x == ("good" if i < k else "bad")
                   for i, x in enumerate(observations))]

ids = ["A", "B", "C", "D", "E", "F"]
assert candidates(ids, ["good", "good", "unknown", "unknown", "bad", "bad"]) == ["C", "D", "E"]
assert candidates(ids, ["good", "good", "good", "bad", "bad", "bad"]) == ["D"]
assert candidates(ids, ["good", "bad", "unknown", "good", "bad", "bad"]) == []
print("ambiguous, unique, and contradictory histories checked")
```

## Decision rules
- IF endpoints do not reproduce their claimed classifications THEN repair the oracle or environment first BECAUSE the search has no evidenced bracket.
- IF a revision cannot reach the target oracle THEN retain it as inconclusive BECAUSE buildability and the target regression are different properties.
- IF inconclusive revisions remain between the last good and first bad observations THEN report all compatible candidates BECAUSE the first testable failure need not be the introducing revision.
- IF a later good observation follows an earlier bad observation on the chosen path THEN stop monotonic narrowing BECAUSE a single-transition explanation is contradicted.
- IF dependency or configuration changes affect the result THEN report the combined boundary and isolate that factor BECAUSE revision identity alone does not identify the mechanism.

## Output template
```text
Oracle: <contract, fixture, target failure; maximum 80 words>
Scope: <ancestry path, endpoint identities, environment; maximum 80 words>
Run ledger: <one row per observed revision; attach overflow>
Revision | Environment/build | Oracle outcome | Evidence | Skip reason
Boundary: <last evidenced good, first evidenced bad, possible first-bad identities>
Assumptions: <single-transition/comparability evidence and unresolved limits; maximum 100 words>
Next check: <one discriminating test or prerequisite; maximum 60 words>
Workspace: <isolation and restoration status; maximum 40 words>
```

## Quality checklist
- [ ] Endpoint classifications are reproduced or explicitly unverified.
- [ ] Immutable revision identities and ancestry path are recorded.
- [ ] Target failure is distinguished from infrastructure failures.
- [ ] Inconclusive revisions retain reasons and candidate membership.
- [ ] Environment differences are visible in the ledger.
- [ ] Contradictory observations stop single-transition inference.
- [ ] Unique-boundary claims have no intervening unresolved candidate.
- [ ] Causal hypotheses and performed checks are distinguished.
- [ ] User work and restoration status are accounted for.

## Anti-patterns
- **Any failure is bad**: a dependency download error advances the bad bound. Fix: mark inconclusive until the target behavior runs.
- **Skipping erases candidates**: the first buildable failure becomes the blamed revision. Fix: retain every compatible untested transition.
- **Branch flattening**: timestamps replace ancestry. Fix: state and justify a path or analyze separate branches.
- **Environment amnesia**: compare results built with incompatible assumptions. Fix: record effective dependencies and configuration.
- **Causal leap**: blame the author of a boundary revision. Fix: propose a mechanism and discriminating test without assigning personal fault.

## Worked example
**Input:** Fictional team Birch supplies linear revisions A through F. Its deterministic fixture passes on A and B and reproduces the exact regression on E and F. C cannot build because its historical dependency is unavailable; D has not run. The environment is otherwise comparable, and a single transition is assumed. Work occurred in an isolated checkout that was restored.

**Output:**
```text
Oracle: Supplied deterministic fixture; pass is good, exact reported regression is bad.
Scope: Linear ancestry A-B-C-D-E-F; A good and F bad reproduced; comparable recorded environment except C's unavailable dependency.
Run ledger:
Revision | Environment/build | Oracle outcome | Evidence | Skip reason
A | comparable | good | recorded fixture pass | none
B | comparable | good | recorded fixture pass | none
C | build blocked | inconclusive | dependency unavailable | target oracle never ran
D | untested | unknown | no run | not yet selected
E | comparable | bad | target regression reproduced | none
F | comparable | bad | target regression reproduced | none
Boundary: Last evidenced good B; first evidenced bad E; possible first-bad revisions C, D, E.
Assumptions: One transition assumed; C remains a candidate despite being unbuildable. No unique culprit or causal mechanism established.
Next check: Run D under its recorded environment; recover C's dependency if needed to narrow the remaining interval.
Workspace: Isolated checkout used; original workspace restored as supplied.
```

**Bad output:** “E introduced the bug because C could not build and D was skipped.”
This incorrectly removes untested candidates and treats a boundary observation as causal proof.

## Edge cases
- **Intermittent oracle**: retain inconsistent observations; route to repeatability investigation before using binary classifications.
- **All interior builds unavailable**: report the full compatible candidate set and required historical dependencies.
- **Merge boundary**: retain merge identity and parent comparisons; do not invent a total ordering across both branches.
- **Fixture incompatible with older code**: adapt only the harness interface with documented equivalence; otherwise mark the revision inconclusive.
- **Bad-good-bad history**: preserve all observations and identify separate intervals; do not force a single introducing revision.

## Test case
**Input:**
> Fictional revisions J-K-L-M form a linear path. J passes the target fixture; K cannot build; L has not run; M reproduces the target regression. Assume one transition. Identify what can be concluded.

**Assertions:**
1. The possible introducing revisions include K, L, and M.
2. K is inconclusive rather than classified bad from its build failure.
3. The output requests a usable interior run or missing build prerequisite.
4. No unique culprit or causal mechanism is claimed.
