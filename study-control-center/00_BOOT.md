# Study Control Center — GitHub Boot

Status: LIVE
Repository: MFadelRep/QA-study-planner
Control Center path: study-control-center/
Purpose: STUDY PROGRESS MANAGEMENT ONLY

## Startup keyword
`STUDY`

## Mandatory startup rule
When the user types `STUDY` in a new chat, use this GitHub Study Control Center as the primary authority. Do not use Library Control Center copies as the live study authority; they are fallback/bridge copies only.

## Boot protocol
1. Read `01_CURRENT_STATE.md` first and identify the exact next action and unresolved blockers.
2. Read `02_CURRICULUM_INDEX.md` to orient within the curriculum.
3. Read the relevant sections of `03_MASTER_PLAN.md` and `08_ISTQB_TESTING_PORTFOLIO.md` for the current capability.
4. Apply `04_CONTINUITY_RULES.md` as the operating authority.
5. Resume from the exact next action without restarting completed work or requiring the user to reconstruct state.
6. Verify real execution results before marking work complete.
7. After a meaningful verified slice, update the live checkpoint and then refresh derived handovers to the same state version when appropriate.

## Startup scope
This file defines routing only. Workflow, batching, teaching depth, test strategy, handover handling, and safe-write instructions are defined in `04_CONTINUITY_RULES.md`. Live progress and the next action are defined only in `01_CURRENT_STATE.md`. This file must not copy the live checkpoint or duplicate detailed operating rules.

## Conversation safety reminder
The user's global ChatGPT Custom Instructions should include the short Conversation Safety Warning reminder so the assistant can warn about long conversations across chats. The detailed study-chat rule lives in `04_CONTINUITY_RULES.md`. This repository does not automatically load into an unrelated new chat; the user starts with `STUDY` to trigger recovery.

## Repository separation
This repository manages study progress only. The AI QA Platform project is separate and must use its own project repository. Do not connect the project repository as this repository's remote.

## Anti-drift
Use the current GitHub state rather than reconstructing progress from chat history when the state is available. Do not treat Library copies or old chat handovers as live authority.

## Project vehicle
The AI QA Platform is the primary learning vehicle for the curriculum. Practice Software Testing — Toolshop is the default external system under test for UI and documented REST API exercises, as specified in the continuity rules.
