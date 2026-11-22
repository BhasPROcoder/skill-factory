# GRF-036 assertions

1. The three-color run returns a complete allowed map covering P,Q,R,I, with different colors on each triangle edge.
2. The two-color run reports infeasible only after a completed search or direct obstruction, not after one greedy attempt.
3. The state-limit-1 run reports unknown, not infeasible.
4. The output keeps I in the node inventory and states that colors have no automatic scheduling meaning.
