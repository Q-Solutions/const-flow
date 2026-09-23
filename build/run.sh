#!/bin/bash
# usage: run.sh name  (expects name.workflow.json)
A=/tmp/archify/archify/bin/archify.mjs; export ARCHIFY_CHROME=/opt/pw-browsers/chromium-1194/chrome-linux/chrome
cd /home/claude/cw2; n=$1; python3 fit.py $n.workflow.json $2
node $A validate workflow $n.workflow.json --quality showcase --json | python3 -c "import json,sys;d=json.load(sys.stdin);print('validate',d['ok'],d.get('error'),d.get('composition',{}).get('summary'),[i.get('message') for i in d.get('composition',{}).get('issues',[])][:5])" || exit 1
node $A deliver workflow $n.workflow.json $n.html --quality showcase --json | python3 -c "import json,sys;d=json.load(sys.stdin);print('deliver',d.get('ok'),d.get('error'))"
node $A visual-check $n.html --json | python3 -c "import json,sys;d=json.load(sys.stdin);print('visual',d.get('status'),[ (x['message'][:200],x.get('evidence',{}).get('scrollHeight')) for x in d.get('diagnostics',[])])"
