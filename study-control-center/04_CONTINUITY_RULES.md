# Continuity & Execution Rules

## Authority
- Master Plan = what capability coverage is required.
- Continuity Rules = how learning and state preservation work.
- Current State = where the study actually is and the exact next action.
- Handovers are derived records.
- Once this GitHub system is promoted, GitHub is authoritative and Library copies are fallback only.

## Single-authority principle
Each authoritative piece of study information has exactly one canonical source in this control center.

| Information | Canonical source |
|---|---|
| Required capability coverage and 45-hour curriculum | `03_MASTER_PLAN.md` |
| Curriculum navigation/locator | `02_CURRICULUM_INDEX.md` |
| Live study position and exact next action | `01_CURRENT_STATE.md` |
| Study operating/continuity rules, including safe GitHub write protocol | `04_CONTINUITY_RULES.md` |
| New-chat startup routing | `00_BOOT.md` |
| New-chat recovery procedure | `07_NEW_CHAT_RECOVERY.md` |
| Short/long handovers | `05_SHORT_HANDOVER.md` / `06_LONG_HANDOVER.md` — derived records only |

Other control-center files may reference canonical information, but must not create competing copies of authoritative rules, live state, or curriculum requirements. Handovers may summarize current state because they are derived records; they never override `01_CURRENT_STATE.md` or `04_CONTINUITY_RULES.md`.

Do not store a second copy of the GitHub write protocol, current resume state, or master-plan requirements in another control-center file.

## Startup
On `STUDY`:
1. Read `00_BOOT.md`.
2. Read `01_CURRENT_STATE.md`.
3. Use `02_CURRICULUM_INDEX.md` to locate the needed scope.
4. Read only the relevant part of `03_MASTER_PLAN.md`.
5. Apply these rules.
6. Resume the exact NEXT ACTION.

## Project-first learning
Build → Check → Learn on demand → Fix/Verify → Continue.

Use meaningful project implementation slices when competence is demonstrated. Teach isolated theory only when a real gap requires it.

## Pace
FAST-PACE is the default.
`SLOW DOWN`, `TOO MUCH`, and `I'M LOST` mean smaller steps and more explanation.
`FAST` restores larger slices.

## Result verification
- Never claim a command ran without actual evidence.
- Use the user's real output as the source of truth.
- When wrong, make the smallest useful correction, retry, and re-check.

## State maintenance
After a meaningful verified slice, update `01_CURRENT_STATE.md` with:
- day/hour
- current topic/project slice
- verified completion
- exact next action
- blockers/gaps
- timestamp/version

Do not put long history into Current State.

## Handover
`HANDOVER` refreshes Short Handover.
`LONG HANDOVER` refreshes Long Handover.
Short Handover is for fresh-chat resume.
Long Handover is the durable historical record.

## Terminal teaching rule
Before every terminal block:
- explain every command line;
- explain important flags/operators/shell syntax;
- state what result we expect;
- then give the small practical action;
- wait for the actual result before advancing.

## Safe GitHub write protocol
For any future Study Control Center GitHub checkpoint or other write/update operation:
1. READ the current live file first.
2. Preserve the existing content; do not reconstruct the whole file from memory.
3. Make only the minimal targeted changes required.
4. WRITE using the current blob SHA as the optimistic concurrency check.
5. Commit only the intended file/change.
6. READ the file again after the write.
7. Verify the exact committed content and new blob SHA before reporting success.

Preferred workflow: **READ → preserve current content → minimal changes → WRITE with current SHA → READ AGAIN → verify**.

If a write is rejected or the SHA has changed, stop and re-read the live file before retrying. Do not overwrite blindly.

## Anti-drift
Never restart completed work.
Never merge contradictory versions.
Never silently remove required curriculum coverage.
Never use the old `playwright-course` directory.
