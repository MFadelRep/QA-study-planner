# Current Study State

**State version:** 4.5-TOOLSHOP-INITIAL-INVENTORY-CHECKPOINT
**Last verified:** 2026-10-12
**Checkpoint:** SAVED — headed Chromium pagination behavior test passed (`1 passed (3.9s)`) and initial Toolshop homepage DOM inventory was captured and recorded below. Sorting investigation is the exact next action; its result is not yet known.
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
- The first immediate inventory was incomplete because it ran before the full shop interface had rendered; do not treat that early inventory as the page's full control list.
- Added a temporary diagnostic wait: wait for `networkidle` for up to 15 seconds, tolerate timeout, then wait another 3 seconds. The subsequent headed Chromium run completed successfully (`1 passed (7.9s)`) and exposed the populated catalog.
- The later inventory confirmed visible checkbox inputs including `name="brand_id"` (brand filters) and `name="eco_friendly"` (sustainability), labels such as `MightyCraft Hardware` and `Show only eco-friendly products`, product-card links and image alt text (e.g. `Combination Pliers`, `Pliers`, `Bolt Cutters`, `Long Nose Pliers`), accessible `Compare` buttons, pagination buttons with accessible names `Previous`, `Page-1` through `Page-5`, and `Next`, plus footer/external links including Learn Test Automation, API Spector, and GitHub.
- Replaced the temporary inventory diagnostics with a focused test named `Toolshop pagination displays different products on page 2`. It uses `page.locator('a[href^="/product/"] h5')` to collect product names, clicks `page.getByRole('button', { name: 'Page-2' })`, and uses `expect.poll()` to wait for the product list to differ without a fixed sleep.
- The user ran `npx playwright test tests/toolshop.spec.ts --project=chromium --headed`; actual output listed 9 distinct product names on each page and reported `1 passed (20.2s)`.
- After the headed test passed, the user ran `npx tsc --noEmit`; they confirmed it returned no output, so no TypeScript errors were reported.
- The user wants the test run headed for visual inspection. `--headed` shows Chromium while the test runs; Playwright normally closes it when the test finishes. `--debug` opens Playwright Inspector for paused interactive inspection.
- User described additional visible controls to cover later: Documentation, Testing Guide, Bug Hunting, Home, Contact, Sign in, language dropdown, Sort, Categories, search box, price-range slider, more checkboxes, product-image links, and pagination. Inventory work is complete enough to begin behavior testing; avoid more broad diagnostics unless a specific gap appears.
- Preserve `playwright.config.ts`, `tests/toolshop.spec.ts`, `src/`, `tsconfig.json`, `package.json`, and `package-lock.json`. Do not discard or overwrite these files.

## 2026-10-12 checkpoint — Toolshop initial homepage inventory
- User ran `npx playwright test tests/toolshop.spec.ts --project=chromium --headed`; actual output passed: `1 passed (3.9s)`. The test logged 9 page-1 product names and 9 different page-2 product names. Page 1: Combination Pliers; Pliers; Bolt Cutters; Long Nose Pliers; Slip Joint Pliers; Claw Hammer with Shock Reduction Grip; Hammer; Claw Hammer; Thor Hammer. Page 2: Sledgehammer; Claw Hammer with Fiberglass Handle; Court Hammer; Wood Saw; Adjustable Wrench; Angled Spanner; Open-end Spanners (Set); Phillips Screwdriver; Mini Screwdriver.
- User then ran a temporary Node/Playwright headed DOM inventory against `https://practicesoftwaretesting.com/`. Observed title: `Practice Software Testing - Toolshop - v5.0`; one visible H1: `Practice Software Testing - Toolshop`.
- Initial homepage DOM inventory counts: 21 visible links; 24 visible buttons; 25 visible inputs; one native select; two elements with slider role; 9 product-card links; pagination includes Previous, Page-1 through Page-5, and Next. These counts are from the initial page state and selector groups can overlap.
- Search input: `#search-query`, placeholder `Search`; Search submit button. Filter inputs: 19 `category_id` checkboxes, 4 `brand_id` checkboxes, and 1 `eco_friendly` checkbox (25 total inputs = 1 search + 24 checkboxes). Two slider-role spans have accessible names `ngx-slider` and `ngx-slider-max`.
- Sort control: `select[aria-label="sort"]`; options observed in the page text: `Name (A - Z)`, `Name (Z - A)`, `Price (High - Low)`, `Price (Low - High)`, `CO₂ Rating (A - E)`, `CO₂ Rating (E - A)`.
- Other observed buttons include Categories, language selector EN (`aria-label="Select language"`), 9 Compare buttons, pagination controls, Open chat, and Show live shop activity. Navigation/content links include Documentation, Home, Contact, Sign in, Explore courses, Learn Test Automation, API Spector, GitHub, Privacy Policy, Barn Images, and Unsplash. The initial page includes the out-of-stock product Long Nose Pliers.
- This is the initial homepage DOM inventory only, not a complete inventory of interaction states or all pages. Dropdown contents and dynamic states still need targeted inspection.
- No project files were changed by the temporary inventory script. Local working-tree status observed earlier in this chat: modified `package.json` and `package-lock.json`; untracked `playwright.config.ts`, `src/`, `tests/`, and `tsconfig.json`; do not discard these.
- User explicitly asked to checkpoint and retain these inventory results for future study sessions.
- Next investigation: use the already-provided headed Node/Playwright script to test the sort control with `Price (Low - High)`, comparing product names before and after. No result has been observed yet.

## Exact next action
Run the already-provided temporary Node/Playwright headed investigation of the sort control in the local `automation-platform` project. It should print the available options from `select[aria-label="sort"]`, record the first-page product names, select `Price (Low - High)`, then print the resulting product names and selected option. The user has not run this investigation yet. Use the actual output to decide the next test; do not create or modify permanent test files for this investigation.


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
