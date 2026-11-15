#!/usr/bin/env python3
"""Check remaining selected nonabelian additive groups of order 16."""
import time,json
from enumerate import abelian,dihedral,quaternion,direct,semidirect,enumerate_braces
start=time.monotonic();out=[]
for G in [direct(dihedral(4),abelian((2,))),direct(quaternion(2),abelian((2,))),semidirect(4,4,3)]:
    print('START',G[0],flush=True)
    try: r=enumerate_braces(G,deadline=start+500)
    except TimeoutError as e:print('TIMEOUT',str(e),flush=True);break
    hits=[e for e in r['examples'] if e['properties']['star_associative'] and not e['properties']['two_sided']]
    print('DONE',G[0],r['brace_count'],'hits',len(hits),'elapsed',round(time.monotonic()-start,3),flush=True)
    out.append({'additive_group':G[0],'total':r['brace_count'],'counterexamples':len(hits)})
with open('probe16_more.json','w') as f:json.dump(out,f,indent=2)
