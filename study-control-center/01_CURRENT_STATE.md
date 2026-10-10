# Current Study State

**State version:** 4.2-TOOLSHOP-TITLE-ASSERTION-PASS
**Last verified:** 2026-10-10
**Checkpoint:** SAVED — named Chromium Playwright smoke test with an exact page-title assertion passed; TypeScript check produced no errors; validator fix remains verified
**Status:** ACTIVE — Day 1 / Hour 1 in progress
**Execution mode:** PROJECT-FIRST / FAST-PACE

## Position
- Day: 1
- Hour: 1
- Curriculum area: Programming + Terminal + Git Survival
- Current topic: TypeScript asynchronous test flow — Promise, async/await; first real Playwright UI smoke test
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
- On 2026-10-10, the user confirmed Toolshop loads in Firefox.
- Installed local dev dependency `@playwright/test@1.63.0`; `npm ls --depth=0` showed it alongside TypeScript `7.0.2`, and `npx playwright --version` reported `1.63.0`.
- `npx playwright install --list` found Chromium, Firefox, and WebKit browser binaries in `~/.cache/ms-playwright/`; no browser download was needed.
- Created `tests/toolshop.spec.ts` with homepage HTTP 200 and visible-body checks; strengthened it with `await expect(page).toHaveTitle('Practice Software Testing - Toolshop - v5.0')` based on the actual observed title.
- Running `npx playwright test tests/toolshop.spec.ts` without a named project passed: `1 passed (3.7s)`.
- Created `playwright.config.ts` with `testDir: './tests'`, Toolshop `baseURL`, and a named `chromium` project.
- On 2026-10-10, the user ran `npx playwright test tests/toolshop.spec.ts --project=chromium`; the user confirmed it passed.
- The user then ran `npx tsc --noEmit`; it produced no output, indicating no reported TypeScript errors.
- The user inspected `h1` text and observed an empty array (`Page headings: []`), so no heading assertion was guessed.
- The user inspected the real browser title (`Practice Software Testing - Toolshop - v5.0`) and replaced the temporary title diagnostic with `await expect(page).toHaveTitle('Practice Software Testing - Toolshop - v5.0')`.
- The user reran the named Chromium test and `npx tsc --noEmit`; the test reported `1 passed (3.0s)` and the type-check emitted no errors.
- Preserve `playwright.config.ts`, `tests/toolshop.spec.ts`, `src/`, `tsconfig.json`, `package.json`, and `package-lock.json`. Do not discard or overwrite these files.

## Exact next action
Inspect the Toolshop homepage for a real user-facing control or product element using a small Playwright diagnostic, then add one stable locator-based assertion based on observed page content. Preserve the HTTP 200 and exact page-title assertions; explain the edit and verify the Chromium test plus TypeScript check. Do not build our own SUT yet.

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
