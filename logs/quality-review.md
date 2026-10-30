# Quality review record

## Scope

The collection is being authored in separate subject assignments. Each author is responsible for task-specific procedures, decision branches, worked examples, and pre-save claim review. External requirements are verification inputs. Numeric technical fixtures are recomputed or executed where supplied.

## Checks and their meaning

- `sf.py check-registry`: identifiers, domains, names, prerequisites, and registry schema.
- `sf.py validate`: frontmatter and required document structure, with explicit failure exit codes for unknown IDs and invalid or missing files.
- `sf.py quality`: required body length, exact equality of procedure/example/test sections, and registry risk/prerequisite agreement. Repeated shared framing is allowed; title substitutions without distinct procedures are not an acceptable skill.
- `sf.py overlap`: lexical candidate pairs for routing review, not an automated semantic verdict.
- Validator regression tests: failure reporting, invalid-manifest atomicity, and idempotent ingestion.

## Review status

The final combined check reports 544 registered, validated skills across 57 domains, with zero audited entries. `sf.py quality --all` passed the structural, length, exact-duplicate, and metadata gates; body lengths ranged from 1176 to 1682 words. Its one lexical overlap candidate, BMD-005 versus TML-008, concerns business-model assumptions versus machine-learning component ablation; their procedures address different decisions.

Recorded substantive reviews:

- [Root collection](review-root-independent.md): all 30 source records with selected full-skill checks, evidence-consistency repairs, and executed arithmetic checks.
- [Technical collection](review-technical-independent.md): all 150 task records and a rendered sample, concrete artifacts, content-based subdomains, and corrected technical edge conditions.
- [Marketing collection](review-marketing-independent.md): all 170 task records/artifact definitions and one rendered example per domain, with assumption and overlap repairs.
- [Government collection](review-government-independent.md): source/example and targeted semantic review, concrete artifacts, final rendered sample across all fifteen domains, and 150 file validations.
- [Technical generalizations](review-claude-technical.md): eleven new AI workflow records, rendered examples, offline fixtures and the three repertoire-engineering skills.
- [Business generalizations](claude-comparison-business.md) and [operations generalizations](claude-comparison-operations.md): scoped source comparisons, concrete fictional artifacts and corrections. These reviews include coordinator follow-up where independent agents could not continue.
- [Independent forward tests](forward-tests.md): new fictional tasks for TKG-002, THK-003, and CTR-001, with actual generated outputs and bounded Python checks. These trials do not establish behavior for the rest of the library.

The eight validator regression tests passed outside the sandbox, whose temporary-directory permissions prevented the initial run. These tests cover registry ingestion, failure reporting, missing migration mappings and changed destination detection, not subject-matter expertise.

## Migration and delivery evidence

The migration check mapped all 57 original source workflows to 88 validated destination skills. The additions comprise 11 technical, 15 operations and 15 business/artifact skills; other source workflows reuse or combine existing procedures. The original folder was removed at the user's explicit request only after this check. The removal check confirmed its absence and unchanged destination hashes. The comparison table and hash receipt retain source names and mapping decisions, not copies of the original personal/vendor-specific instructions.

The router and all 57 domain indexes were regenerated. The portable export and ZIP contain 544 skills; archive integrity passed. Archive SHA256: `60fc40ed07da9f33f7bec89f1db573d0c1d5c8e8704c3854b326f716ae79e9f8`. Exported frontmatter contains name and description; repository metadata is preserved separately in each portable file. Actual tool availability varies by agent.

Do not interpret an embedded test request as an executed test. No claim is made of exhaustive semantic uniqueness, cross-model reliability, professional certification, or live administrative/platform outcomes. The source-level reviews identify distinct procedures and repair observed collisions; changing external requirements remain explicit verification inputs.
