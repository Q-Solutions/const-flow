from lib import *
lanes=[dict(id='data',label='Cost + Value Data'),dict(id='qs',label='QS & Cost Control'),dict(id='fin',label='Finance & Close'),dict(id='mgmt',label='Management')]
nodes=[
 N('commit','data',0,'database','Commitments','POs + subcontracts','Auto'),
 N('actual','data',1,'database','Actual Cost','GRNs, bills, expenses','Auto'),
 N('earned','data',2,'database','Value Earned','certified + unbilled','From billing'),
 N('costrep','qs',1,'backend','Cost Report','budget vs committed','QS · monthly'),
 N('cvr','qs',2,'security','Cost-Value Check','CVR, margin to date','QS · 5th'),
 N('eac','qs',3,'backend','Forecast Final Cost','cost to complete','QS + PM'),
 N('close','fin',2,'backend','Month-End Close','accruals, WIP, P&L','Accountant · 7th'),
 N('alert','mgmt',3,'messagebus','Overrun Alert','code over budget','Auto'),
 N('review','mgmt',4,'security','Monthly Review','margin, cash, risk','Directors · 10th'),
 N('action','mgmt',5,'backend','Corrective Actions','owner + due date','PM'),
]
edges=[
 E('commit','costrep'), DN('actual','costrep'), H('costrep','cvr'), DN('earned','cvr'), H('cvr','eac'),
 DN('cvr','close'), DN('eac','alert'), H('alert','review'), H('review','action'),
]
views=[
 V('data','1. Collect the numbers',['commit','actual','earned'],'Commitments count when approved. Actuals from GRNs and bills. Value from certified and unbilled work.'),
 V('cvr','2. Cost vs value',['costrep','cvr','eac'],'By cost code: budget, committed, actual, forecast. Compare cost to value earned to see real margin.'),
 V('close','3. Close the month',['cvr','close'],'Book accruals for received but unbilled goods, and WIP, so the P&L that goes to review is complete.'),
 V('act','4. Review and act',['alert','review','action'],'Overruns alert as soon as they are committed. Each review ends with actions, an owner and a date.'),
]
cards=[C('cyan','Per Cost Code',['Budget, committed, actual','Forecast final, variance']),
 C('amber','Next Action',['Code over 90% committed: PM alert']),
 C('rose','Close Calendar',['CVR by 5th, close 7th, review 10th'])]
doc('08-cost-control-and-close','Cost Control and Monthly Close','',views,lanes,
 [P('ph1','Collect',0,1),P('ph2','Reconcile',2,3,'emphasis'),P('ph3','Act',4,5,'dashed')],
 ['actual','costrep','cvr','eac','alert','review','action'],nodes,edges,cards)
