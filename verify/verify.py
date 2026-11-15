#!/usr/bin/env python3
"""Independent small-order skew-brace verifier; Python stdlib only.

Method H: classify regular subgroups of G semidirect Aut(G) by conjugation.
Method D: enumerate all identity-preserving bijections K -> G, transport K's
multiplication, and test the brace identity directly (not using H).

No GAP, precomputed brace databases, or network access are used.
"""
import argparse
import itertools
import json
import math
import platform
import time
from collections import defaultdict

SKEW = [0,1,1,1,4,1,6,1,47,4,6,1,38,1,6,1,1605,1,49,1,43,8,6,1,855,4,6,101,29,1,36]
LEFT = [0,1,1,1,4,1,2,1,27,4,2,1,10,1,2,1,357,1,8,1,11,2,2,1,96]
TWO = [0,1,1,1,4,1,1,1,22,4,1,1,4,1,1,1,221,1,4,1,4,1,1,1,22]

class Group:
    def __init__(self, name, elements, product):
        self.name = name
        self.n = len(elements)
        assert len(set(elements)) == self.n
        self.table = tuple(tuple(elements.index(product(x,y)) for y in elements) for x in elements)
        self.e = next(i for i in range(self.n) if all(self.table[i][j] == j and self.table[j][i] == j for j in range(self.n)))
        self.inv = tuple(next(j for j in range(self.n) if self.table[i][j] == self.e and self.table[j][i] == self.e) for i in range(self.n))
        assert all(self.table[self.table[a][b]][c] == self.table[a][self.table[b][c]] for a,b,c in itertools.product(range(self.n),repeat=3))
        # Relabel identity as 0 (all group models should already do so).
        assert self.e == 0
        self.abelian = all(self.table[a][b] == self.table[b][a] for a in range(self.n) for b in range(self.n))
        self.generators = self._generators()
        self.aut = self._automorphisms()
        self.ai = {p:i for i,p in enumerate(self.aut)}
        self.amul = tuple(tuple(self.ai[tuple(p[q[x]] for x in range(self.n))] for q in self.aut) for p in self.aut)
        self.ainv = tuple(next(j for j in range(len(self.aut)) if self.amul[i][j] == 0 and self.amul[j][i] == 0) for i in range(len(self.aut)))
        assert self.aut[0] == tuple(range(self.n))
    def _closure(self, gen):
        s = {0}
        todo = [0]
        while todo:
            a = todo.pop()
            for b in gen:
                c = self.table[a][b]
                if c not in s:
                    s.add(c); todo.append(c)
        return s
    def _generators(self):
        gens = []
        while len(self._closure(gens)) < self.n:
            c = max((x for x in range(1,self.n) if x not in self._closure(gens)),
                    key=lambda x:len(self._closure(gens+[x])))
            gens.append(c)
        return tuple(gens)
    def _automorphisms(self):
        n = self.n; t = self.table
        def order(x):
            y = 0
            for k in range(1,n+1):
                y = t[y][x]
                if y == 0: return k
            raise AssertionError
        images = [[x for x in range(n) if order(x)==order(g)] for g in self.generators]
        aut=[]
        for choices in itertools.product(*images):
            m={0:0}; queue=[0]; valid=True
            for a in queue:
                for g,y in zip(self.generators,choices):
                    b=t[a][g]; z=t[m[a]][y]
                    if b in m:
                        if m[b]!=z: valid=False; break
                    else:
                        m[b]=z; queue.append(b)
                if not valid: break
            if valid and len(m)==n and len(set(m.values()))==n:
                aut.append(tuple(m[i] for i in range(n)))
        return tuple(sorted(set(aut)))

def cyclic_product(*mods):
    els = list(itertools.product(*(range(m) for m in mods)))
    # product(...) enumerates (0,...,0) first.
    return Group('x'.join('C%d'%m for m in mods),els,lambda a,b:tuple((a[i]+b[i])%mods[i] for i in range(len(mods))))

def dihedral(m):
    els = [(i,j) for j in range(2) for i in range(m)]
    return Group('D%d'%(2*m),els,lambda a,b:((a[0]+(-1)**a[1]*b[0])%m,(a[1]+b[1])%2))

def dicyclic(m):
    els = [(i,j) for j in range(2) for i in range(2*m)]
    return Group('Dic%d'%(4*m),els,lambda a,b:((a[0]+(-1)**a[1]*b[0]+m*a[1]*b[1])%(2*m),(a[1]+b[1])%2))

def a4():
    def parity(p):return sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2
    els = [p for p in itertools.permutations(range(4)) if not parity(p)]
    return Group('A4',els,lambda p,q:tuple(p[q[i]] for i in range(4)))

def direct_product(U,V,name):
    els=list(itertools.product(range(U.n),range(V.n)))
    return Group(name,els,lambda x,y:(U.table[x[0]][y[0]],V.table[x[1]][y[1]]))

def semidirect_cyclic(r,s,k,name):
    assert pow(k,s,r)==1
    els=list(itertools.product(range(r),range(s)))
    return Group(name,els,lambda x,y:((x[0]+pow(k,x[1],r)*y[0])%r,(x[1]+y[1])%s))

def generalized_dihedral_9():
    els=list(itertools.product(range(3),range(3),range(2)))
    return Group('Dih(C3xC3)',els,lambda x,y:((x[0]+(-1)**x[2]*y[0])%3,(x[1]+(-1)**x[2]*y[1])%3,(x[2]+y[2])%2))

def groups(maxn=15):
    gs = [cyclic_product(n) for n in range(1,maxn+1)]
    extras = [cyclic_product(2,2), dihedral(3), cyclic_product(4,2),cyclic_product(2,2,2),dihedral(4),dicyclic(2),cyclic_product(3,3), dihedral(5),cyclic_product(6,2),dihedral(6),dicyclic(3),a4(),dihedral(7)]
    if maxn>=18:
        extras += [cyclic_product(3,3,2), dihedral(9),
                   direct_product(dihedral(3),cyclic_product(3),'D6xC3'), generalized_dihedral_9()]
    if maxn>=20:
        extras += [cyclic_product(10,2), dihedral(10),dicyclic(5),semidirect_cyclic(5,4,2,'F20')]
    if maxn>=21: extras += [semidirect_cyclic(7,3,2,'F21')]
    if maxn>=22: extras += [dihedral(11)]
    if maxn>=25: extras += [cyclic_product(5,5)]
    if maxn>=26: extras += [dihedral(13)]
    if maxn>=28: extras += [cyclic_product(14,2),dihedral(14),dicyclic(7)]
    if maxn>=30:
        extras += [dihedral(15),direct_product(dihedral(3),cyclic_product(5),'D6xC5'),
                   direct_product(dihedral(5),cyclic_product(3),'D10xC3')]
    gs += [g for g in extras if g.n<=maxn]
    return sorted(gs,key=lambda g:(g.n,g.name))

def holomorph_braces(G, deadline=None):
    """Orbit BFS on subgroups with injective translation projection; exhaustive."""
    n=G.n; m=len(G.aut); t=G.table; aut=G.aut
    Hmul=lambda x,y:(t[x//m][aut[x%m][y//m]]*m + G.amul[x%m][y%m])
    hid=0; candidates=range(1,n*m)
    # h=(a,alpha), conjugation by (0,beta).
    conj=tuple(tuple(aut[b][h//m]*m + G.amul[G.amul[b][h%m]][G.ainv[b]] for h in range(n*m)) for b in range(m))
    def canon(S):return min(tuple(sorted(p[h] for h in S)) for p in conj)
    def extend(S,gen,h):
        if h//m in {x//m for x in S}: return None
        out=set(S); out.add(h); todo=list(S)+[h]; gens=gen+(h,)
        tr={x//m for x in S}; tr.add(h//m)
        while todo:
            x=todo.pop()
            for y in gens:
                z=Hmul(x,y)
                if z not in out:
                    if z//m in tr: return None
                    tr.add(z//m);out.add(z);todo.append(z)
                    if len(out)>n:return None
        if n%len(out):return None
        return frozenset(out)
    levels={1:{(0,):(frozenset([0]),tuple())}}
    visited=1; attempted=0
    for size in range(1,n):
        if size not in levels: continue
        layer=levels[size]
        for S,gens in layer.values():
            for h in candidates:
                if h//m in {x//m for x in S}:continue
                attempted+=1
                T=extend(S,gens,h)
                if T is not None:
                    key=canon(T)
                    levels.setdefault(len(T),{}).setdefault(key,(T,gens+(h,)))
            if deadline and time.monotonic()>deadline:raise TimeoutError('holomorph deadline at %s level %d'%(G.name,size))
        visited += sum(len(v) for s,v in levels.items() if s>size and s<n)  # diagnostic only
    complete=levels.get(n,{})
    out=set()
    for S,_ in complete.values():
        lam=[None]*n
        for h in S: lam[h//m]=h%m
        assert all(x is not None for x in lam)
        out.add(tuple(lam))
    assert len(out)==len(complete)
    return out,dict(aut=m,subgroups=len(complete),partials=sum(len(v) for s,v in levels.items() if s<n),attempted=attempted)

def canonical_lam(G,lam):
    n=G.n; aut=G.aut; amul=G.amul; inv=G.ainv
    return min(tuple(amul[amul[b][lam[aut[inv[b]][a]]]][inv[b]] for a in range(n)) for b in range(len(aut)))

def direct_braces(G, Klist, deadline=None):
    """Enumerate all transports of each n-element group's multiplication.
    Identity-preserving bijection p: K -> G yields circle on G. Check that
    lambda_a is an additive automorphism, using direct Cayley-table tests.
    Does not enumerate or construct holomorph subgroups.
    """
    n=G.n; t=G.table; inv=G.inv
    autmap={p:i for i,p in enumerate(G.aut)}
    orbit=set(); tried=0; passed=0
    for K in Klist:
        kt=K.table
        for tail in itertools.permutations(range(1,n)):
            p=(0,)+tail
            pi=[0]*n
            for i,x in enumerate(p):pi[x]=i
            lam=[]; valid=True
            for a in range(n):
                pa=a; ir=inv[pa]; row=kt[pi[a]]
                f=tuple(t[ir][p[row[pi[b]]]] for b in range(n))
                k=autmap.get(f)
                if k is None: valid=False;break
                lam.append(k)
            tried+=1
            if valid:
                passed+=1; orbit.add(canonical_lam(G,tuple(lam)))
            if deadline and tried%20000==0 and time.monotonic()>deadline:raise TimeoutError('direct deadline at '+G.name)
    return orbit,dict(transport_maps=tried,passing_maps=passed,classes=len(orbit))

def circle_is_isomorphic(G,lam,K):
    """Separate finite-group isomorphism test via generator images and Cayley graph."""
    n=G.n
    if n!=K.n:return False
    ct=tuple(tuple(G.table[a][G.aut[lam[a]][b]] for b in range(n)) for a in range(n))
    def order(table,x):
        z=0
        for k in range(1,n+1):
            z=table[z][x]
            if z==0:return k
        raise AssertionError
    cand=[[x for x in range(n) if order(ct,x)==order(K.table,g)] for g in K.generators]
    for image in itertools.product(*cand):
        f={0:0};q=[0];ok=True
        for a in q:
            for gen,img in zip(K.generators,image):
                b=K.table[a][gen];c=ct[f[a]][img]
                if b in f:
                    if f[b]!=c:ok=False;break
                else:f[b]=c;q.append(b)
            if not ok:break
        if ok and len(f)==n and len(set(f.values()))==n:return True
    return False

def brace_properties(G,lam,check_ybe=True):
    n=G.n; t=G.table; inv=G.inv; aut=G.aut
    circ=tuple(tuple(t[a][aut[lam[a]][b]] for b in range(n)) for a in range(n))
    assert all(circ[circ[a][b]][c] == circ[a][circ[b][c]] for a,b,c in itertools.product(range(n),repeat=3))
    assert all(circ[a][0]==a and circ[0][a]==a for a in range(n))
    assert all(circ[a][t[b][c]] == t[t[circ[a][b]][inv[a]]][circ[a][c]] for a,b,c in itertools.product(range(n),repeat=3))
    two=G.abelian and all(t[circ[t[a][b]][c]][c]==t[circ[a][c]][circ[b][c]] for a,b,c in itertools.product(range(n),repeat=3))
    if check_ybe:
        # Formula (3.1): u=lambda_a(b), v=lambda_u^{-1}((a o b)^-1 a (a o b)).
        lam_inv=tuple(tuple(G.aut[G.ainv[lam[a]]][x] for x in range(n)) for a in range(n))
        r={}
        for a,b in itertools.product(range(n),repeat=2):
            u=aut[lam[a]][b]; ab=circ[a][b]
            x=t[t[inv[ab]][a]][ab]
            r[a,b]=(u,lam_inv[u][x])
        assert len(set(r.values()))==n*n
        assert all(len({r[a,b][0] for b in range(n)})==n for a in range(n))
        assert all(len({r[a,b][1] for a in range(n)})==n for b in range(n))
        def rr12(x):
            u,v=r[x[0],x[1]];return u,v,x[2]
        def rr23(x):
            u,v=r[x[1],x[2]];return x[0],u,v
        assert all(rr12(rr23(rr12(x)))==rr23(rr12(rr23(x))) for x in itertools.product(range(n),repeat=3))
        invr=all(r[r[a,b]]==(a,b) for a,b in itertools.product(range(n),repeat=2))
        assert invr==G.abelian
        # Verifies r's two outputs multiply in (A,circle) to a circle b.
        assert all(circ[u][v]==circ[a][b] for (a,b),(u,v) in r.items())
    return two

def run(max_h, max_d, seconds, orders=None):
    start=time.monotonic(); deadline=start+seconds if seconds else None
    print('ENV',platform.python_version(),platform.platform(),'max_h',max_h,'max_d',max_d,'seconds',seconds,flush=True)
    assert max_d<=max_h
    allgroups=groups(max_h)
    byorder=defaultdict(list)
    for G in allgroups:byorder[G.n].append(G)
    summary={}
    for n in range(1,max_h+1):
        if orders is not None and n not in orders: continue
        c=b=t=0;qcnt=0;details={}
        for G in byorder[n]:
            tick=time.monotonic()
            H,stats=holomorph_braces(G,deadline)
            if n<=max_d:
                D,dstats=direct_braces(G,byorder[n],deadline)
                assert {canonical_lam(G,x) for x in H}==D,(G.name,len(H),len(D))
                stats['independent_D']=dstats
            types=0; twos=0; qlocal=0
            Q=dicyclic(n//4) if n in (12,20,28) and G.abelian else None
            for lam in H:
                two=brace_properties(G,lam,check_ybe=n<=12)
                twos+=int(two);types+=int(G.abelian)
                if Q is not None: qlocal+=int(circle_is_isomorphic(G,lam,Q))
            c+=len(H); b+=types; t+=twos; qcnt+=qlocal
            stats.update(braces=len(H),classical=types,two_sided=twos,seconds=round(time.monotonic()-tick,3))
            if Q is not None:stats['quaternion_multiplicative']=qlocal
            details[G.name]=stats
            print('GROUP',n,G.name,json.dumps(stats,sort_keys=True),flush=True)
        expected={'skew':SKEW[n] if n<len(SKEW) else None,'left':LEFT[n] if n<len(LEFT) else None,'two':TWO[n] if n<len(TWO) else None}
        counts={'skew':c,'left':b,'two':t}
        assert all(expected[k] is None or counts[k]==expected[k] for k in counts),(n,counts,expected)
        if n in (12,20,28):
            assert qcnt==2,(n,qcnt)
            counts['q(4m)']=qcnt
            print('QUAT',n,qcnt,'PREDICTED 2 MATCH',flush=True)
        summary[n]={'counts':counts,'expected':expected,'groups':details}
        print('ORDER',n,json.dumps(counts,sort_keys=True),'MATCH',flush=True)
    print('FINISHED',round(time.monotonic()-start,3),'seconds',json.dumps({str(n):z['counts'] for n,z in summary.items()},sort_keys=True),flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--holomorph-max',type=int,default=12)
    parser.add_argument('--direct-max',type=int,default=8)
    parser.add_argument('--seconds',type=int,default=1500)
    parser.add_argument('--orders',type=str,default='1-15',help='comma-separated individual orders or inclusive ranges')
    a=parser.parse_args()
    ranges=[]
    for item in a.orders.split(','):
        r=[int(x) for x in item.split('-')]
        ranges.extend(range(r[0],r[-1]+1))
    run(a.holomorph_max,a.direct_max,a.seconds,set(ranges))
