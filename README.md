# Contractor Operations Workflows (Archify)

Eleven Archify workflow diagrams for a general contractor, from inquiry to financial close. Built from the Impala Developers ERP proposal (17 modules) and the OpenConstructionERP module catalogue (procurement, subcontractors, contracts, finance, CVR, payment clock, withholding tax, deadlines, closeout, defects liability).

| # | Diagram | Covers |
|---|---|---|
| 00 | Overview | Inquiry to close, money in and money out |
| 01 | Win the Work | Go/no-go, takeoff, RFQs, bid review, award |
| 02 | Contract Setup and Budget | Contract register, bonds, advance, cost budget, programme, cash forecast |
| 03 | Procure to Pay | Request, budget + stock check, quotes, PO, GRN, 3-way match, payment |
| 04 | Subcontract Lifecycle | Package, award, bond, advance, application, measure, valuation, certificate, pay |
| 05 | Site Execution and Change Control | Lookahead, diary, inspection, NCR, variations, delay events |
| 06 | Client Billing and Receivables | IPC, certification, invoice, receipt, reminders, ageing, escalation |
| 07 | Payables, Cash and Ageing | AP ledger, ageing, 13-week cash forecast, payment run, bank reconciliation |
| 08 | Cost Control and Monthly Close | Commitments, actuals, CVR, forecast final cost, month-end, review |
| 09 | Deadlines and Reminders | The engine that tells each owner what to do next, and escalates |
| 10 | Completion and Financial Close | Taking-over, retention, defects period, final accounts, close |

## How "what to do next" works
- **Node tags** show the owner and timing (for example `QS · 5 days`). Zoom in or open a guided view to see them.
- **Guided views** (4 per diagram) walk through each stage with the next action in one line.
- **Cards** under each diagram list the controls, next actions and ageing rules.
- **NEXT-ACTIONS.md** lists every step with its owner, plus the reminder and escalation rules for the deadline register.

## Files
- `*.workflow.json`: Archify source (schema v2, showcase quality)
- `*.html`: rendered, self-contained diagrams. Open in any browser.
- `build/`: Python scripts that generate the JSON (`lib.py` has the helpers)

## Re-render
```bash
git clone https://github.com/tt-a1i/archify.git && cd archify
node archify/bin/archify.mjs validate workflow 03-procure-to-pay.workflow.json --quality showcase
node archify/bin/archify.mjs deliver  workflow 03-procure-to-pay.workflow.json 03-procure-to-pay.html --quality showcase
```

## Layout limits learned
- Max 6 columns (0-5) and 4 lanes per diagram to fit a 1440x900 screen.
- Keep card lines under about 30 characters so cards stay on one line.
- Same-column links between lanes: use `route: straight` with bottom/top sides and no label.
