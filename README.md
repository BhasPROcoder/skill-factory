# Skill Factory

A local library of portable, task-focused instructions. Each skill contains inputs, an explicit procedure, decision rules, an output template, a fictional worked example, failure cases, and a test request.

## Use a skill

1. Open [ROUTER.md](ROUTER.md) and choose a domain.
2. Follow its domain index and select the task whose description matches your request.
3. Give your model the selected `SKILL.md` and your real inputs. Load one skill at a time rather than the whole library.
4. Check the resulting artifact against the skill's quality checklist and test assertions.

The instructions are plain Markdown and do not require a particular model or plugin. They do not grant permission to send messages, submit applications, change production systems, or publish content.

## Find useful areas

- Datasets, data quality, analytical workflows, model evaluation, and reproducibility.
- Kaggle competition preparation and hackathon delivery workflows.
- SEO: search content, site architecture, local search, campaign planning, email, sales, and ecommerce.
- India and US administrative services, government casework, public policy, education, and research.
- Contracts, compliance preparation, business planning, creative work, media, and communication.

The router shows actual domain coverage. A topic's presence does not imply that every specialization, jurisdiction, or platform feature is covered.

## Accuracy and limits

Skills teach procedures and judgment. Current laws, agency requirements, fees, deadlines, platform rules, and delivery specifications are inputs to verify with their official source, not hardcoded current facts. Worked scenarios are fictional. Verification placeholders identify unresolved facts and where to check them.

`validated` means the repository's format checks passed. `quality` adds body-length, exact-duplicate, and registry-consistency checks. Neither proves factual accuracy or reliability across models. `audited` is reserved for a recorded substantive review, not automatically granted by a script. The library includes test cases; do not describe an unexecuted test as passed. See [logs/quality-review.md](logs/quality-review.md) for the actual review scope and limitations.

For law, finance, security, or other consequential decisions, use the task's professional and authorization boundaries. An organized brief or evidence table is not an authoritative legal determination or a production-system assessment.

## Inspect and validate

Run commands from this folder with an available Python 3 interpreter. The tools use the standard library.

```text
python tools/sf.py status
python tools/sf.py check-registry
python tools/sf.py validate --all
python tools/sf.py quality --all
python tools/sf.py coverage
python tools/sf.py overlap
python -m unittest discover -s tests -p test_sf.py
```

`overlap` produces lexical routing candidates for review; its output is not a semantic duplicate verdict.

## Export and test

```text
python tools/sf.py index --all
python tools/sf.py router
python tools/sf.py export dist/portable-skills
python tools/sf.py testpack CTR-001
```

The export contains one folder per validated or audited skill, with minimal `name` and `description` frontmatter and the full instructions. Generated exports are ignored by Git because they can be rebuilt from the source library. The testpack command creates a request and assertion file; run the request separately and retain actual results before claiming behavioral validation.

## Maintain the library

Read [AGENTS.md](AGENTS.md) and [SPEC.md](SPEC.md). Query registry records through `sf.py` rather than dumping the registry into a model context. Authoring helpers and their task records remain in `tools/` and `staging/` so examples and methods are reviewable. Helpers may regenerate their owned files; preserve reviewed changes in the authoring source before rerunning them.

`sf.py ingest <manifest.json>` appends a staged taxonomy after checking conflicts. Run ingestion serially, then validate the affected skills. It does not silently replace existing records. The prompts under `prompts/` support smaller maintenance batches; their batch sizes are workflow defaults, not a limit on an explicitly authorized larger task.

No license is selected on the user's behalf. Add your chosen license before inviting reuse under specific terms.
