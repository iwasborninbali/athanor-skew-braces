#!/usr/bin/env python3
"""From-scratch finite skew-brace enumeration by regular subgroups of Hol(G).

No GAP, catalog, or external mathematics package is used.
Full list of groups is supplied only for orders 1..12.  Every count of brace
isomorphism classes is the number of Aut(G)-conjugacy classes of regular
subgroups of Hol(G), proved by the standard regular-subgroup correspondence.
"""
import argparse
import itertools
import json
import math
import time
from collections import Counter


def group(name, elems, product):
    assert elems[0] == product(elems[0], elems[0])
    idx = {v:i for i,v in enumerate(elems)}
    n=len(elems)
    op=tuple(tuple(idx[product(a,b)] for b in elems) for a in elems)
    assert all(op[0][x]==x and op[x][0]==x for x in range(n))
    assert all(op[op[a][b]][c] == op[a][op[b][c]] for a in range(n) for b in range(n) for c in range(n))
    inv=tuple(next(y for y in range(n) if op[x][y]==0 and op[y][x]==0) for x in range(n))
    return (name,op,inv)


def abelian(factors):
    elems=list(itertools.product(*(range(x) for x in factors)))
    return group('x'.join('C'+str(x) for x in factors) or 'C1', elems,
                 lambda a,b:tuple((x+y)%f for x,y,f in zip(a,b,factors)))


def dihedral(m):
    elems=[(k,t) for t in range(2) for k in range(m)]
    return group('D'+str(2*m),elems,
                 lambda a,b:((a[0]+(-1)**a[1]*b[0])%m,(a[1]+b[1])%2))


def quaternion(m):
    elems=[(k,t) for t in range(2) for k in range(2*m)]
    return group('Q'+str(4*m),elems,
                 lambda a,b:((a[0]+(-1)**a[1]*b[0]+(m if a[1] and b[1] else 0))%(2*m),(a[1]+b[1])%2))


def direct(G,H):
    x,op,inv=G; y,other,jv=H
    m=len(op);n=len(other)
    elems=[(a,b) for a in range(m) for b in range(n)]
    return group(x+'x'+y,elems,lambda a,b:(op[a[0]][b[0]],other[a[1]][b[1]]))


def semidirect(m,t,unit):
    assert pow(unit,t,m)==1
    elems=[(a,b) for b in range(t) for a in range(m)]
    return group('C'+str(m)+'rt'+str(t)+'_'+str(unit),elems,
                 lambda a,b:((a[0]+pow(unit,a[1],m)*b[0])%m,(a[1]+b[1])%t))


def a4():
    perms=list(itertools.permutations(range(4)))
    def parity(p):
        return sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2
    elems=[(0,1,2,3)]+[p for p in perms if parity(p)==0 and p!=(0,1,2,3)]
    return group('A4',elems,lambda a,b:tuple(a[b[i]] for i in range(4)))


def all_abelian(n):
    def prime_factors(x):
        d=2; ret=[]
        while d*d<=x:
            k=0
            while x%d==0:x//=d;k+=1
            if k:ret.append((d,k))
            d+=1
        if x>1:ret.append((x,1))
        return ret
    def parts(k,low=1):
        if k==0:yield ()
        for i in range(low,k+1):
            for t in parts(k-i,i):yield (i,)+t
    if n==1:
        yield abelian(())
        return
    choices=[]
    for p,e in prime_factors(n):
        choices.append([tuple(p**v for v in part) for part in parts(e)])
    for choice in itertools.product(*choices):
        yield abelian(tuple(v for block in choice for v in block))


def groups_of_order(n):
    yield from all_abelian(n)
    if n in (6,8,10,12,14,20,22):yield dihedral(n//2)
    if n==8:yield quaternion(2)
    if n==12:
        yield quaternion(3)
        yield a4()
    if n==20:
        yield quaternion(5)
        yield semidirect(5,4,2)
    if n==21:yield semidirect(7,3,2)


def element_orders(op):
    n=len(op)
    orders=[]
    for x in range(n):
        y=0
        for k in range(1,n+1):
            y=op[y][x]
            if y==0:break
        assert y==0
        orders.append(k)
    return orders


def generates(op, generators):
    seen={0}; todo=[0]
    for x in todo:
        for g in generators:
            y=op[x][g]
            if y not in seen:seen.add(y);todo.append(y)
    return len(seen)==len(op)


def automorphisms(op):
    n=len(op)
    if n==1:return [tuple(range(n))]
    r=range(1,n)
    gens=next(comb for k in range(1,n) for comb in itertools.combinations(r,k) if generates(op,comb))
    orders=element_orders(op)
    candidates=[[x for x in r if orders[x]==orders[g]] for g in gens]
    result=set()
    for imgs in itertools.product(*candidates):
        if len(set(imgs))!=len(imgs):continue
        mapping=[-1]*n; mapping[0]=0; queue=[0]; valid=True
        for x in queue:
            for gen,img in zip(gens,imgs):
                u=op[x][gen];v=op[mapping[x]][img]
                if mapping[u]<0:mapping[u]=v;queue.append(u)
                elif mapping[u]!=v:valid=False;break
            if not valid:break
        if valid and len(set(mapping))==n and -1 not in mapping:
            assert all(mapping[op[x][y]]==op[mapping[x]][mapping[y]] for x in range(n) for y in range(n))
            result.add(tuple(mapping))
    ident=tuple(range(n))
    return [ident]+sorted(result-{ident})


class Hol:
    def __init__(self,op,inv):
        self.op=op;self.inv=inv;self.n=len(op)
        self.aut=automorphisms(op);self.k=len(self.aut)
        self.aut_idx={a:i for i,a in enumerate(self.aut)}
        self.comp=[[self.aut_idx[tuple(a[b[x]] for x in range(self.n))] for b in self.aut] for a in self.aut]
        self.ai=[next(j for j in range(self.k) if self.comp[i][j]==self.comp[j][i]==0) for i in range(self.k)]
        self.N=self.n*self.k
        self.inverse=[self.aut[self.ai[h%self.k]][inv[h//self.k]]*self.k+self.ai[h%self.k] for h in range(self.N)]
        self.mul=[[self.op[h//self.k][self.aut[h%self.k][j//self.k]]*self.k+self.comp[h%self.k][j%self.k] for j in range(self.N)] for h in range(self.N)]
        self.conj=[]
        for beta in range(self.k):
            b=self.aut[beta]; bi=self.ai[beta]
            self.conj.append([b[x//self.k]*self.k+self.comp[self.comp[beta][x%self.k]][bi] for x in range(self.N)])
        self.candidates=[x for x in range(self.k,self.N) if self.element_order(x) <= self.n and self.n%self.element_order(x)==0]

    def element_order(self,x):
        y=0
        for z in range(1,self.n+1):
            y=self.mul[y][x]
            if y==0:return z
        return self.n+1

    def extend(self,H,x):
        S=set(H);queue=list(H)
        gens=tuple(q for q in H if q)+ (x,self.inverse[x])
        coords={h//self.k for h in S}
        for a in queue:
            for b in gens:
                z=self.mul[a][b]
                if z not in S:
                    c=z//self.k
                    if c in coords:return None
                    S.add(z);coords.add(c);queue.append(z)
                    if len(S)>self.n:return None
        if self.n%len(S):return None
        return tuple(sorted(S))

    def canonical(self,H):
        return min(tuple(sorted(t[h] for h in H)) for t in self.conj)

    def circle(self,H):
        lam={h//self.k:h%self.k for h in H}
        assert len(lam)==self.n
        return tuple(tuple(self.op[a][self.aut[lam[a]][b]] for b in range(self.n)) for a in range(self.n))


def group_invariants(op):
    n=len(op);order=Counter(element_orders(op))
    comm=all(op[a][b]==op[b][a] for a in range(n) for b in range(n))
    return {'abelian':comm,'orders':dict(sorted(order.items()))}


def quaternion_isomorphic(op):
    n=len(op)
    if n%4 or n<8:return False
    target=quaternion(n//4)[1]
    # For small groups match via explicit bijection using images of generators.
    return isomorphic(op,target)


def isomorphic(op,other):
    if len(op)!=len(other):return False
    n=len(op)
    orders=element_orders(other)
    # Try the same generating-set image extension used for automorphisms.
    gens=next(comb for k in range(n) for comb in itertools.combinations(range(1,n),k) if generates(op,comb))
    src_orders=element_orders(op)
    candidates=[[i for i in range(1,n) if orders[i]==src_orders[g]] for g in gens]
    for imgs in itertools.product(*candidates):
        if len(set(imgs))!=len(imgs):continue
        mapping=[-1]*n;mapping[0]=0;todo=[0];valid=True
        for x in todo:
            for g,img in zip(gens,imgs):
                a=op[x][g];b=other[mapping[x]][img]
                if mapping[a]==-1:mapping[a]=b;todo.append(a)
                elif mapping[a]!=b:valid=False;break
            if not valid:break
        if valid and len(set(mapping))==n:return True
    return False


def brace_properties(add,circ):
    n=len(add); inv=[next(j for j in range(n) if add[i][j]==0 and add[j][i]==0) for i in range(n)]
    star=tuple(tuple(add[add[inv[a]][circ[a][b]]][inv[b]] for b in range(n)) for a in range(n))
    assoc=all(star[star[a][b]][c]==star[a][star[b][c]] for a in range(n) for b in range(n) for c in range(n))
    right=all(circ[add[a][b]][c]==add[add[circ[a][c]][inv[c]]][circ[b][c]] for a in range(n) for b in range(n) for c in range(n))
    assert all(circ[a][add[b][c]]==add[add[circ[a][b]][inv[a]]][circ[a][c]] for a in range(n) for b in range(n) for c in range(n))
    return {'star_associative':assoc,'two_sided':right}


def enumerate_braces(G, deadline=None, verbose=False):
    name,op,inv=G
    hol=Hol(op,inv)
    levels={1:{(0,)}}
    # canonicalize all partial subgroups at each stage.  Inclusion of a subgroup
    # not necessarily a Sylow series is covered because every group has a
    # chain of subgroups increasing from {1}.
    for sz in range(1,hol.n):
        if sz not in levels:continue
        current=levels.pop(sz)
        if verbose:print('  level',sz,'classes',len(current),flush=True)
        for H in current:
            coords={h//hol.k for h in H}
            for x in hol.candidates:
                if x//hol.k in coords:continue
                K=hol.extend(H,x)
                if K is None or len(K)==sz:continue
                can=hol.canonical(K)
                levels.setdefault(len(can),set()).add(can)
            if deadline and time.monotonic()>deadline:
                raise TimeoutError('deadline at '+name+' subgroup size '+str(sz))
    complete=levels.get(hol.n,set())
    data=[]
    for H in sorted(complete):
        circ=hol.circle(H)
        props=brace_properties(op,circ)
        invariants=group_invariants(circ)
        # identify quaternion via explicit same-order group isomorphism
        isq=quaternion_isomorphic(circ)
        data.append({'hol_elements':list(H),'circle':circ,'multiplicative':invariants,'quaternion':isq,'properties':props})
    out={'group':name,'order':hol.n,'automorphisms':hol.k,'brace_count':len(data),
         'classical':group_invariants(op)['abelian'],
         'mul_abelian':sum(d['multiplicative']['abelian'] for d in data),
         'quaternion_braces':sum(d['quaternion'] for d in data),
         'associative_star_non_two_sided':sum(d['properties']['star_associative'] and not d['properties']['two_sided'] for d in data),
         'two_sided':sum(d['properties']['two_sided'] for d in data),
         'examples':data}
    return out


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-order',type=int,default=8)
    parser.add_argument('--orders',default=None,help='comma-separated EXACT orders for which group catalog is complete')
    parser.add_argument('--seconds',type=int,default=900)
    parser.add_argument('--output',default='results.json')
    parser.add_argument('--verbose',action='store_true')
    args=parser.parse_args()
    tic=time.monotonic();results=[]
    print('PROGRAM enumerate.py from-scratch regular-subgroup enumeration',flush=True)
    orders = list(map(int,args.orders.split(','))) if args.orders else list(range(1,args.max_order+1))
    for n in orders:
        for g in groups_of_order(n):
            print('START',g[0],n,flush=True)
            try:r=enumerate_braces(g,deadline=tic+args.seconds,verbose=args.verbose)
            except TimeoutError as err:
                print('TIMEOUT',str(err),flush=True)
                with open(args.output,'w') as f:json.dump({'complete_groups':results,'timed_out':g[0]},f,indent=2)
                return
            results.append(r)
            print('DONE',g[0],r['brace_count'],'aut',r['automorphisms'], 'quaternion',r['quaternion_braces'],'mul abelian',r['mul_abelian'],'two-sided',r['two_sided'],'associative-not-two-sided',r['associative_star_non_two_sided'],'elapsed',round(time.monotonic()-tic,3),flush=True)
        print('ORDER',n,'s(n)',sum(x['brace_count'] for x in results if x['order']==n),'b(n)',sum(x['brace_count'] for x in results if x['order']==n and x['classical']),flush=True)
    with open(args.output,'w') as f:json.dump({'complete_groups':results,'elapsed_seconds':round(time.monotonic()-tic,3)},f,indent=2)
    print('SUCCESS output',args.output,flush=True)

if __name__=='__main__':main()
