# Current Study State

**State version:** 3.8-PRACTICE-TARGET-CHECKPOINT
**Last verified:** 2026-10-10
**Checkpoint:** SAVED — passing async test/type-check re-verified; Toolshop selected as default practice SUT
**Status:** ACTIVE — Day 1 / Hour 1 in progress
**Execution mode:** PROJECT-FIRST / FAST-PACE

## Position
- Day: 1
- Hour: 1
- Curriculum area: Programming + Terminal + Git Survival
- Current topic: TypeScript asynchronous test flow — Promise, async/await
- Project: AI QA Platform

## Verified project state
- Local Git repository initialized.
- Branch: main
- Initial root commit: `f2e8917`
- Commit message: `chore: initialize AI QA platform project`
- Repository was verified clean after the root commit.
- `.gitignore` exists and correctly ignores `node_modules/`.
- `src/` and `tests/` directories were created.
- `tsconfig.json` was created.
- `npx tsc --noEmit` passed after adding the TypeScript input.
- TS18003 was resolved by creating `src/index.ts`.
- `src/index.ts` contains the typed `TestResult` model and typed `reportResult(result: TestResult): void` reporter.
- Added `runLoginTest(): Promise<TestResult>` and `main(): Promise<void>`; `main()` awaits the login test and reports its resolved result.
- Removed the old synchronous `loginTest` object and `reportResult(loginTest)` call to prevent duplicate output.
- On 2026-10-10, the user ran `npx tsx src/index.ts` after implementing async/await; actual output was `Starting AI QA Platform` and `Login test: PASSED` exactly once.
- The user then ran `npx tsc --noEmit`; it produced no errors/output.
- The user deliberately changed the password to `WrongPassword!` and confirmed the simulated login reports `Login test: FAILED`.
- `main()` now throws an error when a result fails; the user observed the error stack and explicitly printed `Exit code: 1` immediately after the test command.
- After the deliberate failure/exit-code experiment, the user restored the expected password and confirmed the login test passed again. The TypeScript check also passed without reported errors.

## Latest verified result / blocker
- The user restored the expected password and confirmed the program passed.
- The user also ran the TypeScript check; it passed without reported errors/output.
- The simulated test's failure path and exit code 1 had previously been verified.
- Decision: use Practice Software Testing — Toolshop as the default external system under test for both UI and documented REST API automation. Secondary-site use cases are recorded in `04_CONTINUITY_RULES.md`.

## Exact next action
Open https://practicesoftwaretesting.com/ in Firefox and confirm the site loads and its UI is suitable. Then begin setting up the project for Playwright UI + API tests against Toolshop, checking existing files/dependencies first and avoiding duplicate setup. Do not build our own test application yet. Keep explanations short, realistic, and project-first; explain commands before use and verify actual output.

## Resume constraints
- Do not restart Git initialization, Git identity setup, or the successful initial commit.
- Do not return to the old standalone course directory.
- Do not assume a command succeeded without actual output.
- User wants every terminal command line and important syntax explained before execution.
- User explicitly requests fast pace: avoid unnecessary repetition while retaining one-action-per-turn and actual-output verification.
- The local AI QA Platform repository will be pushed to a separate GitHub repository. The GitHub repository containing this control center is for **study progress management only** and must not be used as the local project remote.
- The study-control repository is `MFadelRep/QA-study-planner` and is authoritative for study progress. Library copies are fallback/legacy only.
- For checkpoint writes: freshly read the file and SHA, preserve content with minimal edits, write using the current SHA, then read back and verify. If the Contents API write is blocked, use the lower-level Git blob/tree/commit/ref workflow with the current branch head and expected SHA.

## Longer-term project intent
Build one portfolio-grade AI QA Platform covering TypeScript, Playwright UI/API/fixtures/auth/network, PostgreSQL, CI/CD, performance testing, Docker, Kubernetes, AI/RAG evaluation, inference testing, security, and MLOps/MLflow.
