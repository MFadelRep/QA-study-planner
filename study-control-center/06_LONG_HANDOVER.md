# LONG HANDOVER — CURRENT RECORD

Derived record, not authoritative.

Canonical state version: 6.2-WORKBENCH-LOCAL-API-2026-10-24
Position: Day 2 / Hour 10
Topic: API testing strategy — authenticated project creation and validation.

## Learning rules
Workbench QA Lab is the primary controlled SUT in MFadelRep/QA-practice-platform-app. The learner branch is learn/rag-unit-tests; main retains completed reference tests. Do not merge the learner branch wholesale. The user authors test implementations; guide with scenario design, progressive hints, review and debugging rather than pasting a finished suite before an attempt. TODO/skipped checks are not functional coverage. Protect study time and prefer practical results over extra scaffolding.

## Previously completed
The separate /run/media/mfadel/New Volume/Projects/QA/automation-platform project completed Day 1 / Hour 6 on 2026-10-19: 15 Playwright UI tests passed in three consecutive two-worker runs (45/45 combined) and TypeScript validation passed. Do not restart by default. It is not the Workbench repository.

## Workbench evidence
- Reported local checkout: /home/mfadel/QA-practice-platform-app.
- Reported branch and commit: learn/rag-unit-tests, 5afe645 (docs: clarify learner coverage and remove whitespace failure).
- User-reported request to http://127.0.0.1:3000/api/health/ready returned HTTP 200 with status ok, service workbench-api, database ready.
- This proves an API answering on port 3000 reported database readiness at that moment. It does not prove which checkout launched it, frontend availability, or local migration/test results.
- git status --short output was not provided; do not claim a clean worktree. Node/npm/Docker versions, frontend, migrations, seed, typecheck and local tests remain unconfirmed.
- Learner-branch CI run 39952194483 passed on 5afe645612b93b3af0840144265ede8f936e2d9e. It validates scaffold/build/runner execution, not TODO feature coverage.

## Startup
Root npm run dev starts API and web together. For the existing checkout, preserve local changes and confirm .env targets the intended local Workbench database, then run:

    cd "/home/mfadel/QA-practice-platform-app" || exit 1
    npm run db:up
    npm run dev

Keep dev running. Verify API readiness from a second terminal with:

    curl -sS -i --max-time 5 http://127.0.0.1:3000/api/health/ready

Expected HTTP 200 and database ready. UI configured URL: http://localhost:5173 (not independently confirmed reachable). API docs: http://127.0.0.1:3000/api/docs. Node.js 22.12+ and Docker Compose are required. If setup is missing, consult the app STUDY_GUIDE.md; do not overwrite an existing checkout or .env. Never run npm run db:reset unless .env is confirmed to point to a disposable local database.

## Resume sequence for STUDY
1. Read study-control-center/01_CURRENT_STATE.md and 04_CONTINUITY_RULES.md in the study planner.
2. Read the app STUDY_GUIDE.md and docs/practice/api-testing-exercise.md on learn/rag-unit-tests.
3. Before edits or branch operations, check git status --short, git branch --show-current, and git log -1 --oneline. Preserve local changes and do not assume GitHub changes are synced locally.
4. If app is not running, check local environment and .env, then use the startup commands above. Do not launch separate API/web processes without evidence they are needed.
5. Inspect the actual project API implementation/docs for authentication, request fields, response contract, validation and persistence.
6. First learner-authored batch in apps/api/test/projects-work-items.e2e-spec.ts: successful authenticated project creation and a meaningful missing/invalid-field validation failure. Assert response body and verify persistence with follow-up GET or database check.
7. The other TODOs cover retrieval/listing, unauthenticated access, work-item creation, cross-workspace isolation, update/delete permissions, boundaries and unexpected properties.
8. Run focused API e2e tests and typecheck based on actual output. Separate failures, skips and TODOs. Update the live checkpoint only after real execution. Continue with auth/RBAC, contracts, UI/API hybrid flows, SQL/PostgreSQL, CI/CD, performance, Docker, Kubernetes, RAG/security, MLOps and senior-QA integration in curriculum order.

## Boundaries
Keep the app repository separate from QA-study-planner, automation-platform and playwright-course. Keep services loopback-only and use fictional local data; do not expose the app/database to the LAN or public internet. Live progress belongs only in 01_CURRENT_STATE.md; this handover is derived and cannot override it.
