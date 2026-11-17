# GRF-022 independent recovery review
Coordinating reviewer, 2026-11-14. Author handle disappeared before its completion report; recovered complete draft without assuming author tests occurred.

Read complete skill. Distinctness relative to G21: evaluates paired workloads with graph identity/join failure decisions and alternate valid evidence paths, rather than constructing a question packet. General evaluation overlap still requires selected CTG-008 body comparison before acceptance.

Executed embedded Python and independent test request: graph evidence true/answer false versus baseline evidence false/answer true returns neither combined success and one unsupported correct baseline answer; unresolved second question is excluded. Empty matched rows produce zero eligible; unanswerable matched question is excluded. Mismatched IDs, differing scope, numeric Boolean substitutes and conflicting answerability reject. All passed. Fictional example counts recomputed: three eligible, one graph-only, one baseline-only, one neither, one graph unsupported-correct. Code only counts supplied judgments; semantic adjudication stays procedural.

Missing-input scenario: absent matched question IDs or provenance means no paired aggregate; request snapshots, run artifacts and rubric together. Edge scenario: alternative valid graph route remains sufficient evidence even when answer is wrong; baseline correct answer remains unsupported; unresolved pair remains excluded. No rate when zero eligible, no claim of statistical or deployment superiority.

Hold acceptance pending substantive CTG-008/CTG-005 comparison and complete scenario outputs. Structural checks and code execution alone do not satisfy remaining gates.

## Completed neighbor and scenario review
Read complete CTG-008 and CTG-005. CTG-008 provides generic case freezing, calibrated qualitative judges and promotion slices; CTG-005 provides bounded source inspection and resumable handoffs. Neither specifies alternative graph path sufficiency, entity-join validity, independent retrieval-support/answer labels, or paired supported-answer outcomes with an excluded-pair ledger. G22 adds these operational decisions and has a distinct evidence-evaluation artifact. Shared generic evaluation safeguards are appropriate, not the basis of uniqueness.

Ordinary fictional case: q1 graph sufficient/correct, baseline insufficient/incorrect; q2 graph insufficient/correct, baseline sufficient/correct; q3 both sufficient/incorrect. Produced output:
```text
Contract: Fictional F1 questions and sources; G1/B1 configurations; supplied equal resource contract.
Question ledger: q1 | answerable | true/true | false/false | adjudicated alternative graph path | baseline omission; q2 | answerable | false/true | true/true | graph lacks supporting passage | unsupported graph answer; q3 | answerable | true/false | true/false | adjudicated sources sufficient | answer errors.
Paired counts: eligible 3; excluded 0; both 0; graph-only 1; baseline-only 1; neither 1.
Support gaps: q2 graph unsupported-correct; q3 both evidence-sufficient/answer-incorrect.
Slices: No critical cost policy supplied; opposing q1/q2 outcomes retained.
Execution: Reference arithmetic executed in recovery review; no live retrieval runs performed.
Decision: No dominance or promotion recommendation; obtain failure costs and preserve fresh held-out questions for tuned configurations.
```

Missing-input case asks for comparison with only two answers, no question IDs/source snapshots. Produced output:
```text
Contract: Unresolved; matched questions, snapshots and resource contract missing.
Question ledger: No adjudicated pairs; supplied answers retained as unscored artifacts.
Paired counts: Not computed; eligibility not established.
Support gaps: Evidence sufficiency unknown for both answers.
Slices: Unavailable.
Execution: No paired run or semantic judgment performed.
Decision: Unresolved. Which matched question/source revisions apply? What run artifacts and budgets were used? What evidence and answer rubric governs adjudication?
```

Edge case follows Test case: qA graph valid alternative support but wrong answer, baseline right answer without support; qB unresolved evidence. Produced output:
```text
Contract: Fictional F2 matched questions/sources and supplied resource contract; G2/B2 frozen runs.
Question ledger: qA | answerable | true/false | false/true | adjudicated alternative route | graph answer error and baseline unsupported answer; qB | answerable | unresolved/true | unresolved/true | support unresolved | pending adjudication.
Paired counts: eligible 1; excluded 1; both 0; graph-only 0; baseline-only 0; neither 1.
Support gaps: qA baseline unsupported-correct; qA graph sufficient evidence with wrong answer.
Slices: qB excluded explicitly; no critical cost policy supplied.
Execution: Matching label fixture executed; semantic judgments supplied by fictional case.
Decision: Neither pipeline meets combined success on qA; resolve qB evidence without counting uncertainty as failure. No winner from answer correctness alone.
```

All four embedded Test case assertions satisfied. Stable arithmetic and bounded code behavior checked; no current external factual claims introduced. Accept recommendation within declared paired graph-retrieval evidence evaluation scope. Earlier hold is resolved by this substantive comparison and full outputs; no whole-library uniqueness or real-world truth guarantee.
