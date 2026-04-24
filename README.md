# CI/CD ML Project

## Project
This project trains a Random Forest model on the Iris dataset and deploys a report using GitHub Actions.

## CI
The CI workflow runs on every push.  
It installs dependencies, runs tests, trains the model, generates metrics, and creates an HTML report.

## CD
The CD workflow deploys the generated HTML report to GitHub Pages so it can be viewed in the browser.

## Issue Faced
GitHub Pages initially returned 404 because the wrong folder was deployed.  
I fixed the workflow to deploy the docs folder correctly.

