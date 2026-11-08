# Interactive Prototype Behavior (IPR)

Implement and test bounded interaction state models for draft recovery, asynchronous result ownership and transactional edit history.

Macro-area: Product & Design

Pick the skill whose triggers best match the request. If none match, use the closest description; if still none, answer without a skill.

| ID | Skill | Use when | Example triggers | Status |
|---|---|---|---|---|
| IPR-001 | [interrupted-form-draft-restoration](interrupted-form-draft-restoration/SKILL.md) | Implement and test a form-draft recovery model when interrupted editing must resume without overwriting newer work or treating a saved draft as a submitted record. | prototype form draft recovery; restore interrupted form edits; test resume editing behavior | validated |
| IPR-002 | [asynchronous-result-generation-ownership](asynchronous-result-generation-ownership/SKILL.md) | Implement and test request-generation ownership when delayed responses must not replace results for a user's newer input. | stop old search results replacing new ones; prototype asynchronous result states; test out-of-order responses | validated |
| IPR-003 | [transactional-edit-history-branching](transactional-edit-history-branching/SKILL.md) | Implement and test undo and redo history when multi-step editing must preserve transaction boundaries and discard abandoned redo branches after a new edit. | prototype undo redo; group edits into one undo action; test redo after a new edit | validated |
