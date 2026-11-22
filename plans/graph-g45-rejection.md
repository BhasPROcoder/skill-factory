# GRF-045 candidate rejection

Proposed scope: retry-safe graph mutation ledger for idempotent node/edge upsert batches, operation IDs, payload binding, partial retry, parallel edges and missing endpoints.

Catalog search exposed GRF-016 `versioned-graph-patch-replay`. Its actual procedure and Python reference already bind event IDs to exact ordered payloads, replay identical envelopes with no new graph effect, reject conflicting event-ID reuse, apply node/edge operations to an isolated candidate, check endpoints, reject partial batches, and compare graph/version/receipts. It explicitly permits parallel edges and tests retries and late failure. The proposed scope would repackage the same primary method. GRF-003 handles initial import reconciliation, GRF-014 storage transactions and GRF-017 identity migration, but GRF-016 is the decisive overlap.

No GRF-045 skill or staging manifest was created, and no registry change was made. A future candidate would need a substantively different method and evidence before receiving this ID.
