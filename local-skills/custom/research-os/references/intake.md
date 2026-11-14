# Intake block

Ask with AskUserQuestion. Two calls of up to 4 questions each. Topic is free text: ask it in plain chat first if the user hasn't said it.

## Call 1
1. **Paper type** — options depend on the topic; offer the 3 most plausible + let Other cover the rest. Values: empirical_ml, slr, mapping_study, survey_study, social_mining, tool_system, benchmark_dataset, replication, position, case_study, mixed_methods, thesis_chapter.
2. **Subfield** — the 3 most plausible of: ml_dl, nlp_llm, cv, systems_distributed, software_engineering, security_privacy, hci, databases, networking, theory_algorithms, cs_education, human_ai_interaction, robotics_embedded.
3. **Target venue** — (a) arXiv preprint first, then a workshop (recommended for a first paper: fastest feedback) (b) a named conference (c) a Q1 journal (d) undecided. Ask for the deadline in the same answer.
4. **Run mode** — copilot (recommended: you see every checkpoint) / autopilot / sprint.

## Call 2
1. **Authorship** — solo / with a co-author (who can approve checkpoints).
2. **Human participants** — none / yes, ethics approval in progress / yes, approved / yes, not started (→ risk).
3. **Compute** — 6 GB local + Colab/Kaggle free (recommended default) / paid GPU available / CPU only.
4. **Data access** — public data only / I have institutional access to paywalled papers / private dataset.

## Defaults when the user says "just start"
copilot · solo · 6 GB + free cloud · no human participants · venue undecided. State these defaults in one line and record each with `--by autopilot_assumption`.
