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

STATE_VERSION = "5.0-BATCH-FIRST-ISTQB-PORTFOLIO-2026-10-12"
DAY = "1"
HOUR = "5"
TOPIC = "Toolshop UI automation batch — fix two failures, then expand UI + ISTQB portfolio coverage"


def make_fixture(root: Path) -> None:
    control = root / "study-control-center"
    tools = root / "tools"
    control.mkdir(parents=True)
    tools.mkdir(parents=True)

    rules = """# Continuity & Execution Rules

## Single-authority principle
One canonical source for each information type.

## Default learning workflow — batch-first
BUILD → RUN → VERIFY → BRIEF EXPLANATION → NEXT CAPABILITY

## Coverage-first, learn-on-demand rule
Complete code and grouped batches; deeper explanation on demand.

## Safe GitHub write protocol
READ → preserve current content → minimal changes → WRITE with current SHA → READ AGAIN → verify

## Control-center validation
Read-only guardrail.
"""
    state = f"""# Current Study State

**State version:** {STATE_VERSION}
**Last verified:** 2026-10-12
**Status:** ACTIVE — accelerated seven-day sprint

## Position
- Day: {DAY}
- Hour: {HOUR}
- Current topic: {TOPIC}
- Project: AI QA Platform

## Exact next action
Build one focused correction batch, verify the two known failures, then continue.
"""
    index_rows = "\n".join(
        f"| {number} | Focus {number} |" for number in range(1, 46)
    )
    index = f"""# Curriculum Index — 45-Hour Capability Catalogue

This index is a locator. Full scope is in {BT}03_MASTER_PLAN.md{BT} and portfolio coverage is in {BT}08_ISTQB_TESTING_PORTFOLIO.md{BT}.

| Hour | Focus |
|---:|---|
{index_rows}

## Accelerated weekly map
Seven integrated days.

## Phase gates
1–4 Foundations

Required strengthened areas: UI, API, ISTQB, security, RAG.
"""
    master = """# Master Plan

## Outcome
Build a coherent platform.

## Learning method
Follow the continuity rules.

## Project
AI QA Platform.

## Required capability coverage
Playwright, API, SQL, CI/CD, performance, containers, AI/RAG, MLOps, ISTQB.

## 45-hour capability catalogue
Full curriculum scope.

## Accelerated seven-day schedule
Integrated weekly plan.

## ISTQB integration
Use study-control-center/08_ISTQB_TESTING_PORTFOLIO.md.

## Evidence standard
Observable project evidence.

## Plan-change rule
Required outcomes must not be silently removed.
"""
    portfolio = """# ISTQB Foundation Testing Portfolio

## Purpose and source
ISTQB CTFL v4.0.1.

## Test levels
Component, integration, system, acceptance.

## Test types
Functional, non-functional, black-box, white-box.

## Test design techniques
Equivalence partitioning, boundary value analysis, decision table testing, state transition testing.

## Non-functional quality characteristics
Performance, compatibility, usability, reliability, security, maintainability, portability, safety.

## Static testing and review
Review requirements, test cases, code.

## Test management, risk, and defects
Plan, trace, report, confirm and regress.

## Automated vs manual evidence
Automation plus manual judgment.

confirmation testing verifies a fix; regression testing checks related areas.
"""
    boot = """# Study Control Center — GitHub Boot

Repository: MFadelRep/QA-study-planner

## Mandatory startup rule
Use GitHub as the authoritative source.

## Boot protocol
1. Read 01_CURRENT_STATE.md.
2. Read 02_CURRICULUM_INDEX.md.
3. Retrieve the relevant Master Plan section.
3. Retrieve the relevant section of 03_MASTER_PLAN.md.
4. Apply 04_CONTINUITY_RULES.md and consult 08_ISTQB_TESTING_PORTFOLIO.md.

Do not use Library Control Center copies as the live study authority.
This file defines routing only.
The project uses a separate repository.
"""
    recovery = f"""# New Chat Recovery

Read {BT}01_CURRENT_STATE.md{BT}.
Apply {BT}04_CONTINUITY_RULES.md{BT}.
Consult {BT}08_ISTQB_TESTING_PORTFOLIO.md{BT}.

The live checkpoint is always read from {BT}01_CURRENT_STATE.md{BT} at recovery time.
Do not store a copied checkpoint in this recovery file.
The local project uses a different GitHub repository.
"""
    short = f"""# SHORT HANDOVER — CURRENT

Canonical state version: {STATE_VERSION}

**Derived record — not authoritative.** Live state is {BT}01_CURRENT_STATE.md{BT}; workflow is {BT}04_CONTINUITY_RULES.md{BT}.

State: Day {DAY} / Hour {HOUR}
Topic: {TOPIC}

Immediate next action:
Correct the two known UI test failures.
"""
    long = f"""# LONG HANDOVER — CURRENT RECORD

Canonical state version: {STATE_VERSION}

**Derived record — not authoritative.** Live state is {BT}01_CURRENT_STATE.md{BT}; workflow is {BT}04_CONTINUITY_RULES.md{BT}.

## Session state
Day {DAY} / Hour {HOUR}
Topic: {TOPIC}

## Exact resume action
Correct the two known UI test failures.
"""
    (control / "00_BOOT.md").write_text(boot, encoding="utf-8")
    (control / "01_CURRENT_STATE.md").write_text(state, encoding="utf-8")
    (control / "02_CURRICULUM_INDEX.md").write_text(index, encoding="utf-8")
    (control / "03_MASTER_PLAN.md").write_text(master, encoding="utf-8")
    (control / "04_CONTINUITY_RULES.md").write_text(rules, encoding="utf-8")
    (control / "05_SHORT_HANDOVER.md").write_text(short, encoding="utf-8")
    (control / "06_LONG_HANDOVER.md").write_text(long, encoding="utf-8")
    (control / "07_NEW_CHAT_RECOVERY.md").write_text(recovery, encoding="utf-8")
    (control / "08_ISTQB_TESTING_PORTFOLIO.md").write_text(portfolio, encoding="utf-8")
    (root / "README.md").write_text(
        "Study control system: study-control-center/08_ISTQB_TESTING_PORTFOLIO.md; "
        "workflow in 04_CONTINUITY_RULES.md; CTFL v4.0.1; accelerated seven-day plan.\n",
        encoding="utf-8",
    )
    (tools / "README.md").write_text(
        "batch-first workflow; 08_ISTQB_TESTING_PORTFOLIO.md; "
        "python3 tools/validate_control_center.py; "
        "python3 -m unittest discover -s tests -v\n",
        encoding="utf-8",
    )


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
                path.read_text(encoding="utf-8") + "\n## Safe GitHub write protocol\n",
                encoding="utf-8",
            )
            errors = validator.validate(root)
            self.assertTrue(any("must exist only in 04_CONTINUITY_RULES.md" in error for error in errors))

    def test_missing_curriculum_hour_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_fixture(root)
            path = root / "study-control-center" / "02_CURRICULUM_INDEX.md"
            text = path.read_text(encoding="utf-8").replace("| 17 | Focus 17 |", "")
            path.write_text(text, encoding="utf-8")
            errors = validator.validate(root)
            self.assertTrue(any("expected exactly hours 1-45" in error for error in errors))

    def test_handover_version_mismatch_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_fixture(root)
            path = root / "study-control-center" / "05_SHORT_HANDOVER.md"
            text = path.read_text(encoding="utf-8").replace(STATE_VERSION, "4.6-OLD-VERSION", 1)
            path.write_text(text, encoding="utf-8")
            errors = validator.validate(root)
            self.assertTrue(any("Canonical state version" in error for error in errors))

    def test_missing_current_state_next_action_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_fixture(root)
            path = root / "study-control-center" / "01_CURRENT_STATE.md"
            text = path.read_text(encoding="utf-8").split("## Exact next action", 1)[0]
            path.write_text(text, encoding="utf-8")
            errors = validator.validate(root)
            self.assertTrue(any("Exact next action is missing or empty" in error for error in errors))

    def test_legacy_micro_step_workflow_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_fixture(root)
            path = root / "study-control-center" / "05_SHORT_HANDOVER.md"
            path.write_text(
                path.read_text(encoding="utf-8") + "\nBefore every terminal block:\n",
                encoding="utf-8",
            )
            errors = validator.validate(root)
            self.assertTrue(any("Before every terminal block:" in error for error in errors))

    def test_missing_istqb_technique_coverage_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            make_fixture(root)
            path = root / "study-control-center" / "08_ISTQB_TESTING_PORTFOLIO.md"
            text = path.read_text(encoding="utf-8").replace("## Test design techniques", "## Design")
            path.write_text(text, encoding="utf-8")
            errors = validator.validate(root)
            self.assertTrue(any("Test design techniques" in error for error in errors))


if __name__ == "__main__":
    unittest.main(verbosity=2)
