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

## Conversation Safety Warning (cross-chat safeguard)

Purpose: warn the user when the current conversation appears to be approaching a risky length, so they have a chance to prepare a new chat. This safeguard does **not** change the study workflow, create automatic checkpoints, or require a GitHub commit after each message.

- Reassess conversation length and complexity while responding, considering substantial pasted code, files, handovers, and long exchanges.
- If the conversation appears to be getting long, give a concise **CAUTION** warning recommending that the user prepare to transition soon.
- If it appears critically long or continued discussion seems risky, give a clear **CRITICAL CONVERSATION SAFETY WARNING** in the current response and recommend switching chats / preserving any needed work now.
- Be conservative, but do not interrupt ordinary study unnecessarily.
- Never claim to know an exact remaining message/token count or promise a warning exactly one or two messages before a limit. The model may not have a reliable live context-capacity indicator; this is a best-effort early warning, not a guaranteed cutoff predictor.
- If the user starts a new chat with the Study Control Center, apply this rule during startup and ongoing work. The short global Custom Instructions reminder is the cross-chat trigger; this GitHub document remains the canonical detailed procedure for study chats.
- If a transition happens without a checkpoint, the user may paste the missing messages and say `RECOVER FROM UNCHECKPOINTED MESSAGES`. Reconcile those messages with canonical state and actual project evidence before continuing; do not blindly overwrite either source.
- A warning alone does not trigger a checkpoint or handover. Follow the existing checkpoint / handover commands and safe GitHub write protocol unchanged.

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

## Non-interactive terminal output and pager avoidance

- Prefer commands that print directly to the terminal; do not send the user into an interactive pager just to inspect output.
- When reading one or more project files, use direct-output commands such as `cat`. For multiple files, prefer this copy-pasteable pattern and substitute the required paths:
  ```bash
  for file in src/index.ts tests/toolshop.spec.ts tsconfig.json; do
    printf '\n===== %s =====\n' "$file"
    cat "$file"
  done
  ```
- For Git commands that may open a pager, prefix the command with `git --no-pager` (for example, `git --no-pager diff` or `git --no-pager log -1 --oneline`).
- Do **not** tell the user to press `q` to exit a pager when a direct-output alternative is available.
- Do **not** disable Git's pager globally or change global Git configuration as a workaround. Use the per-command `git --no-pager` form instead.
- Give the direct-output command in the first place; do not first provide the pager-triggering command and then correct it after the user encounters the issue.

## State maintenance
After a meaningful verified slice, update `01_CURRENT_STATE.md` with:
- day/hour
- current topic/project slice
- verified completion
- exact next action
- blockers/gaps
- timestamp/version

Do not put long history into Current State.
Every meaningful Current State update must advance the State version. Derived handovers must be refreshed to the new canonical state version; the validator checks that they match.

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

Required sequence: **READ → preserve current content → minimal changes → WRITE with current SHA → READ AGAIN → verify**.

For the Study Control Center, implement this with the low-level Git object workflow below: read the current branch head and target files; preserve the full content of each file; make only the necessary edits; create blobs; create a tree from the current base tree; create a commit parented to the current head; update the branch using the original head as the expected SHA; then read back the changed files and branch head and verify the exact content and SHAs. If the branch head changes, stop and re-read before rebuilding. Never report success until read-back verification passes.

## Default GitHub write protocol — low-level Git workflow
**This is the default and required write method for the Study Control Center. Do not use the GitHub Contents API write methods (`update_file` or `create_file`) for these files; they have repeatedly been blocked by tool safety checks. Do not retry a blocked Contents API write.**

For every checkpoint, rule change, handover refresh, or other Study Control Center write, follow this exact sequence:

1. **READ branch head:** fetch `refs/heads/main` and record the current commit SHA.
2. **READ target files:** fetch every file being changed and preserve its full current content and blob SHA.
3. **MINIMAL EDIT:** modify only the required sections; do not reconstruct unrelated content from memory.
4. **CREATE BLOB(S):** create a Git blob for each changed file's complete UTF-8 content.
5. **CREATE TREE:** create a new tree using the current commit's base tree SHA, with only the intended paths replaced by the new blob SHAs. This preserves all unrelated paths.
6. **CREATE COMMIT:** create one commit using that tree and the exact current branch-head commit as its parent.
7. **UPDATE REF WITH LEASE:** update `main` to the new commit using the original branch-head SHA as `expected_sha` (force-with-lease). If rejected, stop and re-read the branch head and target files before rebuilding; never blindly retry.
8. **READ AGAIN:** fetch each changed file from `main` and fetch the branch head again.
9. **VERIFY:** confirm the new branch head is the intended commit and every changed file has the exact intended content/new blob SHA. Report success only after this read-back verification.

Required sequence: **READ HEAD + FILES → PRESERVE → MINIMAL EDIT → BLOB(S) → TREE FROM CURRENT BASE TREE → COMMIT WITH CURRENT PARENT → UPDATE REF WITH EXPECTED SHA → READ BACK → VERIFY**.

The lower-level Git object workflow is not permission to bypass concurrency checks or overwrite newer work. Never update the ref if the branch head changed since step 1. Do not claim a checkpoint was saved unless the final read-back succeeds.

## Control-center validation
A read-only validator at `tools/validate_control_center.py` checks structural consistency, canonical-source ownership, stale duplicated state/rules, required curriculum coverage, handover freshness, and required cross-file references.

The GitHub Actions workflow at `.github/workflows/control-center-validation.yml` runs the validator on pull requests and pushes to `main`.

The validator is a guardrail, not an authority. It may fail a change when the repository violates these rules, but it must never rewrite control-center files or override canonical content. A passing validator proves the deterministic checks pass; semantic decisions still follow the canonical files and these continuity rules.

## Anti-drift
Never restart completed work.
Never merge contradictory versions.
Never silently remove required curriculum coverage.
Never use the old `playwright-course` directory.


## Practice application selection
The default external system under test (SUT) for the AI QA Platform is **Practice Software Testing — Toolshop**:
- UI: https://practicesoftwaretesting.com/
- REST API documentation: https://api.practicesoftwaretesting.com/api/documentation

Use Toolshop as the primary shared target for Playwright UI automation, documented REST API testing, authentication, product search/filtering, cart/checkout workflows, and combined API/UI checks. Inspect the current API documentation before writing tests because hosted demo systems can change. Treat it as a third-party practice environment: avoid destructive or abusive traffic, do not assume data persists, and do not depend on undocumented behavior.

Two secondary practice sites are approved for specific gaps:
1. **Expand Testing** — https://practice.expandtesting.com/
   Use when a lesson needs a focused, isolated UI scenario (dynamic controls, tables/pagination, locators, browser interactions, forms, status codes) or its dedicated Notes API / Practice API Swagger exercises. Switch to it when Toolshop does not expose a needed UI challenge or a smaller reproducible scenario would teach the skill more efficiently.
2. **QA Practice API Playground** — https://www.qapractice.com/api-playground
   Use as a focused supplementary REST API target for bearer-token authentication, products, users, orders, and explicit positive/negative login responses. Switch to it when practicing a compact API-only exercise or when Toolshop's API is unsuitable for a particular auth/status-code exercise.

Selection rule: start with Toolshop by default; use a secondary site only when its stated use case materially fits the current learning objective. Do not switch targets without a reason, and do not build our own SUT yet. Reconsider a small controlled local app later only if required scenarios cannot be reliably exercised on these public targets (for example, controlled fault injection, database-level assertions, or custom AI/RAG/inference behavior).
