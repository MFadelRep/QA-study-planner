# Current Study State

**State version:** 5.3-GHAIA-SCENARIO-MAPPING-2026-10-19
**Last verified:** 2026-10-12
**Status:** ACTIVE — accelerated seven-day study sprint
**Execution mode:** BATCH-FIRST / CODE-FIRST / COVERAGE-FIRST / LEARN-ON-DEMAND

## Position
- Day: 1
- Hour: 5
- Current topic: Toolshop UI automation batch — fix two failures, then expand UI + ISTQB portfolio coverage
- Project: AI QA Platform
- Local project path: `/run/media/mfadel/New Volume/Projects/QA/automation-platform`

The hour number is the nearest curriculum locator for the current work, not a claim that elapsed time alone proves mastery of earlier material. The accelerated schedule combines related topics and revisits foundational gaps only when they block implementation.

## Current checkpoint
The batch-first study workflow, accelerated seven-day map, and ISTQB CTFL v4.0.1 portfolio have been committed to GitHub and read back with matching blob SHAs. GitHub Actions validation passed on commit `6fbe8bf7ac50d846024902d8258a157d63b4b860` (9 unit tests passed; read-only control-center validator passed). The intended learning cadence is defined in `04_CONTINUITY_RULES.md`; the full capability map is in `03_MASTER_PLAN.md` and `08_ISTQB_TESTING_PORTFOLIO.md`.

## Verified local project state
- Project uses Node.js 22.22.1, TypeScript 7.0.2, `tsx` 4.23.15, and `@playwright/test` 1.63.0.
- `playwright.config.ts` uses `testDir: './tests'`, Toolshop as `baseURL`, and the named `chromium` project.
- `tests/toolshop.spec.ts` already contains the homepage/smoke, pagination, and low-to-high price-sorting checks; the two behavior tests were previously verified passing in a one-worker run.
- A separate `tests/toolshop-ui-batch.spec.ts` was created and run on 2026-10-12. The initial run executed 13 tests: **11 passed, 2 failed**.
- Passing coverage in that first batch: positive search, no-results search, brand filter, eco-friendly filter, name sorting A–Z and Z–A, price sorting high-to-low, product-page details, add-to-cart, invalid-login handling, and short-message contact-form validation.
- The two known failing cases are (1) the first category checkbox did not change the displayed product names, and (2) the sort-menu option check received an empty list because it inspected the menu before the catalogue was ready. The test run completed; do not report the batch as fully green.
- A proposed combined correction was provided in chat but **has not been confirmed as executed**. Use the current local test file and error context as the source of truth before patching. Preserve the eleven passing tests.

## Project and environment constraints
- Keep this project separate from `/run/media/mfadel/New Volume/playwright-course`.
- Preserve working project files and changes; do not reset or overwrite the working tree.
- The study-control repository `MFadelRep/QA-study-planner` stores study state and rules only. Do not store application test code or connect the local project as this repository's remote.
- Toolshop is the default SUT. Secondary sites remain available only when a focused scenario is missing or unreliable on Toolshop.

## Exact next action
Build one focused correction batch for the two failed cases in `tests/toolshop-ui-batch.spec.ts`: inspect the current test and failure context; select a real, appropriate Pliers category and assert its actual filtering behavior; wait for the catalogue before asserting the sort-menu options and compare normalized option labels. Run only those two tests first. If they pass, run the complete UI batch plus the existing `tests/toolshop.spec.ts` once, with `--workers=1`, to establish the combined baseline. Then expand the UI batch in coherent feature groups and create ISTQB-mapped manual/automated testing artefacts. Keep the next response code-first and combined; do not revert to command-by-command teaching.
