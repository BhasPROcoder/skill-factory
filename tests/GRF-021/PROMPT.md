Follow the skill below exactly to handle the user request at the end.

<skill>
---
id: GRF-021
name: graph-evidence-path-retrieval
domain: Graph Engineering Foundations
subdomain: Graph-assisted evidence retrieval
version: 1.0
description: Build a bounded evidence packet from graph paths and source passages when a question requires connected facts with reproducible provenance and visible retrieval gaps.
triggers: ["retrieve graph evidence for a question", "build graph assisted context", "select evidence bearing paths", "compare graph and passage retrieval", "explain graph retrieval omissions"]
not_for: ["computing bounded reachability [GRF-006]", "generic context handoff [CTG-005]", "defining inference rules [GRF-018]", "extracting relation candidates [GRF-019]", "benchmarking answer quality across a dataset"]
requires: []
risk_level: medium
---

# Graph Evidence Path Retrieval

## Purpose
Construct a question-specific evidence packet containing selected graph paths and the source passages supporting each relationship. Expose unresolved seeds, missing evidence and budget omissions so the answerer knows which parts of the question remain unsupported. Connectivity helps locate material but does not itself establish an answer or a new entailed relation.

## Inputs to collect
1. **Question and required facts** — obtain the question and decompose its factual needs. Why: graph proximity alone does not define relevance. Default: ask for the question; do not retrieve an arbitrary neighborhood.
2. **Graph snapshot and vocabulary** — obtain versioned nodes, edges, endpoint types and relation meanings. Why: direction and identity determine which paths are interpretable. Default: supplied snapshot only, completeness unknown.
3. **Source passage inventory** — obtain revision-specific passages and edge-to-passage links. Why: the packet must let a reader inspect the basis of each relationship. Default: unavailable sources are explicit gaps, never substituted with invented quotations.
4. **Seed resolution evidence** — obtain entity IDs, aliases and contextual disambiguation. Why: retrieval from the wrong entity produces plausible irrelevant evidence. Default: unresolved names stay ambiguous; do not select the first match.
5. **Retrieval and output bounds** — obtain allowed path patterns, hop bounds, source access rules and packet budget. Why: these define the searched space and omitted material. Default: propose bounds for review without claiming an executed retrieval.
6. **Baseline and reviewer** — identify a passage-only search over the same authorized source inventory and who reviews relevance. Why: compare what each route actually contributed. Default: baseline pending and no performance improvement claim.

If a required input is missing and has no safe default, ask in one message, max 3 questions.

## Procedure
1. Write the factual needs separately, including any requested relationship, time scope and qualification.
2. Resolve each named seed to graph identities with supporting evidence; retain competing resolutions as separate provisional branches.
3. Define permitted path patterns, relation directions and snapshot restrictions from the question and vocabulary.
4. Enumerate candidate paths using an appropriate bounded retrieval method, recording whether enumeration exhausted its declared scope or stopped early.
5. Validate every candidate's edge continuity, direction and source links before considering it for the evidence packet.
6. ⚠️ Inspect supporting passages for the qualified relationship; reject unsupported path interpretations instead of assuming that a valid edge ID guarantees textual support.
7. Assign each candidate to the factual needs it may support, recording the interpretation and relevance rationale for human review.
8. Select candidates under the declared packet budget with deterministic ordering and a visible omission ledger.
9. Retrieve passage-only candidates from the same source inventory using the same question, keeping the baseline's method and budget visible.
10. Compare graph and baseline packets by supported needs, missing qualifications, unique passages and unresolved conflicts; do not infer general superiority from one question.
11. Deliver the packet with source quotations, path witnesses, remaining questions and the exact stopping conditions.

The Python 3 reference below selects from an already enumerated, manually relevance-ordered candidate list. It checks outgoing continuity and source availability, then applies a whole-path budget measured in characters of newly added passages. This is neither a tokenizer nor a search algorithm. It does not verify passage meaning, candidate completeness or relevance. All dictionaries and candidate tuple shapes must be prevalidated; each passage is nonempty frozen text. Record the interpreter version when executing.

```python
def select_packet(seed, edges, passages, candidates, budget):
    if type(budget) is not int or budget < 0:
        raise ValueError("nonnegative integer budget required")
    selected, omitted, included = [], [], set()
    spent, seen = 0, set()
    for cid, path in candidates:
        if cid in seen or not path:
            raise ValueError("duplicate candidate or empty path")
        seen.add(cid)
        node, refs, reason = seed, [], None
        for eid in path:
            if eid not in edges:
                reason = "unknown edge"
                break
            source, target, passage = edges[eid]
            if source != node:
                reason = "disconnected or reversed path"
                break
            if passage not in passages:
                reason = "missing passage"
                break
            refs.append(passage)
            node = target
        if reason:
            omitted.append((cid, reason))
            continue
        new = set(refs) - included
        cost = sum(len(passages[r]) for r in new)
        if spent + cost > budget:
            omitted.append((cid, "packet budget"))
            continue
        included.update(new)
        spent += cost
        selected.append((cid, tuple(path), tuple(refs)))
    return selected, omitted, sorted(included), spent

passages = {"D:v1:p1": "A links B.", "D:v1:p2": "B links C."}
edges = {"e1": ("A", "B", "D:v1:p1"),
         "e2": ("B", "C", "D:v1:p2")}
candidates = [("c1", ["e1"]), ("c2", ["e1", "e2"])]
selected, omitted, refs, spent = select_packet(
    "A", edges, passages, candidates, 10)
assert [c[0] for c in selected] == ["c1"]
assert omitted == [("c2", "packet budget")]
assert refs == ["D:v1:p1"] and spent == 10
print("traceable selection and explicit packet omission checked")
```

Attach the referenced passage text to the packet, not just its identifier. The budget excludes path metadata and formatting; measure the complete serialized packet separately when the destination has a strict size limit. Ordering changes selection: this simple greedy policy does not optimize relevance or coverage. Skipping an oversized candidate allows later affordable candidates to be considered, and every skipped path remains visible.

## Decision rules
- IF seed resolution is ambiguous THEN retain separate provisional results or request disambiguation BECAUSE merging neighborhoods hides identity uncertainty.
- IF any path edge lacks inspectable evidence THEN omit that path from the supported packet and log the gap BECAUSE a partially evidenced chain cannot support the whole interpretation.
- IF a path connects entities through different predicates THEN describe those steps without inventing a direct relation BECAUSE reachability is not entailment.
- IF a budget prevents inclusion THEN report the omitted candidate and budget type BECAUSE an output limit is not evidence that no answer exists.
- IF passage-only retrieval supplies a missing qualification THEN retain it in the comparison BECAUSE graph representations can omit source context.
- IF a factual need remains uncovered THEN give an explicit unanswered item BECAUSE plausible completion would exceed the evidence.

## Output template
```text
Question needs: <numbered factual needs; maximum 6>
Resolution: <mention | seed ID or alternatives | evidence>
Contract: <snapshot, patterns, direction, enumeration bound, packet budget>
Packet: <candidate | need | edge path | passage revisions and quotations | interpretation limit>
Omissions: <candidate or need | reason | next evidence required>
Baseline: <method/budget/status | supported needs | differing evidence>
Checks: <executed checks and pending semantic checks; maximum 80 words>
Answer boundary: <supported and unanswered needs; maximum 80 words>
```
Include all selected candidates in the packet or attach the complete ledger with a concise preview. Do not hide omissions behind a statement that results were “relevant.”

## Quality checklist
- [ ] Question needs drive every relevance assignment.
- [ ] Seed identity and graph revision are visible.
- [ ] Each selected path preserves edge direction and continuity.
- [ ] Every selected edge has an inspectable source passage.
- [ ] Path interpretation does not invent an inferred direct relation.
- [ ] Enumeration stopping and packet omissions are distinguished.
- [ ] Baseline status and evidence differences are explicit.
- [ ] Unanswered needs remain unanswered in the handoff.

## Anti-patterns
- **Neighborhood dumping**: retrieve connected nodes without question mapping. Fix: associate each candidate with a factual need.
- **Graph authority**: treat stored edges as verified observations. Fix: inspect their source evidence and qualification.
- **Hidden truncation**: omit expensive paths without explanation. Fix: retain the omitted candidate and limiting budget.
- **Unfair baseline**: compare against a smaller source inventory. Fix: align authorized sources and disclose resource differences.
- **Path shortcut**: summarize A-to-B-to-C as a direct A-to-C fact. Fix: preserve the individual predicates and inference limits.

## Worked example
**Input:** Fictional question asks which supplied links connect A toward C. The snippet inputs are frozen at graph S1; A is resolved, outgoing link paths have at most two edges, and candidate enumeration produced c1/c2. Packet passage budget is ten characters. No passage-only retrieval has run.

**Output:**
```text
Question needs: 1. Identify supplied links on an A-to-C route.
Resolution: A | A | supplied resolved inventory.
Contract: S1; outgoing link paths; at most two edges; enumerated c1/c2 only; ten passage characters.
Packet: c1 | partial need 1 | e1 | D:v1:p1 “A links B.” | supports only the supplied A-to-B link.
Omissions: c2 | packet budget | add D:v1:p2 under a revised budget to inspect the complete route.
Baseline: Passage-only method/budget unspecified; pending; supported needs and differing evidence not measured.
Checks: Reference fixture checks continuity and passage availability when executed; semantic source review and complete packet size remain pending.
Answer boundary: Packet supports A-to-B only; it cannot answer the complete A-to-C route or establish a direct A-to-C relation.
```

**Bad output:** “A is related directly to C, and graph retrieval is more accurate.”
This invents a direct relation, hides omitted evidence and claims an unmeasured advantage.

## Edge cases
- **Empty results**: report seed resolution, filters and inspected scope; do not claim global absence.
- **Shared passage references**: include text once while preserving every path's reference to it.
- **Contradictory sources**: keep competing qualified evidence visible; retrieval does not adjudicate truth.
- **Unavailable baseline**: mark comparison pending and deliver the graph packet with its limits.
- **Enumeration interruption**: distinguish unexamined candidates from examined but budget-omitted paths.

## Test case
**Input:**
> Fictional A has two candidate paths. One contains an edge without a source passage; the other has a complete passage chain exceeding the packet budget. Passage-only search has not run.

**Assertions:**
1. Reports separate missing-evidence and packet-budget omissions.
2. Does not invent a supported answer from either omitted chain.
3. Marks passage-only comparison pending.
4. Names the evidence or budget change needed to revisit each omission.
</skill>

<user_request>
Fictional A has two candidate paths. One contains an edge without a source passage; the other has a complete passage chain exceeding the packet budget. Passage-only search has not run.
</user_request>
