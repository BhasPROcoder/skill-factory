# GRF-021 author checks

2026-11-14. Draft for independent review; no registry mutation.

Read AGENTS/SPEC and graph queue earlier in this worker; inspected GRF-006 actual traversal procedure and CTG-005 actual generic handoff procedure. GRF-018 vocabulary scope and GRF-019 extraction were reviewed during preceding assignment. G20 was not present when checked; final reviewer should compare its constraint-validation scope before admission.

Distinct deliverable: a question-to-seed-to-path-to-passage evidence packet, with candidate omissions, source qualifications, unanswered needs and a matched-source passage-only baseline. GRF-006 produces reachable nodes and minimum-hop witnesses; CTG-005 produces a generic task handoff; GRF-018 licenses meanings and inference; GRF-019 extracts relation candidates from text. This skill consumes their outputs and does not duplicate their deliverables. No external code/text copied.

Specific claims checked: Python 3 standard syntax and deterministic given-order selection; fixture passages each contain ten characters; shared passages charged once; no token-cost equivalence claimed. Greedy selection explicitly does not optimize relevance or coverage. Connectivity and passage existence do not prove semantic support or truth. No changing platform details or external factual claims added.

sf.validate_text returned errors=[], warnings=[]. Embedded Python executed successfully. Additional executed assertions passed for missing passages, reversed/disconnected path, shared-passage budget accounting, both paths at twenty characters, and empty selection at zero budget.

Manual scenario outputs: ordinary fixture selects c1, omits c2 by packet budget and marks baseline pending. Missing question/source inputs trigger collection of the required question and snapshot/evidence rather than invented seeds. Ambiguous seed retains alternatives and provisional branches. Missing evidence and budget omissions are separate ledger reasons; neither produces an answer. A connected path with incompatible semantic interpretation remains pending semantic review despite code passing. All eight template fields appear in worked output, including unexecuted check labels.

Limitations: selector is not candidate enumeration, NLP, inference, relevance ranking or end-to-end evaluation. Independent reviewer should execute additional adversarial fixtures and compare G20 before acceptance.
