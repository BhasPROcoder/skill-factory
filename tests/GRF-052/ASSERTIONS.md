# GRF-052 assertions

1. Both S1 and S2 return exactly A and B with the permitted path ab to B; C is absent.
2. Every returned path edge and endpoint is replayed against P1 grants.
3. The hidden-edge change leaves the complete visible result map equal in this fixture.
4. Invisible H seed and unknown edge grant are rejected, not reported as ordinary empty results.
5. The result does not claim production-wide noninterference or current policy without owner verification.
