# LONG HANDOVER — CURRENT RECORD

**Derived record — not authoritative.**
Canonical state version: 6.1-WORKBENCH-LEARNER-CI-2026-10-23
**Position:** Day 2 / Hour 10
**Topic:** API testing strategy and test-case design — next: implement the first Workbench API test batch

## Goal and learning rules
The goal is broad, practical Senior QA Automation + MLOps coverage across the accelerated seven-day plan. Workbench QA Lab is now the primary controlled SUT because the user specifically wants to practise against a website/API/database they own rather than be limited by a public practice site.

The application is in MFadelRep/QA-practice-platform-app, learner branch learn/rag-unit-tests. main preserves the completed assistant-authored tests and finished evaluation/load-test tooling as a reference. The learner branch retains application code but deliberately replaces completed automated test implementations with TODO/skipped placeholders; ready-made RAG evaluation and mutation-testing runner/config plus k6 workload scripts were removed so the user can implement them during their curriculum topics. Never merge this learner branch wholesale into main.

The user is supposed to write their own automation tests. The assistant should define the SUT contract, clarify scenario objectives and expected behavior, challenge gaps, give progressive hints, review user-written tests, and diagnose actual output. Do not paste complete test implementations before the user attempts the exercise. A passing command with TODO/skipped tests does not demonstrate feature coverage.

## What was previously completed
In the separate local project at /run/media/mfadel/New Volume/Projects/QA/automation-platform, Day 1 / Hour 6 was recorded as complete on 2026-10-19: 15 Playwright UI tests passed three consecutive parallel runs (45/45 combined) and TypeScript validation passed. Avoid restarting that work by default. This is not the Workbench repo.

## Workbench local setup status
The learner branch and documentation were inspected/updated on GitHub on 2026-10-23. The laptop checkout path, current branch, Docker/browser startup and database migration/seed remain unknown until the user sets up and runs the project locally. Latest learner-branch CI run 39952194483 passed typecheck, build, the configured test runners, API/database suite, contract/browser runner commands, formatting and secret scan; however, the tests are TODO/skipped exercises, so this is scaffold/build validation rather than feature coverage.

The repository's STUDY_GUIDE.md documents fresh-clone commands, app URLs, safety boundaries and the branch rule. Swagger is at http://127.0.0.1:3000/api/docs when the app is running. The app is for loopback/local use with fictional seeded data; do not expose it to a public network and verify .env before any database reset.

## Verified versus unverified
- Verified before conversion: remote main had a passing CI run for the completed generated test suite.
- Verified by GitHub inspection: the learner branch contains the application source, TODO test scaffolds and study documentation.
- Verified: learner-branch CI run 39952194483 passed with the learner scaffolds.
- Not verified: local npm commands, Docker startup, schema/seed application and app runtime.
- Keep those distinctions explicit in all future checkpoints.

## Exact resume action
When the user types STUDY in a new chat:
1. Read study-control-center/01_CURRENT_STATE.md and apply study-control-center/04_CONTINUITY_RULES.md.
2. Read STUDY_GUIDE.md and docs/practice/api-testing-exercise.md on learner branch learn/rag-unit-tests.
3. Verify the local checkout using a grouped read-only diagnostic: git status --short, git branch --show-current, git log -1 --oneline, node --version, npm --version and docker compose version. Preserve local changes and don't assume a path.
4. If the user hasn't set up Workbench, guide them through STUDY_GUIDE.md without replacing an existing directory. Once local app is running, inspect Swagger and begin Day 2 API testing.
5. User's first coding batch is apps/api/test/projects-work-items.e2e-spec.ts: write an authenticated successful project-creation test and an invalid/missing-required-field test, assert the response contract and verify persisted state with a follow-up GET/database check. The current file contains TODO descriptions only. Give hints and code review after their attempt; do not paste a complete finished suite.
6. Run the relevant API end-to-end command and typecheck based on actual user output. Then continue with authentication/RBAC, boundary/contract cases, UI/API hybrid flows, SQL/PostgreSQL, GitHub Actions/GitLab CI, performance, Docker/Compose, Kubernetes, RAG/security, MLOps and Day 7 integration/senior-QA practice in the master-plan sequence.

## Source of truth
The live checkpoint is study-control-center/01_CURRENT_STATE.md. This handover is derived and cannot override it.
