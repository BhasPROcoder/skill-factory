---
id: GRF-059
name: optional-graph-edge-row-contract
domain: Graph Engineering Foundations
subdomain: Optional graph query semantics
version: 1.1
description: Verify a neutral optional directed edge-pattern row multiset when parallel relationships, loops and unmatched seeds must keep their intended result meaning.
triggers: ["check optional graph match rows", "why did unmatched graph nodes disappear", "verify graph optional edge multiplicity", "compare inside versus after optional filters", "preserve parallel edge IDs in optional results"]
not_for: ["graph query-plan tuning [GRF-015]", "minimum-hop reachability [GRF-006]", "knowledge value constraints [GRF-020]", "generic tabular join diagnosis [TDQ-008]", "claiming a specific query language's null semantics"]
requires: []
risk_level: medium
---

# Optional Graph Edge Row Contract

## Purpose
Specify the rows produced by a neutral one-edge optional directed pattern over an explicit seed inventory. Each matching edge ID yields a row; a seed with no matching edge yields one row with an unbound edge and endpoint. Compare filters placed inside the optional pattern with filters applied afterward, without assuming that any particular graph language implements this neutral contract.

## Inputs to collect
1. **Graph snapshot** — obtain complete node IDs and identified directed edges with source, target, relation label and revision. Why: parallel identities and loops affect rows. Default: none.
2. **Seeds** — obtain exact unique seed node IDs, including isolates or nodes with only nonmatching relationships. Why: an edge-derived seed list would hide unbound rows. Default: none.
3. **Pattern** — obtain outgoing or incoming direction and allowed relation labels. Why: direction and label filtering determine matches. Default: no inferred reversal or all-relations wildcard.
4. **Additional predicate placement** — obtain any permitted endpoint condition and whether it belongs inside the optional match or after row production. Why: the two placements may preserve different seeds. Default: no additional predicate; compare placements only when requested.
5. **Unbound and target environment** — confirm a distinguished unbound marker and the actual query engine if translation is required. Why: missing bindings must not be mistaken for graph nodes or engine-specific null rules. Default: Python `None` for the reference, while node IDs must be strings; verify current official engine documentation before adaptation.
6. **Coverage and use** — establish snapshot completeness and who accepts the result contract. Why: missing edges can change rows. Default: supplied scope only, no live query execution claim.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the node and edge inventory, seed list, direction, relation filter and additional predicate.
2. Validate unique nonempty string node and edge IDs, known endpoints and exact four-field edge records.
3. Validate that every seed is a known unique node; `None` remains reserved for unbound output and cannot be a node ID.
4. For each seed, select edge records whose endpoint matches the requested direction, whose relation label is allowed and whose optional inside-pattern endpoint predicate passes.
5. Emit one `(seed, edge ID, other endpoint)` row per selected edge identity. Keep parallel edges separate even when their endpoints and labels match.
6. If no edge qualifies for that seed, emit exactly one `(seed, unbound, unbound)` row. ⚠️ Do not emit an additional unbound row for a seed that already has a match.
7. Compare the complete row multiset with independent per-seed groups keyed by full row identity, including edge ID. A total row count alone can conceal a dropped seed and duplicated edge row.
8. When comparing a post-optional predicate, apply the explicitly declared neutral filter to the already produced rows. Under this fixture, an unbound value fails a target/edge condition; record which seed rows disappear.
9. Confirm that any translation to a real query language implements the selected semantics by testing the same fixture and checking that language's current authoritative documentation. Keep unsupported engine behavior unresolved.
10. Deliver exact rows, seed coverage, filter-placement differences and limits. Do not call an absent match a false graph fact when source coverage is incomplete.

The Python 3 reference uses edges `(edge_id, source, target, label)`, direction `out` or `in`, and a nonempty tuple of allowed labels. `inside_targets` is `None` or a set of permitted other-endpoint IDs. `None` in result rows is a sentinel, not a node. Run the whole snippet and record the observed interpreter version.

```python
from collections import Counter

def validate(nodes, edges, seeds, labels, direction, inside_targets):
    if any(type(n) is not str or not n for n in nodes):
        raise ValueError("invalid node ID")
    if len(set(nodes)) != len(nodes):
        raise ValueError("duplicate node ID")
    known = set(nodes)
    if any(type(s) is not str or s not in known for s in seeds):
        raise ValueError("unknown or invalid seed")
    if len(set(seeds)) != len(seeds):
        raise ValueError("duplicate seed")
    if any(type(e) not in (tuple, list) or len(e) != 4 or
           any(type(x) is not str or not x for x in e) for e in edges):
        raise ValueError("invalid edge record")
    if len({e[0] for e in edges}) != len(edges):
        raise ValueError("duplicate edge ID")
    if any(a not in known or b not in known for _, a, b, _ in edges):
        raise ValueError("unknown endpoint")
    if (direction not in ("out", "in") or type(labels) is not tuple or
        not labels or any(type(x) is not str or not x for x in labels)):
        raise ValueError("invalid pattern")
    if inside_targets is not None and (
        type(inside_targets) is not set or not inside_targets <= known):
        raise ValueError("invalid target condition")

def optional_rows(nodes, edges, seeds, labels, direction,
                  inside_targets=None):
    validate(nodes, edges, seeds, labels, direction, inside_targets)
    rows = []
    for seed in seeds:
        matches = []
        for eid, a, b, label in edges:
            start, other = (a, b) if direction == "out" else (b, a)
            if start == seed and label in labels and (
                    inside_targets is None or other in inside_targets):
                matches.append((seed, eid, other))
        rows.extend(matches or [(seed, None, None)])
    return sorted(rows, key=lambda row: (row[0], row[1] or ""))

def verify_rows(nodes, edges, seeds, labels, direction,
                inside_targets, rows):
    grouped = {seed: Counter() for seed in seeds}
    for eid, a, b, label in edges:
        start, other = (a, b) if direction == "out" else (b, a)
        if start in grouped and label in labels and (
                inside_targets is None or other in inside_targets):
            grouped[start][(start, eid, other)] += 1
    expected = Counter()
    for seed, records in grouped.items():
        expected.update(records or Counter({(seed, None, None): 1}))
    return Counter(rows) == expected

nodes = ["A", "B", "C", "I"]
edges = [("p1", "A", "B", "link"),
         ("p2", "A", "B", "link"),
         ("loop", "B", "B", "link"),
         ("note", "C", "B", "note")]
rows = optional_rows(nodes, edges, nodes, ("link",), "out")
assert Counter(rows) == Counter([
    ("A", "p1", "B"), ("A", "p2", "B"),
    ("B", "loop", "B"), ("C", None, None), ("I", None, None)])
assert verify_rows(nodes, edges, nodes, ("link",), "out", None, rows)
post_filtered = [row for row in rows if row[1] is not None]
assert len(rows) == 5 and len(post_filtered) == 3
assert optional_rows(nodes, edges, nodes, ("link",), "out",
                     set()) == [(n, None, None) for n in nodes]
print("optional edge-ID rows and filter placement checked")
```

The second verifier groups qualifying rows by seed while retaining each edge ID in the complete row key, then adds an unbound row only for an empty group; it compares full multisets. The post-filter example deliberately rejects unbound edge IDs. This is a declared reference rule, not a universal assertion about a query engine's null or undefined semantics.

## Decision rules
- IF a seed has two qualifying parallel edges THEN return two rows BECAUSE each edge ID is distinct.
- IF a seed has no qualifying edge THEN return one unbound row BECAUSE optional matching preserves that seed under this contract.
- IF a seed has a match THEN omit an extra unbound row BECAUSE the optional fallback applies only without matches.
- IF a post-optional predicate rejects unbound values THEN report lost seed rows BECAUSE its placement changes the result.
- IF source coverage is partial THEN limit the no-match conclusion BECAUSE an unseen qualifying edge may exist.

## Output template
```text
Scope: <revision, nodes, seeds, direction and relation filter; maximum 70 words>
Optional rule: <one row per edge ID; one unbound fallback per unmatched seed>
Rows: <seed | edge ID or unbound | endpoint or unbound; full multiset>
Seed coverage: <seed | matched count or fallback; complete ledger>
Filter placement: <inside versus after rows and lost seeds, or not compared>
Verification: <independent multiset comparison executed/pending>
Limits: <source completeness and engine adaptation; maximum 80 words>
Next action: <owner and bounded implementation check; maximum 40 words>
```

## Quality checklist
- [ ] All seed IDs are in the declared node inventory.
- [ ] Edge IDs remain unique and parallel edges separate.
- [ ] Direction and relation filter are explicit.
- [ ] Exactly one unbound fallback appears per unmatched seed.
- [ ] No fallback appears for a matched seed.
- [ ] Row multiset matches independent edge grouping.
- [ ] Filter placement and lost rows are stated.
- [ ] No platform-specific null behavior is asserted without current verification.

## Anti-patterns
- **Endpoint collapse**: replace two parallel edge rows with one. Fix: preserve edge IDs.
- **Dropped isolate**: derive seeds from edges. Fix: start from the supplied seed inventory.
- **Extra null row**: add fallback despite a match. Fix: emit fallback only when match list is empty.
- **Post-filter surprise**: apply a condition after optional matching and silently drop unbound rows. Fix: compare placement explicitly.
- **Universal null claim**: assume a particular engine behaves like this fixture. Fix: verify that engine's current semantics.

## Worked example
**Input:** Fictional Team Pine supplies the snippet graph and seeds A/B/C/I. Match optional outgoing link edges; also show what happens when a post-filter requires a bound link edge.

**Output:**
```text
Scope: Pine exercise P1; A/B/C/I and four identified directed edges; all seeds, outgoing link filter.
Optional rule: One row per matching edge ID, one unbound fallback per unmatched seed.
Rows: A | p1 | B; A | p2 | B; B | loop | B; C | unbound | unbound; I | unbound | unbound.
Seed coverage: A | 2 matches; B | 1; C | fallback; I | fallback.
Filter placement: Inside optional gives five rows. A post-filter requiring bound link edge retains three and loses C/I fallback rows.
Verification: Independent edge-ID grouping and full row multiset comparison executed for P1.
Limits: Neutral fixture only; no claim about an external query language or unseen source edges.
Next action: Query owner tests the intended engine's current optional and filter behavior on P1 before deployment.
```

**Bad output:** “A/B have links; C/I disappear because they have none, and p1/p2 can be deduplicated.”
That violates both optional seed preservation and edge-ID row identity.

## Edge cases
- **Empty seeds**: return no rows without inventing a seed.
- **Only nonmatching relation**: return one unbound row for that seed.
- **Incoming direction**: swap source/target roles for matching, retaining original edge IDs.
- **Self-loop**: one edge row at its endpoint, not two for one direction.
- **Unbound sentinel collision**: reject nonstring node IDs so `None` cannot be a node.

## Test case
**Input:**
> Fictional A has two A→B link edge IDs, B has a B→B link loop, C has only a note edge, and I is isolated. Return optional outgoing link rows for all four seeds and compare a bound-edge post-filter.

**Assertions:**
1. Returns two A rows, one B loop row and one unbound row each for C and I.
2. Reports five optional rows and three after the post-filter.
3. Keeps p1 and p2 separate and preserves the original seed inventory.
4. Does not claim a particular external query language was executed.
