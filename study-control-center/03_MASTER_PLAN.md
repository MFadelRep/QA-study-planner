# Senior QA Automation + MLOps — Master Plan

## Outcome
Build and be able to explain a coherent, portfolio-grade AI QA Platform while gaining broad, practical exposure to Senior QA Automation and MLOps capabilities. The priority is demonstrable working evidence and interview-ready explanations under a one-week deadline. The plan is not a guarantee of complete mastery or a job offer.

## Learning method
Follow the single authoritative batch-first workflow and learning-depth rules in `04_CONTINUITY_RULES.md`. Use this plan for required outcomes, the weekly sequence, and evidence—not as a second copy of the operating rules.

## Project
One coherent AI QA Platform is the primary learning vehicle. Practice Software Testing — Toolshop is the default external system under test for browser UI and its documented REST API. Keep test code in the separate local project repository, not in this study-control repository. Prefer integrated, realistic tasks over disconnected toy exercises when they demonstrate the same capability.

## Required capability coverage
- **Playwright:** locators/assertions, user journeys, reusable fixtures, POM where appropriate, configuration/projects, auth/state reuse, API/UI hybrid flows, network interception/diagnostics, isolation, traces/artifacts, and flake diagnosis.
- **API:** request construction, authentication, status/header/body assertions, schemas/contracts, positive/negative/boundary cases, chaining, safe setup/cleanup, and API-to-database checks where a controlled database exists. Use agent-tool examples such as wrong arguments, invalid customer IDs, authorization failures, and verifying that HTTP success matches actual state.
- **Data:** SQL/PostgreSQL querying, joins/aggregations, test-data setup, and consistency verification.
- **CI/CD:** GitHub Actions early, then GitLab CI, environment variables/secrets, reports/artifacts, quality gates, and failure diagnosis. Where relevant, use the real-world pattern of factory-generated test-data duplication, merge-request review, and validation of AI-assisted code as a debugging case study.
- **Performance:** JMeter/Locust scenarios, workload models, latency/throughput/error-rate interpretation, and evidence-based conclusions, including AI-agent latency, concurrency, timeouts, and downstream-service failures where appropriate.
- **Containers/platform:** Docker, Compose, Kubernetes workloads/services/configuration, test execution, health/readiness, and reliability failure modes.
- **AI QA/RAG:** nondeterministic test oracles, retrieval/answer signals, grounding and citation/support checks, hallucination/misinformation controls, robustness, safety boundaries, latency/cost awareness, adversarial/regression datasets, and inference testing. Practice diagnosing retrieval-versus-grounding failures; prompt/model regressions; wrong agent-tool selection or arguments; and strict tenant isolation.
- **MLOps:** reproducibility, data/model lifecycle, experiment tracking, metrics, artifacts, quality gates, registry/promotion concepts, and rollback reasoning. Compare model or prompt versions with the same evaluation set rather than expecting identical wording.
- **Senior QA:** risk-based planning, test strategy, architecture trade-offs, maintainability, defect communication, test reporting, and interview reasoning. Apply these to competing client deadlines, scope changes, quality gates, release recommendations, escalation, and concise progress/action reporting.
- **ISTQB CTFL manual-testing knowledge:** practical test design, test levels/types, static testing/reviews, non-functional testing, test management, risk, defects, and regression/confirmation testing. The canonical detailed map is `08_ISTQB_TESTING_PORTFOLIO.md`.

## 45-hour capability catalogue
The catalogue remains the complete scope; overlapping capabilities are deliberately integrated into the accelerated schedule rather than taught as isolated one-hour silos.

### 1–4 — Foundations
Programming, terminal/Git, TypeScript for automation, async/testable code, and CI survival.

### 5–15 — Playwright, API, Data
Playwright UI foundations/architecture, auth/state, network reliability, API test strategy, SQL/PostgreSQL, integration checks, static review, traceability, and test architecture.

### 16–19 — CI/CD
CI/CD fundamentals, GitHub Actions, GitLab CI, artifacts and test reporting.

### 20–23 — Performance
Performance concepts, JMeter, Locust, and evidence-based performance analysis.

### 24–29 — Containers and Kubernetes
Docker, Compose, containerized CI, Kubernetes fundamentals, test execution, and reliability.

### 30–35 — AI QA and RAG
AI QA foundations, AI-assisted QA, RAG, retrieval/answer evaluation, inference testing, and project integration.

### 36–38 — MLOps
MLOps foundations, MLflow, experiment/artifact handling, reproducibility, and MLOps CI/CD.

### 39–45 — Senior QA and interviews
Risk-based senior QA strategy, reliability/flakiness, security, scalability/governance, capstone hardening, interview engineering, and final simulation.

## Accelerated seven-day schedule
Target approximately six focused hours per day. The 45-hour catalogue is treated as required scope, but related lessons, code, setup, and verification are combined into fewer larger batches. Prefer integrated coverage across the seven days over perfect mastery of one narrow area. If time slips, prioritize a working end-to-end slice and the strengthened gaps listed above; record anything deferred instead of silently deleting its requirement.

1. **Day 1 — Foundations + Toolshop UI + ISTQB:** close only blocking TypeScript/async gaps; create a substantial UI test suite in feature batches; add manual test cases and an ISTQB coverage matrix.
2. **Day 2 — Advanced Playwright + API:** fixtures/POM as needed, authentication/state, network handling, complete compact API batch, positive/negative/boundary cases, contracts and UI/API integration.
3. **Day 3 — SQL + CI/CD:** SQL/PostgreSQL, controlled test data, GitHub Actions, GitLab CI, reporting, traceability, review, and defect examples—including realistic test-data collision and merge-request investigation scenarios.
4. **Day 4 — Performance + Docker:** practical JMeter/Locust tests, interpret real results, package app/tests using Docker and Compose.
5. **Day 5 — Kubernetes + MLOps:** execute in container/Kubernetes environments and create a minimal MLflow-based lifecycle with reproducible runs and artifacts.
6. **Day 6 — AI QA + RAG + security:** implement/evaluate representative RAG and inference checks, grounding, robustness, safety boundaries, basic web/API security reasoning, agent tool-call validation, and cross-tenant isolation.
7. **Day 7 — Integration + senior QA + interviews:** integrate, harden, produce a demonstrable report, practise risk/architecture/interview questions, and identify follow-up depth work using scenarios involving competing deadlines, scope trade-offs, stakeholder reporting, residual risk, and go/no-go recommendations.

## ISTQB integration
ISTQB is practised through the same project, not as a disconnected theory course. Apply the relevant test levels/types and design techniques to Toolshop UI/API cases; preserve manual cases, exploratory charters, review notes, requirements traceability, defect examples, and a test summary alongside automated tests. Automate suitable repeatable checks, but do not pretend that human-centered usability assessment, review, exploratory judgment, or unavailable implementation-level checks are proven by a browser assertion. Use a controlled project component for white-box/component testing where Toolshop does not expose the implementation. Use the detailed mapping in `08_ISTQB_TESTING_PORTFOLIO.md`.

## Evidence standard
A capability is complete only when there is observable project evidence, a verified result, a reviewed manual artifact, or a clear technical explanation tied to an implemented result. Reading alone is not completion. Distinguish verified green tests from draft coverage and failed/pending tests in checkpoints.

## Plan-change rule
The plan can be resequenced or integrated when that makes progress faster, but required outcomes may not be silently removed. If a scenario is unsuitable or impossible on the public Toolshop environment, record the limitation and use a suitable secondary target or controlled project component.
