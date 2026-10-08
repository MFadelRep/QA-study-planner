from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

BT = chr(96)

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "tools" / "validate_control_center.py"

spec = importlib.util.spec_from_file_location("control_validator", VALIDATOR_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError("Could not load validator module")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


STATE_VERSION = "3.2-GITHUB-CHECKPOINT"
DAY = "1"
HOUR = "1"
TOPIC = "TypeScript project foundation — typed QA test-result model"


def make_fixture(root: Path) -> None:
    control = root / "study-control-center"
    control.mkdir(parents=True)

    rules = """# Continuity & Execution Rules

## Single-authority principle
Each authoritative piece of study information has exactly one canonical source.

## Safe GitHub write protocol
READ → preserve current content → minimal changes → WRITE with current SHA → READ AGAIN → verify

## Control-center validation
Read-only validator.

## Anti-drift
Never restart completed work.
"""

    state = f"""# Current Study State

**State version:** {STATE_VERSION}
**Last verified:** 2026-10-08
**Status:** ACTIVE

## Position
- Day: {DAY}
- Hour: {HOUR}
- Current topic: {TOPIC}
- Project: AI QA Platform

## Exact next action
Do the next verified project action.
"""

    index_rows = "\n".join(
        f"| {number} | Focus {number} |" for number in range(1, 46)
    )
    index = f"""# Curriculum Index — 45 Hours

This index is a locator; the complete scope is in {BT}03_MASTER_PLAN.md{BT}.

| Hour | Focus |
|---:|---|
{index_rows}

## Phase gates
1–4 Foundations

Required strengthened areas: architecture, API validation, security.
"""

    master = """# Senior QA Automation + MLOps — Master Plan

## Outcome
Senior-level QA automation + MLOps capability.

## Execution model
Build → Check → Learn on demand → Fix/Verify → Continue.

## Project
One coherent AI QA Platform.

## Required capability coverage
Playwright, API, AI QA, RAG, MLOps, Security.

## 45-hour scope
Full curriculum.

## Evidence standard
Observable project evidence.

## Plan-change rule
Required outcomes must not be silently removed.
"""

    boot = """# Study Control Center — GitHub Boot

Status: LIVE
Repository: MFadelRep/QA-study-planner

## Mandatory startup rule
Use GitHub as primary authority.

## Boot protocol
1. Read 01_CURRENT_STATE.md.
2. Read 02_CURRICULUM_INDEX.md.
3. Read 03_MASTER_PLAN.md.
4. Apply 04_CONTINUITY_RULES.md.

Do NOT use the Library Control Center copies as the live study authority.

this boot file only defines startup routing and must not duplicate live state or detailed operating rules.

MFadelRep/QA-study-planner is a separate repository.
"""

    recovery = f"""# NEW CHAT RECOVERY

## Required behavior
Read {BT}01_CURRENT_STATE.md{BT} first.
Apply {BT}04_CONTINUITY_RULES.md{BT}.

The live checkpoint is always read from {BT}01_CURRENT_STATE.md{BT} at recovery time.
Do not store a copied checkpoint in this recovery file.

This recovery file belongs to a different GitHub repository from the local project.
"""

    short = f"""# SHORT HANDOVER — CURRENT

Canonical state version: {STATE_VERSION}

**Derived record — not authoritative.** The live study state is {BT}01_CURRENT_STATE.md{BT}; operating rules are {BT}04_CONTINUITY_RULES.md{BT}.

State: Day {DAY} / Hour {HOUR} — in progress
Topic: {TOPIC}

Immediate next action:
Do the next verified project action.
"""

    long = f"""# LONG HANDOVER — CURRENT RECORD

Canonical state version: {STATE_VERSION}

**Derived record — not authoritative.** The live study state is {BT}01_CURRENT_STATE.md{BT}; operating rules are {BT}04_CONTINUITY_RULES.md{BT}.

## Session state
Day {DAY} / Hour {HOUR}
Topic: {TOPIC}

## Exact resume action
Do the next verified project action.
"""

    files = {
        "00_BOOT.md": boot,
        "01_CURRENT_STATE.md": state,
        "02_CURRICULUM_INDEX.md": index,
        "03_MASTER_PLAN.md": master,
        "04_CONTINUITY_RULES.md": rules,
        "05_SHORT_HANDOVER.md": short,
        "06_LONG_HANDOVER.md": long,
        "07_NEW_CHAT_RECOVERY.md": recovery,
    }

    for name, content in files.items():
        (control / name).write_text(content, encoding="utf-8")


class ValidatorTests(unittest.TestCase):
    def test_clean_control_center_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_fixture(root)
            self.assertEqual(validator.validate(root), [])

    def test_validator_is_read_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_fixture(root)
            before = {
                path.relative_to(root): path.read_bytes()
                for path in root.rglob("*")
                if path.is_file()
            }

            self.assertEqual(validator.validate(root), [])

            after = {
                path.relative_to(root): path.read_bytes()
                for path in root.rglob("*")
                if path.is_file()
            }
            self.assertEqual(before, after)

    def test_stale_recovery_checkpoint_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_fixture(root)
            path = root / "study-control-center" / "07_NEW_CHAT_RECOVERY.md"
            path.write_text(
                path.read_text(encoding="utf-8") + "\nTS18003\n",
                encoding="utf-8",
            )

            errors = validator.validate(root)

            self.assertTrue(any("TS18003" in error for error in errors))

    def test_duplicated_write_protocol_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_fixture(root)
            path = root / "study-control-center" / "00_BOOT.md"
            path.write_text(
                path.read_text(encoding="utf-8")
                + "\n## Safe GitHub write protocol\n",
                encoding="utf-8",
            )

            errors = validator.validate(root)

            self.assertTrue(
                any("must exist only in 04_CONTINUITY_RULES.md" in error for error in errors)
            )

    def test_missing_curriculum_hour_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_fixture(root)
            path = root / "study-control-center" / "02_CURRICULUM_INDEX.md"
            text = path.read_text(encoding="utf-8")
            text = text.replace("| 17 | Focus 17 |", "")
            path.write_text(text, encoding="utf-8")

            errors = validator.validate(root)

            self.assertTrue(any("expected exactly hours 1-45" in error for error in errors))

    def test_handover_version_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_fixture(root)
            path = root / "study-control-center" / "05_SHORT_HANDOVER.md"
            text = path.read_text(encoding="utf-8").replace(
                STATE_VERSION, "3.1-OLD-VERSION", 1
            )
            path.write_text(text, encoding="utf-8")

            errors = validator.validate(root)

            self.assertTrue(
                any("Canonical state version" in error for error in errors)
            )

    def test_missing_current_state_next_action_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_fixture(root)
            path = root / "study-control-center" / "01_CURRENT_STATE.md"
            text = path.read_text(encoding="utf-8")
            text = text.split("## Exact next action", 1)[0]
            path.write_text(text, encoding="utf-8")

            errors = validator.validate(root)

            self.assertTrue(
                any("Exact next action is missing or empty" in error for error in errors)
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
