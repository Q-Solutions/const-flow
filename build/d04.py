from lib import *
lanes=[dict(id='sub',label='Subcontractors'),dict(id='site',label='Site Team'),dict(id='qs',label='QS & Contracts'),dict(id='fin',label='Finance & AP')]
nodes=[
 N('scope','qs',0,'backend','Package Scope','scope, BOQ, budget','QS'),
 N('bids','sub',1,'external','Sub Quotes','from approved list','Subs · 7 days'),
 N('level','qs',1,'backend','Level Bids','scope gaps, rates','QS'),
 N('award','qs',2,'security','Award Subcontract','rates, retention, terms','PM + Director'),
 N('bond','sub',2,'external','Bond + Insurance','before start','Sub'),
 N('advance','fin',2,'backend','Advance Paid','against guarantee','AP'),
 N('works','site',3,'cloud','Works on Site','daily records','Site Eng'),
 N('variation','qs',3,'messagebus','Sub Variation','instructed change','QS'),
 N('apply','sub',4,'external','Payment Application','monthly claim','Sub · by cut-off'),
 N('measure','site',4,'security','Measure + Verify','qty vs BOQ, quality','Site Eng · 5 days'),
 N('value','qs',4,'backend','Valuation','gross less deductions','QS · 5 days'),
 N('ledger','fin',4,'database','Sub Ledger','retention, recoveries','Auto'),
 N('cert','qs',5,'frontend','Payment Certificate','net amount due','PM approves'),
 N('pay','fin',5,'backend','Pay Sub','by due date, tax cert','AP · per terms'),
]
edges=[
 E('scope','bids','RFQ'), DN('bids','level'), H('scope','level'), H('level','award','best value'),
 UP('award','bond'), DN('award','advance'), E('award','works','start'),
 E('works','apply','monthly'), DN('apply','measure'), DN('measure','value'), H('value','cert'), DN('cert','pay'),
 DN('works','variation'), H('variation','value','priced'), DN('value','ledger'), H('advance','ledger','recover'),
]
views=[
 V('tender','1. Tender and award',['scope','bids','level','award'],'Define the package, get quotes from approved subs, level scope gaps, and award within the budget.'),
 V('start','2. Secure and start',['award','bond','advance','works'],'No start without bond and insurance on file. Advance is paid only against a guarantee.'),
 V('value','3. Measure and value',['apply','measure','value','variation'],'Sub claims monthly. Site verifies quantity and quality. QS values it with approved variations only.'),
 V('pay','4. Certify and pay',['cert','ledger','pay'],'Net = work done less retention, advance recovery, backcharges and tax. Pay by the contract due date.'),
]
cards=[C('cyan','Deductions',['Retention, advance recovery','Backcharges, tax']),
 C('amber','Next Action',['Claim not valued in 5 days: alert','Insurance lapsed: hold payment']),
 C('rose','Rule',['Pay only measured, certified work'])]
doc('04-subcontract-lifecycle','Subcontract Lifecycle','',views,lanes,
 [P('ph1','Tender + award',0,2),P('ph2','Work + claim',3,4,'emphasis'),P('ph3','Pay',5,5,'dashed')],
 ['scope','level','award','works','apply','measure','value','cert','pay'],nodes,edges,cards)
