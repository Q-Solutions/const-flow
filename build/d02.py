from lib import *
lanes=[dict(id='client',label='Client & Engineer'),dict(id='comm',label='Commercial & QS'),dict(id='plan',label='Planning & Site'),dict(id='fin',label='Finance & Accounts')]
nodes=[
 N('loa','comm',0,'database','Contract Signed','LOA + agreement','Contracts'),
 N('register','comm',1,'database','Contract Register','sum, retention, LDs','Contracts · 5 days'),
 N('setup','fin',0,'backend','Project Setup','cost codes, limits','Finance · 3 days'),
 N('securities','fin',1,'frontend','Bonds + Insurance','performance, CAR','Finance · by due date'),
 N('advance','fin',2,'external','Advance Received','against guarantee','AR'),
 N('budget','comm',2,'database','Cost Budget','estimate to cost code','QS · 2 weeks'),
 N('programme','plan',2,'backend','Baseline Programme','milestones, logic','Planner · 2 weeks'),
 N('approve','client',3,'security','Programme Review','engineer consent','Engineer'),
 N('cashplan','fin',3,'database','Cash-Flow Forecast','in vs out by month','Finance'),
 N('packages','plan',4,'backend','Procurement Plan','packages, long-lead','Procurement'),
 N('mobilize','plan',5,'cloud','Mobilize Site','access, setup, staff','PM'),
]
edges=[
 H('loa','register'), DN('loa','setup'), DN('register','securities'), H('securities','advance','claim'),
 H('register','budget','turnover'), DN('budget','programme'), E('programme','approve','submit'),
 E('approve','packages','accepted'), H('packages','mobilize'),
 BR('programme','cashplan','cost + time'), H('advance','cashplan'),
]
views=[
 V('record','1. Record the contract',['loa','register','setup'],'Enter every term with a date: sum, retention, LDs, notice periods. Set cost codes and approval limits.'),
 V('secure','2. Bonds and advance',['register','securities','advance'],'Issue bonds and insurance before their due dates, then claim the advance against the guarantee.'),
 V('plan','3. Budget and programme',['budget','programme','approve','cashplan'],'Turn the estimate into a cost budget, build the programme, and forecast cash in and out by month.'),
 V('go','4. Buy and mobilize',['packages','mobilize'],'Place long-lead orders and subcontract packages first, then mobilize the site.'),
]
cards=[C('cyan','Register Holds',['Every contract date and notice period','Bond and insurance expiry dates']),
 C('amber','Next Action',['Bond expiring in 30 days: renew']),
 C('rose','Budget Rule',['No spend until the cost budget is approved'])]
doc('02-contract-setup','Contract Setup and Budget','',views,lanes,
 [P('ph1','Record',0,1),P('ph2','Budget + plan',2,3,'emphasis'),P('ph3','Mobilize',4,5,'dashed')],
 ['loa','register','budget','programme','approve','packages','mobilize'],nodes,edges,cards)
