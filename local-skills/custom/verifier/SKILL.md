---
name: verifier
description: Verification gate for ResearchOS drafts. Use when the user wants to check that every reference in a draft or .bib is real (DOI/Crossref/OpenAlex/arXiv/Semantic Scholar), detect retracted papers or preprints that now have a published version, find broken BibTeX, check that each cited paper actually supports the sentence citing it, check every number in the draft against results files and run IDs, or decide whether a draft may go to submission. Do NOT use for finding new papers (lit-search), screening papers (screen-extract), improving style, clarity or argument (review-submit), or rewriting sentences (paper-writer).
---

# verifier

## Purpose
Nothing reaches submission with a citation that doesn't resolve, a claim its source doesn't support, or a number that can't be traced to a run or a source. Existence checks are deterministic. Support checks are LLM judgements, made by two isolated checkers and spot-checked by the user; say so in the methods section.

## Runtime check
`python -c "import researchos_core"`. On claude.ai the APIs aren't reachable from the sandbox: resolve each reference with WebSearch/WebFetch against doi.org, arxiv.org or the publisher page, mark every result "web-checked", and state that the gate is advisory, not scripted.

## Inputs
- Draft: `paper/sections/*.md|.tex`, `paper/main.tex` (or paths passed with `--draft`).
- `lit/references.bib` exported by lit-search (each entry has `note = {ResearchOS S-xxxx}`).
- `registry/runs.jsonl` and `results/<run_id>/metrics.json|csv`.
- Trace-tag conventions in `references/trace_tags.md`.

## Workflow
1. **References.** `python -m researchos_core.verify refs --cited-only`
   Report from `verify/refs.md`: unresolved (possible fabrication), title/year/author mismatches, retracted, preprint-with-published-version, missing BibTeX fields, duplicate keys, entries not linked to the source registry. Lookup failures are `unverified` and block the gate until a re-run succeeds; never mark them resolved yourself.
2. **Claims (fan-out F7).** `python -m researchos_core.verify claims-prepare`
   Finds every sentence with a citation (`\cite{}`, `[@key]`, `[S-0001]`, or an `S-` trace tag), registers it in `registry/claims.jsonl`, and writes briefs: two checkers per batch with different framings. Spawn all checker agents in one message (parallel) with: "Read the brief at <path> and follow it exactly. Do not open other files in that fanout folder." Then `python -m researchos_core.verify claims-merge --fanout <id>`.
   Merge rule per (claim, source): both supported → supported; both unsupported → unsupported; any other mix → partial; any cannot_access → unverified (get the PDF from the user, run `screen fulltext --ids S-…`, re-check).
3. **Spot check (mandatory).** Show `verify/spot_check.csv` (10 % of supported claims). The user marks agree/disagree. `python -m researchos_core.verify spot-check`. Any disagreement flips that claim to partial and raises a high risk about checker reliability: offer to re-check all supported claims.
4. **Escalate checkpoint** for `verify/claims_review.md`: for each partial/unsupported claim, offer (A) rewrite the sentence to match what the source says (paper-writer), (B) change the citation, (C) keep a partial claim deliberately: `python -m researchos_core.verify ack --claim C-xxxx --rationale "..."`. Unsupported claims cannot be acknowledged.
5. **Numbers.** `python -m researchos_core.verify numbers`
   Every result or statistic in prose must be tagged (see `references/trace_tags.md`). Tagged values are compared with the results files at the displayed precision (0.83 matches 0.8312; 83.1% matches 0.8312). Untagged numbers are listed with context; years, section/table/figure numbers and list markers are ignored. Report mismatches first.
6. **Gate.** `python -m researchos_core.verify gate`
   PASS only when: 0 unresolved/mismatched/unverified references, 0 retracted, 0 BibTeX errors, all references linked to the registry, every claim supported or acknowledged-partial, no unknown citation keys, 0 mismatched or untraced numbers, and the draft hasn't changed since claims were prepared. Show the reasons list verbatim on FAIL.

## Parallel agents
F7: two isolated checkers per batch of 30 claims (framing A source-first, B claim-first). Failures: missing verdicts leave the claim `unverified` (blocks); invalid lines are rerun once with the validation error.

## Checkpoints
Spot check (mandatory) · claims review (Escalate) · gate result (Approve; mandatory before format/submit).

## Outputs
`verify/refs.json`, `verify/refs.md`, `verify/claims_batch_*.jsonl`, `verify/claims_review.md`, `verify/spot_check.csv`, `verify/unknown_citations.json`, `verify/numbers.json`, `registry/claims.jsonl`, `state.verification`.

## Quality gates
- **G-CITE** and **G-NUM**, combined by `verify gate`. No other path sets `verification.gate = pass`. If the user asks to skip it, explain what reviewers will find, and record their decision with `ros decide --type approve --irreversible`; the gate itself stays FAIL.

## Good vs bad
Bad: "Explanations reduce overreliance [@bansal2021]" when the paper found explanations *increased* acceptance of wrong AI advice. The checkers return unsupported; the fix is to rewrite the claim, not to re-run until it passes.
Good: "In Bansal et al.'s experiments, explanations increased acceptance of AI recommendations whether or not they were correct [@bansal2021]" with locator p. 7.

## Failure modes
- Crossref down → refs `unverified`; re-run later. Don't downgrade the gate.
- Draft uses author–year text citations without keys → claims-prepare finds nothing; ask the author to use keys or `[S-xxxx]`.
- Results live in a notebook only → numbers can't be traced; ask method-experiment to emit `results/<run_id>/metrics.json`.
