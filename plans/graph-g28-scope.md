# G28 graph projection and aggregation scope

Discovery decision: pursue a bounded analysis-projection contract. This is a candidate, not a registered or accepted skill. No external sources or code copied; no external format or algorithm conformance claim.

## Actual neighbor comparison

Read selected actual Procedure sections and code in GRF-001 graph-model-contract-design, GRF-003 graph-edge-list-import-reconciliation, GRF-017 reversible-graph-identity-migration, GRF-012 restart-walk-rank-sensitivity and GRF-013 graph-community-partition-sensitivity. Catalog metadata queried using sf.py.

GRF-001 chooses representation against questions and defines repetition semantics. It does not materialize an analysis projection with an aggregate contribution ledger. G28 consumes that representation and a specific analytical requirement.

GRF-003 preserves separate edge identities and reconciles accepted/quarantined input rows; its undirected canonicalization retains edge IDs. G28 deliberately combines selected occurrences into analysis edges and records every contribution, making information loss explicit. Import correctness alone cannot decide whether summing relationship weights is meaningful.

GRF-017 requires bijective node mapping and inverse reconstruction, stopping many-to-one merges. G28 must retain source identity outside the derived projection and must not claim that aggregated analysis edges can reconstruct all original records. It creates a derived artifact without changing source entity identity.

GRF-012 validates supplied weights and normalizes outgoing mass, then compares ranks. G28 determines which relation kinds and original weights produce those inputs, exposes additive versus nonadditive quantities, and retains excluded relationship evidence. It must not duplicate rank computation or claim a sum preserves ranking across different projection choices.

GRF-013 records projection changes as possible confounders and compares partition memberships; it neither constructs nor validates the projected edge contributions. G28 produces the exact projection manifest that such a run should cite.

## Distinct deliverable

A versioned derived graph plus source-contribution and exclusion ledgers. Contract fields: source snapshot, node cohort and isolated-node policy, included relation kinds, direction conversion, self-loop policy, weight meaning/unit, aggregation rule, missing/invalid weight behavior, output edge identity and consumer algorithm requirements. Every included source edge has exactly one declared contribution target for the bounded one-to-one-edge-contribution reference; every omitted edge has a reason. A more complex projection creating several output contributions needs a separate tested allocation rule rather than silent duplication.

Materialization procedure: validate source inventory and edge IDs; freeze selected cohort; classify edges by relation/endpoints/weight policy; derive directed or undirected grouping keys; aggregate only compatible quantities; preserve each contributing edge ID/value; emit excluded rows with reasons; retain explicit isolated nodes; reconcile ledger coverage; verify each aggregate from its individual contributions; deliver known semantic losses and downstream requirements. Distinguish newly isolated nodes caused by filtering from originally isolated nodes.

Default unresolved decisions must block dependent aggregation. Do not silently turn missing weights into one, mix counts with currency or distances, equate inverse relation records with independent events, or turn signed scores into nonnegative strengths. No universal aggregation rule should be claimed; sum, mean, maximum, binary presence and count encode different questions. The first executable reference can implement explicitly approved sum over nonnegative integer occurrence counts, with other choices recorded as unsupported rather than guessed.

## Proposed acceptance fixtures

1. Fictional inventory A/B/I, two included A-to-B occurrence edges weighted 2 and 3, one B-to-A edge weighted 7. Directed sum gives A-to-B 5 and B-to-A 7; undirected sum gives A-B 12 only when the owner explicitly permits direction loss. Contribution IDs remain recoverable in the ledger, and I remains present.
2. Add a relation outside the allowed set: its weight must not enter either aggregate; output exclusion names its source ID and reason.
3. Add missing weight, negative weight or unknown endpoint: reject or quarantine under an explicit contract; never silently omit the error from source accounting. No output acceptance when its required semantic decision is missing.
4. Distinct parallel occurrence IDs remain separate contributions. Duplicate source IDs block ambiguous accounting; opposite records representing one event must be adjudicated upstream or explicitly excluded to avoid double counting.
5. Filter every incident edge of B: retain B when the cohort policy says so and classify it as projection-isolated. Empty selected edge set still has its declared node inventory.
6. Tamper with one aggregate while preserving total edge count: contribution recomputation must expose the mismatch. Retained provenance does not make the lossy projected graph itself reversible.

Before authoring, inspect any newly accepted projection-related skills and finalize the consumer contract. Independent review must assess both semantic aggregation choices and executable reconciliation; mechanical code equality cannot prove that the chosen measure is meaningful.
