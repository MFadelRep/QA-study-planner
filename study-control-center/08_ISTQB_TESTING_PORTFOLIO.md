# ISTQB Foundation Testing Portfolio — Practical Coverage Map

## Purpose and source
This document maps the relevant **ISTQB Certified Tester Foundation Level (CTFL) v4.0.1** concepts into exercises using Workbench QA Lab as the primary controlled SUT. Practice Software Testing — Toolshop is a secondary target for scenarios Workbench does not represent. It is the canonical detailed testing-portfolio map; the Master Plan defines when it is integrated into the week, the Current State records progress, and [09_LESSONS_LEARNED.md](09_LESSONS_LEARNED.md) captures reusable lessons established while applying the coverage.

Official syllabus: https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf
Official CTFL page and sample exams: https://www.istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/

This is a coverage plan, not a claim that every item has already been tested. Mark each item complete only when there is project evidence or an explicitly documented reason it cannot be exercised on the current SUT.

## Fundamentals and lifecycle
Practise the purpose of testing, testing versus debugging, error/defect/failure terminology, the testing principles, the testing mindset, independence and collaboration, and how testing activities fit within sequential, iterative, and agile lifecycles. Apply analysis, design, implementation, execution, monitoring/control, and completion to a small real feature. Distinguish confirmation testing (did the fix work?) from regression testing (did the change break related behavior?).

## Test levels
- **Component testing:** test small TypeScript helpers or controlled project components in isolation, including price parsing/ordering or validation logic.
- **Component integration testing:** verify interaction between helpers, fixtures, API clients, database setup, and reporters where those boundaries exist.
- **System testing:** exercise complete Workbench user journeys in Playwright and complete API journeys through its documented REST API. Use Toolshop only for external storefront scenarios Workbench does not represent.
- **System integration testing:** verify meaningful interaction between UI, REST API, database, container, CI job, or AI/RAG components when the integration is available.
- **Acceptance testing:** derive scenario examples from user/business acceptance criteria and verify user-visible outcomes; distinguish business acceptance from technical system checks.

A public black-box SUT does not expose its internals for component/white-box claims. Use the project's own controlled components for those exercises. Do not label an end-to-end browser test as proof of every test level.

## Test types
- **Functional:** Workbench authentication, role permissions, projects/work items, knowledge documents, comments, notifications, audit, and API CRUD/validation. Use Toolshop-specific search/filter/cart/checkout examples only when a secondary storefront target is useful.
- **Non-functional:** quality characteristics listed below, selected according to relevance and evidence available.
- **Black-box:** derive expected behavior from observable requirements/acceptance criteria without inspecting implementation.
- **White-box:** inspect project implementation and design tests around statements/branches or control flow where source access and meaningful coverage instrumentation exist.

Test types are not the same thing as test levels. A test can simultaneously have a level, a type, a design technique, and a purpose (for example, a black-box system functional regression test).

## Test design techniques
Apply these to real requirements and keep the resulting cases or calculations in the project's manual-test artifacts:
- **Equivalence partitioning:** divide input data into valid/invalid classes for search, email, login, message length, and quantities where business rules are known.
- **Boundary value analysis:** test the values immediately around known min/max lengths, quantity limits, price ranges, pagination edges, and similar boundaries. Do not invent boundaries; first establish the rule from observed requirements or validation.
- **Decision table testing:** model combinations of conditions and outcomes for login, product availability, cart actions, form submission, and permission-dependent behavior where conditions are observable.
- **State transition testing:** test transitions such as signed-out/signed-in, empty/non-empty cart, product in/out of stock, and valid/invalid form states; verify both permitted and rejected transitions.
- **Statement/branch coverage (white-box):** exercise controlled TypeScript helpers and later service code with appropriate instrumentation. Do not claim coverage without an actual tool report.
- **Error guessing:** deliberately try plausible mistakes—empty inputs, malformed values, repeated clicks, stale state, unexpected order, and interrupted workflows—without destructive activity.
- **Exploratory testing:** write time-boxed charters, record observations and risks, and report defects rather than treating unstructured clicking as complete coverage.
- **Checklist-based testing:** reusable checks for workspace setup, project/work-item flows, permissions, documents/collaboration, notifications, regression, and browser compatibility; retain storefront checklists only for Toolshop exercises.

## Non-functional quality characteristics
Choose relevant checks and state their evidence limits:
- **Performance efficiency:** navigation and interaction timing for a baseline; later JMeter/Locust workloads with response time/percentiles, throughput, and error rate. A single browser timing is not a load test.
- **Compatibility:** browser projects and supported viewport/device differences; record the browsers actually run.
- **Usability:** manual review of clarity, navigation, feedback, form errors, cognitive load, and recovery from mistakes.
- **Reliability:** repeat important workflows, inspect flakiness, and later exercise failures/restarts/health checks in controlled services.
- **Security:** safe authentication/authorization, session/token handling, input validation, access-control reasoning, secret handling, and relevant CI checks. Avoid destructive probing of the public demo.
- **Maintainability:** review fixture/POM boundaries, duplication, naming, readability, and change impact; combine human review with static analysis.
- **Portability:** verify execution/configuration across relevant target environments when available.
- **Safety:** assess relevance to the product's context. Record “not applicable to this SUT” with reasoning when a meaningful safety scenario does not exist; do not invent one.

Accessibility checks may be added as useful project coverage, but do not confuse a selected accessibility tool's results with full usability assurance.

## Static testing and review
Practise reviews without executing the software: requirements/acceptance-criteria review for ambiguity or missing conditions; test-case review for weak steps, expected results, and omitted partitions; code review for fragile selectors, misleading assertions, duplication, and maintainability. Compare informal review, walkthrough, technical review, and inspection at Foundation Level depth. Use TypeScript checks, lint/static-analysis tools where adopted, and dependency/security checks as supporting tools; these do not replace human review.

## Test management, risk, and defects
Create a lightweight test plan with scope, risks, priorities, assumptions, environment, entry/exit criteria, and completion summary. Maintain traceability from requirements or acceptance criteria to manual/automated tests and defects. Prioritize by likelihood/impact and business risk. Produce concise reproducible defect reports with environment, setup, steps, expected/actual result, evidence, severity/priority rationale, and affected areas. After a fix, run confirmation testing plus appropriately selected regression tests. Report pass/fail/blocked/not-run honestly.

## Automated vs manual evidence
Automate repeatable checks that benefit from speed, determinism, frequency, and regression. Keep manual work where exploratory judgment, visual/usability assessment, requirement interpretation, or access limitations matter. A manual test case may seed an automated case, but automation does not replace test analysis, risk assessment, reviews, defect judgment, or test reporting.

For each meaningful feature batch, aim to produce:
1. Complete UI/API automated tests for the suitable happy, negative, boundary, and regression paths.
2. Manual test cases or a checklist for applicable scenarios that should be independently reasoned through.
3. A traceability/coverage row linking requirement, technique, test artifact, and status.
4. A defect report when an actual reproducible defect is observed; do not invent defects merely to fill the file.
5. A concise execution summary with the actual run command, environment, results, and known gaps.

## Integration with the one-week sprint
- **Day 1:** Workbench functional UI coverage and black-box design (equivalence partitions, boundaries, error guessing, checklist, exploratory charter).
- **Day 2:** Workbench API positives/negatives/boundaries, state transitions, decision tables, UI/API integration, and authentication.
- **Day 3:** static review, traceability, defect reports, test planning/reporting, and white-box examples in controlled code.
- **Day 4:** performance/non-functional types and analysis.
- **Day 5:** reliability, component/service integration, environment compatibility, and execution evidence.
- **Day 6:** AI/RAG robustness, safety/security boundaries, adversarial and regression sets.
- **Day 7:** risk-based prioritization, acceptance/system coverage, confirmation/regression, test summary, and interview explanation.

The portfolio is cumulative: don't delay working automation until every manual artifact is perfect. Create the artifacts in coherent batches, update their coverage status based on evidence, and revisit any blocking concept on demand.
