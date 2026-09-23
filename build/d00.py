from lib import *
lanes=[dict(id='client',label='Client & Consultants'),dict(id='comm',label='Commercial & Contracts'),dict(id='ops',label='Site & Procurement'),dict(id='fin',label='Finance & Accounts')]
nodes=[
 N('inquiry','client',0,'external','Inquiry / RFP','tender documents','BD'),
 N('bid','comm',0,'backend','Estimate + Bid','BOQ, rates, margin','Estimating'),
 N('award','client',1,'security','Award','LOA or regret','Client'),
 N('register','comm',1,'database','Contract Register','terms, bonds, dates','Contracts · 5 days'),
 N('budget','comm',2,'database','Budget + Cash Plan','by cost code','QS + Finance'),
 N('buy','ops',2,'backend','Buy + Subcontract','PO, agreements','Procurement'),
 N('build','ops',3,'cloud','Build + Record','diary, progress, QA','Site team · daily'),
 N('vo','comm',3,'messagebus','Variations','notice, price, agree','QS · within notice'),
 N('ipc','comm',4,'frontend','Bill Client','monthly IPC','QS · by cut-off'),
 N('certify','client',4,'security','Certify','engineer approves','Engineer'),
 N('paysub','fin',3,'backend','Pay Subs + Suppliers','only verified work','AP · by due date'),
 N('collect','fin',4,'database','Collect + Reconcile','AR ageing','AR · weekly'),
 N('closeout','ops',5,'cloud','Complete + Snag','test, handover docs','PM'),
 N('final','comm',5,'database','Final Accounts','client, subs, retention','QS'),
 N('handover','client',5,'external','Take Over','DLP starts','Client'),
]
edges=[
 E('inquiry','bid',route='straight',fromSide='bottom',toSide='top'), E('bid','award','submit'), E('award','register',route='straight',fromSide='bottom',toSide='top'),
 E('register','budget',route='straight'), E('budget','buy',route='straight',fromSide='bottom',toSide='top'), E('buy','build','materials, subs',route='straight'),
 E('build','ipc','measured'), E('ipc','certify'), E('certify','collect','certified'),
 BR('build','paysub','verified'), BR('build','vo','instruction'), BR('vo','ipc','priced VO'),
 BR('build','closeout','complete'), E('closeout','handover'), BR('handover','final','DLP ends'),
]
views=[
 V('win','1. Win and set up',['inquiry','bid','award','register','budget'],'Win the job, record every contract term and date, and turn the estimate into a budget before any spend.'),
 V('build','2. Buy and build',['budget','buy','build','paysub'],'Buy against budget, build and record daily, pay subs and suppliers only for verified work.'),
 V('cash','3. Bill and collect',['build','vo','ipc','certify','collect'],'Measure monthly, bill the client with variations, chase certification and cash by ageing.'),
 V('close','4. Close out',['closeout','handover','final'],'Complete, hand over, settle every final account and release retention and bonds.'),
]
cards=[C('cyan','Money In',['Monthly IPC, variations, retention release']),
 C('amber','Money Out',['Suppliers by 3-way match','Subs by certified valuation']),
 C('rose','Every Record Has',['Owner, due date, next action'])]
doc('00-overview','Contractor Operations: Inquiry to Close','',views,lanes,
 [P('ph1','Win',0,1),P('ph2','Set up + buy',2,2),P('ph3','Build + bill',3,4,'emphasis'),P('ph4','Close',5,5,'dashed')],
 ['inquiry','bid','award','register','budget','buy','build','ipc','certify','collect'],nodes,edges,cards)
