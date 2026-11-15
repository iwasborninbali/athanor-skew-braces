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

## skew224 (Problem 2.24 of Vendramin's list)

- Priority: settled for every classical brace by I. Lau, *An associative left brace is a ring*, J. Algebra Appl. 19 (2020),
  no. 9, DOI 10.1142/S0219498820501790 (arXiv:1811.04894), Theorem 1.1; `status/REPORT.md` still lists row 2.24 as open, which
  is outdated (the attack report and `skew224/REPORT.md` record Lau's theorem).
- Replay: `skew224/enumerate.g` run by the guide on the lab VM (GAP 4.12.1, YangBaxter 0.10.7, cryst, polycyclic) for all
  classical braces of orders 1-31 in the YangBaxter database (`skew224/run-1-31.log`, exit 0): associative star and two-sided
  counts agree at every order and no associative-not-two-sided brace occurs, as Lau's theorem requires; the totals b(n) agree
  with Table 5.3 of the paper (for example b(8) = 27, b(16) = 357, b(24) = 96, b(27) = 37). A consistency check of the
  database and the program, not a new result.
