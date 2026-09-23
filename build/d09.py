from lib import *
lanes=[dict(id='src',label='Dated Records'),dict(id='eng',label='Deadline Register'),dict(id='own',label='Record Owner'),dict(id='mgmt',label='Escalation',variant='exception')]
nodes=[
 N('records','src',0,'database','Every Dated Record','IPC, bill, bond, VO, NCR','All modules'),
 N('register','eng',1,'database','Deadline Register','owner, due, next step','Auto'),
 N('sweep','eng',2,'security','Daily Sweep','approaching, due, late','Auto · daily'),
 N('notify','own',3,'messagebus','Notify Owner','the next step to take','Auto'),
 N('act','own',4,'backend','Owner Acts','do it, attach proof','Owner'),
 N('done','own',5,'database','Closed','time-stamped','Auto'),
 N('escalate','mgmt',4,'messagebus','Escalate','late past 3 days','PM, then Director'),
 N('digest','mgmt',5,'frontend','Weekly Digest','open items by owner','Auto · Monday'),
]
edges=[
 E('records','register','due date'), H('register','sweep'), E('sweep','notify','approaching'), H('notify','act'), H('act','done','closed'),
 E('notify','escalate','no action',v='security',role='error'), UP('escalate','act'), H('escalate','digest'),
]
views=[
 V('capture','1. Every date has an owner',['records','register'],'Any record with a date (IPC, bill, bond, VO notice, NCR) enters the register with an owner and a next step.'),
 V('sweep','2. Daily sweep',['register','sweep','notify'],'Each day the system flags what is approaching, due, or late, and tells the owner exactly what to do next.'),
 V('act','3. Act and close',['notify','act','done'],'The owner does the step and attaches proof. The item closes with a time stamp.'),
 V('escalate','4. Escalate',['escalate','act','digest'],'Late for 3 days goes to the PM, then the Director. Monday digest lists open items by owner.'),
]
cards=[C('cyan','Money Dates',['IPC, certificate, receipt','Supplier and sub due dates']),
 C('amber','Contract Dates',['Notice time-bars, bond expiry','DLP end, retention release']),
 C('rose','Rule',['No record without an owner'])]
doc('09-deadlines-and-reminders','Deadlines and Reminders','',views,lanes,
 [P('ph1','Register',0,1),P('ph2','Sweep + notify',2,3,'emphasis'),P('ph3','Act or escalate',4,5,'dashed')],
 ['records','register','sweep','notify','act','done'],nodes,edges,cards)
