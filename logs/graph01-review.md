# GRF-001 independent review

Reviewer: separate agent review_graph01. Scope: existing graph-model-contract-design draft; no registry mutation. Review performed against AGENTS.md and SPEC.md. Decision: accept for coordinator validation and ingestion; no blocking finding.

## Uniqueness comparison

Queried TDS-002, TAP-001, TDE-004 and SEQ-001 with sf.py, then inspected their relevant procedures. TDS-002 reconstructs dataset ancestry; TAP-001 distinguishes request-field meanings; TDE-004 plans producer/consumer schema transitions; SEQ-001 diagnoses cycles in an already specified prerequisite graph. GRF-001 instead chooses a representation from query requirements, identifies occurrences separately from participants, defines endpoint roles and completeness-scoped cardinalities, and tests whether a candidate encoding loses repetition. These are different artifacts and decisions. Shared identity, provenance and fixture practices do not make this task a renamed neighbor.

## Actual executable checks

Extracted and executed the draft's Python block using Python 3.14.6. Terminal output:

```text
complete, missing-role, duplicate-role and wrong-source cases passed
interpreter 3.14.6
ordinary [] loan-count 2
partial-export-mechanical-result [('role-count', 'l2', 'ITEM', 0)]
duplicate-observation [('role-count', 'l1', 'ITEM', 2)]
wrong-target [('invalid-edge', 'l1', 'BORROWER', 'i')]
additional reviewer checks passed
```

The reviewer additionally asserted wrong-target detection. The partial-export line is intentionally a raw check result from a complete-record validator; the prose correctly prohibits treating that output as a factual business violation under partial evidence. No database, production dataset, import or storage implementation was tested.

## Reviewer scenario runs

These are outputs produced by applying the skill directly as an independent reviewer, not a claim that a separate model benchmark or external application was executed.

### Ordinary request

Input: fictional depot Birch supplies complete loan occurrences l1 and l2, person p and item i; each loan has one borrower and one item. Count occurrences and identify their items.

```text
Scope: Birch's supplied complete records; conceptual contract only.
Questions: occurrence count | integer; occurrence item | loan/item pairs.
Nodes: Person | borrower entity | scoped p | none; Item | lent entity | scoped i | none; Loan | occurrence | l1 or l2 | none.
Edges: BORROWER | Loan -> Person | occurrence borrower | exactly one per complete loan; ITEM | Loan -> Item | occurrence item | exactly one per complete loan.
Semantics: Preserve separate occurrence IDs even when endpoints agree. No current possession or reciprocal relationship is implied. Source-scoped IDs supply provenance; conflicting corrections remain open until source evidence resolves them.
Fixtures: l1/l2 complete | count 2 and l1/i, l2/i | executed role checks returned no errors and count 2.
Alternatives: single unlabelled Person->Item edge | cannot distinguish the two loan occurrences.
Open decisions: storage owner | physical representation | verify target support and rerun fixture; source owner | later corrections | supply correction evidence if any.
```

Result: preserves two occurrences and answers both queries without inventing current availability.

### Required input missing

Input: "Model our operation as a graph" with no workflow or required questions.

Output: "Which questions and decisions must the graph support? Please supply ordinary workflow records and any repeated or exceptional cases. Which source identifiers and business constraints are confirmed?"

Result: one message, three questions, no invented entities or alleged finished contract. This follows the explicit missing-input exception rather than filling an unsupported template.

### Partial evidence and duplicate observation

Input: fictional x and y are distinct loan IDs involving person p; x has item i and y has no item link in a partial export. A repeated source observation names x and the same item; there is no evidence of a third occurrence.

```text
Scope: Fictional partial loan export; missing evidence remains unresolved.
Questions: count evidenced occurrences | integer; known item per occurrence | loan/item or unresolved.
Nodes: Person | borrower | p | none; Item | lent entity | i | none; Loan | occurrence | x and y | unresolved item for y.
Edges: BORROWER | Loan -> Person | borrower role | proposed one per complete loan pending owner confirmation; ITEM | Loan -> Item | item role | proposed one per complete loan, not enforced as an absence fact in this partial export.
Semantics: x and y remain distinct. Repeated observation of x/i is retained as source evidence, not counted as a new loan. No reciprocal fact or current possession is inferred.
Fixtures: x and y | two evidenced occurrence IDs | reviewer traced input; y missing item | unresolved | complete-record snippet would flag a zero role count, but that is not a business violation under declared partial coverage; repeated x/i observation | no third evidenced occurrence | source occurrence identity matches.
Alternatives: endpoint deduplication | loses occurrence distinctions; treating missing y/item as prohibited | confuses incomplete evidence with a rule violation.
Open decisions: domain owner | complete-record role minima | supply controlling rule; source owner | missing y item | supply complete occurrence; storage owner | physical encoding | verify support before implementation.
```

Result: all five draft test assertions are met, including distinct occurrence identity, partial-evidence handling, direction and completeness, no inferred possession or implementation, and repetition versus duplicate-observation fixtures.

## Accuracy and limits

Reviewed the specific claims: fictional count two is recomputed from two distinct IDs; exactly-one role is explicitly owner-supplied in the example, not universal; endpoint equality alone does not prove event identity; reverse traversal does not establish a reciprocal fact; missing partial evidence does not prove absence. Python built-ins in the snippet were executed. Storage support remains a current-documentation verification step. No invented external sources, prices, standards, API versions or statistics appear. The snippet is explicitly limited to complete lending fixtures and is not a universal graph validator.

No blocking correction requested. An optional enhancement would be an explicit duplicate-observation row in the worked example, but the procedure, decision rules and test assertion already prescribe that distinction and the reviewer exercised it above. Structural acceptance and registry state remain the coordinator's responsibility.
