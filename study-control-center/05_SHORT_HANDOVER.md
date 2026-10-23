# SHORT HANDOVER — CURRENT

**Derived record — not authoritative.**
**Canonical state version:** 6.0-WORKBENCH-LEARNER-API-2026-10-23
**Position:** Day 2 / Hour 10
**Topic:** API testing strategy and test-case design — next: implement the first Workbench API test batch

## Context
- The live checkpoint is study-control-center/01_CURRENT_STATE.md in MFadelRep/QA-study-planner.
- Primary SUT is Workbench QA Lab in MFadelRep/QA-practice-platform-app, learner branch learn/rag-unit-tests.
- main retains the completed reference tests; the learner branch has TODO/skip exercises. A TODO/skip run is not feature coverage.
- The local laptop checkout, runtime, Docker startup, migrations, seed and post-conversion CI are not yet verified.

## Immediate next action:
When the user types STUDY, read 01_CURRENT_STATE.md and this project's STUDY_GUIDE.md. Check local branch/worktree/runtime first without overwriting local work. If setup is not done, use STUDY_GUIDE.md. Then study Day 2 API testing through docs/practice/api-testing-exercise.md and apps/api/test/projects-work-items.e2e-spec.ts. The user writes the tests; provide scenario design, progressive hints, review and debugging—not completed test files.

## Preserve
- Do not switch to main for study work or merge the learner branch wholesale.
- Keep the older automation-platform project separate; do not restart its verified 15-test Playwright baseline by default.
- Verify real local execution before updating study completion.
