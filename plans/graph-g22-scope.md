# G22 retrieval evaluation discovery card

Candidate only; no registry entry or accepted skill. Follow G21 implementation readiness before authoring.

Deliverable: paired question-level graph/plain retrieval evaluation ledger separating seed-resolution failures, missing evidence paths, incorrect joins, source support failures, and answer fabrication. Freeze both retrieval configurations, graph and document snapshots, question set, evidence adjudication, and resource budget before comparison.

Catalog metadata reviewed through sf.py: CTG-008 language-model-evaluation-harness, CTG-005 bounded-context-retrieval-handoff, TML-001 validation-split-design. These describe general evaluation, handoff, and split design. Metadata is insufficient to establish uniqueness: substantively inspect those selected bodies and actual G21 before authoring. Reject this candidate if its procedure adds only graph terminology to a general harness.

Potential unique procedure: identify valid alternative evidence paths rather than exact path-string equality; score retrieval sufficiency separately from answer correctness; retain cases where the correct answer is generated without retrieved support; classify failed entity joins separately from missing sources; compare graph and document baselines on the same questions without using test questions to tune relation filters. A path's existence does not prove its semantic composition supports an answer. Record both question-level results and denominators, and preserve uncertainty where evidence labels are unresolved.

Acceptance cases to design: equivalent alternate paths; answer correct but unsupported; path connects identical labels with distinct entity identities; source absent from both snapshots; graph evidence available but retrieval budget truncates it; no answerable questions in a slice; baseline wins on some questions while graph wins on others. Avoid selecting a winner from an aggregate without examining relevant failure costs and unresolved cases.

Code scope should compute transparent paired counts from supplied adjudicated labels and refuse mismatched question sets or snapshots; it should not pretend to adjudicate meaning automatically. Any synthetic arithmetic must be recomputed. No numerical quality threshold, software version requirement, research claim, or current platform rule is proposed here. Independent authoring and review remain required.
