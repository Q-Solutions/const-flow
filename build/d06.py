from lib import *
lanes=[dict(id='client',label='Client & Engineer'),dict(id='qs',label='QS & Billing'),dict(id='fin',label='Finance & AR'),dict(id='exc',label='Ageing & Disputes',variant='exception')]
nodes=[
 N('cutoff','qs',0,'backend','Monthly Cut-off','progress + VOs','QS · 25th'),
 N('draft','qs',1,'backend','Draft IPC','work, VOs, materials','QS · 3 days'),
 N('review','qs',2,'security','Internal Review','PM signs off','PM · 2 days'),
 N('assess','client',3,'security','Engineer Assessment','within contract days','Engineer'),
 N('cert','client',4,'frontend','Payment Certificate','certified amount','Engineer'),
 N('invoice','fin',4,'frontend','Tax Invoice','on certificate','AR · same day'),
 N('receipt','fin',5,'database','Receipt + Match','bank, allocate','AR · on receipt'),
 N('dispute','exc',3,'messagebus','Under-certified','query, resubmit','QS · 7 days'),
 N('remind','exc',4,'messagebus','Due Date Reminder','7 days before, on due','Auto'),
 N('overdue','exc',5,'messagebus','Overdue Escalation','30, 60, 90 days','PM, then Director'),
]
edges=[
 H('cutoff','draft'), H('draft','review'), E('review','assess','submit'), H('assess','cert'), DN('cert','invoice'),
 H('invoice','receipt','paid'),
 DN('assess','dispute',v='security',role='error'), ASY('invoice','remind','due date'), E('remind','overdue','not paid',v='security',role='error'),
]
views=[
 V('prepare','1. Prepare the IPC',['cutoff','draft','review'],'At cut-off, value work done, approved VOs and materials on site, less retention and advance recovery.'),
 V('certify','2. Get it certified',['review','assess','cert','dispute'],'Submit on time. Track the engineer\'s certification deadline. Query any short-certified item in 7 days.'),
 V('collect','3. Invoice and collect',['cert','invoice','receipt'],'Invoice the certified amount the same day. Match every receipt to its invoice and bank line.'),
 V('ageing','4. Ageing and follow-up',['remind','overdue','receipt'],'Remind 7 days before due and on due. At 30, 60, 90 days overdue, escalate and apply contract remedies.'),
]
cards=[C('cyan','IPC Formula',['Work + VOs + materials on site','Less retention, advance, previous']),
 C('amber','Ageing Buckets',['Current, 1-30, 31-60, 61-90, 90+']),
 C('rose','Remedies',['Interest, notice, suspension'])]
doc('06-billing-and-receivables','Client Billing and Receivables','',views,lanes,
 [P('ph1','Prepare',0,2),P('ph2','Certify',3,4,'emphasis'),P('ph3','Collect',5,5,'dashed')],
 ['cutoff','draft','review','assess','cert','invoice','receipt'],nodes,edges,cards)
