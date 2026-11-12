# Graph Engineering Foundations (GRF)

Specify and verify graph representations, identity and structural contracts from explicit task evidence.

Macro-area: Software Engineering

Pick the skill whose triggers best match the request. If none match, use the closest description; if still none, answer without a skill.

| ID | Skill | Use when | Example triggers | Status |
|---|---|---|---|---|
| GRF-001 | [graph-model-contract-design](graph-model-contract-design/SKILL.md) | Turn workflow evidence and required questions into an explicit graph representation contract before choosing storage or importing relationship data. | model this workflow as a graph; decide graph nodes and edges; design a graph representation contract | validated |
| GRF-002 | [graph-entity-merge-impact-review](graph-entity-merge-impact-review/SKILL.md) | Review proposed graph entity merges against identity evidence and relationship consequences when duplicate-looking nodes could change graph meaning. | review graph entity merges; resolve duplicate graph nodes; check entity merge consequences | validated |
| GRF-003 | [graph-edge-list-import-reconciliation](graph-edge-list-import-reconciliation/SKILL.md) | Convert an explicit node inventory and edge list into a traceable graph import while preserving direction, relationship identity, parallel edges and rejected-row evidence. | import an edge list without losing edges; reconcile graph import counts; preserve isolated nodes during import | validated |
| GRF-004 | [rooted-forest-contract-validation](rooted-forest-contract-validation/SKILL.md) | Validate a declared parent-to-child forest against explicit roots, parent cardinality and whole-snapshot reachability, returning defect witnesses and evidence-bound repair proposals. | validate this graph is a rooted forest; check hierarchy structural invariants; find nodes outside declared roots | validated |
| GRF-005 | [graph-two-clock-snapshot-reconstruction](graph-two-clock-snapshot-reconstruction/SKILL.md) | Reconstruct an evidence-linked graph edge view at an effective-time point and a recorded-time cutoff when late corrections or retractions change historical answers. | reconstruct a graph as known then; separate effective time from recorded time; query graph history after late corrections | validated |
