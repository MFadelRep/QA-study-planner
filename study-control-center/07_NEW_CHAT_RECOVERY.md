# NEW CHAT RECOVERY

## Trigger
When the user starts a new chat and types:

`STUDY`

## Required behavior
1. Use the GitHub Study Control Center in `MFadelRep/QA-study-planner`.
2. Treat GitHub as the authoritative study source.
3. Read `study-control-center/01_CURRENT_STATE.md` first.
4. Read only the relevant curriculum/rules sections needed to resume.
5. Continue from the exact recorded NEXT ACTION.
6. Do not restart completed setup or ask the user to reconstruct prior progress.

## Repository separation
`QA-study-planner` is for study management only.
The user's local `automation-platform` project will use a different GitHub repository.

## Library status
The Library is only a fallback/bridge location. Do not treat the legacy Library Control Center copies as live authority.

## Current saved checkpoint
Day 1 / Hour 1 — TypeScript project foundation.
Blocker: TS18003 because there are no TypeScript inputs.
Next action: create minimal `src/index.ts`, run `npx tsc --noEmit`, and inspect the actual result.
