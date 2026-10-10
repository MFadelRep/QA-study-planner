# LONG HANDOVER — CURRENT RECORD

Canonical state version: 3.8-PRACTICE-TARGET-CHECKPOINT

**Derived record — not authoritative.** The live study state is `01_CURRENT_STATE.md`; operating rules are `04_CONTINUITY_RULES.md`; curriculum coverage is `03_MASTER_PLAN.md`.

## Session state
Day 1 / Hour 1 of the 45-hour Senior QA Automation + MLOps program. The AI QA Platform is the primary learning vehicle. Execution mode is project-first / fast-pace.

Topic: TypeScript asynchronous test flow — Promise, async/await, failure reporting and process exit codes.

## Verified environment
The user's local project uses Node.js 22.22.1, local TypeScript 7.0.2, and tsx 4.23.15.

## Verified Git milestones
- Repository initialized on main.
- Local Git identity configured.
- Initial root commit: `f2e8917`.
- Repository was verified clean after the root commit.

## Project foundation
- `.gitignore` created and verified to ignore `node_modules/`.
- `src/` and `tests/` created.
- `tsconfig.json` created.
- TS18003 was resolved by creating `src/index.ts`.
- Added the typed `TestResult` model and typed `reportResult(result: TestResult): void` reporter.
- Added `runLoginTest(): Promise<TestResult>` and `main(): Promise<void>`; `main()` awaits the login operation and reports the resolved result.
- Removed the old synchronous `loginTest` object and `reportResult(loginTest)` call to prevent duplicate output.
- On 2026-10-10, the user ran `npx tsx src/index.ts`; actual output was `Starting AI QA Platform` and `Login test: PASSED` exactly once.
- The user then ran `npx tsc --noEmit`; it produced no errors/output.
- The user deliberately changed the test password to `WrongPassword!`; the simulated login returned `Login test: FAILED`.
- `main()` was updated to throw an error when `result.passed` is false.
- The user verified exit code `1` with `npx tsx src/index.ts; echo "Exit code: $?"` (with echo directly after the test command); a subsequent `npx tsc --noEmit` produced no errors.
- The user later restored the expected password and confirmed the program passed; the TypeScript check also passed.

## Current resume point
The async test flow reports failures and throws an error so the process exits nonzero; the user verified exit code 1 for the deliberate wrong-password case, then restored the expected password and confirmed the test passed. TypeScript checking also passed. Toolshop was selected as the default UI + REST API practice target.

## Exact resume action
Open https://practicesoftwaretesting.com/ in Firefox and confirm it loads. Then set up Playwright UI + API tests against Toolshop after checking the current files/dependencies. See `04_CONTINUITY_RULES.md` for secondary-site use cases. Do not build our own SUT yet. Keep pace fast, examples realistic, explanations short, and verify actual output.

## Learning constraints
- Project-first / fast pace.
- Explain every terminal command line and important syntax before execution.
- Verify actual results.
- Correct minimally and retry.
- Preserve the exact next action at checkpoints.
- Use `04_CONTINUITY_RULES.md` for operating rules rather than duplicating them here.

## Repository architecture
- `QA-study-planner` is the study-control repository only.
- The local AI QA Platform project will use a different GitHub repository.
- The local project repository must not be connected as the remote for this study-control repository.
- This handover is a historical/continuity aid derived from the canonical control-center state; it does not override canonical files.
