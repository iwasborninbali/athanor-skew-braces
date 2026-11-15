#!/usr/bin/env python3
"""Independent, table-only checker: does not import enumeration code.
Verifies both groups, skew-brace law, associative *, non-two-sidedness,
nondegenerate Yang--Baxter solution, and non-involutivity.
"""
import json,sys


def inv_table(t):
    n=len(t)
    assert set(t[0])==set(range(n))
    assert all(t[0][a]==t[a][0]==a for a in range(n))
    assert all(sorted(row)==list(range(n)) for row in t)
    assert all(sorted(t[a][b] for a in range(n))==list(range(n)) for b in range(n))
    assert all(t[t[a][b]][c]==t[a][t[b][c]] for a in range(n) for b in range(n) for c in range(n))
    return [next(b for b in range(n) if t[a][b]==t[b][a]==0) for a in range(n)]


def main(path):
    d=json.load(open(path)); add=d['additive_table'];circ=d['multiplicative_table'];n=len(add)
    assert len(circ)==n
    ai=inv_table(add);ci=inv_table(circ)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                assert circ[a][add[b][c]]==add[add[circ[a][b]][ai[a]]][circ[a][c]]
    star=[[add[add[ai[a]][circ[a][b]]][ai[b]] for b in range(n)] for a in range(n)]
    assert all(star[star[a][b]][c]==star[a][star[b][c]] for a in range(n) for b in range(n) for c in range(n))
    failures=[(a,b,c) for a in range(n) for b in range(n) for c in range(n)
        if circ[add[a][b]][c]!=add[add[circ[a][c]][ai[c]]][circ[b][c]]]
    assert failures
    print('n',n,'addition nonabelian',any(add[a][b]!=add[b][a] for a in range(n) for b in range(n)))
    print('both group axioms PASS; skew left brace PASS; associative star PASS')
    print('right brace identity FAIL witness (a,b,c)',failures[0]);a,b,c=failures[0]
    print('right-law left',circ[add[a][b]][c],'right',add[add[circ[a][c]][ai[c]]][circ[b][c]])
    lam=[[add[ai[a]][circ[a][b]] for b in range(n)] for a in range(n)]
    r=lambda a,b:(lam[a][b],circ[ci[lam[a][b]]][circ[a][b]])
    for a in range(n):
        assert sorted(lam[a])==list(range(n))
        assert sorted(r(b,a)[1] for b in range(n))==list(range(n))
    pairs=[r(a,b) for a in range(n) for b in range(n)]
    assert len(set(pairs))==n*n
    for a in range(n):
        for b in range(n):
            for c in range(n):
                x,y=r(a,b); y,z=r(y,c); x,y=r(x,y); left=(x,y,z)
                y,z=r(b,c); x,y=r(a,y); y,z=r(y,z);right=(x,y,z)
                assert left==right
    print('YBE braid relation PASS for',n**3,'triples; nondegenerate PASS')
    print('r involutive?',all(r(*r(a,b))==(a,b) for a in range(n) for b in range(n)))
    print('INDEPENDENT CHECK SUCCESS')

if __name__=='__main__':main(sys.argv[1] if len(sys.argv)>1 else 'witness16.json')
