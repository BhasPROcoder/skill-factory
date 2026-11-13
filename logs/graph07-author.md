# GRF-007 author evidence

Candidate: weak-component-scope-diagnosis. Author components_author; held for independent review. No registry mutations or acceptance claims.

## Candidate comparison

Read AGENTS.md, SPEC.md, creation-order.md, the GOLD-SKILL structure, GRF-004 in full, and selected actual procedure/input/code sections of SEQ-001, TDS-002 and TDS-012 after sf.py metadata discovery. A lexical component search returned unrelated interface/component tasks, not proof of catalog-wide uniqueness.

GRF-004 checks a directed parent graph against declared roots, indegrees and root reachability. SEQ-001 supplies a cycle witness or prerequisite order. TDS-002 maps provenance; TDS-012 traces authorized withdrawal effects through descendants. None produces a complete weak-component partition with spanning evidence, retained inventory isolates and excluded-edge witnesses explaining filter-induced separation. Pending G06 is a bounded traversal from a seed; this candidate exhaustively assigns every node without a depth cap. Future G08 concerns strong connectivity, which this skill expressly excludes. Novelty is supported against these neighbors, not asserted exhaustively for every library entry.

No external skill content or code was copied. This is an original implementation of the approved G07 task, following the user's graph-priority queue.

## Specific claims reviewed before saving

Weak connectivity ignores direction without adding reciprocal facts. Traversal from every unassigned node gives disjoint complete reachability classes in the undirected projection. Every retained edge stays inside one such class; discovery edges connect each nonsingleton class. Loops and parallel edges preserve identity but do not by themselves join separate endpoint sets. Excluded edges can connect distinct projected components, so separation in the projection does not establish separation in the wider source. Component labels using minimum string IDs are snapshot-local. No changing platform behavior, source statistics or fabricated citation appears.

Fixture arithmetic: five nodes with selected p:A->B and r:C->D yield three components {A,B}, {C,D}, {E}; restoring excluded q:C->B yields two components {A,B,C,D}, {E}. Two discovery edges suffice for the selected two pairs; the singleton uses none. The published four-node test yields {P,Q}, {R}, {S}; R loses incident y by the filter while S has no source incident edge. These statements were checked by actual execution below.

## Executed checks

Executed the exact Python fence under Python 3.14.6. Direct tools.sf.validate_text returned errors=[] and warnings=[]. Body whitespace word count: 1581. This direct check does not register or accept the draft.

Observed output:

```text
validation [] []
body_words 1581
filtered partition, isolates and excluded-link comparison passed
published test, empty, loop/parallel, 3 input-rejection cases passed
exhaustive weak-partition comparisons 512
Python 3.14.6
```

Additional assertions used the published P/Q/R/S fixture; an empty graph; a self-loop plus reciprocal parallel relationship fixture; repeated node IDs, an unknown endpoint and duplicate edge IDs. All invalid fixtures raised ValueError as expected.

The bounded exhaustive test enumerated all 512 directed edge subsets on three nodes including loops. An independent Boolean transitive-closure oracle symmetrized each edge and compared every node-pair membership against the helper. It also checked that total discovery edges equal nodes minus components for every case. All comparisons passed. This does not test production scale, malformed tuple shape (explicit caller prevalidation), node-filter implementation or database behavior.

Independent ordinary/missing/edge scenario review remains required. Source snapshot completeness and domain meanings are input evidence, not properties established by the helper.
