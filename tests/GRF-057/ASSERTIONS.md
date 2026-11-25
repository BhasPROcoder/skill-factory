# GRF-057 assertions

1. The candidate contains e1 A→Org1, e2 B→Org2, e4 A→B and unchanged e5, all with original IDs and locators.
2. e3 is held exactly once and full cutover remains incomplete.
3. The duplicate-e3 candidate is rejected as fan-out or invalid partition.
4. The A→A e4 candidate is rejected by occurrence-ledger replay.
