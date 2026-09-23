from lib import *
lanes=[dict(id='src',label='Bills In'),dict(id='ap',label='Accounts Payable'),dict(id='mgmt',label='Finance Director / Treasury'),dict(id='exc',label='Holds & Shortfalls',variant='exception')]
nodes=[
 N('supp','src',0,'database','Supplier Bills','3-way matched','From P2P'),
 N('subc','src',1,'frontend','Sub Certificates','net of deductions','From QS'),
 N('petty','src',2,'cloud','Site Expenses','petty cash, limits','Site Admin · weekly'),
 N('ledger','ap',2,'database','AP Ledger','due date, tax, cost code','AP · 2 days'),
 N('ageing','ap',3,'database','AP Ageing','due this week, overdue','AP · weekly'),
 N('proposal','ap',4,'backend','Payment Proposal','due + priority rules','AP · weekly'),
 N('forecast','mgmt',3,'database','Cash Forecast','13 weeks, AR vs AP','Finance · weekly'),
 N('approve','mgmt',4,'security','Approve Run','within cash, limits','FD'),
 N('pay','ap',5,'backend','Pay + Remit','bank file, tax certs','AP · run day'),
 N('recon','mgmt',5,'database','Bank Reconcile','post to GL','Accountant · weekly'),
 N('hold','exc',2,'messagebus','Bill on Hold','missing proof','AP chases'),
 N('short','exc',4,'messagebus','Cash Shortfall','defer, fund, chase AR','FD + PM'),
]
edges=[
 E('supp','ledger'), E('subc','ledger'), DN('petty','ledger'), H('ledger','ageing'), H('ageing','proposal'),
 DN('proposal','approve'), E('approve','pay','approved'), DN('pay','recon'),
 E('ageing','forecast','AP due',v='dashed',role='async'), E('forecast','approve','cash'),
 DN('ledger','hold',v='security',role='error'), ERR('approve','short','short'),
]
views=[
 V('capture','1. Capture every bill',['supp','subc','petty','ledger'],'Matched supplier bills, certified sub payments and site expenses land in one ledger with due dates.'),
 V('plan','2. Age and forecast',['ageing','forecast'],'Each week, age what is due and overdue, and forecast 13 weeks of cash with expected client receipts.'),
 V('pay','3. Propose, approve, pay',['proposal','approve','pay','recon'],'AP proposes by due date and priority. FD approves within cash. Pay, send remittance, reconcile bank.'),
 V('exceptions','Holds and shortfalls',['hold','short'],'Bills without proof are held and chased. If cash is short, FD defers, funds, or pushes AR collection.'),
]
cards=[C('cyan','Priority Rules',['Tax and statutory first','Critical subs and suppliers next']),
 C('amber','Next Action',['Bill due in 7 days: add to run','Overdue bill: FD review']),
 C('rose','Cash Rule',['Approve only what cash covers'])]
doc('07-payables-and-cash','Payables, Cash and Ageing','',views,lanes,
 [P('ph1','Capture',0,2),P('ph2','Age + plan',3,4,'emphasis'),P('ph3','Pay',5,5,'dashed')],
 ['petty','ledger','ageing','proposal','approve','pay','recon'],nodes,edges,cards)
