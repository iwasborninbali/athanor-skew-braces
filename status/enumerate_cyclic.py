#!/usr/bin/env python3
"""Exhaustive regular-subgroup count for Hol(C_n), n=2,3,4.
Only a smoke test, NOT a new enumeration of all braces of these orders.
"""
import itertools
import json
from math import gcd


def compute(n):
    units = [u for u in range(n) if gcd(u, n) == 1]
    hol = [(v, u) for v in range(n) for u in units]
    identity = (0, 1)
    def mul(a, b):
        return ((a[0] + a[1] * b[0]) % n, a[1] * b[1] % n)
    regular = []
    for extra in itertools.combinations((g for g in hol if g != identity), n - 1):
        subgroup = frozenset((identity,) + extra)
        if len({g[0] for g in subgroup}) != n:
            continue
        if all(mul(a, b) in subgroup for a in subgroup for b in subgroup):
            regular.append(subgroup)
    def key(subgroup):
        return tuple(sorted(subgroup))
    def conjugates(subgroup):
        return [key({((z * v) % n, u) for v, u in subgroup}) for z in units]
    reps = sorted({min(conjugates(H)) for H in regular})
    witnesses = []
    for rep in reps:
        action = {v: u for v, u in rep}
        circle = [[(a + action[a] * b) % n for b in range(n)] for a in range(n)]
        witnesses.append({"affine_subgroup": [list(x) for x in rep], "circle": circle})
    return {"n": n, "holomorph_order": len(hol), "regular_subgroups": len(regular),
            "additive_aut_conjugacy_classes": len(reps), "witnesses": witnesses}


if __name__ == "__main__":
    for order in (2, 3, 4):
        print(json.dumps(compute(order), sort_keys=True, separators=(",", ":")))
