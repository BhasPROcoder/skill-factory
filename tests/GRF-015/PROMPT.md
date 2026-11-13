Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-015
name: graph-query-plan-equivalence
domain: Graph Engineering Foundations
subdomain: Graph query verification
version: 1.0
description: Tune a bounded relationship query using observed query plans while preserving its edge-sequence result multiset, direction and multiplicity contract.
triggers: ["tune a graph relationship query", "check graph query rewrite equivalence", "preserve parallel-edge paths during tuning", "inspect a graph query execution plan", "separate query speed from changed results"]
not_for: ["diagnosing generic join-key multiplication [TDQ-008]", "implementing graph storage [GRF-014]", "unbounded recursive graph traversal", "production index deployment or universal database selection"]
requires: []
risk_level: medium
---

# Graph Query Plan Equivalence

## Purpose
Produce a tested query-tuning proposal with a preserved result contract and observed access-plan evidence. Distinguish legitimate relationship combinations from accidental duplication before changing a query or index. A smaller result or different plan is not by itself an optimization or a measured speed improvement.

## Inputs to collect
1. **Query and result contract** — obtain the exact statement, bound parameters, output columns and ordering requirement. Why: equivalence concerns the requested result, not similar-looking endpoints. Default: unresolved until supplied; a fictional fixture demonstrates only its own contract.
2. **Graph semantics** — obtain direction, relation filters, permitted edge reuse and whether results represent walks, simple paths, distinct endpoints or existence. Why: these have different multiplicities. Default: no inferred deduplication or cycle exclusion.
3. **Frozen data and schema** — obtain snapshot, edge identities, indexes, constraints and representative fixtures. Why: before/after results must use the same graph. Default: disposable copy only; never tune by deleting inconvenient edges.
4. **Environment evidence** — collect the installed engine/driver versions, planner settings and available plan output. Why: optimizer choices and plan formats can change. Default: inspect the actual environment and current official documentation before adapting commands.
5. **Workload and acceptance** — collect parameter distribution, latency/resource concern and tolerated regressions. Why: an index useful for one lookup may cost writes or storage elsewhere. Default: equivalence and plan experiment only; no unmeasured speed target.
6. **Change authority** — establish whether only a sandbox proposal or a live change is authorized. Why: schema tuning can affect other workloads. Default: disposable test database; deployment and rollback approval remain separate.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the source graph and write the row meaning, including direction, exact hop count, filters and edge-identity fields.
2. Enumerate expected edge sequences independently on a small fixture containing parallel edges, a loop, an excluded relation and an unreachable node.
3. Execute the baseline query with bound parameters and retain its complete result multiset; compare it with the independently enumerated expectation before tuning.
4. Capture the baseline plan and relevant environment settings. Interpret it using the installed engine's documentation; do not assume a plan node's name or ordering is a stable interface.
5. Form one explicit tuning hypothesis, such as an index supporting the source-and-relation lookup of each hop. Record its possible write/storage costs and the parameters it is intended to help.
6. Apply that single candidate change to the disposable copy, keeping the data, parameters and requested output contract unchanged.
7. Execute the candidate and compare complete row multiplicities against baseline and independent expectations. If order is part of the contract, compare the declared deterministic order separately.
8. ⚠️ Reject a change that removes legitimate relationship combinations, even if it runs faster. Adding endpoint DISTINCT or early LIMIT can answer a different question; obtain a changed contract before treating that as acceptable.
9. Capture the candidate plan. Explain observed access differences without claiming runtime improvement from plan shape alone.
10. If performance evidence is required, run representative parameter cases under a stated repeatable measurement protocol, retaining variability and write/storage tradeoffs. Mark unperformed measurements pending.
11. Deliver the executable candidate, equivalence evidence, plan observations and deployment boundary. A failed equivalence check blocks promotion regardless of timing results.

This Python 3 reference uses its standard `sqlite3` driver in a disposable in-memory database. It queries exactly two directed link edges, allowing repeated nodes and edge reuse: these are walks, not a simple-path query. SQL returns both edge identities and destination. Check the installed versions printed by the fixture. Consult current [SQLite query-plan documentation](https://www.sqlite.org/eqp.html) and [index-planning documentation](https://www.sqlite.org/queryplanner.html) before interpreting or adapting plans; do not hardcode their text in tests.

```python
import sqlite3
import sys
from collections import Counter

edges = [("e1", "A", "B", "link"), ("e2", "A", "B", "link"),
         ("e3", "B", "C", "link"), ("e4", "B", "C", "link"),
         ("e5", "B", "B", "link"), ("e6", "B", "A", "link"),
         ("e7", "A", "X", "note")]
sql = """SELECT a.id, b.id, b.target
FROM edge AS a JOIN edge AS b ON a.target=b.source
WHERE a.source=? AND a.relation=? AND b.relation=?"""
params = ("A", "link", "link")
expected = Counter((a[0], b[0], b[2]) for a in edges for b in edges
                   if a[1] == params[0] and a[3] == params[1]
                   and a[2] == b[1] and b[3] == params[2])
con = sqlite3.connect(":memory:")
try:
    con.execute("CREATE TABLE edge(id TEXT PRIMARY KEY NOT NULL, "
                "source TEXT NOT NULL, target TEXT NOT NULL, relation TEXT NOT NULL)")
    con.executemany("INSERT INTO edge VALUES (?, ?, ?, ?)", edges)
    baseline = Counter(con.execute(sql, params).fetchall())
    before = con.execute("EXPLAIN QUERY PLAN " + sql, params).fetchall()
    assert baseline == expected and sum(baseline.values()) == 8
    con.execute("CREATE INDEX hop_lookup ON edge(source, relation, target, id)")
    candidate = Counter(con.execute(sql, params).fetchall())
    after = con.execute("EXPLAIN QUERY PLAN " + sql, params).fetchall()
    assert candidate == baseline == expected
    assert con.execute(sql, ("Z", "link", "link")).fetchall() == []
    assert len({row[2] for row in candidate}) == 3
    print("runtime", sys.version.split()[0], "SQLite", sqlite3.sqlite_version)
    print("rows", sum(candidate.values()), "distinct destinations", 3)
    print("baseline plan", before)
    print("candidate plan", after)
finally:
    con.close()
```

## Decision rules
- IF the contract counts relationship sequences THEN retain edge identities and row multiplicities BECAUSE equal endpoints can represent different walks.
- IF baseline disagrees with the independent fixture THEN fix correctness before tuning BECAUSE preserving an existing wrong answer is insufficient.
- IF a candidate changes results THEN reject equivalence BECAUSE performance cannot justify an unapproved semantic change.
- IF plans differ but representative measurements are unavailable THEN report only the observed plan change BECAUSE optimizer shape is not elapsed-time evidence.
- IF an ordering is required THEN specify and test its tie-breaking keys BECAUSE incidental database row order is not a stable result contract.

## Output template
```text
Contract: <snapshot, parameters, walk/path meaning, row identity and order; maximum 90 words>
Baseline: <statement/reference, expected and observed multiplicities>
Candidate: <executable query/index change, hypothesis and possible costs>
Equivalence: <exact multiset and independent-fixture checks; executed/pending>
Plan evidence: <environment and before/after observations; maximum 100 words>
Performance: <measured protocol/results or pending; no invented speedup>
Disposition: <equivalent candidate / rejected / incomplete; reason>
Next action: <representative validation, owner and deployment boundary; maximum 70 words>
```

## Quality checklist
- [ ] Walk/path/existence semantics and multiplicity are explicit.
- [ ] Baseline matches an independently enumerated fixture.
- [ ] Parallel relationships retain distinct edge identities.
- [ ] Baseline and candidate use the same snapshot and parameters.
- [ ] Exact result multiplicities are compared, not only row totals.
- [ ] Any required ordering is checked separately.
- [ ] Plan observations are separated from measured performance.
- [ ] Candidate costs and deployment authority remain explicit.

## Anti-patterns
- **DISTINCT as speed repair**: collapse legitimate walks to endpoints. Fix: preserve the approved row meaning.
- **Equal count proof**: accept equal totals with different edge pairs. Fix: compare complete multisets.
- **Plan-name test**: require an exact optimizer description string. Fix: inspect actual plans with version context.
- **Tiny benchmark promise**: claim production speed from a small fixture. Fix: measure the representative workload separately.
- **Unordered pagination**: apply LIMIT to arbitrary rows. Fix: define ordering and pagination semantics before comparison.

## Worked example
**Input:** Fictional team Rowan supplies the snippet graph and asks for all two-link walks from A, including repeated nodes. It permits a disposable index experiment but provides no production workload.

**Output:**
```text
Contract: Rowan fixture; A/link/link; exactly two directed edges; walks allow repeated nodes; rows retain both edge IDs and destination; order unspecified.
Baseline: Supplied join; independent enumeration and query each yield eight edge-sequence rows.
Candidate: CREATE INDEX hop_lookup ON edge(source, relation, target, id); test source/relation access; extra index maintenance/storage remains unmeasured.
Equivalence: Reference assertions compare complete multisets before/after and expected sequences when executed. Empty Z lookup remains empty.
Plan evidence: Capture the actual printed engine versions and both plans; no plan change asserted until execution.
Performance: Pending representative measurements; no speedup claimed.
Disposition: Equivalent candidate only after assertions execute; endpoint DISTINCT would return three destinations instead of eight sequences and is rejected for this contract.
Next action: Owner supplies workload cases and measures lookup/write costs before any deployment.
```

**Bad output:** “Add DISTINCT target: three rows are faster than eight, so the query is fixed.”
It replaces edge-sequence enumeration with destination existence and provides no timing evidence.

## Edge cases
- **Simple paths requested**: specify node/edge repetition rules and independently test them; the supplied walk query is not sufficient.
- **Null or malformed graph fields**: resolve schema/data validity first; do not treat null-induced missing matches as a tuning success.
- **Changing graph snapshot**: rerun both variants against one frozen revision; results from different data cannot prove equivalence.
- **Empty or absent seed**: distinguish a valid no-walk result from an unresolved seed identity using the node inventory; the edge-only fixture tests only no matches.
- **Large results**: use an exact scalable comparison or explicitly bounded evidence; matching sample totals or hashes alone do not establish full equality.

## Test case
**Input:**
> Fictional edges p and q both link S to M, and r links M to T. The query must return both two-edge sequences with their edge IDs. A proposed rewrite returns DISTINCT destination T. No runtime measurements exist.

**Assertions:**
1. Retains p/r and q/r as two required sequences.
2. Rejects the one-destination rewrite as nonequivalent despite matching endpoint reachability.
3. Requires exact result comparison and actual plan evidence for a valid candidate.
4. Claims no measured speedup or authorized production deployment.
</skill>

<user_request>
Fictional edges p and q both link S to M, and r links M to T. The query must return both two-edge sequences with their edge IDs. A proposed rewrite returns DISTINCT destination T. No runtime measurements exist.
</user_request>
