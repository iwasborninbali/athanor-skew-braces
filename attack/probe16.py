#!/usr/bin/env python3
"""Targeted n=16 search for associative * but non-two-sided skew braces.
Not a classification of all n=16 skew braces or additive groups.
"""
import json,time
from enumerate import (abelian,dihedral,quaternion,direct,semidirect,enumerate_braces)


def targets():
    yield dihedral(8)
    yield quaternion(4)
    yield semidirect(8,2,3)
    yield semidirect(8,2,5)
    yield direct(dihedral(4),abelian((2,)))
    yield direct(quaternion(2),abelian((2,)))
    yield semidirect(4,4,3)


def main():
    t=time.monotonic(); all_results=[]
    for G in targets():
        print('START',G[0],flush=True)
        try:res=enumerate_braces(G,deadline=t+600)
        except TimeoutError as e:
            print('TIMEOUT',str(e),flush=True);break
        hits=[e for e in res['examples'] if e['properties']['star_associative'] and not e['properties']['two_sided']]
        print('DONE',G[0],res['brace_count'],'hits',len(hits),'elapsed',round(time.monotonic()-t,3),flush=True)
        all_results.append({'group':G[0],'brace_count':res['brace_count'],'hits':len(hits)})
        if hits:
            with open('witness16.json','w') as f:json.dump({'additive_group':G[0],'additive_table':G[1], 'multiplicative_table':hits[0]['circle'], 'holomorph_elements':hits[0]['hol_elements']},f,indent=2)
            print('WITNESS',G[0],len(hits),'first witness saved',flush=True)
            break
    with open('probe16.json','w') as f:json.dump(all_results,f,indent=2)

if __name__=='__main__':main()
