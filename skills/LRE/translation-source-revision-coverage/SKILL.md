---
id: LRE-003
name: translation-source-revision-coverage
domain: Localization Resource Engineering
subdomain: Translation lineage
version: 1.0
description: Reconcile translated resources with current source keys and reviewed source revisions when renames or meaning changes can leave apparently complete catalogs stale.
triggers: ["check stale translations after source edits", "reconcile renamed translation keys", "trace translation source revisions", "audit current localization coverage", "find translations reviewed against old copy"]
not_for: ["design-token rename migration [DST-003]", "deciding translation fluency", "runtime fallback resolution [LRE-002]"]
requires: []
risk_level: medium
---

# Translation source revision coverage

## Purpose
Determine which current source messages have target entries reviewed against the intended source meaning and context. Keep resource-key presence, translation lineage and approval distinct so a renamed key or unchanged spelling does not silently authorize stale text.

## Inputs to collect
1. **Current source catalog:** Obtain scoped keys, source text, context and stable source revision identifiers. This defines current work. Default: none; keys without a trustworthy revision basis cannot support freshness claims.
2. **Target catalog:** Obtain locale-specific entries with their reviewed source revision and review state. This supplies lineage. Default: unknown lineage if metadata is absent, not automatically current or stale.
3. **Change ledger:** Obtain old-to-new key mappings, source meaning changes, context changes and any splits or merges. This distinguishes identity changes from content changes. Default: no assumed mapping from similar names.
4. **Approval policy:** Identify what review state qualifies and who can approve migration or meaning equivalence. This establishes the readiness rule. Default: inventory only until the project supplies its criterion.
5. **Consumer scope:** Obtain the current referenced keys and generated-resource boundary. This identifies retired candidates without deleting resources used elsewhere. Default: obsolete candidates remain retained pending consumer evidence.
6. **Execution scope:** Identify the input snapshot and permission to run a comparison on a copy. Default: read-only report; no translation overwrite or catalog cleanup.

If a required input has no safe default, ask in one message with at most three questions. Group source/change evidence, target review metadata and acceptance/consumer policy.

## Procedure
1. Freeze the source and target snapshots and explain how their source revision identifiers change when meaning or relevant context changes. ⚠️ A revision system that ignores context cannot prove that a translation still suits a newly reused interface role.
2. List every current source key independently of target coverage. A missing target entry must remain visible even when an older key has similar wording.
3. Attach target review metadata to the exact source revision it reviewed. Separate unknown revision, known older revision and current revision rather than treating all nonempty translations equally.
4. Compare approved key mappings with changed meaning and context. A key-only rename can nominate a translation for review or authorized migration; a split, merge or altered meaning requires explicit destination-specific decisions.
5. Detect collisions where the new key already has a target entry. Preserve both histories and ask the translation owner which content and review basis govern rather than overwriting one by file order.
6. Classify each current key as missing, lineage unknown, stale, review pending or ready under the supplied criterion. Keep coverage presence and review readiness as separate columns.
7. Identify target keys outside the current source scope as retired candidates. ⚠️ Do not delete them from a partial catalog comparison: external consumers, another namespace or a staged release may still use them.
8. Execute the bounded comparison and inspect cases where source text stayed identical but context changed. Confirm that the revision metadata captures those changes or leave freshness unresolved.
9. Prepare an owner queue for fresh translation, re-review, authorized key migration or consumer retirement checks. Retain old evidence until the project's migration condition is satisfied.
10. Replay the comparison after approved changes and report the exact source snapshot it now covers. A current result expires when the source meaning, context or acceptance policy changes.

The following runnable Python 3 fixture accepts dictionaries keyed by message identifier. Source values are immutable meaning-and-context revision labels supplied by the project; target records contain `source_revision` and `approved`. These are fictional schema fields, not a platform API. The comparison checks metadata only and does not judge the translation text. Save it as a Python file, run with the available Python 3 interpreter and record the actual environment.

```python
def coverage(source, target):
    rows = {}
    for key, revision in source.items():
        if key not in target:
            rows[key] = "missing"
        elif target[key].get("source_revision") is None:
            rows[key] = "lineage unknown"
        elif target[key]["source_revision"] != revision:
            rows[key] = "stale"
        elif target[key].get("approved") is not True:
            rows[key] = "review pending"
        else:
            rows[key] = "ready by supplied metadata"
    return rows, sorted(set(target) - set(source))

source = {"new.title": "meaning-B", "action": "meaning-C"}
target = {
    "old.title": {"source_revision": "meaning-A", "approved": True},
    "action": {"source_revision": "meaning-B", "approved": True}
}
rows, old = coverage(source, target)
assert rows == {"new.title": "missing", "action": "stale"}
assert old == ["old.title"]
assert coverage({"k": "r"}, {"k": {}})[0]["k"] == "lineage unknown"
assert coverage({"k": "r"}, {
    "k": {"source_revision": "r", "approved": False}})[0]["k"] == "review pending"
assert coverage({"k": "r"}, {
    "k": {"source_revision": "r", "approved": True}})[0]["k"] == "ready by supplied metadata"
print("lineage fixture checks passed; translation quality not assessed")
```

## Decision rules
- IF a key exists but its reviewed source revision differs THEN mark it stale BECAUSE presence alone does not show review of the current meaning.
- IF revision metadata is absent THEN mark lineage unknown BECAUSE missing evidence does not identify which source was reviewed.
- IF a rename has no approved equivalence mapping THEN retain the new key as missing BECAUSE similar key names do not authorize transferring a translation.
- IF current metadata reports approval THEN describe readiness as metadata-supported BECAUSE the comparison does not independently assess linguistic quality.
- IF old keys have unverified consumers THEN retain them pending retirement review BECAUSE a local source snapshot does not prove global disuse.

## Output template
```text
Snapshot: <source, target locale and revision scheme; up to three lines>
Acceptance basis: <supplied readiness criterion; up to two sentences>
Coverage ledger:
Current key | Target presence | Reviewed source | Current source | Readiness/action
<up to twelve rows; continue explicitly if larger>
Rename and collision queue: <up to five mappings, authority and unresolved conflicts>
Retired candidates: <keys and consumer checks, or None>
Executed check: <fixture or real comparison, observed result and environment reference>
Limits: <two sentences separating metadata from meaning and runtime behavior>
```

## Quality checklist
- [ ] Source revision identity includes relevant meaning and context changes.
- [ ] Every scoped current key has a coverage row.
- [ ] Unknown lineage is distinct from known stale lineage.
- [ ] Current revision and approval are separate checks.
- [ ] Renames use explicit mappings rather than name similarity.
- [ ] Destination collisions preserve both histories.
- [ ] Old keys remain candidates until consumer retirement evidence exists.
- [ ] The report does not claim linguistic or runtime validation from metadata.

## Anti-patterns
- **Nonempty means ready:** any target text counts as complete. Fix: compare reviewed source revision and required approval.
- **String-only identity:** identical source words conceal changed button or label context. Fix: include relevant context in revision tracking.
- **Rename auto-copy:** translations move by key resemblance. Fix: use approved mappings and retain destination-specific review decisions.
- **Collision overwrite:** a destination entry is replaced by migration order. Fix: preserve competing histories for owner disposition.
- **Cleanup by absence:** old keys are deleted from a partial comparison. Fix: trace consumers and staged-release needs first.

## Worked example
**Input:**
> Fictional app Elm has current source snapshot S, locale target snapshot T, and a revision scheme covering meaning and context. Current key menu.open has source revision B. T contains menu.open approved against A. Current key page.title has revision C but is absent from T; old key heading remains approved against C. A proposed rename heading to page.title has not been approved. Readiness requires current revision and explicit approval. No consumer inventory is available.

**Output:**
```text
Snapshot: Elm source S, target T, revision labels cover meaning and context.
Acceptance basis: Ready requires review against the current source revision and explicit approval.
Coverage ledger:
Current key | Target presence | Reviewed source | Current source | Readiness/action
menu.open | present | A, approved | B | stale; re-review current meaning/context
page.title | absent | none | C | missing; resolve proposed migration
Rename and collision queue: heading -> page.title is proposed only; translation owner must approve equivalence and migration before readiness can transfer.
Retired candidates: heading is outside current source scope; retain until consumer and migration checks establish its disposition.
Executed check: No execution claimed in this example; supplied metadata compared manually against the stated criterion.
Limits: Metadata does not establish translation fluency. No runtime fallback, live catalog change or consumer retirement was tested.
```

**Bad output:** “Copy heading to page.title and approve everything because both keys have translated text.”
This invents rename authority, ignores menu.open's stale revision and mistakes proposed content movement for current approval.

## Edge cases
- **One key splits into several contexts:** create a separate destination review row for each; do not duplicate approval across different meanings.
- **Source text reverts:** use the project's explicit revision/equivalence evidence before reusing historical approval; identical text may have different context.
- **Machine draft replaces reviewed text:** retain its own review state and provenance instead of inheriting the overwritten entry's approval.
- **Partial namespace export:** label retired results as outside this scoped source export, not globally unused resources.

## Test case
**Input:**
> Fictional app Fir keeps source key open but changes its role from a navigation command to a status adjective. Its revision scheme records context changes, so source revision advances from X to Y. Target text exists and is approved only against X. The words in the source happen to remain identical.

**Assertions:**
1. Marks the target stale despite identical source words and key presence.
2. Requests context-sensitive re-review against Y.
3. Preserves the historical approval against X without treating it as current.
4. Does not claim translation quality from metadata alone.
