from lib import *
lanes=[dict(id='client',label='Client & Engineer'),dict(id='site',label='Site & Project Team'),dict(id='qs',label='QS & Contracts'),dict(id='fin',label='Finance & Accounts')]
nodes=[
 N('complete','site',0,'cloud','Practical Completion','notice to engineer','PM'),
 N('snag','site',1,'backend','Snag + Commission','tests, O&M, as-builts','PM · 14 days'),
 N('toc','client',2,'security','Taking-Over Cert','DLP starts','Engineer'),
 N('dlp','site',3,'cloud','Defects Period','fix notified defects','PM · per notice'),
 N('ret1','qs',2,'frontend','Retention Claim 1','first half from client','QS · 7 days'),
 N('subret1','fin',2,'backend','Sub Retention 1','release first half','AP'),
 N('dcert','client',4,'security','Defects Certificate','end of DLP','Engineer'),
 N('final','qs',4,'database','Final Account','VOs, claims, retention 2','QS · per contract'),
 N('subfinal','qs',5,'database','Sub Final Accounts','agree + release','QS'),
 N('close','fin',5,'backend','Close Project','bonds back, codes shut','Finance'),
]
edges=[
 H('complete','snag'), E('snag','toc','ready'), E('toc','dlp','DLP'), DN('toc','ret1'), DN('ret1','subret1'),
 E('dlp','dcert','defects fixed'), DN('dcert','final'), H('final','subfinal'), DN('subfinal','close'),
]
views=[
 V('complete','1. Complete and hand over',['complete','snag','toc'],'Give completion notice, clear snags, commission, hand over O&M and as-builts, get the taking-over certificate.'),
 V('ret1','2. First half retention',['toc','ret1','subret1'],'Claim the first half of retention from the client. Release the first half to subs whose work is accepted.'),
 V('dlp','3. Defects period',['dlp','dcert'],'Fix each notified defect within the notice period. At DLP end, get the defects certificate.'),
 V('close','4. Final accounts and close',['final','subfinal','close'],'Agree the client final account and every sub final account, release retention 2, recover bonds, close codes.'),
]
cards=[C('cyan','Dates to Watch',['DLP end, bond expiry','Final account submission date']),
 C('amber','Next Action',['Defect open past notice: PM alert']),
 C('rose','Unresolved',['Claims go to dispute process'])]
doc('10-completion-and-closeout','Completion and Financial Close','',views,lanes,
 [P('ph1','Complete',0,2),P('ph2','Defects period',3,4,'emphasis'),P('ph3','Close',5,5,'dashed')],
 ['complete','snag','toc','dlp','dcert','final','subfinal','close'],nodes,edges,cards)
