Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-019
name: evidence-span-relation-candidate-extraction
domain: Graph Engineering Foundations
subdomain: Evidence-linked relation extraction
version: 1.0
description: Convert supplied text into reviewable relation candidates with exact evidence spans and preserved qualification when preparing knowledge graph assertions.
triggers: ["extract graph relations from text", "attach evidence spans to relations", "review relation extraction candidates", "preserve negation in graph extraction", "map document statements to predicates"]
not_for: ["designing relation meanings [GRF-018]", "auditing prose citations [GRV-008]", "extracting study outcome fields [GRV-004]", "merging entity identities [GRF-002]", "automatically verifying real-world truth"]
requires: []
risk_level: medium
---

# Evidence Span Relation Candidate Extraction

## Purpose
Produce an evidence ledger connecting proposed graph relations to exact passages in a frozen text revision. Preserve who said what, about whom, under which qualifications, so a reviewer can decide whether an assertion is admissible. A correctly located quotation establishes textual support, not independent truth.

## Inputs to collect
1. **Source text and revision** — supply the exact text to inspect and its source identifier. Why: offsets refer to a particular representation. Default: none; required before extracting candidates.
2. **Relation vocabulary** — supply predicate definitions, direction and permitted endpoint classes. Why: a similar verb can mean a different relation. Default: provisional labels requiring vocabulary review; never invent an approved predicate.
3. **Entity inventory** — supply scoped identifiers, aliases and identity evidence. Why: a mention must resolve before its relation can enter a graph. Default: document-local mention IDs with unresolved global identity.
4. **Extraction scope** — identify documents, sections and relation families. Why: a bounded inspection supports a truthful coverage statement. Default: all supplied text, with every skipped section listed.
5. **Qualification policy** — define treatment of reported speech, negation, hypotheses, time and conditions. Why: losing these changes the claim. Default: retain them in candidate fields; no automatic graph insertion.
6. **Review owner** — identify who approves source-supported assertions and how decisions are recorded. Why: extraction and acceptance have different evidence requirements. Default: pending review with no approved assertions.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Freeze the source representation and assign its revision identifier before locating spans.
2. List the inspected sections and any unavailable content, including unreadable tables or figures.
3. Identify entity mentions with document-local identifiers while retaining the exact mention spelling.
4. Resolve each mention against the supplied inventory, recording alternatives when more than one referent fits.
5. Select a passage that supports the proposed relationship together with its necessary surrounding qualification.
6. Record the passage using a source revision and zero-based, end-exclusive character offsets into the frozen Python string, plus its exact quotation.
7. ⚠️ Classify polarity, modality, attribution and conditions from the entire supporting passage; retain ambiguous values as unknown instead of reading only the relationship verb.
8. Map the qualified statement to the vocabulary, checking subject/object direction and endpoint classes.
9. Assign each candidate a disposition: ready for semantic review, unresolved, excluded from requested scope, or unsupported mapping. Record a reason for every disposition.
10. Verify the evidence spans mechanically and review the proposed meaning against the full passage separately.
11. Group repeated candidates by proposed relation while retaining their distinct evidence occurrences and source dependencies.
12. Deliver the candidate ledger and review queue; record any later approval as a separate dated decision referring to the frozen candidate revision.

Use this Python 3 reference to verify span integrity. Record the installed interpreter version when executing it. It deliberately accepts supplied semantic annotations without attempting to understand language; a passing check never approves those annotations. Each support span must be nonempty, within the source, and an exact slice. Several spans can support a single candidate, but their logical connection still requires review.

```python
def verify_spans(texts, candidates):
    seen = set()
    for candidate in candidates:
        cid = candidate["id"]
        if not isinstance(cid, str) or not cid or cid in seen:
            raise ValueError("invalid or duplicate candidate ID")
        seen.add(cid)
        if not candidate["supports"]:
            raise ValueError("missing evidence")
        for source, revision, start, end, quote in candidate["supports"]:
            key = (source, revision)
            if key not in texts:
                raise ValueError("unknown source revision")
            text = texts[key]
            if type(start) is not int or type(end) is not int:
                raise ValueError("offsets must be integers")
            if not 0 <= start < end <= len(text):
                raise ValueError("span outside source")
            if text[start:end] != quote:
                raise ValueError("quotation mismatch")
    return len(seen)

text = "A owns B. A owns B."
texts = {("fiction", "v1"): text}
candidates = [
    {"id": "c1", "supports": [("fiction", "v1", 0, 9, "A owns B.")]},
    {"id": "c2", "supports": [("fiction", "v1", 10, 19, "A owns B.")]}
]
assert verify_spans(texts, candidates) == 2
bad = [{"id": "c3", "supports": [("fiction", "v1", 0, 8, "A owns B.")]}]
try:
    verify_spans(texts, bad)
except ValueError:
    pass
else:
    raise AssertionError("changed quotation boundary accepted")
print("distinct occurrences and invalid boundary checked")
```

Before using offsets from another system, verify its indexing convention against the frozen text. Byte offsets, normalized text and rendered document positions are not interchangeable with these string offsets. Preserve the conversion artifact when deriving text from another format; unverified conversion prevents a claim of exact correspondence to the original document.

## Decision rules
- IF a passage denies a relation THEN preserve negative polarity and withhold a positive assertion BECAUSE deleting negation reverses the statement.
- IF a relation is conditional or hypothetical THEN retain its condition and modality BECAUSE a scenario is not an occurrence report.
- IF a pronoun has several plausible referents THEN leave endpoint resolution pending BECAUSE selecting one silently invents identity evidence.
- IF identical wording occurs repeatedly THEN retain occurrence-specific offsets BECAUSE text matching alone cannot identify the intended occurrence.
- IF the source revision changes THEN relocate and recheck all affected spans BECAUSE old offsets may point to different words.
- IF no supplied predicate matches the meaning THEN request vocabulary review BECAUSE forcing a mapping changes the claim.

## Output template
```text
Scope: <source revisions and inspected sections; maximum 60 words>
Vocabulary: <revision or provisional; unresolved mappings>
Candidates:
<ID | subject mention/resolution | predicate | object mention/resolution | polarity/modality/attribution/conditions | evidence spans | disposition and reason>
Span checks: <executed/pending, representation, result; maximum 60 words>
Review queue: <candidate | decision owner | evidence needed; maximum 10 rows>
Coverage: <omissions and extraction limitations; maximum 60 words>
Acceptance: <separate recorded approvals or none; maximum 40 words>
```
Use one row per qualified candidate. Supply a separate complete ledger when more than ten candidates would obscure the review queue; do not truncate candidates silently.

## Quality checklist
- [ ] Every span names the frozen source revision.
- [ ] Quoted text matches its declared offset convention.
- [ ] Negation and hypothetical language survive in candidate fields.
- [ ] Ambiguous referents retain alternatives or unresolved status.
- [ ] Predicate direction and endpoint types are explicitly checked.
- [ ] Repeated wording retains distinct source occurrences.
- [ ] Mechanical span checks are distinguished from semantic review.
- [ ] No extraction result is described as an independently verified fact.

## Anti-patterns
- **Verb-only extraction**: omit a nearby denial. Fix: inspect the complete qualified clause.
- **Pronoun guessing**: bind an ambiguous pronoun to the nearest name automatically. Fix: record unresolved alternatives.
- **Quotation camouflage**: attach a genuine quote to an unsupported predicate. Fix: review the mapping separately from span integrity.
- **Repeated-text collapse**: use the first matching occurrence for every candidate. Fix: preserve the intended occurrence offsets.
- **Approval by execution**: promote candidates because code passed. Fix: require an explicit semantic acceptance record.

## Worked example
**Input:** Fictional source D revision v1 contains exactly: “A does not own B.” Supplied entity IDs A and B are resolved. Vocabulary V defines owns as a positive ownership relationship; no negative-edge representation is approved.

**Output:**
```text
Scope: Entire supplied D v1 text inspected.
Vocabulary: V; owns has no approved negative-edge representation.
Candidates:
c1 | A/resolved | owns | B/resolved | negative/asserted/source D/no condition | D v1 [0,17): A does not own B. | unresolved: preserve denial; positive insertion prohibited
Span checks: Pending execution; Python string offsets, zero-based and end-exclusive.
Review queue: c1 | vocabulary owner | decide how a source denial should be represented
Coverage: Only supplied sentence inspected; source truth not independently verified.
Acceptance: None.
```

**Bad output:** “Insert A owns B because both entities and the ownership verb occur.”
This discards the explicit denial and invents approval.

## Edge cases
- **Reported speech**: retain the attributed speaker and reporting source; do not turn a speaker's statement into narrator-confirmed truth.
- **Hypothetical ownership**: retain the hypothetical condition and keep the positive relation out of the asserted-fact view.
- **Ambiguous mention**: preserve local mention identity and list candidate global IDs; never merge them to make extraction succeed.
- **Source correction**: retain the old ledger for traceability and create a new revision with relocated evidence.
- **Contradictory passages**: preserve both qualified candidates and route the conflict for review; extraction does not choose a winner.

## Test case
**Input:**
> Fictional text says: “A met C. If A owned B, it could lease B.” Extract ownership and leasing candidates; the referent of “it” is unresolved and no ownership occurrence is asserted.

**Assertions:**
1. Preserves the ownership condition and hypothetical modality.
2. Keeps the leasing subject unresolved instead of guessing a referent.
3. Attaches source passages without claiming that correct offsets establish truth.
4. Records no approved positive ownership or leasing assertion.
</skill>

<user_request>
Fictional text says: “A met C. If A owned B, it could lease B.” Extract ownership and leasing candidates; the referent of “it” is unresolved and no ownership occurrence is asserted.
</user_request>
