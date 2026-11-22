# GRF-037 independent review

Reviewer g33_reviewer. Read SPEC, full candidate and author evidence, plus actual procedures of GRF-007, GRF-013 and GRF-029. G07 partitions connectivity, G13 compares supplied community assignments, and G29 reports pair connectivity consequences of one removal. G37 instead repeats degree-threshold peeling and provides a round-complete certificate for the maximal induced survivor set. This is a scoped uniqueness check, not a whole-library guarantee. Registry untouched.

## Execution evidence

Executed embedded Python in the repaired draft under Python 3.14.6; it printed `k-core, cascaded peeling and ledger checks passed`. Extra runs of extracted `peel` and `verify` returned:

```text
empty: ([], [])
parallel A/B pair, k=2: ([], [[('A', 1), ('B', 1)]])
single loop at A, k=1: ([], [[('A', 0)]])
edgeless A/I, k=0: (['A', 'I'], [])
triangle A/B/C plus C/D/E tail and isolate I, k=2: (['A','B','C'], [[('E',1),('I',0)],[('D',1)]])
tampered recorded degree: REJECT
omitted low-degree vertex in a round: REJECT
invented removal of a degree-2 triangle vertex: REJECT
negative k: REJECT nonnegative integer k required
duplicate edge ID: REJECT duplicate edge or unknown endpoint
unknown endpoint: REJECT duplicate edge or unknown endpoint
three-character string record: REJECT invalid edge record
mapping record: REJECT invalid edge record
short tuple record: REJECT invalid edge record
```

Initial review found that a three-character string was accepted as an edge triple. The author repaired `adjacency` to require tuple/list shape; I inspected the saved condition and reran the embedded code and all fixtures above. The policy is consistent: parallel records add one distinct neighbor; self-loops add none; IDs remain in the source inventory. For maximality, every ledger round equals the complete current set of vertices with degree below k. Induction shows no valid k-core can contain any removed vertex; the final induced set meets the threshold. The verifier separately reconstructs adjacency, replays complete rounds and checks the final degrees. It therefore rejects both missing and invented removals under the declared policy.

## Ordinary scenario

```text
Scope: Fictional Willow W1; supplied undirected A/B/C/D/E/I inventory complete for this exercise.
Threshold and degree policy: k=2; distinct retained neighbors; parallel A/B records count one neighbor; E loop counts none.
Survivors: A, B, C.
Peeling rounds: Round 1 | E | 1; I | 0. Round 2 | D | 1.
Source exceptions: None; both A/B edge IDs and the E loop remain in the source ledger.
Verification: Executed construction and independent round replay; final A/B/C induced degrees are 2 each.
Limits: Exercise topology only; no community, importance or wider graph claim.
Next action: Graph owner checks omitted links before using the result in another analysis.
```

## Missing-input scenario

```text
Scope: Node inventory, direction policy and k are unavailable.
Threshold and degree policy: Pending owner choice; no default threshold or direction conversion.
Survivors: Pending.
Peeling rounds: Pending.
Source exceptions: Inventory and interpretation missing.
Verification: No peeling or ledger replay executed.
Limits: No complete core claim can be made from these inputs.
Next action: Owner supplies scoped nodes and edge records, approved undirected projection and nonnegative k.
```

## Edge/Test scenario

```text
Scope: Fictional A/B with two parallel edge IDs p,q and a loop at A; complete undirected exercise inventory.
Threshold and degree policy: k=2; distinct neighbors; p,q give one A/B neighbor and loop gives none.
Survivors: None.
Peeling rounds: Round 1 | A | 1; B | 1.
Source exceptions: None; p,q and loop remain separate source records.
Verification: Executed parallel-pair and loop fixtures and round replay; both nodes are below 2 at the first round.
Limits: Structural induced-subgraph result only; no social or operational ranking.
Next action: Preserve the source records and use an explicit alternate degree policy if needed.
```

## Verdict

Recommend acceptance after the shape repair. Worked example arithmetic and Test case assertions agree with executed results. The maximality claim is supported by complete-round replay and final degrees under the explicitly stated distinct-neighbor policy. No invented sources, unstable current values or unsupported semantic importance claims found. Scale and source completeness are stated limits.
