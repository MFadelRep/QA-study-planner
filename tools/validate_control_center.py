#!/usr/bin/env python3
"""Read-only consistency and anti-drift validation for the Study Control Center."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED = [
    "00_BOOT.md",
    "01_CURRENT_STATE.md",
    "02_CURRICULUM_INDEX.md",
    "03_MASTER_PLAN.md",
    "04_CONTINUITY_RULES.md",
    "05_SHORT_HANDOVER.md",
    "06_LONG_HANDOVER.md",
    "07_NEW_CHAT_RECOVERY.md",
    "08_ISTQB_TESTING_PORTFOLIO.md",
]
SUPPORT_FILES = ["README.md", "tools/README.md"]
BT = chr(96)

LEGACY_WORKFLOW_FRAGMENTS = [
    "DO → CHECK → DETAILED EXPLANATION → CORRECT/RETRY → NEXT",
    "Before every terminal block:",
    "explain every command line;",
    "wait for the actual result before advancing.",
    "one terminal action at a time",
    "## Terminal teaching rule",
    "Build → Check → Learn on demand → Fix/Verify → Continue.",
    "Investigate its unusually long duration",
]


def validate(root: Path) -> list[str]:
    """Return deterministic validation errors without modifying files."""
    root = Path(root).resolve()
    control = root / "study-control-center"
    errors: list[str] = []
    docs: dict[str, str] = {}

    def error(message: str) -> None:
        errors.append(message)

    def must_contain(name: str, text: str, needle: str) -> None:
        if needle not in text:
            error(f"{name}: missing required text: {needle!r}")

    def must_not_contain(name: str, text: str, needle: str) -> None:
        if needle in text:
            error(f"{name}: contains forbidden/duplicated text: {needle!r}")

    for filename in REQUIRED:
        path = control / filename
        if not path.is_file():
            error(f"Missing required control-center file: {path.relative_to(root)}")
        else:
            docs[filename] = path.read_text(encoding="utf-8")

    support: dict[str, str] = {}
    for filename in SUPPORT_FILES:
        path = root / filename
        if not path.is_file():
            error(f"Missing required supporting document: {path.relative_to(root)}")
        else:
            support[filename] = path.read_text(encoding="utf-8")

    if errors:
        return errors

    rules = docs["04_CONTINUITY_RULES.md"]
    for required in [
        "## Single-authority principle",
        "## Default learning workflow — batch-first",
        "BUILD → RUN → VERIFY → BRIEF EXPLANATION → NEXT CAPABILITY",
        "## Coverage-first, learn-on-demand rule",
        "## Safe GitHub write protocol",
        "## Control-center validation",
        "READ → preserve current content → minimal changes → WRITE with current SHA → READ AGAIN → verify",
    ]:
        must_contain("04_CONTINUITY_RULES.md", rules, required)

    canonical_headings = [
        "## Single-authority principle",
        "## Default learning workflow — batch-first",
        "## Safe GitHub write protocol",
    ]
    all_docs = {**docs, **{f"SUPPORT:{k}": v for k, v in support.items()}}
    for heading in canonical_headings:
        owners = [name for name, content in all_docs.items() if heading in content]
        if heading == "## Single-authority principle" or heading == "## Default learning workflow — batch-first":
            # Only the rules file may define canonical headings for operational rules.
            expected_owner = ["04_CONTINUITY_RULES.md"]
        else:
            expected_owner = ["04_CONTINUITY_RULES.md"]
        if owners != expected_owner:
            error(f"{heading} must exist only in 04_CONTINUITY_RULES.md; found in {owners}")

    for name, content in all_docs.items():
        for fragment in LEGACY_WORKFLOW_FRAGMENTS:
            must_not_contain(name, content, fragment)

    state = docs["01_CURRENT_STATE.md"]
    state_version_match = re.search(r"\*\*State version:\*\*\s*(.+)", state)
    day_match = re.search(r"^- Day:\s*(.+)", state, re.MULTILINE)
    hour_match = re.search(r"^- Hour:\s*(.+)", state, re.MULTILINE)
    topic_match = re.search(r"^- Current topic:\s*(.+)", state, re.MULTILINE)
    next_match = re.search(r"## Exact next action\n(.*?)(?=\n## |\Z)", state, re.DOTALL)

    if not state_version_match:
        error("01_CURRENT_STATE.md: missing State version")
    if not day_match:
        error("01_CURRENT_STATE.md: missing Day")
    if not hour_match:
        error("01_CURRENT_STATE.md: missing Hour")
    if not topic_match:
        error("01_CURRENT_STATE.md: missing Current topic")
    if not next_match or not next_match.group(1).strip():
        error("01_CURRENT_STATE.md: Exact next action is missing or empty")

    if state_version_match and day_match and hour_match and topic_match and next_match:
        state_version = state_version_match.group(1).strip()
        day = day_match.group(1).strip()
        hour = hour_match.group(1).strip()
        topic = topic_match.group(1).strip()
    else:
        state_version = day = hour = topic = ""

    index = docs["02_CURRICULUM_INDEX.md"]
    master = docs["03_MASTER_PLAN.md"]
    portfolio = docs["08_ISTQB_TESTING_PORTFOLIO.md"]

    hour_numbers = {
        int(number)
        for number in re.findall(r"^\|\s*(\d+)\s*\|", index, re.MULTILINE)
    }
    expected_hours = set(range(1, 46))
    if hour_numbers != expected_hours:
        missing = sorted(expected_hours - hour_numbers)
        extra = sorted(hour_numbers - expected_hours)
        error(
            "02_CURRICULUM_INDEX.md: expected exactly hours 1-45; "
            f"missing={missing}, extra={extra}"
        )

    for required in [
        "This index is a locator.",
        "## Accelerated weekly map",
        "## Phase gates",
        "Required strengthened areas",
        "08_ISTQB_TESTING_PORTFOLIO.md",
    ]:
        must_contain("02_CURRICULUM_INDEX.md", index, required)

    for required in [
        "## Outcome",
        "## Learning method",
        "## Project",
        "## Required capability coverage",
        "## 45-hour capability catalogue",
        "## Accelerated seven-day schedule",
        "## ISTQB integration",
        "## Evidence standard",
        "## Plan-change rule",
        "08_ISTQB_TESTING_PORTFOLIO.md",
    ]:
        must_contain("03_MASTER_PLAN.md", master, required)

    for required in [
        "## Purpose and source",
        "## Test levels",
        "## Test types",
        "## Test design techniques",
        "## Non-functional quality characteristics",
        "## Static testing and review",
        "## Test management, risk, and defects",
        "## Automated vs manual evidence",
        "CTFL v4.0.1",
        "equivalence partitioning",
        "boundary value analysis",
        "decision table testing",
        "state transition testing",
        "confirmation testing",
        "regression testing",
    ]:
        must_contain("08_ISTQB_TESTING_PORTFOLIO.md", portfolio, required)

    boot = docs["00_BOOT.md"]
    recovery = docs["07_NEW_CHAT_RECOVERY.md"]
    for required in [
        "01_CURRENT_STATE.md",
        "02_CURRICULUM_INDEX.md",
        "03_MASTER_PLAN.md",
        "04_CONTINUITY_RULES.md",
        "08_ISTQB_TESTING_PORTFOLIO.md",
    ]:
        must_contain("00_BOOT.md", boot, required)

    for required in [
        "Do not use Library Control Center copies as the live study authority",
        "This file defines routing only",
    ]:
        must_contain("00_BOOT.md", boot, required)

    for stale in [
        "TS18003",
        "## Exact next action",
        "## Current saved checkpoint",
        "Immediate next action:",
        "## Safe GitHub write protocol",
        "## Single-authority principle",
    ]:
        must_not_contain("00_BOOT.md", boot, stale)

    for required in [
        "01_CURRENT_STATE.md",
        "04_CONTINUITY_RULES.md",
        "08_ISTQB_TESTING_PORTFOLIO.md",
        "The live checkpoint is always read from",
        "Do not store a copied checkpoint in this recovery file.",
        "different GitHub repository",
    ]:
        must_contain("07_NEW_CHAT_RECOVERY.md", recovery, required)

    for stale in [
        "TS18003",
        "## Current saved checkpoint",
        "Immediate next action:",
        "## Exact next action",
        "## Safe GitHub write protocol",
        "## Single-authority principle",
    ]:
        must_not_contain("07_NEW_CHAT_RECOVERY.md", recovery, stale)

    short = docs["05_SHORT_HANDOVER.md"]
    long = docs["06_LONG_HANDOVER.md"]
    for name, content in [
        ("05_SHORT_HANDOVER.md", short),
        ("06_LONG_HANDOVER.md", long),
    ]:
        must_contain(name, content, "**Derived record — not authoritative.**")
        must_contain(name, content, "01_CURRENT_STATE.md")
        must_not_contain(name, content, "## Single-authority principle")
        must_not_contain(name, content, "## Safe GitHub write protocol")
        must_not_contain(name, content, "## Default learning workflow — batch-first")

    if state_version:
        for name, content in [
            ("05_SHORT_HANDOVER.md", short),
            ("06_LONG_HANDOVER.md", long),
        ]:
            must_contain(name, content, f"Canonical state version: {state_version}")

    if day and hour:
        marker = f"Day {day} / Hour {hour}"
        must_contain("05_SHORT_HANDOVER.md", short, marker)
        must_contain("06_LONG_HANDOVER.md", long, marker)

    if topic:
        must_contain("05_SHORT_HANDOVER.md", short, topic)
        must_contain("06_LONG_HANDOVER.md", long, topic)

    must_contain("05_SHORT_HANDOVER.md", short, "# SHORT HANDOVER — CURRENT")
    must_contain("06_LONG_HANDOVER.md", long, "# LONG HANDOVER — CURRENT RECORD")
    must_contain("05_SHORT_HANDOVER.md", short, "Immediate next action:")
    must_contain("06_LONG_HANDOVER.md", long, "## Exact resume action")

    for name in [
        "00_BOOT.md",
        "02_CURRICULUM_INDEX.md",
        "03_MASTER_PLAN.md",
        "05_SHORT_HANDOVER.md",
        "06_LONG_HANDOVER.md",
        "07_NEW_CHAT_RECOVERY.md",
        "08_ISTQB_TESTING_PORTFOLIO.md",
    ]:
        must_not_contain(name, docs[name], "## Safe GitHub write protocol")
        must_not_contain(name, docs[name], "## Single-authority principle")
        must_not_contain(name, docs[name], "## Default learning workflow — batch-first")

    for name in [
        "00_BOOT.md",
        "02_CURRICULUM_INDEX.md",
        "03_MASTER_PLAN.md",
        "07_NEW_CHAT_RECOVERY.md",
        "08_ISTQB_TESTING_PORTFOLIO.md",
    ]:
        must_not_contain(name, docs[name], "**State version:**")

    readme = support["README.md"]
    for required in [
        "study-control-center/08_ISTQB_TESTING_PORTFOLIO.md",
        "04_CONTINUITY_RULES.md",
        "CTFL v4.0.1",
        "accelerated seven-day plan",
    ]:
        must_contain("README.md", readme, required)

    tools_readme = support["tools/README.md"]
    for required in [
        "python3 tools/validate_control_center.py",
        "batch-first",
        "08_ISTQB_TESTING_PORTFOLIO.md",
        "python3 -m unittest discover -s tests -v",
    ]:
        must_contain("tools/README.md", tools_readme, required)

    must_contain("00_BOOT.md", boot, "MFadelRep/QA-study-planner")
    must_contain("00_BOOT.md", boot, "separate")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)

    if errors:
        print("CONTROL CENTER VALIDATION: FAIL")
        for item in errors:
            print(f"  - {item}")
        return 1

    print("CONTROL CENTER VALIDATION: PASS")
    print(f"  - {len(REQUIRED)} required control-center files present")
    print(f"  - {len(SUPPORT_FILES)} supporting documents present")
    print("  - Batch-first workflow is uniquely defined")
    print("  - Legacy micro-step teaching instructions are rejected")
    print("  - Curriculum index covers hours 1-45 and the accelerated week")
    print("  - ISTQB CTFL portfolio coverage and manual/automated distinctions verified")
    print("  - Boot/recovery avoid copied live state")
    print("  - Short/long handovers match canonical state")
    print("  - Repository separation checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
