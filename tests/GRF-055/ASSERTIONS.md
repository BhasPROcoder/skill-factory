# GRF-055 assertions

1. Base A has one maximal conflict window `[5,8)` and B has none.
2. Base `[5,6)` evidence contains e1,e1b,e2, while `[6,8)` contains e1,e2; e1b alone never creates a conflict.
3. e2 and e3 touching at 10 do not overlap under `[start,end)`.
4. Adding e5 extends A's maximal conflict to `[5,9)` without merging B's records.
