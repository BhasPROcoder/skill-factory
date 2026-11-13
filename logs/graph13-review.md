# GRF-013 independent review

Reviewer: community_review, 2026-11-14. Decision: accept for coordinator ingestion/checks; no blocking findings. Only this log was changed. No registry status was changed.

## Scope and comparison

Read AGENTS.md, SPEC.md and the complete draft. Queried sf.py for TAN-008, TML-002, GRF-007 and GRF-008, then inspected their actual inputs and numbered procedures. TAN-008 varies scalar scenario assumptions; TML-002 compares baseline/candidate scores against held-out labels. GRF-007 computes weak connectivity and GRF-008 computes mutual-reachability regions. GRF-013 instead compares supplied hard community assignments with node-universe reconciliation, assignment-state evidence, run-local-label invariance and changed co-membership witnesses. That deliverable and its confounding decisions are distinct from these selected neighbors. This is a targeted comparison, not proof of exhaustive semantic uniqueness.

## Actual executed checks

Extracted the Python code fence directly from the draft and executed it with Python 3.14.6. Observed embedded output: `relabeling, pair changes, assignment coverage and empty denominator passed`.

Independent fixtures and actual asserted results:

- Published test: P/Q remain together under renamed labels while R becomes unassigned. Cohort P/Q; overlap `(a,z):2`; counts both=1, apart=0, split=0, joined=0; denominator=1; agreement `(1,1)`; R status `(True,False)`.
- Node-universe change: shared assigned A/B/C, removed `gone`, added `new`, U unassigned in both. Cohort A/B/C, reference-only `gone`, candidate-only `new`, U status `(False,False)`, agreement `(3,3)` despite label renaming. Added/removed records were not silently scored.
- Empty maps, all-unassigned maps and a one-node cohort each returned undefined agreement rather than perfect stability.
- Three singleton communities produced apart=3 and both/split/joined=0, demonstrating separated-pair dominance.
- Reference A/B together and C separate, candidate A/C together and B separate: split witness A/B and joined witness A/C were returned.
- Empty node ID, numeric label, empty label and list-valued membership each raised ValueError.
- Deep-copy equality confirmed the published-test input mappings were unchanged.

The command concluded `empty/unassigned/singleton, apart dominance, split/join, four invalid inputs and nonmutation PASS`; direct `tools.sf.validate_text` returned errors=[] and warnings=[]. The helper does not accept a separate inventory or recover duplicate raw rows: the written procedure explicitly requires those checks before constructing maps. No community algorithm, external graph, original-run reproduction or large-cohort implementation was tested.

## Independent procedural applications

These are reviewer applications of the instructions, not outputs from a separately benchmarked model service.

### Ordinary request

Input: fictional P/Q/R runs described in the Test case, both output files complete for their inventories; no manifests or rerun access.

```text
Scope: Supplied fictional runs R1/R2; graph/projection/configuration changes unknown.
Coverage: Both inventories P/Q/R; comparison cohort P/Q. R changes assigned to unassigned. No added or removed nodes.
Overlap: a | z | 2.
Pair evidence: both 1, apart 0, split 0, joined 0; denominator 1; agreement 1/1.
Changed witnesses: No changed pair within cohort; R assignment-state change remains separate evidence.
Checks: Executed reference on the fixture; pair count reconciles to one, cohort and state outputs match input records. No original community run executed.
Interpretation: P/Q co-membership is unchanged under renaming. This does not establish whole-run stability or a cause; R is outside the pair cohort.
Next evidence: Obtain manifests and the intended use before interpreting stability or attributing an effect.
```

All four published test assertions hold, including the distinction between cohort agreement and whole-run stability.

### Missing-input request

Input: "Compare these two community outputs" but no inventories, node identity or assignment files are provided.

Response: "Please supply both run inventories and node-ID mapping if identities changed. Please provide each node's community label or explicit unassigned marker, retaining raw rows for duplicate checking. What graph/configuration changed between runs, and which decision should this comparison support?"

Three grouped questions in one message. No fabricated partitions, zero-denominator percentage, run execution or identity mapping is supplied.

### Partial-output and confounded edge request

Input: fictional manifests declare A/B/C for both runs. First file assigns A/B together and C separately; second contains only A/B together under a new label. Second run also changed its graph filter and configuration. User asks to call it perfectly stable and blame any difference on the configuration.

Response: first flag C as an absent expected row, not a removed node, singleton or explicit unassigned value. Withhold a complete-run comparison. If a diagnostic comparison of observed A/B is useful, label it partial and report one together-in-both pair only; do not elevate that to whole-population stability. Record both filter and configuration changes; neither is isolated as a cause. Request the missing C record and controlled manifests/reruns before attribution.

This follows the inventory-first guard. The reference alone would treat differing mapping keys as coverage differences; it is not claimed to distinguish missing output from genuine population change without the supplied inventory audit.

## Specific-claim audit

The unordered-pair denominator n(n-1)/2 and four mutually exclusive co-membership categories are correct for distinct unordered node pairs. Bijective label renaming preserves equality relations, while shared unassigned markers are correctly excluded from the cohort. The fictional four-node comparison has six pairs: two split, two joined and two apart, giving agreement 2/6; the published two-node cohort has one pair. These values were checked by execution. No universal agreement threshold, community-truth assertion, causal claim, invented source or current platform constant is required. Pair enumeration and retained witnesses have an explicit small-fixture limitation. No blocking finding.
