# GRF-051 assertions

1. Q1 adds D at distance one; Q2 and Q3 content remains equal.
2. Every r1 key is marked stale for r2 despite equal content for two queries.
3. Each new answer is checked against the same query direction, filter and bound.
4. No live cache refresh or graph mutation is claimed.
