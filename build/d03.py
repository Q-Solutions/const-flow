from lib import *
lanes=[dict(id='site',label='Site & Stores'),dict(id='proc',label='Procurement'),dict(id='fin',label='Finance & AP'),LANES['exc']]
nodes=[
 N('req','site',0,'cloud','Material Request','from lookahead','Site Eng'),
 N('check','proc',0,'security','Budget + Stock','cost code balance','Auto check'),
 N('quotes','proc',1,'external','Get 3 Quotes','suppliers reply','Buyer · 2 days'),
 N('approve','proc',2,'security','Compare + Approve','by authority limit','PM / Director'),
 N('po','proc',3,'frontend','Issue PO','rates, dates, terms','Buyer · same day'),
 N('commit','fin',3,'database','Commitment','budget reduced now','Auto'),
 N('deliver','site',3,'external','Delivery','note quotes PO no.','Supplier'),
 N('grn','site',4,'database','Goods Received','qty, photos, partial','Store · same day'),
 N('stock','site',5,'database','Stores Ledger','issue to work pack','Storekeeper'),
 N('match','fin',4,'security','3-Way Match','PO, GRN, invoice','AP · 3 days'),
 N('pay','fin',5,'backend','Payment Run','by due date, post GL','Finance · weekly'),
 N('overbudget','exc',0,'messagebus','Over Budget','transfer or change','PM decides'),
 N('late','exc',5,'messagebus','Past Due Date','supplier chasing','Escalate to FD'),
 N('hold','exc',4,'messagebus','Invoice on Hold','query, debit note','AP'),
]
edges=[
 E('req','check'), E('check','quotes','in budget'), E('quotes','approve'),
 E('approve','po','approved'), E('po','deliver'), E('deliver','grn'),
 E('grn','match','+ invoice'), E('match','pay','matched'),
 ASY('po','commit','commit'), BR('grn','stock','stock in'),
 ERR('check','overbudget','over'), RET('grn','deliver','reject'), ERR('pay','late','missed'), ERR('match','hold','mismatch'),
]
views=[
 V('request','1. Request and approve',['req','check','quotes','approve'],'Site raises it, system checks budget and stock, buyer gets 3 quotes, the right person approves by value.'),
 V('order','2. Order and receive',['po','commit','deliver','grn','stock'],'PO counts against budget the day it is issued. Store records what arrived, partial or full, same day.'),
 V('pay','3. Match and pay',['grn','match','pay'],'Pay only what was ordered and received. AP matches PO, GRN and invoice, then it joins the next payment run.'),
 V('exceptions','Exceptions',['overbudget','grn','deliver','hold','late'],'Over budget goes to the PM. Bad goods go back. Mismatches wait on hold. Missed due dates go to FD.'),
]
cards=[C('cyan','Controls',['No PO without budget','No payment without GRN']),
 C('amber','Next Action',['Unmatched invoice: AP chases in 3 days','PO past delivery date: buyer chases']),
 C('rose','Ageing',['Bills due in 7 days go to payment run'])]
doc('03-procure-to-pay','Procure to Pay: Materials','Site request to supplier payment',views,lanes,
 [P('ph1','Request + approve',0,2),P('ph2','Order + receive',3,3,'emphasis'),P('ph3','Match + pay',4,5,'dashed')],
 ['req','check','quotes','approve','po','deliver','grn','match','pay'],nodes,edges,cards)
