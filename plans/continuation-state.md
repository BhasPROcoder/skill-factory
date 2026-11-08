# Continuous expansion execution

User instruction: continue until all 5,000 net additions are finished and push reviewed small batches throughout. Original baseline: 544; target total: 5,544. The active goal is not complete when a batch ends.

Use observed sf.py status for counts. Maintain uniqueness by comparing the proposed artifact, procedure, and failure decisions against neighboring skills. Domain allocation targets are flexible; never count renamed variants or unrelated changes as additions.

Workflow for each checkpoint:

1. Coordinator assigns disjoint domain files and manifests to available workers.
2. Authors query sf.py for neighbors, inspect relevant procedures for substantive comparison, and reject duplicate task candidates before authoring.
3. Authors complete format, specific-claim review, fictional arithmetic and any required executable checks.
4. A different worker executes ordinary, missing-input and edge requests for each skill and saves actual outputs with limitations. Unavailable agents do not imply completed reviews; recover existing evidence and finish missing work explicitly.
5. Coordinator serially ingests only complete manifests, validates, checks registry and quality, resolves findings, and updates relevant indexes/router/topic map.
6. Package and commit each reviewed small domain batch or coordinated set. Push to origin/main, verify success and matching local/remote heads. Preserve unready work unstaged.
7. Immediately select the next useful gaps; continue the active goal. Never mark the 5,000 target complete based on a batch count, filenames, or structural validation alone.

Last observed checkpoint: sf.py reports 602 validated skills, 58 net additions against the original 544, and 4,942 remaining. Batch six added three each of ATR, LRE and IPR, with independent executable checks and a repaired IPR recovery-identity defect. Batch five added GAS-011 and six each of RNT, PRT and EXP after independent text reviews. The proposed fourth SVC and ARC skills were not created or counted.

Current working batch: GEO (three mesh geometry diagnostics), TBX (three table transformation contracts), SEQ (three dependency schedule computations). Candidate scopes require substantive comparison before authoring. Each must include runnable reference examples and executed checks as well as independent review. Assigned manifests are staging/b7_geo.json, staging/b7_tbx.json and staging/b7_seq.json. Drafts remain outside the accepted count until independent review and serial ingestion. Counts and completion must be read from actual outputs rather than inferred from this queue.

Use `python tools/sf.py expansion` for conservative net accounting against the immutable baseline commit. This checks identity, status and file presence; it does not prove semantic uniqueness or behavioral quality.

Candidate gap queue after this batch: shipping document-to-consignment reconciliation; returns condition/evidence disposition; museum exhibit label revision propagation; event seating sightline evidence review; customer-support attachment redaction handoff; maintenance work-order completion evidence; design asset licensing handoff; course assignment resubmission history; research instrument calibration-record organization. These are candidates, not approved scopes, planned registry entries, or created skills. Compare each against the current catalog before assigning IDs.
