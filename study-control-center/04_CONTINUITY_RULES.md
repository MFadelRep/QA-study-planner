# Continuity & Execution Rules

## Authority
- Master Plan = required capabilities, accelerated schedule, and evidence outcomes.
- Curriculum Index = curriculum locator and weekly map.
- Current State = live position, verified results, blockers, and exact next action.
- Continuity Rules = the single authority for study workflow, learning depth, continuity, safe writes, and execution behavior.
- ISTQB Testing Portfolio = the canonical mapping of CTFL topics to practical/manual/automated exercises.
- Short/Long Handovers = derived records; never authoritative.
- GitHub is the authoritative study-control source. Library copies are fallback only.

## Single-authority principle
Each authoritative information type has one canonical source.

| Information | Canonical source |
|---|---|
| Required capability outcomes and compressed seven-day schedule | `03_MASTER_PLAN.md` |
| Curriculum navigation | `02_CURRICULUM_INDEX.md` |
| ISTQB manual/automated testing coverage map | `08_ISTQB_TESTING_PORTFOLIO.md` |
| Live checkpoint and exact next action | `01_CURRENT_STATE.md` |
| Learning workflow, batching, learning depth, safe GitHub writes, state/handover rules | `04_CONTINUITY_RULES.md` |
| New-chat startup routing | `00_BOOT.md` |
| New-chat recovery procedure | `07_NEW_CHAT_RECOVERY.md` |
| Short/long handovers | `05_SHORT_HANDOVER.md` / `06_LONG_HANDOVER.md`, derived only |

Do not create competing copies of current progress, the detailed learning workflow, the write protocol, or curriculum requirements. Other documents may link to the canonical source and state their role. A derived handover may summarize state but cannot override `01_CURRENT_STATE.md`.

## Startup
When the user types `STUDY` in a new chat:
1. Follow `00_BOOT.md`.
2. Read `01_CURRENT_STATE.md` and identify the exact next action, known output, blockers, and whether proposed fixes have actually run.
3. Use `02_CURRICULUM_INDEX.md` to orient and read only relevant sections from `03_MASTER_PLAN.md` and `08_ISTQB_TESTING_PORTFOLIO.md`.
4. Apply these rules and resume the existing project state.
5. Do not ask the user to reconstruct known progress or redo completed setup. When the repo or project file is available, inspect it before generating a replacement.

## Conditional interview-priority overlay

At each `STUDY` startup, inspect the conditional interview status recorded in `01_CURRENT_STATE.md`.

- If the Ghaia technical-interview outcome or next-round status is still unknown, ask one brief status question before choosing the day's priority. If there is no confirmed next round, resume the saved study action.
- If the user confirms passing the technical round or confirms a final Project Manager interview is scheduled, temporarily activate the interview track defined in `03_MASTER_PLAN.md` (estimated 4–6 focused hours over 2–3 days, adapted to the date and observed gaps).
- While the interview track is active, preserve the existing Day/Hour, project files, blockers, and exact next action. Do not mark curriculum work complete, reset the plan, or discard pending local work.
- After the interview or when the user asks to resume normal study, return to the canonical next action in `01_CURRENT_STATE.md`.
- The interview overlay is conditional and must not divert study time solely because an interview might happen.

## Default learning workflow — batch-first
The required cadence is **BUILD → RUN → VERIFY → BRIEF EXPLANATION → NEXT CAPABILITY**.

- **BUILD:** Prepare the full useful slice, not a tiny isolated step. Combine related actions, features, tests, setup, and supporting files. If multiple files are required, provide them together in one cohesive delivery or a small number of grouped messages (usually no more than three).
- **RUN:** Give complete, copy-pasteable terminal blocks or complete file contents. Where safe, combine backups, file creation/patching, and the focused run into the same block. The assistant cannot directly modify the user's local laptop through chat; be clear when the user must run a supplied block locally.
- **VERIFY:** Use actual terminal output, reports, or file state. Distinguish passed, failed, skipped, and not-yet-run work. Never infer a run succeeded just because code was written.
- **BRIEF EXPLANATION:** Explain the purpose, important reusable patterns, and expected result briefly after the code has been exercised. Do not teach every line before the user can try it.
- **NEXT CAPABILITY:** Move to the next useful area once the current slice works well enough. Do not linger on cosmetic or low-risk imperfections.

## Coverage-first, learn-on-demand rule
The user is in a time crunch and explicitly wants broad practical coverage before deep mastery. Supply the complete code so the user has it available to read, execute, and question later. The user may stop the flow whenever a concept is confusing or blocks a dependent topic; otherwise keep advancing. Do not require the user to explain code back, solve every implementation step unaided, or study every line before continuing.

For every subject—not only UI automation—batch related material aggressively: Playwright UI tests by feature, API tests in compact suites, SQL examples and checks together, CI/CD configuration plus validation, performance scenarios plus analysis, Docker/Compose build and run, Kubernetes manifests plus test execution, and AI/RAG/MLOps implementation with evaluation. Use coherent file boundaries rather than forcing everything into one enormous file. A batch may be split into a few messages if that avoids missing supporting files or produces an unwieldy block; never fragment it into one test/action per message without a real need.

Prefer breadth, integration, and a working project path over exhaustive mastery of isolated basics. Explain deeper theory when the user asks, says they are lost, or a critical dependency is blocking the build. If there is a small nonblocking imperfection, record it and proceed. If the capability works, move on. Investigate only a genuine failure, security/correctness risk, or recurring instability. Fix related failures together; run failing tests narrowly first when appropriate, then run the combined suite after the batch stabilizes. Avoid repeated full-suite runs that add no evidence.

## ISTQB testing portfolio rule
Apply the coverage map in `08_ISTQB_TESTING_PORTFOLIO.md` during UI, API, integration, performance, and senior-QA work. Include manual test design and testing techniques, levels/types, static reviews, non-functional assessment, risk, defect reporting, confirmation/regression, and test completion where relevant. Maintain the useful manual artifacts and automate suitable repeatable cases. Do not claim every testing technique or quality characteristic can be fully proven through Playwright. Record environment/access limits and use a controlled project component or secondary target when needed.

## Pace and user control
- Default to FAST-PACE, batch-first work.
- `SLOW DOWN`, `TOO MUCH`, and `I'M LOST` mean reduce scope and explain the blocking idea more deeply.
- `FAST` returns to larger integrated batches.
- `SKIP` means record the gap and continue when it does not block dependent work.
- Ask a clarifying question only when a missing fact truly prevents safe or meaningful progress. Otherwise make a sensible, stated assumption and proceed.
- Keep updates useful and concise; do not narrate tool activity as filler.

## Result verification
- Never claim a command ran without actual evidence.
- Treat the user's real output as the source of truth.
- When a test fails, use the actual failure details; repair the related cases as a batch while preserving passing coverage.
- Prefer condition-based assertions over fixed sleeps. Do not add diagnostic waits or broaden investigations without evidence.
- Use one worker during local test development when resource contention or noisy parallel runs would distort the result; return to normal concurrency later when useful.

## Terminal delivery style
- Group related commands into one copy-pasteable block and explain the block's purpose and expected outcome briefly.
- Include backup/preservation steps when replacing a file that may already contain useful work.
- Use direct-output commands such as `cat`, `sed`, and `git --no-pager` instead of sending the user into an interactive pager.
- Explain a command or syntax detail only when it materially affects safety, correctness, or the user's ability to execute the block. Do not make the user approve each line independently.
- Never discard the user's local changes, overwrite unknown content, or use a destructive command merely to simplify the workflow.

## Conversation safety warning
Reassess conversation length and complexity, including pasted code, files, and long exchanges. If the conversation appears long, give a concise **CAUTION** recommending that the user prepare a transition. If it appears critically long or a transition seems prudent, give a clear **CRITICAL CONVERSATION SAFETY WARNING** and recommend preserving verified work and opening a new chat. Do not claim to know an exact remaining message/token count or promise a warning exactly one or two messages before a limit. This is a best-effort warning, not a guaranteed predictor.

A warning alone does not trigger a checkpoint. If a new chat starts before a checkpoint, reconcile any supplied messages with the current GitHub checkpoint and actual project evidence before changing canonical state. Do not blindly overwrite either source.

## State maintenance
After a meaningful verified slice, update `01_CURRENT_STATE.md` with the position, current project slice, verified completion, known failures/limitations, blockers, and the exact next action. Advance the state version for every meaningful state update. Keep live state concise; put useful historical context in `06_LONG_HANDOVER.md`. Never mark proposed or supplied-but-unrun corrections as completed.

## Handover
`HANDOVER` refreshes `05_SHORT_HANDOVER.md`; `LONG HANDOVER` refreshes `06_LONG_HANDOVER.md`. Both are derived from the newest Current State and must carry the same canonical state version, Day/Hour, topic, and resume direction. The validator is expected to detect stale handovers. The new chat must read Current State first even when a handover is available.

## Safe GitHub write protocol
Required sequence: **READ → preserve current content → minimal changes → WRITE with current SHA → READ AGAIN → verify**.

For this Study Control Center, use the lower-level Git object workflow. Prior Contents API writes were blocked; do not retry a blocked Contents API write. For each coordinated update:

1. Read `refs/heads/main` and record the branch-head commit SHA.
2. Fetch every target file and preserve its complete content and blob SHA. Confirm the branch head and file SHAs have not changed since the audit.
3. Apply the necessary minimal edits. When a full coherent replacement is needed, base it on the freshly read content and preserve unrelated verified facts.
4. Create blobs for the complete UTF-8 contents of changed files.
5. Create a tree from the current commit's base tree, replacing only the intended paths. Include the new blob for any new file.
6. Create one commit whose parent is the exact current branch-head SHA.
7. Update `main` using the original head as `expected_sha` (force-with-lease). If rejected or if the head changed, stop and repeat the read/preserve/edit process with the new head; never blindly retry.
8. Read each changed file and the branch head again.
9. Verify exact contents, blob SHAs, commit parent, and intended new head. Report success only after read-back verification.

The lower-level workflow does not permit bypassing concurrency checks or overwriting newer work.

## Control-center validation
`tools/validate_control_center.py` is read-only. It checks required files, the single-authority structure, 45-hour catalogue completeness, current-state/handover freshness, ISTQB coverage, batch-first workflow requirements, legacy-workflow drift, and repository separation. Its unit tests live in `tests/test_validate_control_center.py`. GitHub Actions runs the tests and validator on pushes and pull requests.

The validator is a guardrail, not an authority. A passing deterministic check does not replace judgment or real project/test evidence. The validator and its tests must never rewrite control-center state.

## Anti-drift
Do not restart completed work. Do not merge contradictory versions. Do not silently remove a required capability. Keep the study-control repository separate from the AI QA Platform repository. Never report a test, local edit, or checkpoint as successful without evidence.

## Practice application selection
The default external system under test (SUT) is **Practice Software Testing — Toolshop**:
- UI: https://practicesoftwaretesting.com/
- REST API documentation: https://api.practicesoftwaretesting.com/api/documentation

Use Toolshop first for UI automation, documented REST API tests, search/filter/cart/auth workflows, and combined API/UI checks. Inspect current API documentation before relying on endpoints because the hosted demo can change. Treat it as a third-party practice environment: use non-destructive and reasonable traffic, do not assume data persists, and do not depend on undocumented behavior.

Two secondary practice sites are approved for appropriate gaps:
1. **Expand Testing** — https://practice.expandtesting.com/ — isolated UI scenarios and focused forms, dynamic controls, tables, pagination, locators, status codes, and its dedicated API exercises.
2. **QA Practice API Playground** — https://www.qapractice.com/api-playground — compact REST API scenarios for token authentication, products, users, orders, and explicit positive/negative login responses.

Start with Toolshop; switch only when a secondary site's stated use case materially fits the current goal or Toolshop cannot exercise the scenario reliably. Do not build our own SUT unless public targets cannot support a required scenario (for example, controlled fault injection, direct database assertions, or custom AI/RAG inference behavior).
