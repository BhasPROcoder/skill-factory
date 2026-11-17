# GRF-019 independent review

Reviewer g18_independent_review, 2026-11-14. Read complete candidate and author evidence; inspected procedures of GRV-008 and GRV-004 and previously reviewed GRF-018. GRV-008 repairs prose claims and GRV-004 structures study results. This candidate instead constructs qualified, directional relation candidates with mention identity, revision-bound occurrence spans and pending semantic approval. The scoped neighbor comparison supports a distinct workflow; it is not a whole-library semantic audit.

## Executed checks

Python 3.14.6 executed the complete embedded snippet successfully. Independently verified full spans for ordinary, negative and hypothetical sources: lengths 9, 17 and 40 respectively. Rejected empty support, unknown revision, Boolean offset, negative start, excessive end, incorrect quotation boundary and duplicate candidate ID. Repeated-text fixture retained both distinct occurrences. Empty candidates returned zero; this does not establish extraction coverage. An intentionally wrong semantic annotation passed, confirming the expressly documented boundary that span verification does not understand or approve meanings. No registry mutations performed.

## Independently produced scenario outputs

Ordinary source D v1: A owns B. Supplied inventory resolves A/B with endpoint classes compatible with V.

```text
Scope: D v1, entire supplied sentence.
Vocabulary: V; owns direction and endpoint types match the supplied contract.
Candidates:
c1 | A/resolved | owns | B/resolved | positive/asserted/source D/no condition | D v1 [0,9): A owns B. | ready for semantic review: qualified mapping supported
Span checks: Executed; Python string positions; exact full span passed.
Review queue: c1 | designated reviewer | semantic acceptance decision
Coverage: Supplied sentence only; no independent truth verification.
Acceptance: None.
```

Missing source request: “Extract ownership relations” with no text.

```text
Scope: Source unavailable.
Vocabulary: Provisional; no predicate approved.
Candidates:
None; no source or offsets invented.
Span checks: Pending source input.
Review queue: extraction | requester | provide frozen source text and revision; provide vocabulary and entity inventory if available
Coverage: Nothing inspected.
Acceptance: None.
```

Negative source D v1: A does not own B. Vocabulary permits only positive owns edges.

```text
Scope: D v1, complete supplied sentence.
Vocabulary: V; negative-edge representation unresolved.
Candidates:
c1 | A/resolved | owns | B/resolved | negative/asserted/source D/no condition | D v1 [0,17): A does not own B. | unresolved: preserve denial, prohibit positive insertion
Span checks: Executed; exact Python string slice passed.
Review queue: c1 | vocabulary owner | approve a denial representation
Coverage: One sentence; source truth unverified.
Acceptance: None.
```

Hypothetical source D v1: A met C. If A owned B, it could lease B. Global identities and predicate typing are unavailable.

```text
Scope: D v1, all supplied text; extraction limited to ownership and leasing.
Vocabulary: Provisional owns and leases; typed mappings pending.
Candidates:
c1 | A/local mention | owns | B/local mention | positive/hypothetical/source D/if A owned B | D v1 [0,40): A met C. If A owned B, it could lease B. | unresolved: hypothetical ownership, identity and vocabulary pending
c2 | it/unresolved | leases | B/local mention | positive/conditional possibility/source D/if A owned B | D v1 [0,40): A met C. If A owned B, it could lease B. | unresolved: ambiguous subject and hypothetical modality
Span checks: Executed; full passage exactly matches frozen string.
Review queue: c1,c2 | vocabulary and source reviewers | resolve identity and typed mappings without turning hypotheticals into observations
Coverage: Meeting relation excluded by scope; no occurrence asserted for ownership or leasing.
Acceptance: None.
```

Repeated source fiction v1: A owns B. A owns B.

```text
Scope: fiction v1, both sentences.
Vocabulary: Provisional owns; endpoint types unresolved.
Candidates:
c1 | A/local | owns | B/local | positive/asserted/source fiction/no condition | fiction v1 [0,9): A owns B. | unresolved: mapping and identity review
c2 | A/local | owns | B/local | positive/asserted/source fiction/no condition | fiction v1 [10,19): A owns B. | unresolved: mapping and identity review
Span checks: Executed; both occurrences passed and retain different positions.
Review queue: c1,c2 | reviewer | group proposed relation while retaining both dependent occurrences
Coverage: Both sentences inspected; repetition in one source is not independent corroboration.
Acceptance: None.
```

## Verdict

Accept within the documented extraction-and-review scope. No required repair found. The worked example uses all seven template labels in order, preserves denial, has correct [0,17) arithmetic and accurately labels execution pending. The verifier deliberately assumes dictionary/tuple-shaped inputs and reports malformed structures through ordinary Python exceptions; it is a bounded reference, not a production parser. The procedure separately checks semantic annotations, identity, typing and approval. No invented external facts, dates, citations or statistics found. Source correspondence beyond the frozen string, linguistic completeness and real-world truth remain unproven as explicitly stated.
