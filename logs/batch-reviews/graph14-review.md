# GRF-014 independent review

Reviewed 2026-11-14 by storage_review. Decision: accept for coordinator checks; no blocking finding. The complete draft exists despite the absent author-evidence log. This reviewer executed its code independently and did not change the skill or registry.

## Scope and uniqueness

Read AGENTS.md, SPEC.md and the full GRF-014 draft. Queried sf.py for GRF-001/003 and TDE-004/006, then read their relevant actual procedures. Recovered TDE-006 procedure separately after combined output truncation. GRF-001 selects representations and local modeling fixtures; GRF-003 reconciles import rows without storage execution; TDE-004 plans schema compatibility/consumer rollout; TDE-006 defines observation/freshness contracts. GRF-014 instead creates a concrete node/edge schema, checks connection-level enforcement, exercises transactional failure and reopens stored records. This selected-neighbor comparison supports distinct implementation value, not exhaustive whole-library uniqueness.

The draft contains all SPEC sections, a complete runnable reference and worked/test examples. Direct tools.sf.validate_text returned errors=[] and warnings=[]. That is draft validation, not registry acceptance.

## Actual execution

Extracted and executed the Python fence on the installed Python 3.14.6 with SQLite 3.50.4. Observed stdout:

```text
parallel edges, rollback, delete restriction and reopen checks passed
review: P/Q/R parallel fixture, 4 rejected batches, parameter isolation, reopen rejection PASS
Python 3.14.6 SQLite 3.50.4
direct validation ([], [])
```

The first line is the exact supplied fixture. Independent additional assertions instantiated P/Q/R with distinct x/y relationships P-to-Q. Both edges survived a parameterized outgoing query, and inventory-only R remained. Four rejected batches covered: insert N followed by an N-to-missing-M edge; null endpoint; repeated node key; deletion of referenced Q. All raised IntegrityError and left no open transaction. Full node-table equality proved the earlier N insert did not survive its failed batch. A bound string resembling SQL syntax returned no rows rather than changing the predicate. After close/reopen, foreign_keys returned 1, foreign_key_check returned no rows, edge rows equaled the committed input, and a new missing-endpoint insert was rejected again.

All test databases used unique temporary directories and were removed by the standard context manager after connections closed. No existing user database, live service, concurrent writer or crash recovery was tested.

## Official interface checks and claim audit

Consulted [Python sqlite3 documentation](https://docs.python.org/3/library/sqlite3.html) and [SQLite foreign-key documentation](https://www.sqlite.org/foreignkeys.html). The reference explicitly uses SQL BEGIN/COMMIT/ROLLBACK under its chosen connection mode, rather than relying on Python commit()/rollback() calls that are ineffective under autocommit=True. SQLite documents connection-level enforcement and the need to enable it outside a transaction. The draft checks actual settings before writes and after reopening instead of assuming defaults. Parameters bind values rather than interpolating identifiers into SQL.

Observed runtime numbers above are environment evidence, not required current releases. The skill correctly asks users to verify interface support before adaptation. Independent edge IDs preserve the two relationships; NOT NULL prevents the foreign-key null exception; RESTRICT rejects the declared deletion case. No endpoint-type, role-cardinality, crash durability or production-suitability claim is inferred from these constraints. Example arithmetic is three nodes and three edges, with two outgoing A relationships and one B self-loop, matching execution.

## Ordinary procedural application

Input: fictional P/Q/R fixture, separate x/y P-to-Q edges, source locators, no extra property types, fresh disposable prototype only, atomic batch and referenced-node deletion restriction.

```text
Scope: Reviewer P/Q/R fixture; fresh temporary SQLite database; no existing storage changed.
Invariant map: Independent node/edge keys; endpoint NOT NULL and references; per-connection enforcement checked; RESTRICT deletion. Additional role/lifecycle rules not supplied.
Implementation: Executed the draft's complete schema, connect(), batch() and bound-parameter access code with the reviewer fixture.
Fixture: P/Q/R stored; x and y both P->Q with separate source locators; outgoing P returns x and y; R retained.
Checks: Valid load passed; missing-endpoint batch rolled back N; duplicate node/null endpoint/referenced-Q deletion rejected; reopened rows equal committed rows and new invalid edge rejected.
Disposition: Prototype verified for these exact constraints and fixtures.
Limits: No production deployment, semantic role validation, concurrency, performance or crash-recovery evidence.
```

All published test assertions hold. Implementation here refers to the actual executed reference artifact, not an unexecuted proposal.

## Missing-input application

Input: “Store my relationship data” with no graph semantics, environment or permission boundary.

Response: “What are the node/edge identities, direction, permitted repetitions/loops and required properties? Which database/runtime and access queries are required? Is this a new disposable prototype or an existing database, and what deletion/failure policies apply?”

Three questions in one message. Until answered, only a clearly fictional sandbox example is possible; no production schema or migration is claimed.

## Edge application

Input: owner requires Loan-to-Person borrower edges and asks whether valid node references alone prove this semantic rule.

Response: the generic endpoint references prove existence only. Mark the endpoint-role invariant unimplemented; add and independently test a suitable typed constraint or application check under the accepted contract before declaring it verified. Do not invent type semantics or claim the existing table rejects a Loan-to-Item borrower edge. Existing-storage requests remain outside the fresh-schema prototype boundary and require a separate migration plan. These are procedural applications, not claims that those additional controls were implemented.
