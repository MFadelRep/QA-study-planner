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
1. Read 01_CURRENT_STATE.md first and identify the exact next action and unresolved blockers.
2. Read 02_CURRICULUM_INDEX.md to orient within the curriculum.
3. Read relevant sections of 03_MASTER_PLAN.md and 08_ISTQB_TESTING_PORTFOLIO.md for the current capability.
4. Apply 04_CONTINUITY_RULES.md as the operating authority.
5. Consult only the relevant entries in 09_LESSONS_LEARNED.md before implementation; use them as reusable knowledge, not as live state or a replacement for the plan.
6. Resume from the exact next action without restarting completed work or requiring reconstruction of known progress.
7. Verify real execution results before marking work complete.
8. After a meaningful verified slice, update the live checkpoint and refresh derived handovers to the same state version when appropriate. Record reusable, evidence-backed technical lessons in 09_LESSONS_LEARNED.md according to 04_CONTINUITY_RULES.md.

## Startup scope
This file defines routing only. Workflow, batching, teaching depth, test strategy, handover handling, and safe-write instructions are defined in `04_CONTINUITY_RULES.md`. Live progress and the exact next action are defined only in `01_CURRENT_STATE.md`. Reusable, evidence-backed technical takeaways are in `09_LESSONS_LEARNED.md`. This file must not copy the live checkpoint or duplicate detailed operating rules.

## Conversation safety reminder
The user's global ChatGPT Custom Instructions should include the short Conversation Safety Warning reminder so the assistant can warn about long conversations across chats. The detailed study-chat rule lives in `04_CONTINUITY_RULES.md`. This repository does not automatically load into an unrelated new chat; the user starts with `STUDY` to trigger recovery.

## Repository separation
This repository manages study progress only. The Workbench QA Lab application is in the separate repository `MFadelRep/QA-practice-platform-app`; its learner branch is `learn/rag-unit-tests`. Do not connect the application repository as this repository's remote or place application/test code in the study-control repository.

## Anti-drift
Use the current GitHub state rather than reconstructing progress from chat history when the state is available. Do not treat Library copies or old chat handovers as live authority.

## Project vehicle
Workbench QA Lab in `MFadelRep/QA-practice-platform-app`, branch `learn/rag-unit-tests`, is the primary system under test and hands-on learning project. The learner authors test implementations in curriculum order; `main` preserves completed reference tests and implementations. Practice Software Testing — Toolshop remains an optional external SUT when a specific public storefront/API scenario benefits from it or Workbench cannot exercise the requirement.
