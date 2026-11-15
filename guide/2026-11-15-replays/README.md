# Guide's replays of round 1 (Claude, 2026-11-15)

- `verify/verify.py --holomorph-max 30 --direct-max 10 --orders 1-15,17-23,25-26,28-30 --seconds 1200`: replayed on macOS
  (Python 3.14, 31 s); every `ORDER` and `QUAT` line identical to `verify/run.log`.
- `attack/enumerate.py` (orders 1-12 and 13, 14, 15, 20, 21, 22), `attack/crosscheck.py`, `attack/check_witness.py`:
  replayed; every `DONE` line (counts of skew, classical, quaternion, two-sided and associative-not-two-sided braces) identical
  to the committed logs; the replay prints extra verbose `level 1 classes` lines, timings differ; crosscheck and the
  order-16 witness check identical.
- Cross-check against a third source: GAP 4.12.1 with the YangBaxter package 0.10.7 on the lab VM gives
  `NrSmallSkewbraces(8) = 47` and `NrSmallBraces(8) = 27`, matching both programs and Table 5.1/5.3 of the paper.

These are replications of published tables and of a known order-16 counterexample (skew, not classical), not new results.
