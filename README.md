# CI/CD Pipeline — Containerized App on ECS Fargate

An automated pipeline that takes a code push to GitHub and ships it to production with zero manual steps.

**Flow:** GitHub → AWS CodePipeline → CodeBuild (build Docker image → push to ECR) → ECS Fargate (rolling deploy)

## Stack
- **Source:** GitHub (via CodeConnections)
- **Build:** AWS CodeBuild + `buildspec.yml`
- **Registry:** Amazon ECR
- **Compute:** Amazon ECS on Fargate (serverless containers)
- **Orchestration:** AWS CodePipeline
- **App:** Python Flask, returns a version string to demo live deploys
- **Region:** us-east-2 (Ohio) · Built entirely in the AWS Console

## What it demonstrates
Push a commit → the pipeline auto-builds a new image, pushes it to ECR, and rolls it out to ECS with no downtime. Bump the app version, commit, and watch it flip live.
