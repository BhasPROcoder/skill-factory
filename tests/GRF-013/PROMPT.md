Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-013
name: graph-community-partition-sensitivity
domain: Graph Engineering Foundations
subdomain: Community output comparison
version: 1.0
description: Compare supplied graph community partitions across controlled run changes using label-invariant membership evidence while separating assignment instability from node-coverage and projection changes.
triggers: ["compare graph community runs", "check community partition sensitivity", "did renamed cluster labels change membership", "explain split and merge evidence between partitions", "compare communities after changing graph filters"]
not_for: ["computing weak components [GRF-007]", "strong-component condensation [GRF-008]", "supervised model baseline evaluation [TML-002]", "overlapping or probabilistic memberships", "inferring social identities from graph groups"]
requires: []
risk_level: medium
---

# Graph Community Partition Sensitivity

## Purpose
Identify which membership relationships persist or change between supplied community-detection runs. Compare membership rather than arbitrary community labels, and expose changes in included nodes or assignment coverage before summarizing agreement. Stable output does not establish that the groups represent true communities or useful domain categories.

## Inputs to collect
1. **Run manifests** — obtain graph revision, projection rules, algorithm configuration, randomization record and execution status for each run. Why: several changed factors prevent attributing a difference to one cause. Default: unknown factors remain explicit; do not claim a controlled experiment.
2. **Node inventories and identities** — collect the included IDs for every run and any evidenced identity mapping. Why: identical labels can hide changed populations. Default: exact shared IDs only; retain added and removed nodes separately.
3. **Partition records** — obtain one community label or explicit unassigned marker per included node. Why: missing rows, unassigned nodes and singleton groups are different states. Default: no inferred assignments; reject duplicate rows before creating a mapping.
4. **Comparison scope** — specify reference run, proposed perturbations and whether the graph population should remain fixed. Why: comparing different projections answers a different question from solver repeatability. Default: describe the supplied comparison without inventing reruns.
5. **Decision and tolerances** — identify what will use the groups and which changes matter. Why: a high aggregate agreement can conceal changes involving critical nodes. Default: report counts and witnesses without a universal pass threshold.
6. **Execution capability** — establish whether original runs can be repeated and which implementation version is installed. Why: a partition file alone cannot prove reproducible computation. Default: compare supplied outputs only; verify current implementation options in official documentation before rerunning.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze each run's graph and partition evidence with its manifest; distinguish executed output from a proposed configuration.
2. Audit partition coverage against each inventory, rejecting duplicate IDs, unknown nodes or unsupported multiple memberships. Retain explicit unassigned nodes rather than silently placing them in one group.
3. Build a change ledger for graph revision, projection, parameters, seed and node universe. Attribute a difference to a factor only when the comparison design supports that attribution.
4. Define the comparison cohort as shared nodes assigned in both runs, and separately report shared unassigned nodes, assignment-status changes, additions and removals.
5. Build an overlap table counting nodes for each reference-label/candidate-label pair. Treat the labels as local to their run; do not align them by spelling or numeric order.
6. Compare every unordered pair in the cohort by whether its endpoints share a label in each run. Classify pairs as together in both, separated in both, split, or joined.
7. ⚠️ Report all four counts and the pair denominator. A large number of separated-in-both pairs can dominate agreement, so do not call a partition stable from one aggregate fraction alone.
8. Retain concrete changed-pair witnesses and affected node sets. Inspect overlap rows and columns for split/merge patterns without forcing a one-to-one label correspondence.
9. If reruns are available, vary one declared factor at a time where feasible and repeat the same cohort and count checks. Record joint changes separately and preserve execution failures as missing comparisons.
10. Deliver the comparison and its decision implications. Distinguish reproducibility under tested perturbations from domain validity, and request domain evidence before interpreting group labels as meaningful categories.

This Python 3 reference compares two small in-memory maps from nonempty string node IDs to string labels or None for explicit unassigned state. Duplicate input rows must be caught before mapping; the reference cannot recover them. It does not run community detection or inspect graph edges. Execute the snippet with the available interpreter and record its version. Pair enumeration is intended for small fixtures; use an independently verified counting implementation for large cohorts.

```python
from itertools import combinations

def compare(reference, candidate):
    for run in (reference, candidate):
        if any(not isinstance(n, str) or not n for n in run):
            raise ValueError("nonempty string node IDs required")
        if any(v is not None and
               (not isinstance(v, str) or not v) for v in run.values()):
            raise ValueError("string label or explicit None required")
    shared = set(reference) & set(candidate)
    cohort = sorted(n for n in shared
                    if reference[n] is not None and candidate[n] is not None)
    statuses = {n: (reference[n] is not None, candidate[n] is not None)
                for n in sorted(shared) if n not in cohort}
    overlap, groups = {}, {k: [] for k in ("both", "apart", "split", "joined")}
    for n in cohort:
        key = (reference[n], candidate[n])
        overlap[key] = overlap.get(key, 0) + 1
    for a, b in combinations(cohort, 2):
        old = reference[a] == reference[b]
        new = candidate[a] == candidate[b]
        kind = "both" if old and new else "split" if old else "joined" if new else "apart"
        groups[kind].append((a, b))
    counts = {k: len(v) for k, v in groups.items()}
    total = len(cohort) * (len(cohort) - 1) // 2
    assert sum(counts.values()) == total
    return {"cohort": cohort, "reference_only": sorted(set(reference)-shared),
            "candidate_only": sorted(set(candidate)-shared), "statuses": statuses,
            "overlap": overlap, "counts": counts, "pairs": groups,
            "denominator": total,
            "agreement": None if total == 0 else (counts["both"]+counts["apart"], total)}

old = {"A": "red", "B": "red", "C": "blue", "D": "blue", "E": None}
new = {"A": "one", "B": "two", "C": "one", "D": "two", "E": "three"}
result = compare(old, new)
assert result["counts"] == {"both": 0, "apart": 2, "split": 2, "joined": 2}
assert result["agreement"] == (2, 6)
assert result["statuses"] == {"E": (False, True)}
renamed = {"A": "q", "B": "q", "C": "p", "D": "p", "E": None}
assert compare(old, renamed)["agreement"] == (6, 6)
assert compare({"A": "x"}, {"A": "y"})["agreement"] is None
print("relabeling, pair changes, assignment coverage and empty denominator passed")
```

## Decision rules
- IF only label names change while co-membership stays identical THEN report unchanged membership BECAUSE labels are run-local identifiers.
- IF node coverage changes THEN disclose the restricted comparison cohort BECAUSE agreement on surviving nodes does not describe the whole population.
- IF a node is unassigned in either run THEN exclude it from pair counts and report its state BECAUSE shared unassigned markers do not define a community.
- IF several run factors changed THEN describe sensitivity without assigning one cause BECAUSE the comparison does not isolate that cause.
- IF pair agreement is high but important pairs change THEN show those witnesses BECAUSE aggregate agreement can mask decision-relevant instability.

## Output template
```text
Scope: <run IDs, graph/projection evidence and controlled changes; maximum 90 words>
Coverage: <inventories, comparison cohort, added/removed/unassigned/status-changed nodes>
Overlap: <reference label | candidate label | count; full table or attachment>
Pair evidence: <both/apart/split/joined counts, denominator, agreement or undefined>
Changed witnesses: <split/joined node pairs and affected nodes; full attachment if large>
Checks: <coverage, count reconciliation, relabeling and execution evidence>
Interpretation: <supported sensitivity, confounding and decision implication; maximum 100 words>
Next evidence: <rerun or domain validation needed; maximum 70 words>
```

## Quality checklist
- [ ] Run manifests distinguish graph changes from solver changes.
- [ ] Node identity and assignment coverage are reconciled before comparison.
- [ ] Labels are compared through membership rather than their spelling.
- [ ] Unassigned states never become a shared community by default.
- [ ] Four pair counts sum to the stated denominator.
- [ ] Changed-pair witnesses resolve to original node IDs.
- [ ] Undefined small-cohort agreement is not reported as perfect stability.
- [ ] Stability conclusions remain separate from domain truth.

## Anti-patterns
- **Label-number drift**: call group 1 becoming group 2 a change. Fix: compare co-membership.
- **Missing means singleton**: silently assign omitted nodes unique labels. Fix: reconcile inventories and explicit states.
- **Noise becomes community**: group every unassigned node together. Fix: exclude and report those states.
- **One score declares truth**: equate stable partitions with real communities. Fix: obtain independent domain evidence.
- **Confounded cause**: blame a parameter while graph filters also changed. Fix: record joint changes or rerun a controlled comparison.

## Worked example
**Input:** Fictional studio Birch supplies runs R1/R2 from the snippet on nodes A–E. Both outputs are available, but the run manifests are missing. E is unassigned in R1 and singleton-assigned in R2. Compare the partitions without claiming a cause.

**Output:**
```text
Scope: Birch R1/R2 supplied outputs; graph/projection/configuration changes unknown.
Coverage: Both inventories A–E. Pair cohort A/B/C/D; E changes unassigned to assigned and is excluded from pair counts. No added or removed IDs.
Overlap: red|one|1; red|two|1; blue|one|1; blue|two|1.
Pair evidence: both 0, apart 2, split 2, joined 2; denominator 6; agreement 2/6.
Changed witnesses: split A-B,C-D; joined A-C,B-D; affected nodes A/B/C/D.
Checks: Reference assertions reconcile six pairs and assignment-state evidence when executed; renamed equivalent labels give 6/6.
Interpretation: Co-membership changes within the common assigned cohort. Cause and whole-population stability are unresolved; no domain-community validity established.
Next evidence: Supply run manifests and a decision-relevant tolerance; rerun controlled factors if attribution is required.
```

**Bad output:** "R2 is better because it has three communities, and two-thirds of nodes changed labels."
This invents quality from group count and compares arbitrary labels rather than membership.

## Edge cases
- **Fewer than two comparable assigned nodes**: report zero pair denominator and undefined agreement, retaining coverage evidence.
- **All singleton groups**: report separated-in-both dominance explicitly; perfect agreement alone supplies no meaningful grouping validation.
- **Overlapping memberships**: stop this hard-partition comparison and specify an appropriate set-valued method; do not choose one label arbitrarily.
- **Node splits or merges between snapshots**: require an evidenced identity comparison policy; raw intersection alone may not answer the intended question.
- **Incomplete output file**: keep absent records separate from explicit unassigned states and withhold a complete-run comparison.

## Test case
**Input:**
> Fictional runs both include P/Q/R. R1 assigns P/Q to a and R to b; R2 assigns P/Q to renamed label z and leaves R explicitly unassigned. Compare membership with no manifest or rerun access.

**Assertions:**
1. Compares only P/Q and reports one together-in-both pair with denominator one.
2. Reports R's assigned-to-unassigned change outside pair counts.
3. Does not treat renaming a to z as membership change.
4. Limits agreement to the comparable cohort without asserting whole-run stability or a cause.
</skill>

<user_request>
Fictional runs both include P/Q/R. R1 assigns P/Q to a and R to b; R2 assigns P/Q to renamed label z and leaves R explicitly unassigned. Compare membership with no manifest or rerun access.
</user_request>
