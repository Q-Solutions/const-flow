from lib import *
lanes=[dict(id='client',label='Client & Engineer'),dict(id='qs',label='QS & Controls'),dict(id='site',label='Site Team'),LANES['exc']]
nodes=[
 N('lookahead','site',0,'backend','Lookahead Plan','3 weeks by trade','Site Manager · weekly'),
 N('execute','site',1,'cloud','Execute Works','own crews + subs','Foreman'),
 N('diary','site',2,'database','Daily Diary','labour, plant, weather','Site Eng · daily'),
 N('inspect','site',3,'security','Inspection','engineer signs IR','Engineer · 24 h'),
 N('progress','qs',4,'database','Progress by BOQ','% done, S-curve','QS · monthly'),
 N('billing','qs',5,'frontend','To Billing','IPC + sub valuations','QS · by cut-off'),
 N('instr','client',1,'external','Site Instruction','change, RFI answer','Engineer'),
 N('notice','qs',2,'messagebus','Variation Notice','within notice period','QS · per contract'),
 N('price','qs',3,'backend','Price Variation','rates, time impact','QS · 14 days'),
 N('approve','client',4,'security','Approve VO','signed VO','Engineer'),
 N('ncr','exc',3,'messagebus','NCR + Rework','cause, fix, recheck','Site Eng'),
 N('eot','exc',2,'messagebus','Delay Event','EOT notice, records','PM · per contract'),
]
edges=[
 H('lookahead','execute'), H('execute','diary'), H('diary','inspect'), E('inspect','progress','passed'), H('progress','billing'),
 E('instr','notice','instruction'), H('notice','price'), E('price','approve','submit'), E('approve','billing','add to sum'),
 ERR('inspect','ncr','rejected'), ERR('diary','eot','delay'),
]
views=[
 V('build','1. Plan and build',['lookahead','execute','diary'],'Plan three weeks ahead, build, and record labour, plant, weather and delays every day.'),
 V('inspect','2. Inspect and record',['inspect','ncr','progress'],'Nothing is covered up without a signed inspection. Failed work becomes an NCR and is rechecked.'),
 V('change','3. Change control',['instr','notice','price','approve'],'Every instruction gets a written notice inside the contract period, then a priced VO.'),
 V('time','4. Delay and billing',['eot','progress','billing'],'Delays are noticed on time with diary records. Approved progress and VOs go to monthly billing.'),
]
cards=[C('cyan','Time Bars',['Variation notice window','EOT notice window']),
 C('amber','Next Action',['Open NCR over 7 days: escalate','VO unpriced 14 days: QS alert']),
 C('rose','Records',['Diary backs every claim'])]
doc('05-site-and-change-control','Site Execution and Change Control','',views,lanes,
 [P('ph1','Plan + build',0,2),P('ph2','Inspect',3,3,'emphasis'),P('ph3','Measure + bill',4,5,'dashed')],
 ['lookahead','execute','diary','inspect','progress','billing'],nodes,edges,cards)
