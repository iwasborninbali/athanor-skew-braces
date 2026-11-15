#!/usr/bin/env python3
"""Independent table-only verifier for skew224 WITNESS_JSON lines.

Does not import GAP, YangBaxter, or any enumeration routines. It checks
classical brace axioms, associative star, and an explicit right-law failure.
Only reported table witnesses (n <= 64) are certified; an empty log proves
nothing about an exhaustive database search.

Usage: python3 skew224/check_witness.py skew224/run.log
       python3 skew224/check_witness.py - < skew224/run.log
"""
import json
import sys
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def group_inverse(t, name):
    n = len(t)
    universe = list(range(n))
    require(n > 0, f"{name}: empty table")
    require(all(isinstance(row, list) and len(row) == n for row in t),
            f"{name}: non-square table")
    require(all(all(type(x) is int and 0 <= x < n for x in row) for row in t),
            f"{name}: invalid entries")
    require(all(t[0][a] == a and t[a][0] == a for a in universe),
            f"{name}: identity is not index 0")
    require(all(sorted(row) == universe for row in t),
            f"{name}: row is not a permutation")
    require(all(sorted(t[a][b] for a in universe) == universe
                for b in universe), f"{name}: column is not a permutation")
    inv = []
    for a in universe:
        xs = [b for b in universe if t[a][b] == 0 and t[b][a] == 0]
        require(len(xs) == 1, f"{name}: inverse failure at {a}")
        inv.append(xs[0])
    for a in universe:
        for b in universe:
            for c in universe:
                require(t[t[a][b]][c] == t[a][t[b][c]],
                        f"{name}: not associative at {(a, b, c)}")
    return inv


def check(d):
    n = d["n"]
    k = d["k"]
    require(type(n) is int and 1 <= n <= 64, "invalid witness order")
    require(type(k) is int and k >= 1, "invalid database index")
    plus = d["additive_table"]
    circle = d["multiplicative_table"]
    require(len(plus) == n and len(circle) == n, "order mismatch")
    minus = group_inverse(plus, "addition")
    group_inverse(circle, "circle")
    idx = range(n)
    require(all(plus[a][b] == plus[b][a] for a in idx for b in idx),
            "not a classical brace: addition is non-abelian")

    lam = [[plus[minus[a]][circle[a][b]] for b in idx] for a in idx]
    star = [[plus[lam[a][b]][minus[b]] for b in idx] for a in idx]
    # Verify full compatibility, not merely the weaker generator tests
    # used by the GAP enumerator. The group checks above are separate.
    for a in idx:
        for b in idx:
            for c in idx:
                require(circle[a][plus[b][c]] ==
                        plus[plus[circle[a][b]][minus[a]]][circle[a][c]],
                        f"left brace identity failed at {(a, b, c)}")
                require(star[star[a][b]][c] == star[a][star[b][c]],
                        f"star not associative at {(a, b, c)}")

    failure = None
    for a in idx:
        if failure is not None:
            break
        for b in idx:
            if failure is not None:
                break
            for c in idx:
                lhs = circle[plus[a][b]][c]
                rhs = plus[plus[circle[a][c]][minus[c]]][circle[b][c]]
                if lhs != rhs:
                    failure = (a, b, c, lhs, rhs)
                    break
    require(failure is not None, "reported witness is actually two-sided")
    return f"PASS n={n} k={k} classical=YES left=YES associative_star=YES " \
           f"two_sided=NO right_failure={failure}"


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 skew224/check_witness.py LOGFILE (or -)")
    lines = (sys.stdin if sys.argv[1] == "-" else
             Path(sys.argv[1]).open(encoding="utf-8"))
    witnesses = 0
    with lines:
        for lineno, raw in enumerate(lines, start=1):
            if raw.startswith("WITNESS_JSON "):
                try:
                    payload = json.loads(raw[len("WITNESS_JSON "):])
                    print(check(payload))
                except (ValueError, KeyError, TypeError) as exc:
                    raise SystemExit(f"FAIL line={lineno}: {exc}") from exc
                witnesses += 1
    if witnesses == 0:
        print("NO_TABLE_WITNESSES (does not certify completed orders or absence)")
    else:
        print(f"VERIFIED {witnesses} independent full-table witness(es)")


if __name__ == "__main__":
    main()
