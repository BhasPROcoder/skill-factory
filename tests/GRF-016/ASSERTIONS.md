# GRF-016 assertions

1. Rejects the batch because e still references Y.
2. Leaves Z absent and preserves e, Y and version 4.
3. Does not create a success receipt for the rejected batch.
4. Requires an explicitly corrected envelope and version check rather than silently cascading e.
