import json,sys
legend=json.load(open('/home/claude/cw2/legend.json'))
def N(i,l,c,t,label,sub=None,tag=None,**k):
    n=dict(id=i,lane=l,col=c,type=t,label=label,width=k.pop('width',132))
    if sub: n['sublabel']=sub
    if tag: n['tag']=tag
    n.update(k); return n
def E(f,t,label=None,v="emphasis",**k):
    e={"from":f,"to":t,"variant":v}
    if label: e["label"]=label
    e.update(k); return e
def ERR(f,t,label=None,**k): return E(f,t,label,"security",role="error",**k)
def BR(f,t,label=None,**k): return E(f,t,label,"dashed",role="branch",**k)
def RET(f,t,label=None,**k): return E(f,t,label,"dashed",role="return",**k)
def ASY(f,t,label=None,**k): return E(f,t,label,"dashed",role="async",**k)
def V(i,label,focus,note): return dict(id=i,label=label,focus=focus,note=note)
def C(dot,title,items): return dict(dot=dot,title=title,items=items)
def doc(name,title,subtitle,views,lanes,phases,main,nodes,edges,cards):
    d={"schema_version":2,"diagram_type":"workflow","meta":{"title":title,"quality_profile":"showcase","legend":legend,"views":views},
      "lanes":lanes,"phases":phases,"mainPath":main,"nodes":nodes,"edges":edges,"cards":cards}
    for v in views: assert len(v['note'])<=140,(v['id'],len(v['note']))
    json.dump(d,open(f'/home/claude/cw2/{name}.workflow.json','w'),indent=2)
LANES={
 'client':dict(id='client',label='Client & Consultants'),
 'comm':dict(id='comm',label='Commercial & Contracts'),
 'site':dict(id='site',label='Site & Procurement'),
 'fin':dict(id='fin',label='Finance & Accounts'),
 'exc':dict(id='exc',label='Exceptions & Escalation',variant='exception'),
}
def L(*ids): return [LANES[i] for i in ids]
def P(i,label,a,b,variant=None):
    p=dict(id=i,label=label,fromCol=a,toCol=b)
    if variant: p['variant']=variant
    return p
def DN(f,t,label=None,v="emphasis",**k): return E(f,t,label,v,**k) if label else E(f,t,None,v,route='straight',fromSide='bottom',toSide='top',**k)
def UP(f,t,label=None,v="emphasis",**k): return E(f,t,label,v,**k) if label else E(f,t,None,v,route='straight',fromSide='top',toSide='bottom',**k)
def H(f,t,label=None,v="emphasis",**k): return E(f,t,label,v,route='straight',**k)
