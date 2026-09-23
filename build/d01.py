from lib import *
lanes=[dict(id='client',label='Client & Consultants'),dict(id='bd',label='Business Development'),dict(id='est',label='Estimating'),LANES['exc']]
nodes=[
 N('inquiry','client',0,'external','Inquiry / RFP','tender docs, deadline','Client'),
 N('gonogo','bd',0,'security','Go / No-Go','fit, risk, capacity','BD Head · 2 days'),
 N('takeoff','est',1,'backend','Quantity Takeoff','drawings to BOQ','Estimator'),
 N('rfq','bd',1,'messagebus','Sub + Supplier RFQs','quotes per package','Estimator · 5 days'),
 N('price','est',2,'backend','Build Up Price','direct + OH + margin','Estimator'),
 N('clarify','client',2,'external','Tender Queries','RFIs, addenda','Client'),
 N('review','bd',3,'security','Bid Review','price, risk, cash','Directors'),
 N('submit','bd',4,'frontend','Submit Bid','bid bond attached','BD · before deadline'),
 N('negotiate','client',4,'external','Negotiate','clarify, revise','Client'),
 N('award','client',5,'security','Award','LOA or regret','Client'),
 N('contract','bd',5,'database','Sign Contract','handover to project','BD + PM'),
 N('decline','exc',0,'messagebus','Decline','log reason','BD'),
 N('lost','exc',5,'database','Lost: Debrief','price gap, winner','BD'),
]
edges=[
 DN('inquiry','gonogo'), E('gonogo','takeoff','go'), UP('takeoff','rfq','packages',v='dashed',role='branch'),
 H('takeoff','price'), BR('rfq','price','best rates'), ASY('price','clarify','queries'),
 E('price','review'), H('review','submit','approved'), UP('submit','negotiate'), H('negotiate','award'),
 DN('award','contract','awarded'),
 ERR('gonogo','decline','no-go'), ERR('award','lost','not awarded'),
]
views=[
 V('qualify','1. Qualify',['inquiry','gonogo','decline'],'Log every inquiry with its deadline. Decide go or no-go in 2 days. Record why you declined.'),
 V('price','2. Price',['takeoff','rfq','price','clarify'],'Take off quantities, send RFQs early, and raise tender queries before the query deadline.'),
 V('submit','3. Review and submit',['review','submit'],'Directors sign off price, risk and cash need. Submit with bid bond before the deadline.'),
 V('award','4. Award',['negotiate','award','contract','lost'],'Negotiate, sign, and hand the contract to the project team. If lost, get a debrief.'),
]
cards=[C('cyan','Deadlines Tracked',['Query deadline','Bid submission date','Bid bond validity']),
 C('amber','Next Action',['RFQ not answered in 5 days: chase or replace']),
 C('rose','Win / Loss',['Record price gap on every lost bid'])]
doc('01-win-the-work','Win the Work: Inquiry to Contract','',views,lanes,
 [P('ph1','Qualify',0,0),P('ph2','Price',1,2),P('ph3','Submit',3,4,'emphasis'),P('ph4','Award',5,5,'dashed')],
 ['inquiry','gonogo','takeoff','price','review','submit','negotiate','award','contract'],nodes,edges,cards)
