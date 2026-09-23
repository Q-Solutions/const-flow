# Next-Action Playbook

Every step in the 11 diagrams, with who owns it and when. The owner and timing also show on each node as its tag. To see tags, zoom in or open a guided view.

Timings are defaults. Set them to your contract terms before go-live.

## Contractor Operations: Inquiry to Close
File: `00-overview.workflow.json`

| Step | What it covers | Owner / timing | Lane |
|---|---|---|---|
| Inquiry / RFP | tender documents | BD | Client & Consultants |
| Estimate + Bid | BOQ, rates, margin | Estimating | Commercial & Contracts |
| Award | LOA or regret | Client | Client & Consultants |
| Contract Register | terms, bonds, dates | Contracts · 5 days | Commercial & Contracts |
| Budget + Cash Plan | by cost code | QS + Finance | Commercial & Contracts |
| Buy + Subcontract | PO, agreements | Procurement | Site & Procurement |
| Variations | notice, price, agree | QS · within notice | Commercial & Contracts |
| Build + Record | diary, progress, QA | Site team · daily | Site & Procurement |
| Pay Subs + Suppliers | only verified work | AP · by due date | Finance & Accounts |
| Certify | engineer approves | Engineer | Client & Consultants |
| Bill Client | monthly IPC | QS · by cut-off | Commercial & Contracts |
| Collect + Reconcile | AR ageing | AR · weekly | Finance & Accounts |
| Take Over | DLP starts | Client | Client & Consultants |
| Final Accounts | client, subs, retention | QS | Commercial & Contracts |
| Complete + Snag | test, handover docs | PM | Site & Procurement |

**What to do next, by stage:**

- **1. Win and set up**: Win the job, record every contract term and date, and turn the estimate into a budget before any spend.
- **2. Buy and build**: Buy against budget, build and record daily, pay subs and suppliers only for verified work.
- **3. Bill and collect**: Measure monthly, bill the client with variations, chase certification and cash by ageing.
- **4. Close out**: Complete, hand over, settle every final account and release retention and bonds.

## Win the Work: Inquiry to Contract
File: `01-win-the-work.workflow.json`

| Step | What it covers | Owner / timing | Lane |
|---|---|---|---|
| Inquiry / RFP | tender docs, deadline | Client | Client & Consultants |
| Go / No-Go | fit, risk, capacity | BD Head · 2 days | Business Development |
| Decline | log reason | BD | Exceptions & Escalation |
| Sub + Supplier RFQs | quotes per package | Estimator · 5 days | Business Development |
| Quantity Takeoff | drawings to BOQ | Estimator | Estimating |
| Tender Queries | RFIs, addenda | Client | Client & Consultants |
| Build Up Price | direct + OH + margin | Estimator | Estimating |
| Bid Review | price, risk, cash | Directors | Business Development |
| Negotiate | clarify, revise | Client | Client & Consultants |
| Submit Bid | bid bond attached | BD · before deadline | Business Development |
| Award | LOA or regret | Client | Client & Consultants |
| Sign Contract | handover to project | BD + PM | Business Development |
| Lost: Debrief | price gap, winner | BD | Exceptions & Escalation |

**What to do next, by stage:**

- **1. Qualify**: Log every inquiry with its deadline. Decide go or no-go in 2 days. Record why you declined.
- **2. Price**: Take off quantities, send RFQs early, and raise tender queries before the query deadline.
- **3. Review and submit**: Directors sign off price, risk and cash need. Submit with bid bond before the deadline.
- **4. Award**: Negotiate, sign, and hand the contract to the project team. If lost, get a debrief.

## Contract Setup and Budget
File: `02-contract-setup.workflow.json`

| Step | What it covers | Owner / timing | Lane |
|---|---|---|---|
| Contract Signed | LOA + agreement | Contracts | Commercial & QS |
| Project Setup | cost codes, limits | Finance · 3 days | Finance & Accounts |
| Contract Register | sum, retention, LDs | Contracts · 5 days | Commercial & QS |
| Bonds + Insurance | performance, CAR | Finance · by due date | Finance & Accounts |
| Cost Budget | estimate to cost code | QS · 2 weeks | Commercial & QS |
| Baseline Programme | milestones, logic | Planner · 2 weeks | Planning & Site |
| Advance Received | against guarantee | AR | Finance & Accounts |
| Programme Review | engineer consent | Engineer | Client & Engineer |
| Cash-Flow Forecast | in vs out by month | Finance | Finance & Accounts |
| Procurement Plan | packages, long-lead | Procurement | Planning & Site |
| Mobilize Site | access, setup, staff | PM | Planning & Site |

**What to do next, by stage:**

- **1. Record the contract**: Enter every term with a date: sum, retention, LDs, notice periods. Set cost codes and approval limits.
- **2. Bonds and advance**: Issue bonds and insurance before their due dates, then claim the advance against the guarantee.
- **3. Budget and programme**: Turn the estimate into a cost budget, build the programme, and forecast cash in and out by month.
- **4. Buy and mobilize**: Place long-lead orders and subcontract packages first, then mobilize the site.

## Procure to Pay: Materials
File: `03-procure-to-pay.workflow.json`

| Step | What it covers | Owner / timing | Lane |
|---|---|---|---|
| Material Request | from lookahead | Site Eng | Site & Stores |
| Budget + Stock | cost code balance | Auto check | Procurement |
| Over Budget | transfer or change | PM decides | Exceptions & Escalation |
| Get 3 Quotes | suppliers reply | Buyer · 2 days | Procurement |
| Compare + Approve | by authority limit | PM / Director | Procurement |
| Delivery | note quotes PO no. | Supplier | Site & Stores |
| Issue PO | rates, dates, terms | Buyer · same day | Procurement |
| Commitment | budget reduced now | Auto | Finance & AP |
| Goods Received | qty, photos, partial | Store · same day | Site & Stores |
| 3-Way Match | PO, GRN, invoice | AP · 3 days | Finance & AP |
| Invoice on Hold | query, debit note | AP | Exceptions & Escalation |
| Stores Ledger | issue to work pack | Storekeeper | Site & Stores |
| Payment Run | by due date, post GL | Finance · weekly | Finance & AP |
| Past Due Date | supplier chasing | Escalate to FD | Exceptions & Escalation |

**What to do next, by stage:**

- **1. Request and approve**: Site raises it, system checks budget and stock, buyer gets 3 quotes, the right person approves by value.
- **2. Order and receive**: PO counts against budget the day it is issued. Store records what arrived, partial or full, same day.
- **3. Match and pay**: Pay only what was ordered and received. AP matches PO, GRN and invoice, then it joins the next payment run.
- **Exceptions**: Over budget goes to the PM. Bad goods go back. Mismatches wait on hold. Missed due dates go to FD.

## Subcontract Lifecycle
File: `04-subcontract-lifecycle.workflow.json`

| Step | What it covers | Owner / timing | Lane |
|---|---|---|---|
| Package Scope | scope, BOQ, budget | QS | QS & Contracts |
| Sub Quotes | from approved list | Subs · 7 days | Subcontractors |
| Level Bids | scope gaps, rates | QS | QS & Contracts |
| Bond + Insurance | before start | Sub | Subcontractors |
| Award Subcontract | rates, retention, terms | PM + Director | QS & Contracts |
| Advance Paid | against guarantee | AP | Finance & AP |
| Works on Site | daily records | Site Eng | Site Team |
| Sub Variation | instructed change | QS | QS & Contracts |
| Payment Application | monthly claim | Sub · by cut-off | Subcontractors |
| Measure + Verify | qty vs BOQ, quality | Site Eng · 5 days | Site Team |
| Valuation | gross less deductions | QS · 5 days | QS & Contracts |
| Sub Ledger | retention, recoveries | Auto | Finance & AP |
| Payment Certificate | net amount due | PM approves | QS & Contracts |
| Pay Sub | by due date, tax cert | AP · per terms | Finance & AP |

**What to do next, by stage:**

- **1. Tender and award**: Define the package, get quotes from approved subs, level scope gaps, and award within the budget.
- **2. Secure and start**: No start without bond and insurance on file. Advance is paid only against a guarantee.
- **3. Measure and value**: Sub claims monthly. Site verifies quantity and quality. QS values it with approved variations only.
- **4. Certify and pay**: Net = work done less retention, advance recovery, backcharges and tax. Pay by the contract due date.

## Site Execution and Change Control
File: `05-site-and-change-control.workflow.json`

| Step | What it covers | Owner / timing | Lane |
|---|---|---|---|
| Lookahead Plan | 3 weeks by trade | Site Manager · weekly | Site Team |
| Site Instruction | change, RFI answer | Engineer | Client & Engineer |
| Execute Works | own crews + subs | Foreman | Site Team |
| Variation Notice | within notice period | QS · per contract | QS & Controls |
| Daily Diary | labour, plant, weather | Site Eng · daily | Site Team |
| Delay Event | EOT notice, records | PM · per contract | Exceptions & Escalation |
| Price Variation | rates, time impact | QS · 14 days | QS & Controls |
| Inspection | engineer signs IR | Engineer · 24 h | Site Team |
| NCR + Rework | cause, fix, recheck | Site Eng | Exceptions & Escalation |
| Approve VO | signed VO | Engineer | Client & Engineer |
| Progress by BOQ | % done, S-curve | QS · monthly | QS & Controls |
| To Billing | IPC + sub valuations | QS · by cut-off | QS & Controls |

**What to do next, by stage:**

- **1. Plan and build**: Plan three weeks ahead, build, and record labour, plant, weather and delays every day.
- **2. Inspect and record**: Nothing is covered up without a signed inspection. Failed work becomes an NCR and is rechecked.
- **3. Change control**: Every instruction gets a written notice inside the contract period, then a priced VO.
- **4. Delay and billing**: Delays are noticed on time with diary records. Approved progress and VOs go to monthly billing.

## Client Billing and Receivables
File: `06-billing-and-receivables.workflow.json`

| Step | What it covers | Owner / timing | Lane |
|---|---|---|---|
| Monthly Cut-off | progress + VOs | QS · 25th | QS & Billing |
| Draft IPC | work, VOs, materials | QS · 3 days | QS & Billing |
| Internal Review | PM signs off | PM · 2 days | QS & Billing |
| Engineer Assessment | within contract days | Engineer | Client & Engineer |
| Under-certified | query, resubmit | QS · 7 days | Ageing & Disputes |
| Payment Certificate | certified amount | Engineer | Client & Engineer |
| Tax Invoice | on certificate | AR · same day | Finance & AR |
| Due Date Reminder | 7 days before, on due | Auto | Ageing & Disputes |
| Receipt + Match | bank, allocate | AR · on receipt | Finance & AR |
| Overdue Escalation | 30, 60, 90 days | PM, then Director | Ageing & Disputes |

**What to do next, by stage:**

- **1. Prepare the IPC**: At cut-off, value work done, approved VOs and materials on site, less retention and advance recovery.
- **2. Get it certified**: Submit on time. Track the engineer's certification deadline. Query any short-certified item in 7 days.
- **3. Invoice and collect**: Invoice the certified amount the same day. Match every receipt to its invoice and bank line.
- **4. Ageing and follow-up**: Remind 7 days before due and on due. At 30, 60, 90 days overdue, escalate and apply contract remedies.

## Payables, Cash and Ageing
File: `07-payables-and-cash.workflow.json`

| Step | What it covers | Owner / timing | Lane |
|---|---|---|---|
| Supplier Bills | 3-way matched | From P2P | Bills In |
| Sub Certificates | net of deductions | From QS | Bills In |
| Site Expenses | petty cash, limits | Site Admin · weekly | Bills In |
| AP Ledger | due date, tax, cost code | AP · 2 days | Accounts Payable |
| Bill on Hold | missing proof | AP chases | Holds & Shortfalls |
| AP Ageing | due this week, overdue | AP · weekly | Accounts Payable |
| Cash Forecast | 13 weeks, AR vs AP | Finance · weekly | Finance Director / Treasury |
| Payment Proposal | due + priority rules | AP · weekly | Accounts Payable |
| Approve Run | within cash, limits | FD | Finance Director / Treasury |
| Cash Shortfall | defer, fund, chase AR | FD + PM | Holds & Shortfalls |
| Pay + Remit | bank file, tax certs | AP · run day | Accounts Payable |
| Bank Reconcile | post to GL | Accountant · weekly | Finance Director / Treasury |

**What to do next, by stage:**

- **1. Capture every bill**: Matched supplier bills, certified sub payments and site expenses land in one ledger with due dates.
- **2. Age and forecast**: Each week, age what is due and overdue, and forecast 13 weeks of cash with expected client receipts.
- **3. Propose, approve, pay**: AP proposes by due date and priority. FD approves within cash. Pay, send remittance, reconcile bank.
- **Holds and shortfalls**: Bills without proof are held and chased. If cash is short, FD defers, funds, or pushes AR collection.

## Cost Control and Monthly Close
File: `08-cost-control-and-close.workflow.json`

| Step | What it covers | Owner / timing | Lane |
|---|---|---|---|
| Commitments | POs + subcontracts | Auto | Cost + Value Data |
| Actual Cost | GRNs, bills, expenses | Auto | Cost + Value Data |
| Cost Report | budget vs committed | QS · monthly | QS & Cost Control |
| Value Earned | certified + unbilled | From billing | Cost + Value Data |
| Cost-Value Check | CVR, margin to date | QS · 5th | QS & Cost Control |
| Month-End Close | accruals, WIP, P&L | Accountant · 7th | Finance & Close |
| Forecast Final Cost | cost to complete | QS + PM | QS & Cost Control |
| Overrun Alert | code over budget | Auto | Management |
| Monthly Review | margin, cash, risk | Directors · 10th | Management |
| Corrective Actions | owner + due date | PM | Management |

**What to do next, by stage:**

- **1. Collect the numbers**: Commitments count when approved. Actuals from GRNs and bills. Value from certified and unbilled work.
- **2. Cost vs value**: By cost code: budget, committed, actual, forecast. Compare cost to value earned to see real margin.
- **3. Close the month**: Book accruals for received but unbilled goods, and WIP, so the P&L that goes to review is complete.
- **4. Review and act**: Overruns alert as soon as they are committed. Each review ends with actions, an owner and a date.

## Deadlines and Reminders
File: `09-deadlines-and-reminders.workflow.json`

| Step | What it covers | Owner / timing | Lane |
|---|---|---|---|
| Every Dated Record | IPC, bill, bond, VO, NCR | All modules | Dated Records |
| Deadline Register | owner, due, next step | Auto | Deadline Register |
| Daily Sweep | approaching, due, late | Auto · daily | Deadline Register |
| Notify Owner | the next step to take | Auto | Record Owner |
| Owner Acts | do it, attach proof | Owner | Record Owner |
| Escalate | late past 3 days | PM, then Director | Escalation |
| Closed | time-stamped | Auto | Record Owner |
| Weekly Digest | open items by owner | Auto · Monday | Escalation |

**What to do next, by stage:**

- **1. Every date has an owner**: Any record with a date (IPC, bill, bond, VO notice, NCR) enters the register with an owner and a next step.
- **2. Daily sweep**: Each day the system flags what is approaching, due, or late, and tells the owner exactly what to do next.
- **3. Act and close**: The owner does the step and attaches proof. The item closes with a time stamp.
- **4. Escalate**: Late for 3 days goes to the PM, then the Director. Monday digest lists open items by owner.

## Completion and Financial Close
File: `10-completion-and-closeout.workflow.json`

| Step | What it covers | Owner / timing | Lane |
|---|---|---|---|
| Practical Completion | notice to engineer | PM | Site & Project Team |
| Snag + Commission | tests, O&M, as-builts | PM · 14 days | Site & Project Team |
| Taking-Over Cert | DLP starts | Engineer | Client & Engineer |
| Retention Claim 1 | first half from client | QS · 7 days | QS & Contracts |
| Sub Retention 1 | release first half | AP | Finance & Accounts |
| Defects Period | fix notified defects | PM · per notice | Site & Project Team |
| Defects Certificate | end of DLP | Engineer | Client & Engineer |
| Final Account | VOs, claims, retention 2 | QS · per contract | QS & Contracts |
| Sub Final Accounts | agree + release | QS | QS & Contracts |
| Close Project | bonds back, codes shut | Finance | Finance & Accounts |

**What to do next, by stage:**

- **1. Complete and hand over**: Give completion notice, clear snags, commission, hand over O&M and as-builts, get the taking-over certificate.
- **2. First half retention**: Claim the first half of retention from the client. Release the first half to subs whose work is accepted.
- **3. Defects period**: Fix each notified defect within the notice period. At DLP end, get the defects certificate.
- **4. Final accounts and close**: Agree the client final account and every sub final account, release retention 2, recover bonds, close codes.

## Reminder and Escalation Rules

Feed these into the deadline register (diagram 09). Each rule notifies the owner first, then escalates after 3 days late.

| Trigger | Reminder | Owner | Escalate to |
|---|---|---|---|
| Bid submission date | 7 and 2 days before | BD | Directors |
| Tender query deadline | 3 days before | Estimator | BD Head |
| RFQ unanswered | 5 days after sending | Buyer / Estimator | Procurement lead |
| Bond or insurance expiry | 30 and 7 days before | Finance | FD |
| PO past delivery date | on the day | Buyer | PM |
| Invoice unmatched | 3 days after receipt | AP | Finance lead |
| Supplier or sub bill due | 7 days before | AP | FD |
| Sub application not valued | 5 days after receipt | QS | PM |
| Monthly IPC cut-off | 3 days before | QS | PM |
| Engineer certificate due | on the contract day | QS | PM, then Director |
| Client payment due | 7 days before, on due | AR | PM |
| Client payment overdue | 30, 60, 90 days | AR | PM, then Director |
| Variation notice window | half-way, 2 days before | QS | PM |
| EOT notice window | half-way, 2 days before | PM | Director |
| NCR open | 7 days after raised | Site Eng | PM |
| Cost code over 90% committed | on commit | QS | PM |
| Defect notice open | per notice period | PM | Director |
| DLP end / retention release | 30 days before | QS | PM |
| Final account submission | 30 days before | QS | Director |
