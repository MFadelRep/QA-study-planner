# LONG HANDOVER — CURRENT RECORD

Canonical state version: 5.0-BATCH-FIRST-ISTQB-PORTFOLIO-2026-10-12

**Derived record — not authoritative.** Live progress and next action: `01_CURRENT_STATE.md`. Operating rules: `04_CONTINUITY_RULES.md`. Full capability plan: `03_MASTER_PLAN.md`. ISTQB map: `08_ISTQB_TESTING_PORTFOLIO.md`.

## Session state
Day 1 / Hour 5 of the accelerated seven-day Senior QA Automation + MLOps sprint. The 45-hour capability catalogue remains the scope, with overlapping activities combined into practical batches. Current topic: Toolshop UI automation batch — fix two failures, then expand UI + ISTQB portfolio coverage

## Learning approach now in force
Batch-first implementation across all subjects. The user wants complete code and supporting files supplied in grouped batches, followed by real execution, verification, a brief explanation, and the next capability. Broad coverage and a functioning integrated project come before deep mastery; the user asks for deeper explanations when something blocks understanding. The workflow is defined only in `04_CONTINUITY_RULES.md`.

## Project and environment facts
- Local project path: `/run/media/mfadel/New Volume/Projects/QA/automation-platform`.
- Runtime/tools previously verified: Node.js 22.22.1, TypeScript 7.0.2, `tsx` 4.23.15, and `@playwright/test` 1.63.0.
- `playwright.config.ts` uses `testDir: './tests'`, Toolshop `baseURL`, and a named Chromium project.
- The existing `tests/toolshop.spec.ts` contains homepage/smoke validation plus pagination and low-to-high price sorting. The two behavioral tests were previously verified passing in a one-worker run.
- Preserve the local working tree and keep this project separate from the old `/run/media/mfadel/New Volume/playwright-course` directory and separate from this study-control repository.

## Verified Toolshop observations
- Site title observed: `Practice Software Testing - Toolshop - v5.0`.
- Pagination exposes Previous, Page-1 through Page-5, and Next; page 1 and page 2 were observed to contain different product sets.
- The homepage includes search, category/brand/eco-friendly filters, a sort select, price sliders, product cards, Compare controls, language selection, account navigation, contact navigation, and footer/external links.
- Sort choices previously observed: Name A–Z, Name Z–A, Price High–Low, Price Low–High, and CO₂ Rating in both directions. These observations are a useful starting point; verify live labels/selectors before depending on them.

## Current UI batch result (2026-10-12)
The user created `tests/toolshop-ui-batch.spec.ts` from a supplied full-file block and ran it. Actual result: 13 tests, 11 passed and 2 failed (about 50 seconds). Passed areas: positive search, unknown search result, brand and eco-friendly filters, A–Z/Z–A sorting, price descending, product details, add-to-cart, invalid login, and short-message contact validation. Failures: first category checkbox did not change the products, and sort-menu option extraction yielded an empty list because the test inspected before catalog readiness. A possible correction block was supplied but its execution/result is unconfirmed; treat the actual local file and current error context as the source of truth. Do not report the batch green or rewrite the eleven passing tests unnecessarily.

## Curriculum changes
- The one-week sprint is now organized around seven integrated days: (1) foundations, UI automation, ISTQB; (2) advanced Playwright/API; (3) SQL and CI/CD; (4) performance and Docker; (5) Kubernetes and MLOps; (6) AI QA/RAG/security; (7) integration, senior QA, and interviews.
- ISTQB CTFL v4.0.1 techniques and coverage are mapped in `08_ISTQB_TESTING_PORTFOLIO.md`, including black-box/experience-based design, levels, types, static testing/reviews, non-functional assessment, risk, defects, reporting, confirmation, and regression. Manual judgment is distinguished from checks that can be meaningfully automated.
- Official baseline syllabus: https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf

## Exact resume action
Create and run a focused correction for the two observed UI failures. First inspect the current file and the relevant Playwright error context; fix category selection/assertions and sort-menu timing/label normalization as a pair. Run only those two tests initially. After both pass, execute the combined Toolshop suite once with one worker. Continue with the next UI coverage batch and the ISTQB manual/automated artifacts. Do not return to one-test-per-turn pacing.

## Project boundaries
`MFadelRep/QA-study-planner` is for study management, curriculum, state, and continuity rules only. The local AI QA Platform application/test code belongs in a separate project repository. The handover is a continuity aid, not an authority, and must always match the canonical state version when refreshed.
