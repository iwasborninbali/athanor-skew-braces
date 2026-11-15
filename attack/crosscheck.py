#!/usr/bin/env python3
"""Independent enumeration by all lambda assignments (small automorphism groups).
Avoids the holomorph subgroup-extension algorithm.  Uses group constructors and
Aut(G) enumeration from enumerate.py, but independent classification method.
"""
import itertools
from enumerate import groups_of_order,automorphisms

def count_lambdas(op):
    n=len(op); aut=automorphisms(op);k=len(aut);idx={a:i for i,a in enumerate(aut)}
    comp=[[idx[tuple(a[b[x]] for x in range(n))] for b in aut] for a in aut]
    ai=[next(j for j in range(k) if comp[i][j]==comp[j][i]==0) for i in range(k)]
    valid=set()
    for vals in itertools.product(range(k),repeat=n-1):
        lam=(0,)+vals
        if all(lam[op[a][aut[lam[a]][b]]]==comp[lam[a]][lam[b]] for a in range(n) for b in range(n)):
            transformed=[]
            for beta in range(k):
                new=[-1]*n
                for a in range(n):
                    new[aut[beta][a]]=comp[comp[beta][lam[a]]][ai[beta]]
                transformed.append(tuple(new))
            valid.add(min(transformed))
    return len(valid)

if __name__=='__main__':
    for n in range(1,7):
        for G in groups_of_order(n):
            print('BRUTE',G[0],n,count_lambdas(G[1]),flush=True)
    G=next(G for G in groups_of_order(8) if G[0]=='C8')
    print('BRUTE',G[0],8,count_lambdas(G[1]),flush=True)
