# GRF-021 independent review

Reviewer g18_independent_review, 2026-11-14. Read complete candidate and inspected the accepted GRF-020 procedure and reference boundaries, plus sf.py metadata for GRF-006. GRF-020 checks distinct-value cardinality constraints with completeness-sensitive witnesses; GRF-021 assembles question-specific source packets from paths with explicit budget omissions and a passage-only comparison. GRF-006 computes bounded reachability. These deliverables and failure decisions are distinct within the reviewed neighborhood.

## Executed checks

Python 3.14.6 ran the complete embedded snippet successfully. Independently tested a budget of 20: c1/c2 both selected, two unique passage references, spent 20. The example budget 10 selected c1 only and omitted c2 for packet budget. Missing passage, oversized chain, reversed path and unknown edge produced four separate omissions and no selected paths. An oversized first candidate did not prevent a later affordable candidate from being selected. Two candidates sharing the same passage consumed 10 characters once. Zero budget selected none for these nonempty passages. Negative, Boolean and fractional budgets were rejected. The example's ten-character passage arithmetic is correct.

## Scenario outputs produced during review

Ordinary scenario uses the reference graph at S1, complete c1/c2 enumeration, resolved A, budget 20 and an unavailable baseline.

```text
Question needs: 1. Inspect the supplied A-to-C link route.
Resolution: A | A | supplied resolved inventory.
Contract: S1, outgoing links, two-edge bound, supplied c1/c2 enumerated, 20 newly included passage characters.
Packet: c1 | partial need 1 | e1 | D:v1:p1 “A links B.” | first step only; c2 | need 1 | e1,e2 | D:v1:p1 “A links B.” and D:v1:p2 “B links C.” | a supplied two-step route, not a direct A-to-C fact.
Omissions: None among the supplied candidates.
Baseline: Method and budget unavailable; pending; differences unmeasured.
Checks: Executed continuity, source availability and unique-passage budget accounting; source truth and broader graph completeness unverified.
Answer boundary: Both supplied route steps are inspectable; direct A-to-C relation and comparative performance remain unsupported.
```

Missing-input scenario supplies a graph but no question or authorized retrieval bounds.

```text
Question needs: Unspecified; request the question before retrieval.
Resolution: Pending question and seed evidence.
Contract: Snapshot supplied; patterns and budgets unresolved. Ask for the question, seed identity evidence and retrieval/output bounds in one message.
Packet: None produced.
Omissions: Retrieval not executed because its relevance target and bounds are missing.
Baseline: Pending question and method.
Checks: None executed for this request.
Answer boundary: No answer or graph-absence claim supported.
```

Edge scenario supplies one missing-passage path and a complete two-edge chain costing 20 characters under budget 10.

```text
Question needs: 1. Inspect a supported route from A.
Resolution: A | A | supplied inventory.
Contract: S1; supplied outgoing candidate paths only; passage budget 10.
Packet: Empty.
Omissions: missing | missing passage | retrieve its authorized frozen passage; large | packet budget | increase passage budget to at least 20 to include this complete chain under the supplied selection order.
Baseline: Not run; method and budget pending; differences unmeasured.
Checks: Executed missing-evidence and budget checks; no whole path selected.
Answer boundary: Neither omitted path supports an answer in the delivered packet; empty packet does not establish global absence.
```

## Verdict

Accept within documented scope; no required repairs found. The worked example follows all eight output fields and labels checks conditional on execution. It distinguishes partial need coverage from a complete answer. Source quotations and revision references are present. The code assumes prevalidated dictionary/tuple shapes and nonempty passages as explicitly stated; it is a selection reference rather than candidate enumeration, relevance scoring, token measurement or semantic verification. No external factual claims or invented citations found. Mechanical tests do not establish source truth, baseline superiority or whole-catalog uniqueness. Registry untouched by reviewer.
