# Study Control Center — GitHub Boot

Status: LIVE
Repository: MFadelRep/QA-study-planner
Control Center path: study-control-center/
Purpose: STUDY PROGRESS MANAGEMENT ONLY

## Startup keyword
STUDY

## Mandatory startup rule
When the user types `STUDY` in a new chat, use the **GitHub Study Control Center in this repository as the primary authority**.
Do NOT use the Library Control Center copies as the live study authority.
The Library contains only a small bridge/fallback because Library retrieval/upload limits can occur.

## Boot protocol
1. Read `01_CURRENT_STATE.md`.
2. Read `02_CURRICULUM_INDEX.md`.
3. Retrieve only the relevant Master Plan section for the current work.
4. Apply `04_CONTINUITY_RULES.md`.
5. Resume the exact NEXT ACTION.
6. Verify the real result before advancing.
7. Record verified state in `01_CURRENT_STATE.md`.

## Authority
GitHub is the authoritative source for live study state, curriculum-control documents, continuity rules, and derived handovers.

## Separation from project repository
The user's local AI QA Platform project is a separate repository.
Do not connect the local project repository to this study-control repository.
This repository exists solely to manage study progress.

## Anti-drift
Do not restart completed work.
Do not reconstruct progress from chat history when GitHub state exists.
Do not treat Library copies as authoritative.

## Project vehicle
The AI QA Platform is the primary learning vehicle for the 45-hour Senior QA Automation + MLOps curriculum.
