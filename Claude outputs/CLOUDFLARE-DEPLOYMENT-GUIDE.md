# Deploying const-flow.q-sols.com to Cloudflare Pages

## What We Have Ready
Your const-flow project is prepared and ready to deploy. All contractor workflow files are included along with a minimal Cloudflare configuration.

## Deployment Steps

### 1. Create a GitHub Repository

Since Cloudflare Pages deploys from Git, you need to push this project to GitHub first.

Option A: Create a new repo on GitHub called `const-flow` and push these files:
```bash
cd const-flow
git init
git add .
git commit -m "Initial deployment of const-flow workflows"
git remote add origin https://github.com/[YOUR-USERNAME]/const-flow.git
git branch -M main
git push -u origin main
```

Option B: Add it as a new directory in an existing Q-Solutions repo.

### 2. Connect to Cloudflare Pages

1. Log in to your Cloudflare account (Qasimshabbir@gmail.com)
2. Go to **Workers & Pages → Create application → Pages → Connect to Git**
3. Select your GitHub account and the `const-flow` repository
4. Fill in these settings:
   - **Production branch:** main
   - **Build command:** (leave empty — this is static HTML, no build needed)
   - **Build output directory:** / (root directory)
   - **Root directory:** (leave empty)

5. Click **Save and Deploy**

### 3. Add the Custom Domain

Once deployed:

1. Go to the new **const-flow** Pages project
2. Navigate to **Custom domains**
3. Click **Set up custom domain**
4. Enter: `const-flow.q-sols.com`
5. Cloudflare will automatically create the DNS record and provision SSL
6. Wait for status to show **Active** with SSL enabled

### 4. Verify the Deployment

- The site should be live at https://const-flow.q-sols.com
- All workflow HTML files and diagrams should load correctly
- Share the link with your client

## File Structure

```
const-flow/
├── index.html                    # Navigation hub
├── 00-overview.html              # Project overview diagram
├── 01-win-the-work.html          # Winning work workflows
├── 02-contract-setup.html        # Contract setup flows
├── 03-procure-to-pay.html        # Procurement workflows
├── 04-subcontract-lifecycle.html # Subcontractor management
├── 05-site-and-change-control.html  # Site operations
├── 06-billing-and-receivables.html  # Billing workflows
├── 07-payables-and-cash.html     # Payment flows
├── 08-cost-control-and-close.html   # Cost management
├── 09-deadlines-and-reminders.html  # Timeline management
├── 10-completion-and-closeout.html  # Project closeout
├── *.workflow.json               # Workflow data files
├── package.json                  # Project metadata
├── wrangler.toml                 # Cloudflare config
├── .gitignore                    # Git ignore rules
├── README.md                     # Original documentation
└── NEXT-ACTIONS.md              # Next steps
```

## Important Notes

- **No build step required.** This is pure static HTML, so Cloudflare will serve it directly.
- **DNS already hosted on Cloudflare.** Since q-sols.com is already on Cloudflare, adding the subdomain is just a few clicks — no need to modify DNS elsewhere.
- **SSL is automatic.** The custom domain setup includes free SSL certificate provisioning.
- **All files included.** Every HTML diagram and workflow JSON file is in the deployment.

## What the Client Sees

Your client can access all contractor operation workflows at `const-flow.q-sols.com`. The index page provides navigation to each of the 10 workflow diagrams covering the full project lifecycle.

## Next Steps After Deployment

1. Test the site in a browser
2. Verify all links and diagrams load correctly
3. Share the URL with your client
4. Monitor Cloudflare dashboard for any issues

## Troubleshooting

- **404 on subdomain?** Wait a few minutes for DNS/SSL provisioning to complete
- **Blank pages?** Check browser console for any loading errors
- **Need updates?** Push changes to the GitHub repo — Cloudflare will auto-deploy

Questions? Check your Cloudflare dashboard under the const-flow Pages project for deployment logs.
