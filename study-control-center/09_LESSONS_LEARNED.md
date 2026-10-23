# Lessons Learned — Senior QA Automation + MLOps

## Purpose and authority

This is the cumulative record of reusable technical lessons established during study. It captures what the project demonstrated, what the evidence did and did not establish, and what should be reused in later capabilities.

This page is not the live checkpoint, curriculum, or workflow authority. Those remain [Current Study State](01_CURRENT_STATE.md), [Master Plan](03_MASTER_PLAN.md), and [Continuity Rules](04_CONTINUITY_RULES.md). Handovers are derived aids.

## How to use this record

At startup, read only the sections relevant to the next capability. Use these examples to avoid repeating mistakes, but check the current local project and outputs before applying a lesson.

Evidence labels mean:
- **VERIFIED** — supported by executed commands, test output, or directly inspected code.
- **OBSERVED — NOT CAUSAL PROOF** — a trace/run showed behavior but did not isolate its cause.
- **HYPOTHESIS** — a plausible explanation that still needs a focused test.

A green run is evidence for that run, not a guarantee that an external service will always be available.

## Lesson entry format

Record meaningful lessons with: capability/ID; evidence status; context/problem; actual evidence; decision/resolution; reusable rule; and limitations. Do not record every command. Keep current position and exact next action in 01_CURRENT_STATE.md instead of duplicating them here.

## Playwright fundamentals and assertions

### LL-UI-001 — Assert the outcome, not only the action

**Evidence status: VERIFIED**

Clicking Page 2, checking a filter, or submitting a form proves only that an action was attempted. It does not establish that the application reached the intended state.

**Project example:** Pagination captures initial product names, clicks Page 2, then verifies the list changed. Search checks returned product names, and form tests check the visible validation result.

**Reusable rule:** Pair important interactions with assertions about resulting state. When possible, assert the business rule—for example, that every returned product belongs to the selected category—rather than merely checking that something changed.

### LL-UI-002 — Choose test data that exercises the intended behavior

**Evidence status: VERIFIED**

The original category-filter test selected the first checkbox (Hand Tools), which was already represented on the first page. A generic “the list must change” assertion was unreliable. Selecting Power Tools returned five different products in the observed run.

**Reusable rule:** Choose a known input and define correct output. A changed list is a weak oracle if unrelated or incorrect results can also pass.

### LL-UI-003 — Prefer accessible locators when practical

**Evidence status: VERIFIED**

The suite uses checkboxes and buttons by accessible role/name where reliable; CSS selectors remain useful when no dependable user-facing locator exists.

**Reusable rule:** Prefer role/name and label-based locators for user-visible controls. A locator describes how to find an element; it does not guarantee that the element is ready.

### LL-UI-004 — Match assertions to the actual contract

**Evidence status: VERIFIED**

The sort menu uses “CO₂ Rating”, not a plain “CO2” label. The earlier regular expressions did not match as intended.

**Reusable rule:** Inspect received values and compare the contract the application actually exposes. Do not weaken assertions just to make tests green.

## Page Object Model and fixtures

### LL-POM-001 — Page objects own interactions; tests own scenario expectations

**Evidence status: VERIFIED**

Catalogue search, product selection, sorting, filters, cart interactions, login, and contact-form actions were moved into CataloguePage, ProductPage, LoginPage, and ContactPage. Tests still own scenario-specific assertions.

**Reusable rule:** Keep selectors and reusable page interactions in page objects. Keep expected scenario behavior in tests. Avoid turning page objects into repositories for every business assertion.

### LL-POM-002 — Use fixtures to supply shared dependencies

**Evidence status: VERIFIED**

tests/fixtures/test.ts supplies page objects through a custom Playwright fixture. Tests request only the objects they need instead of constructing them repeatedly.

**Reusable rule:** Use fixtures to standardize construction and setup. Keep setup minimal and avoid coupling unrelated scenarios to global setup.

### LL-POM-003 — Avoid unrelated setup

**Evidence status: VERIFIED**

A global homepage beforeEach made login/contact tests visit the catalogue before immediately navigating elsewhere. Homepage setup was scoped to catalogue/product suites; login and contact flows wait for their own controls.

**Reusable rule:** Scope setup to the test or suite that requires it. Extra navigation consumes time and adds unrelated dependencies.

## Navigation readiness and synchronization

### LL-WAIT-001 — Navigation completion is not application readiness

**Evidence status: VERIFIED**

Catalogue navigation waits for navigation commit and then a visible product card. Login and contact navigation wait for their relevant form controls.

**Reusable rule:** Synchronize against the state required by the next step—not an arbitrary delay and not necessarily the browser's full load event. A product card is appropriate for catalogue tests, not every page.

### LL-WAIT-002 — Avoid arbitrary sleeps and treat timeouts as evidence

**Evidence status: VERIFIED**

Prefer retrying assertions and condition-based waits. Increase a timeout only when observed operation duration justifies it; a longer timeout must not conceal a bad selector, failed request, or incorrect assertion.

**Project context:** The current configuration allows 60 seconds per test, 10 seconds for default expectations, and up to 30 seconds for a product card after navigation commit because the external practice site showed slow responses. These are environment-specific settings, not universal defaults.

## Parallel reliability and evidence-based diagnosis

### LL-PAR-001 — Sequential success does not establish parallel reliability

**Evidence status: VERIFIED**

Earlier parallel runs showed different failures: the catalogue did not render in time, search/pagination did not reach expected states, and navigation timed out. Some failures passed on isolated reruns; a sequential run also failed once.

**Reusable rule:** Validate under the execution mode the project will actually use. Do not disable parallelism merely to make the report green if parallel execution is a project requirement.

### LL-PAR-002 — Preserve diagnostic evidence

**Evidence status: VERIFIED**

Playwright was configured to retain traces and screenshots on failure. Traces showed JavaScript/CSS resources taking roughly 4–23 seconds, including a navigation timeout waiting for DOMContentLoaded.

**Reusable rule:** Inspect assertions, browser snapshot, trace actions, requests, console, and screenshot before changing code. Different failure stages need different remedies.

### LL-PAR-003 — Separate observation from causal explanation

**Evidence status: OBSERVED — NOT CAUSAL PROOF**

Traces contained HTTP 401 responses from an unauthenticated /users/me request, but did not establish that those responses caused the UI failures. Several reliability changes were applied together, so their individual effects were not isolated.

**Reusable rule:** Report what traces prove and what they only suggest. Do not treat every non-2xx response as a defect or claim a combined change proves one root cause.

### LL-PAR-004 — Repeat runs and state the limits

**Evidence status: VERIFIED**

**Verified on 2026-10-19:** After combined readiness, test-setup, timeout, and optional-telemetry changes, the 15-test suite passed three consecutive times using two workers: 15/15 in 2.0 minutes, 15/15 in 3.2 minutes, and 15/15 in 2.6 minutes (45 successful test executions).

**Limitations:** This is evidence of stability across those three runs, not a guarantee of future success. The combined experiment does not isolate which individual change contributed most. The public site and network remain external dependencies.

### LL-PAR-005 — Test-only interception must match test scope

**Evidence status: VERIFIED**

An automatic fixture returns an empty JavaScript response for Cloudflare's optional analytics beacon during these functional tests.

**Reusable rule:** Intercept optional third-party telemetry only when it is irrelevant to the scenario. This deliberately excludes the real analytics script from coverage; do not reuse this configuration for analytics testing or representative performance tests without reconsidering it.

## Safe editing and regression verification

### LL-EDIT-001 — Preserve before broad edits; validate immediately

**Evidence status: VERIFIED**

Scripted text replacement caused a missing closing delimiter in a test file, and another edit inserted a literal backslash-n sequence into TypeScript. Both needed correction before tests could run.

**Reusable rule:** Back up files, ensure each replacement target matches exactly once, then typecheck and run focused tests. Never assume a script succeeded just because it printed a success message.

### LL-EDIT-002 — Validate in layers and preserve the baseline

**Evidence status: VERIFIED**

The UI suite stayed at 15 scenarios through the POM/fixture refactor. Validation used TypeScript, focused tests, the full suite, and repeated parallel runs.

**Reusable rule:** Typecheck for structural errors, focused tests to diagnose changes, regression tests to protect existing behavior, and repeated runs for intermittent failures. Preserve passing work and inspect real output.

### LL-EDIT-003 — Keep study control separate from application code

**Evidence status: VERIFIED**

MFadelRep/QA-study-planner manages study state, curriculum, continuity rules, validation, and lessons learned. The local AI QA Platform repository holds the actual automation code and tests.

**Reusable rule:** Keep learning governance and application implementation in separate repositories. A study checkpoint records progress and evidence but is not a copy of the source code.

## Updating this record

Follow [Continuity Rules](04_CONTINUITY_RULES.md) for the maintenance process. Add or refine entries only when an observation has reusable value. Label uncertainty, keep examples evidence-based, and do not duplicate the live checkpoint, curriculum requirements, or operational rules.

## Learner-owned test practice

### LL-STUDY-001 — Keep the app implementation and the test-learning exercise separate

**Evidence status: VERIFIED BY REPOSITORY INSPECTION; local execution remains unverified**

**Context/problem:** Workbench QA Lab was built as a controlled SUT, but the first implementation pass also added completed unit/API/browser tests and later RAG/performance test runners. That delivered code while removing the user's intended practice of designing and writing those tests.

**Decision:** Preserve `main` as the completed reference baseline. Use `learn/rag-unit-tests` as the curriculum's learner branch, keep application source intact, and replace generated test implementations with TODO or skipped placeholders until the user implements each batch. Remove ready-made later-stage RAG-evaluation, mutation-testing and k6 workload implementations from the learner branch.

**Reusable rule:** The assistant builds or maintains the app and learning environment. The user owns the curriculum's automation implementations. Before each batch, provide the feature contract, risks, expected outcomes and useful test-design prompts; let the user attempt the code, then review and debug their actual output. Do not paste a complete test implementation before the attempt.

**Limitations:** TODO/skipped tests are not feature coverage. The branch's post-conversion CI and the user's laptop setup must be verified independently. Keep `main` as reference; never report a green runner with TODO tests as proof of application quality.

