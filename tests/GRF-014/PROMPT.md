Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-014
name: relational-graph-storage-implementation
domain: Graph Engineering Foundations
subdomain: Graph storage implementation
version: 1.0
description: Implement and test a node-and-edge relational schema from an explicit graph contract when relationship identity, endpoint integrity and transactional persistence must survive storage.
triggers: ["implement graph storage tables", "store parallel graph edges without collapse", "verify graph foreign key enforcement", "test transactional graph persistence", "turn a graph contract into a relational schema"]
not_for: ["designing graph meaning from scratch [GRF-001]", "reconciling an edge-list import [GRF-003]", "migrating existing producer schemas [TDE-004]", "choosing a database product or tuning production queries"]
requires: []
risk_level: medium
---

# Relational Graph Storage Implementation

## Purpose
Create executable storage definitions and access examples that preserve an agreed graph representation. Verify identity, endpoint references, transaction rollback and reopened contents instead of treating successful table creation as proof that the graph survived. The implementation establishes only the tested storage contract, not broader business semantics or production suitability.

## Inputs to collect
1. **Graph contract** — obtain node and edge identities, direction, permitted multiplicity, loops and required properties. Why: constraints must preserve intended facts. Default: none; do not infer uniqueness from a sample.
2. **Source fixture** — collect a bounded node inventory, edge records and source locators. Why: isolated nodes and repeated relationships need concrete preservation tests. Default: clearly fictional fixture only, not claimed user data.
3. **Target environment** — obtain the actual database engine, driver/runtime and transaction configuration. Why: constraint enforcement and transaction behavior require environment verification. Default: disposable reference environment; check current official documentation before adapting.
4. **Required access patterns** — name outgoing/incoming lookup and exact output fields. Why: storage must answer the intended questions without collapsing edge identities. Default: outgoing-edge lookup with one row per relationship.
5. **Change policies** — obtain endpoint deletion, identity update and failure handling. Why: automatic cascades can remove relationship evidence. Default: reject referenced-node deletion in the prototype; request approval for another policy.
6. **Deployment boundary** — identify whether a new sandbox or an existing database is authorized. Why: creating a prototype is different from altering existing storage. Default: unique temporary database only; migration and production rollout remain separate work.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the accepted contract and map each invariant to a database constraint, application check or explicit unimplemented requirement.
2. Separate node identity from edge identity; use an independent edge key when distinct relationships may share endpoints.
3. Define endpoint references and null handling explicitly, retaining source locators beside stored facts.
4. Define property columns and type checks from supplied meanings; do not assume a foreign key enforces endpoint type, lifecycle or role cardinality.
5. Create the schema in a disposable environment and verify enforcement settings on every connection before beginning writes.
6. ⚠️ Insert the node/edge batch inside an explicit transaction. On failure, roll back the whole batch rather than preserving earlier statements from a partially failed import.
7. Execute parameterized access queries and compare complete returned edge identities, endpoints and properties against expected records.
8. Attempt missing-endpoint, duplicate-key and referenced-node deletion cases; require the declared rejection behavior rather than assuming declarations are active.
9. Close and reopen the test database, re-enable and verify connection settings, then reconcile stored rows with the committed fixture.
10. Deliver executable definitions, access examples and observed checks, distinguishing them from untested concurrency, recovery, scale and deployment requirements.

This Python 3 reference uses the `sqlite3` connection `autocommit` argument and therefore requires an interpreter supporting that interface. Check the installed interpreter and SQLite versions, not a supposed current release. The temporary database is deleted after the fixture; its reopen check is not a crash-durability test. Input identity fields are prevalidated nonempty strings; SQLite text affinity is not an identifier-type validator. Read current [driver transaction documentation](https://docs.python.org/3/library/sqlite3.html) and [foreign-key documentation](https://www.sqlite.org/foreignkeys.html) before adapting the connection setup.

```python
import sqlite3
from pathlib import Path
from tempfile import TemporaryDirectory

def connect(path):
    con = sqlite3.connect(path, autocommit=True)
    con.execute("PRAGMA foreign_keys = ON")
    assert con.execute("PRAGMA foreign_keys").fetchone() == (1,)
    return con

def batch(con, statements):
    con.execute("BEGIN")
    try:
        for sql, values in statements:
            con.execute(sql, values)
        con.execute("COMMIT")
    except Exception:
        if con.in_transaction:
            con.execute("ROLLBACK")
        raise

schema = """
CREATE TABLE node (
 id TEXT PRIMARY KEY NOT NULL CHECK(length(id)>0),
 kind TEXT NOT NULL, source_record TEXT NOT NULL
);
CREATE TABLE edge (
 id TEXT PRIMARY KEY NOT NULL CHECK(length(id)>0),
 source TEXT NOT NULL REFERENCES node(id) ON DELETE RESTRICT,
 target TEXT NOT NULL REFERENCES node(id) ON DELETE RESTRICT,
 relation TEXT NOT NULL, source_record TEXT NOT NULL
);
CREATE INDEX edge_source_lookup ON edge(source);
"""
node_sql = "INSERT INTO node VALUES (?, ?, ?)"
edge_sql = "INSERT INTO edge VALUES (?, ?, ?, ?, ?)"
nodes = [("A", "item", "n:0"), ("B", "item", "n:1"),
         ("I", "item", "n:2")]
edges = [("e1", "A", "B", "link", "e:0"),
         ("e2", "A", "B", "link", "e:1"),
         ("e3", "B", "B", "link", "e:2")]

with TemporaryDirectory() as folder:
    path = str(Path(folder) / "fixture.sqlite")
    con = connect(path)
    con.executescript(schema)
    batch(con, [(node_sql, n) for n in nodes]
               + [(edge_sql, e) for e in edges])
    query = "SELECT id,target FROM edge WHERE source=? ORDER BY id"
    assert con.execute(query, ("A",)).fetchall() == [("e1", "B"), ("e2", "B")]
    for statements in [
        [(node_sql, ("X", "item", "n:bad")),
         (edge_sql, ("bad", "X", "Z", "link", "e:bad"))],
        [(edge_sql, edges[0])],
        [("DELETE FROM node WHERE id=?", ("B",))]
    ]:
        try:
            batch(con, statements)
        except sqlite3.IntegrityError:
            pass
        else:
            raise AssertionError("invalid change accepted")
        assert not con.in_transaction
    assert con.execute("SELECT * FROM node ORDER BY id").fetchall() == nodes
    assert con.execute("PRAGMA foreign_key_check").fetchall() == []
    con.close()
    reopened = connect(path)
    assert reopened.execute("SELECT * FROM node ORDER BY id").fetchall() == nodes
    assert reopened.execute("SELECT * FROM edge ORDER BY id").fetchall() == edges
    reopened.close()
print("parallel edges, rollback, delete restriction and reopen checks passed")
```

## Decision rules
- IF parallel relationships are meaningful THEN key edges independently of endpoint pairs BECAUSE pair uniqueness would discard valid occurrences.
- IF enforcement cannot be verified THEN stop integrity claims BECAUSE a declared reference alone is not observed rejection behavior.
- IF any statement in an atomic batch fails THEN roll back its earlier statements BECAUSE a partially stored graph can satisfy counts while misrepresenting the intended revision.
- IF a semantic invariant is absent from the schema THEN retain an explicit application check BECAUSE endpoint existence does not prove permitted endpoint roles.
- IF the destination already holds user data THEN separate migration from new-schema prototyping BECAUSE creating fresh tables does not preserve existing consumers automatically.

## Output template
```text
Scope: <contract, target and authorized sandbox; maximum 70 words>
Invariant map: <rule | database/application enforcement | pending checks>
Implementation: <complete schema, connection setup and parameterized access code>
Fixture: <node/edge identities and expected query records; full table or attachment>
Checks: <valid load, invalid writes, rollback, reopen | executed/pending | observation>
Disposition: <prototype verified / incomplete; unresolved requirement>
Limits: <untested semantic, operational and deployment behavior; maximum 80 words>
```

## Quality checklist
- [ ] Edge identity preserves permitted parallel relationships.
- [ ] Required endpoints cannot be null or absent from the node inventory.
- [ ] Connection enforcement is checked before writes and after reopening.
- [ ] Partial failure leaves no earlier records from the failed batch.
- [ ] Query output retains every expected relationship identity.
- [ ] Isolated nodes and allowed self-loops survive reconciliation.
- [ ] Semantic constraints absent from the schema remain visible.
- [ ] Reopen evidence is not presented as crash recovery or production deployment.

## Anti-patterns
- **Pair primary key**: collapse distinct events sharing endpoints. Fix: use the supplied edge identity.
- **Declared means enforced**: trust schema text without invalid-write tests. Fix: check settings and rejection behavior.
- **Half-committed import**: keep early inserts after a failed edge. Fix: roll back the declared batch.
- **Cascade by convenience**: remove all relationships when deleting a node. Fix: implement the approved deletion policy.
- **Foreign key overclaim**: call valid references a complete graph contract. Fix: map role and lifecycle rules to additional checks.

## Worked example
**Input:** Fictional workshop Larch supplies the reference fixture: three item nodes, two separate A-to-B relationships and one B self-loop; loops and parallel edges are permitted. Every record has a locator. Implement only a fresh temporary prototype.

**Output:**
```text
Scope: Larch fixture, temporary relational prototype, no existing database changed.
Invariant map: Independent node/edge IDs; nonnull referenced endpoints; parallel edges allowed; referenced-node deletion rejected. Role cardinality not required by this fixture.
Implementation: Complete Python/SQL reference above, including connection verification, atomic batch and bound-parameter outgoing query.
Fixture: Nodes A/B/I; edges e1 A->B, e2 A->B, e3 B->B. Outgoing A returns e1 and e2; I remains stored.
Checks: Reference assertions test valid load, failed-batch rollback, duplicate edge rejection, restricted B deletion and identical reopened rows when executed.
Disposition: Prototype verified only after those assertions execute successfully; otherwise pending.
Limits: Temporary storage only; no concurrency, crash recovery, production scale or deployment tested.
```

**Bad output:** “Use source/target as the key and enable cascading deletes; the schema proves every graph rule.”
This loses repeated relationships, invents deletion policy and overstates reference constraints.

## Edge cases
- **Identifier coercion**: validate exact input strings before binding; do not let numeric conversion merge source identities.
- **Undirected graph**: adopt an approved endpoint convention while retaining original evidence; do not silently insert reciprocal duplicates.
- **Additional role constraints**: implement and test typed relation checks separately; this generic table permits any existing endpoint types.
- **Concurrent writers**: design and test isolation/retry behavior in the actual target; the single-connection fixture proves none of it.
- **Unknown property types**: request meanings and null rules before selecting columns; a generic text field is not semantic validation.

## Test case
**Input:**
> Fictional contract permits distinct edges x and y from P to Q and an isolated node R. A batch inserts node N, then an edge from N to missing M. Implement a fresh prototype with complete-batch rollback and referenced-node deletion rejection.

**Assertions:**
1. Stores x and y separately and retains R.
2. Rejects the missing endpoint and leaves no N from the failed batch.
3. Demonstrates the required deletion rejection and actual connection enforcement check.
4. Separates executed reopen verification from untested crash recovery and production deployment.
</skill>

<user_request>
Fictional contract permits distinct edges x and y from P to Q and an isolated node R. A batch inserts node N, then an edge from N to missing M. Implement a fresh prototype with complete-batch rollback and referenced-node deletion rejection.
</user_request>
