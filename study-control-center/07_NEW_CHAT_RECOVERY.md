# NEW CHAT RECOVERY

## Trigger
When starting a study chat, the user types `STUDY`.

## Recovery procedure
1. Read the live study-control-center/01_CURRENT_STATE.md from MFadelRep/QA-study-planner first.
2. Apply study-control-center/04_CONTINUITY_RULES.md before taking action.
3. Read only the relevant curriculum sections from study-control-center/02_CURRICULUM_INDEX.md, study-control-center/03_MASTER_PLAN.md and study-control-center/08_ISTQB_TESTING_PORTFOLIO.md.
4. Consult relevant entries in study-control-center/09_LESSONS_LEARNED.md; use them as reusable technical knowledge, not the live checkpoint.
5. Read STUDY_GUIDE.md and the active exercise brief from MFadelRep/QA-practice-platform-app on branch learn/rag-unit-tests.
6. Distinguish verified remote code, actual local execution, TODO tests and skipped tests. Do not call TODO or skipped exercises feature coverage.
7. When the user has set up Workbench locally, verify the current branch, worktree status, runtime versions and actual command output before editing. Never overwrite local changes or assume a GitHub branch change is already synced.
8. Resume the exact next action from 01_CURRENT_STATE.md. The current expected subject is Day 2 API testing, with apps/api/test/projects-work-items.e2e-spec.ts as the first exercise. The learner authors the tests; guide with scenario design, hints, review and debugging rather than pasting completed test files.
9. Preserve passing work and avoid repeating verified setup. After a meaningful executed slice, update Current State and refresh handovers to its canonical state version.

## Authority
The live checkpoint is always read from `01_CURRENT_STATE.md` at recovery time. Do not store a copied checkpoint in this recovery file. Operating rules come from `04_CONTINUITY_RULES.md`; handovers are derived aids only.

## Library status
Library Control Center copies are bridge/fallback records only, not live authority.

## Repository separation
`QA-study-planner` manages study progress only. The application is in the different GitHub repository `MFadelRep/QA-practice-platform-app` on its learner branch. Do not place application source or test code in the study-control repository.
