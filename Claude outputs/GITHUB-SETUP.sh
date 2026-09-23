#!/bin/bash

# const-flow GitHub Setup Script
# Run this after creating an empty GitHub repo

# Change to the const-flow directory
cd const-flow

# Initialize git (if not already done)
git init

# Add all files
git add .

# Initial commit
git commit -m "Initial const-flow deployment

- All 10 contractor workflow diagrams
- Navigation hub and supporting files
- Ready for Cloudflare Pages deployment"

# Set the remote (replace YOUR-USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR-USERNAME/const-flow.git

# Set main as default branch
git branch -M main

# Push to GitHub
git push -u origin main

echo "✓ Push complete. Your repo is ready for Cloudflare Pages connection."
echo "Next: Log in to Cloudflare and connect this repo via Pages."
