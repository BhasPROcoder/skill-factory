# Phase engine

Order: ideate → scope → search → screen_extract → synthesize → design → execute → analyze → write → verify → review → format → submit → disseminate

| Phase | Skill | Batch available |
|---|---|---|
| ideate, scope | idea-scoping | Batch 2 |
| search | lit-search | Batch 1 |
| screen_extract | screen-extract | Batch 1 |
| synthesize | synthesis | Batch 2 |
| design, execute | method-experiment (survey-study / social-data when the paper type says so) | Batches 3–4 |
| analyze | analysis | Batch 3 |
| write, disseminate | paper-writer | Batch 2 |
| verify | verifier | Batch 1 |
| review, format, submit | review-submit | Batch 5 |

If a skill isn't installed yet, say so and do that phase in conversation with the same state commands, flagging that it isn't scripted.

## Per paper type (the `init` command applies this automatically)

| Paper type | Changes from "run everything" |
|---|---|
| empirical_ml | search light (focused related work), screen_extract light |
| slr | design = review protocol; execute skipped |
| mapping_study | design = mapping protocol; execute skipped |
| survey_study | search/screen light; execute = survey-study |
| social_mining | search/screen light; execute = social-data |
| tool_system | search/screen light |
| benchmark_dataset | search/screen light; execute = dataset build + datasheet + baselines |
| replication | ideate skipped; scope = pick target; search/screen light |
| position | design, execute, analyze skipped |
| case_study | search/screen light; execute = case protocol |
| mixed_methods | execute runs quantitative and qualitative branches in parallel |
| thesis_chapter | submit, disseminate skipped |

"light" means: no PRISMA protocol, single query round, single-stage screening of related work, extraction limited to a comparison table. Say this to the user when it applies.

## Gates by phase
- search: every query logged with date and hit count; partial queries (hits > limit) resolved or accepted.
- screen_extract: G-PROTOCOL, G-KAPPA-title_abstract, G-KAPPA-full_text (SLR/mapping only), G-EXTRACT.
- verify: G-CITE + G-NUM must pass before format/submit.
