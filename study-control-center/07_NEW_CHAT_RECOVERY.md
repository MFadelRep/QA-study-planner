# NEW CHAT RECOVERY

## Trigger
When starting a new study chat, the user types `STUDY`.

## Recovery procedure
1. Read the live `study-control-center/01_CURRENT_STATE.md` from `MFadelRep/QA-study-planner`.
2. Apply `04_CONTINUITY_RULES.md` before taking action.
3. Read only the relevant curriculum sections from `02_CURRICULUM_INDEX.md`, `03_MASTER_PLAN.md`, and `08_ISTQB_TESTING_PORTFOLIO.md`.
4. Identify what is verified, what failed, and which proposed changes have not yet been run.
5. Resume the exact next action with a batch-first solution; inspect current local files and actual output where available.
6. Preserve passing work and avoid repeating completed setup.

## Authority
The live checkpoint is always read from `01_CURRENT_STATE.md` at recovery time. Do not store a copied checkpoint in this recovery file. Operating rules come from `04_CONTINUITY_RULES.md`; handovers are derived aids only.

## Library status
Library Control Center copies are bridge/fallback records only, not live authority.

## Repository separation
`QA-study-planner` is the study-control repository. The user's local `automation-platform` project must use a different GitHub repository.
