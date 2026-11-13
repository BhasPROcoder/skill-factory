# Independent LRE review

Reviewer recover_atr did not author LRE. Read all three instructions and the repaired LRE-001 example, then executed `python logs/b6_lre_review.py` on observed Python 3.14.6. The script extracts and executes each saved skill's Python block, runs fresh fixture assertions, and reports source hashes. All embedded and fresh assertions passed. No production formatter, live loader, interface rendering or translation fluency was tested. All requests below are fictional; locale names are fixture labels rather than claims about real languages.

## LRE-001 ordinary

Request: Fictional parcel app P, source S and target T for locale coast, uses the documented double-bracket grammar. Contract requires sender, recipient and parcel once each. Pattern is `[[recipient]] receives [[parcel]] from [[sender]]`. No competent language-review evidence or UI render is supplied. Produce the bounded check.

Actual output:
```text
Boundary: P, source S/target T, coast, restricted double-bracket fixture grammar.
Contract ledger:
Key/branch | Parameter and role | Target occurrence | Mechanical finding | Meaning review
delivery/default | sender gives parcel | once after from | present once | pending competent review
delivery/default | recipient receives parcel | once before receives | present once | pending competent review
delivery/default | parcel being transferred | once | present once | pending competent review
Executed cases: Python 3.14.6 independent check returned missing=[] and unexpected=[].
Repairs: No token-count repair established; obtain role review and distinct-value rendering before broader approval.
Pending: Who can review the locale's role expression, and where can the pattern be rendered with distinct fictional values?
Limits: Fixture token identities pass. Meaning and interface behavior remain unverified.
```

Checks: passed token correspondence without equating reordered tokens to an error or linguistic approval. The request defines the contract; no parameter role was inferred solely from an identifier.

## LRE-001 missing parameter

Request: Same fictional boundary and contract, but target is `[[parcel]] delivered to [[recipient]]`. Caller still supplies sender. Produce the defect record, without changing source requirements.

Actual output:
```text
Boundary: P, source S/target T, coast; fixture grammar and unchanged contract.
Contract ledger:
Key/branch | Parameter and role | Target occurrence | Mechanical finding | Meaning review
delivery/default | sender gives parcel | absent | missing sender | pending repair
delivery/default | recipient receives parcel | once | present | not linguistically assessed
delivery/default | parcel transferred | once | present | not linguistically assessed
Executed cases: Independent Python check returned missing=[sender], unexpected=[].
Repairs: Pattern owner restores the required sender role or obtains an explicit approved contract change; recheck token correspondence and render distinct values.
Pending: Which corrected target pattern expresses all required roles?
Limits: Missing token is established under the supplied contract. No live formatter or display has been inspected.
```

Checks: absent target parameter reported separately from unavailable caller data; does not delete contract requirement to make the check pass.

## LRE-001 edge: repeated parameter

Request: Same fictional boundary, pattern `[[sender]] [[sender]] [[parcel]] [[recipient]]`, required list still one of each. A stakeholder says a name appearing twice is harmless. Also assess `[[parcel-name]]` under this restricted grammar.

Actual output:
```text
Boundary: P, source S/target T, coast; fixture grammar, once-per-parameter contract.
Contract ledger:
Key/branch | Parameter and role | Target occurrence | Mechanical finding | Meaning review
delivery/default | sender gives parcel | twice | unexpected extra sender | explicit repetition permission absent
delivery/default | parcel and recipient | once each | no missing tokens | not linguistically assessed
alternate/default | parcel-name | malformed for fixture identifier grammar | unsupported syntax | cannot establish production interpretation
Executed cases: Repetition check returned missing=[], unexpected=[sender]. Alternate pattern returned syntax=unsupported or malformed token.
Repairs: Owner corrects repetition or supplies an approved branch contract; identify the real formatter before interpreting hyphenated syntax outside the fixture.
Pending: Is repetition actually permitted by the message contract, and what grammar governs the alternate pattern?
Limits: Fixture results do not establish whether a real formatter accepts the alternate spelling. No language or UI acceptance is claimed.
```

Checks: counted excess occurrence, retained policy-dependent repetition, rejected unsupported fixture token rather than treating it as an ordinary production variable.

## LRE-002 ordinary

Request: Fictional app M asks for go in namespace actions, snapshot R, requested coast. Explicit order coast then island; both loaded; empty values do not qualify. Coast supplies Proceed and island Fallback.

Actual output:
```text
Lookup: M, go, actions, coast, snapshot R.
Policy: coast then island; null and empty missing; both bundles loaded.
Trace:
Candidate | Loading state | Key/value state | Decision
coast/actions | loaded | go=Proceed | selected
Selection: Fixture selects Proceed from coast; island is not reached.
Coverage: Requested-locale resource is present under the supplied policy. Translation quality is not established.
Correction and replay: No resolution correction identified; compare actual runtime trace if runtime assurance is required.
Evidence limit: Independent Python 3.14.6 result reports coast/Proceed and one selected trace entry. No live application executed.
```

Checks: stops at first valid candidate without inferring approval from fallback availability.

## LRE-002 missing resources

Request: Fictional M lookup go, actions, coast, snapshot R2; order coast/island/inland. Coast bundle absent, loaded island lacks key, loaded inland has explicit null. No pending load is reported; no application missing-key behavior supplied.

Actual output:
```text
Lookup: M go, actions, coast, supplied R2 snapshot.
Policy: coast then island then inland; null/empty missing.
Trace:
Candidate | Loading state | Key/value state | Decision
coast/actions | unavailable in snapshot | no bundle | continue
island/actions | loaded | key absent | continue
inland/actions | loaded | null | skip by policy
Selection: No candidate supplies a value; fixture locale and value are null.
Coverage: No usable value in the supplied chain; requested-locale translation unavailable.
Correction and replay: Resource owner supplies intended go resource; replay chain after update. Obtain application's missing-key behavior before claiming a displayed placeholder.
Evidence limit: Independent fixture trace distinguishes absent bundle, absent key and null value. No runtime loading failure or observed placeholder is inferred.
```

Checks: absence categories remain separate; missing display behavior not invented.

## LRE-002 edge: intentional empty value

Request: Fictional M subtitle, actions, coast, snapshot R3; coast has empty string, island has Extra; explicit policy permits empty string. Both loaded. Also test accidentally duplicated coast in configured candidate order.

Actual output:
```text
Lookup: M subtitle, actions, coast, R3.
Policy: coast then island; intentional empty string qualifies.
Trace:
Candidate | Loading state | Key/value state | Decision
coast/actions | loaded | subtitle empty | select intentional value
Selection: Fixture selects coast and empty string; Extra is not used.
Coverage: Intentional blank satisfies this supplied resolution policy; it is not a missing target entry.
Correction and replay: Preserve the blank. Correct duplicated candidate configuration before using the strict reference fixture; its duplicate-order guard raised ValueError.
Evidence limit: Python fixture checks passed for intentional blank and duplicate-order rejection. No assertion is made that a production library must reject duplicates the same way.
```

Checks: empty string is not truthiness-skipped; reference policy is not presented as universal platform behavior.

## LRE-003 ordinary

Request: Fictional app N source S/target T for coast, save key context-D. Target save has source_revision context-D and approved true. Project revision labels include meaning and context; readiness requires matching revision and explicit approval.

Actual output:
```text
Snapshot: N source S/target T coast; meaning-and-context revision labels.
Acceptance basis: Current source revision and explicit approval required.
Coverage ledger:
Current key | Target presence | Reviewed source | Current source | Readiness/action
save | present | context-D, approved | context-D | ready by supplied metadata
Rename and collision queue: None supplied.
Retired candidates: None in scoped comparison.
Executed check: Independent Python 3.14.6 comparison returned save=ready by supplied metadata and no retired candidates.
Limits: Metadata supports readiness under the supplied rule. Linguistic quality and runtime resource behavior remain untested.
```

Checks: affirmative result appropriately bounded rather than calling the translation independently validated.

## LRE-003 missing lineage

Request: Fictional N source S2 has save revision D and close E. Target T2 contains save with no review metadata; close absent. Same readiness policy applies.

Actual output:
```text
Snapshot: N S2/T2, coast, supplied meaning-and-context revisions.
Acceptance basis: Reviewed source must match and approval must be explicit.
Coverage ledger:
Current key | Target presence | Reviewed source | Current source | Readiness/action
save | present | unknown | D | lineage unknown; obtain review basis
close | absent | none | E | missing; obtain target translation and review
Rename and collision queue: None supplied; no mappings inferred.
Retired candidates: None in scoped comparison.
Executed check: Python result save=lineage unknown, close=missing; retired list empty.
Limits: Missing evidence does not prove save was reviewed against an older revision. No text, catalog or approval was changed.
```

Checks: unknown lineage distinct from stale or absent entry; no guessed approval history.

## LRE-003 edge: changed context and collision

Request: Fictional N source S3 keeps open but changes command-A to status-B. Current title.new uses title-C. Target T3 has open approved against command-A, title.new against title-C but unapproved, and title.old approved against title-C. Proposed title.old to title.new migration lacks authority; consumer inventory absent.

Actual output:
```text
Snapshot: N S3/T3, coast; source revision scheme includes changed context.
Acceptance basis: Current revision and explicit approval required.
Coverage ledger:
Current key | Target presence | Reviewed source | Current source | Readiness/action
open | present | command-A, approved | status-B | stale; review changed role
title.new | present | title-C, unapproved | title-C | review pending
Rename and collision queue: Proposed title.old -> title.new collides with existing target; preserve both histories for authorized disposition, do not transfer approval automatically.
Retired candidates: title.old outside current source scope; retain pending consumer and migration evidence.
Executed check: Python returned open=stale, title.new=review pending, retired candidates=[title.old].
Limits: Metadata comparison does not authorize overwriting the destination or deleting old consumers' resource. No runtime or language judgment performed.
```

Checks: context revision invalidates old approval; existing destination pending review not overwritten; historical approval does not automatically migrate.

## Result and claim review

No blocker found in nine fresh task applications and the executable cases. The saved script additionally checks malformed fixture syntax and duplicate candidate order. Mechanical output alone does not perform semantic role, policy-authority or consumer-retirement judgments; the text applications retain those boundaries. LRE-001's repaired worked example now provides its S/T/West/run-record identities in the fictional input. Stable Python behavior and authored fixture schemas are the only executable claims; no library version, API, production syntax, locale-parent rule or translation statistic is asserted.

These scopes are distinct from GLA's language briefs and names/numbers review, DST's token dependency and rename migration, and each other: LRE-001 checks message parameter roles/occurrences; LRE-002 traces runtime candidate resolution under a supplied policy; LRE-003 checks source-context review lineage independently of key presence. No external source text was copied. This review does not mark registry entries audited.
