# Current Study State

**State version:** 6.0-WORKBENCH-LEARNER-API-2026-10-23
**Last verified:** 2026-10-23 (GitHub project/docs inspected; laptop runtime is unverified)
**Status:** ACTIVE — accelerated seven-day study sprint on the Workbench learner branch
**Execution mode:** BATCH-FIRST / CODE-FIRST / LEARNER-WRITES-TESTS / EVIDENCE-BASED

## Position
- Day: 2
- Hour: 10
- Current topic: API testing strategy and test-case design — next: implement the first Workbench API test batch
- Project: Workbench QA Lab (primary system under test)
- Application repository: https://github.com/MFadelRep/QA-practice-platform-app
- Required branch: learn/rag-unit-tests (historically named for the first RAG exercise; now the general learner branch)
- Local project path: not yet confirmed; the user will set up the learner branch on the laptop

The hour number is a curriculum locator, not proof of mastery. The 45-hour catalogue remains required scope; related capabilities are integrated across the accelerated seven-day sequence.

## Current checkpoint
The previous Playwright foundation/architecture work in the separate local project `/run/media/mfadel/New Volume/Projects/QA/automation-platform` is recorded as complete through Day 1 / Hour 6. Evidence from 2026-10-19: 15 Playwright UI tests passed in three consecutive two-worker runs (45/45 total), with TypeScript validation passing. Do not restart those completed exercises by default.

The learning vehicle has now changed to Workbench QA Lab because the user explicitly wants a controlled website/API/database they own and can use as the system under test. The app repository already contains the implemented React/Vite UI, NestJS API, PostgreSQL schema/seed data, authentication/RBAC, tenant-scoped workspaces, collaboration, notifications, audit, deterministic RAG, fault lab, observability and OpenAPI docs.

The learner branch is separate from `main`. `main` retains the completed assistant-authored tests as reference. On `learn/rag-unit-tests`, completed automated test implementations were replaced with TODO exercises or skipped Playwright placeholders, and ready-made RAG evaluation, mutation-testing configuration, and k6 workload scripts were removed for later learner-authored exercises. TODO/skipped output is not functional coverage.

## Verified versus unverified
- **Verified before this learning-branch conversion:** the remote `main` branch had a passing CI run for its completed generated test suite.
- **Verified by repository inspection on 2026-10-23:** the learner branch exists; application source is retained; test files contain learner TODOs or Playwright skips; study/setup guides are present.
- **Not verified:** the learner branch's post-conversion CI, local Docker/browser startup, database migration/seed, local tests, and exact laptop checkout/path.
- Do not describe TODO/skipped tests as passing feature coverage. Re-check current GitHub Actions and the user's local output before reporting a result as verified.

## Project and environment constraints
- Use Workbench QA Lab as the primary SUT for API, SQL, browser integration, CI, performance, fault handling, observability, RAG/security, and capstone exercises.
- The local app repository is separate from `MFadelRep/QA-study-planner` and from the older `/run/media/mfadel/New Volume/Projects/QA/automation-platform` and `/run/media/mfadel/New Volume/playwright-course` directories.
- Never assume a local path, clean worktree, current branch, or Docker state. Inspect before switching branches or editing; preserve local changes.
- Do not merge the learning branch into `main` wholesale. `main` is the reference baseline.
- Keep services bound to loopback; demo accounts are fictional and local-only; don't expose the app/database to the LAN or public internet.
- Test implementations are learner-owned for this plan. Coach with requirements, case-design prompts, progressive hints, code review and actual failure diagnosis; do not write the complete exercise before the user attempts it.

## Exact next action
When the user types `STUDY` in a new chat, read this live state and the Workbench `STUDY_GUIDE.md`, then resume Day 2 API testing without asking the user to restate the goal. Since laptop setup may have happened after this checkpoint, first verify the local checkout with one grouped diagnostic: `git status --short`, `git branch --show-current`, `git log -1 --oneline`, `node --version`, `npm --version`, and `docker compose version`. If setup has not been done, guide the user using the clone/setup steps in Workbench `STUDY_GUIDE.md`; do not overwrite an existing folder or local changes.

Once on the learner branch with Workbench running, open `http://127.0.0.1:3000/api/docs` and begin `docs/practice/api-testing-exercise.md`. The first coding target is `apps/api/test/projects-work-items.e2e-spec.ts`: the user should replace a small pair of TODOs with executable tests for a successful authenticated project creation and a meaningful validation failure, check the response body, then verify persisted state through a follow-up GET or database check. The assistant should challenge expected results and review/debug the user's attempt, not paste a completed test suite. Run the relevant API e2e command and typecheck based on actual local output before expanding to auth/RBAC, boundaries, contracts, UI/API hybrid testing, and SQL.
