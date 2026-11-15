#!/usr/bin/env python3
"""Independent multiplication-table checker, reading enumerator JSON lines."""
import json
import sys
from math import gcd


def check(d):
    n = d["n"]
    groups = d["witnesses"]
    assert len(groups) == d["additive_aut_conjugacy_classes"]
    units = [u for u in range(n) if gcd(u, n) == 1]
    for witness in groups:
        C = witness["circle"]
        assert len(C) == n and all(sorted(row) == list(range(n)) for row in C)
        assert C[0] == list(range(n)) and [row[0] for row in C] == list(range(n))
        assert all(C[C[a][b]][c] == C[a][C[b][c]] for a in range(n)
                   for b in range(n) for c in range(n))
        assert all(C[a][(b+c) % n] == (C[a][b]-a+C[a][c]) % n
                   for a in range(n) for b in range(n) for c in range(n))
    for i, first in enumerate(groups):
        for second in groups[i+1:]:
            A, B = first["circle"], second["circle"]
            assert not any(all((u*A[a][b]) % n == B[(u*a)%n][(u*b)%n]
                               for a in range(n) for b in range(n)) for u in units)
    return n, len(groups)


if __name__ == "__main__":
    for line in sys.stdin:
        n, classes = check(json.loads(line))
        print(f"PASS n={n} count={classes} identity/associativity/brace/isomorphism")
