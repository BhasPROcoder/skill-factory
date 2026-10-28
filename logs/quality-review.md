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

Final counts, review findings, and remaining limitations will be recorded here after the combined library is assembled. Do not interpret the presence of a worked example or test request as evidence that a separate model executed it successfully.
