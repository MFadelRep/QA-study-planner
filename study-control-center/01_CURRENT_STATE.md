# Current Study State

**State version:** 6.2-WORKBENCH-LOCAL-API-2026-10-24
**Last verified:** 2026-10-24 (user-reported local checkout and API readiness)
**Status:** ACTIVE — accelerated seven-day study sprint
**Execution mode:** BATCH-FIRST / CODE-FIRST / LEARNER-WRITES-TESTS / EVIDENCE-BASED

## Position
- Day 2 / Hour 10
- Topic: API testing strategy and test-case design; first tests are authenticated project creation and validation failure.
- Primary SUT: Workbench QA Lab
- App repository: https://github.com/MFadelRep/QA-practice-platform-app
- Required branch: learn/rag-unit-tests
- Reported local checkout: `/home/mfadel/QA-practice-platform-app`
- Last reported branch/commit: `learn/rag-unit-tests` at `5afe645` (`docs: clarify learner coverage and remove whitespace failure`)

The hour is a curriculum locator, not proof of mastery. The 45-hour catalogue remains required scope.

## Checkpoint
The separate `/run/media/mfadel/New Volume/Projects/QA/automation-platform` project is complete through Day 1 / Hour 6: 15 Playwright UI tests passed in three consecutive two-worker runs (45/45 total), and TypeScript validation passed. Do not restart this by default.

Workbench QA Lab is the primary controlled website/API/database for practice. `main` retains completed reference tests; learner branch `learn/rag-unit-tests` deliberately contains TODO/skipped exercises. TODO/skipped output is not feature coverage.

## Verified versus unverified
- GitHub inspection confirmed the learner branch, `STUDY_GUIDE.md`, and eight TODOs in `apps/api/test/projects-work-items.e2e-spec.ts`.
- Learner-branch CI run 39952194483 passed on commit `5afe645612b93b3af0840144265ede8f936e2d9e`. This validates scaffold/build/runner execution, not functional coverage of TODOs.
- User terminal reported checkout path, branch and commit above. Request to `http://127.0.0.1:3000/api/health/ready` returned HTTP 200 with `{"status":"ok","service":"workbench-api","database":"ready"}`.
- The readiness response proves an API on port 3000 reported database readiness at that moment. It does not prove the process came from this checkout, the frontend works, or migrations/tests passed locally.
- `git status --short` output, Node/npm/Docker versions, frontend availability, migrations, seed, typecheck and local tests remain unconfirmed. Never claim the worktree is clean or local tests passed without evidence.

## Local startup and URLs
Root `npm run dev` starts API and web together. For the existing checkout, after preserving local changes and confirming `.env` targets the intended local Workbench database:
```bash
cd "/home/mfadel/QA-practice-platform-app" || exit 1
npm run db:up
npm run dev
```
Keep the dev command running. Verify from another terminal:
```bash
curl -sS -i --max-time 5 http://127.0.0.1:3000/api/health/ready
```
Expected HTTP 200 and `"database":"ready"`. Do not blindly rerun setup or overwrite `.env`.
- UI: http://localhost:5173 (configured URL; not independently verified reachable)
- API: http://127.0.0.1:3000
- API docs: http://127.0.0.1:3000/api/docs
- Node.js 22.12+ and Docker Compose are required.
- Never run `npm run db:reset` unless `.env` is confirmed to point to a disposable local Workbench database. Use app `STUDY_GUIDE.md` for fresh setup only if needed.

## Exact next action for STUDY
1. Read this state, `04_CONTINUITY_RULES.md`, app `STUDY_GUIDE.md`, and `docs/practice/api-testing-exercise.md` on `learn/rag-unit-tests`.
2. Preserve local work; check `git status --short`, `git branch --show-current`, and `git log -1 --oneline` before edits or branch operations.
3. Inspect the real project API implementation/docs for request fields, authentication, response contract, validation and persistence.
4. In `apps/api/test/projects-work-items.e2e-spec.ts`, first implement two learner-authored tests: successful authenticated project creation, and one meaningful missing/invalid-field validation failure. Assert the response contract and verify persistence with a follow-up GET or database check.
5. The other TODOs cover retrieval/listing, unauthenticated access, work-item creation, cross-workspace isolation, update/delete permissions, boundaries and unexpected properties.
6. Run focused API e2e tests and typecheck based on actual output. Coach with design, hints, review and debugging; do not paste a completed suite. Record progress only after real execution.

## Constraints
- Keep Workbench separate from the study planner and older `automation-platform` / `playwright-course` projects.
- Do not assume a clean worktree or synced remote changes; preserve local edits.
- Do not merge the learner branch into `main` wholesale.
- Keep services loopback-only and use fictional local data; do not expose the app/database to the LAN or internet.
- Protect study time: practical outcomes over unnecessary scaffolding.
