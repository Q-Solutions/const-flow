# const-flow Deployment Checklist

## Pre-Deployment (Cloudflare)
- [ ] Logged in to Cloudflare as Qasimshabbir@gmail.com
- [ ] Account ID verified: 8d3b7b750509cbb059e5cff5b0f91cab
- [ ] q-sols.com DNS confirmed on Cloudflare (already migrated from SiteGround)

## GitHub Setup
- [ ] Created new GitHub repo (or chose existing repo/branch)
- [ ] Pushed const-flow files to GitHub
- [ ] Repository is public or accessible to Cloudflare GitHub app

## Cloudflare Pages Configuration
- [ ] Navigated to Workers & Pages → Create application
- [ ] Selected Pages → Connect to Git
- [ ] Authorized GitHub access
- [ ] Selected correct repository: `const-flow`
- [ ] Set production branch to `main`
- [ ] Left build command empty (no build needed)
- [ ] Set build output directory to `/` (root)
- [ ] Left root directory empty
- [ ] Clicked "Save and Deploy"
- [ ] Deployment shows "Success" status

## Custom Domain Setup
- [ ] Navigated to const-flow Pages project
- [ ] Clicked Custom domains
- [ ] Clicked "Set up custom domain"
- [ ] Entered: `const-flow.q-sols.com`
- [ ] Waited for DNS record auto-creation
- [ ] Confirmed status: Active with SSL enabled

## Verification
- [ ] Opened https://const-flow.q-sols.com in browser
- [ ] Index page loads correctly
- [ ] Navigation menu visible
- [ ] Clicked through 2-3 workflow diagrams to confirm they load
- [ ] SSL certificate working (green lock icon in browser)
- [ ] Responsive design works on mobile

## Client Sharing
- [ ] Copied deployment URL
- [ ] Verified all content loads before sharing
- [ ] Sent https://const-flow.q-sols.com to client
- [ ] Provided brief explanation of project

## Post-Deployment
- [ ] Saved GitHub repo URL for future updates
- [ ] Documented any custom environment variables (none needed for static site)
- [ ] Noted that updates auto-deploy when pushing to main branch

---

**Estimated Time:** 10-15 minutes

**Support:** Check Cloudflare Pages project dashboard → Deployments tab for build logs if issues occur
