import json,sys,subprocess
R=float(sys.argv[2]) if len(sys.argv)>2 else 1.56
f=sys.argv[1]; d=json.load(open(f)); d['meta'].pop('viewBox',None); json.dump(d,open(f,'w'),indent=2)
r=json.loads(subprocess.run(['node','/tmp/archify/archify/bin/archify.mjs','validate','workflow',f,'--layout-json'],capture_output=True,text=True).stdout)
vb=r.get("requiredViewBox") or r.get("viewBox")
if not vb: print("fit skipped:",[x["message"][:300] for x in r.get("diagnostics",[])]); sys.exit(0)
w,h=vb
if w/h<R: d["meta"]["viewBox"]=[round(h*R),h]
json.dump(d,open(f,'w'),indent=2); print('viewBox',w,h,'->',d['meta'].get('viewBox'))
