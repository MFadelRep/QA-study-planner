#!/usr/bin/env python3
"""Deterministic, read-only validation for the Study Control Center.

This validator never edits repository files. It checks that the canonical
documents remain internally consistent and that derived records do not become
competing sources of truth.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTROL = ROOT / "study-control-center"

REQUIRED = [
    "00_BOOT.md",
    "01_CURRENT_STATE.md",
    "02_CURRICULUM_INDEX.md",
    "03_MASTER_PLAN.md",
    "04_CONTINUITY_RULES.md",
    "05_SHORT_HANDOVER.md",
    "06_LONG_HANDOVER.md",
    "07_NEW_CHAT_RECOVERY.md",
]

FAIL = 1

errors: list[str] = []
warnings: list[str] = []


def error(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


def must_contain(name: str, text: str, needle: str) -> None:
    if needle not in text:
        error(f"{name}: missing required text: {needle!r}")


def must_not_contain(name: str, text: str, needle: str) -> None:
    if needle in text:
        error(f"{name}: contains forbidden/duplicated text: {needle!r}")


docs: dict[str, str] = {}
for filename in REQUIRED:
    path = CONTROL / filename
    if not path.is_file():
        error(f"Missing required control-center file: {path.relative_to(ROOT)}")
        continue
    docs[filename] = path.read_text(encoding="utf-8")


if errors:
    print("CONTROL CENTER VALIDATION: FAIL")
    for item in errors:
        print(f"  - {item}")
    sys.exit(FAIL)


# ---------------------------------------------------------------------------
# Canonical authority checks
# ---------------------------------------------------------------------------

rules = docs["04_CONTINUITY_RULES.md"]

must_contain("04_CONTINUITY_RULES.md", rules, "## Single-authority principle")
must_contain("04_CONTINUITY_RULES.md", rules, "## Safe GitHub write protocol")
must_contain("04_CONTINUITY_RULES.md", rules, "## Control-center validation")
must_contain(
    "04_CONTINUITY_RULES.md",
    rules,
    "READ → preserve current content → minimal changes → WRITE with current SHA → READ AGAIN → verify",
)

unique_sections = {
    "## Single-authority principle": [
        name for name, text in docs.items() if "## Single-authority principle" in text
    ],
    "## Safe GitHub write protocol": [
        name for name, text in docs.items() if "## Safe GitHub write protocol" in text
    ],
}

for section, owners in unique_sections.items():
    if owners != ["04_CONTINUITY_RULES.md"]:
        error(f"{section} must exist only in 04_CONTINUITY_RULES.md; found in {owners}")


# ---------------------------------------------------------------------------
# Current-state checks
# ---------------------------------------------------------------------------

state = docs["01_CURRENT_STATE.md"]

state_version_match = re.search(r"\*\*State version:\*\*\s*(.+)", state)
day_match = re.search(r"^- Day:\s*(.+)", state, re.MULTILINE)
hour_match = re.search(r"^- Hour:\s*(.+)", state, re.MULTILINE)
topic_match = re.search(r"^- Current topic:\s*(.+)", state, re.MULTILINE)
next_match = re.search(
    r"## Exact next action\n(.*?)(?=\n## |\Z)", state, re.DOTALL
)

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


# ---------------------------------------------------------------------------
# Curriculum integrity
# ---------------------------------------------------------------------------

index = docs["02_CURRICULUM_INDEX.md"]
master = docs["03_MASTER_PLAN.md"]

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
    "This index is a locator; the complete scope is in `03_MASTER_PLAN.md`.",
    "## Phase gates",
    "Required strengthened areas:",
]:
    must_contain("02_CURRICULUM_INDEX.md", index, required)

for required in [
    "## Outcome",
    "## Execution model",
    "## Project",
    "## Required capability coverage",
    "## 45-hour scope",
    "## Evidence standard",
    "## Plan-change rule",
]:
    must_contain("03_MASTER_PLAN.md", master, required)


# ---------------------------------------------------------------------------
# Boot / recovery routing checks
# ---------------------------------------------------------------------------

boot = docs["00_BOOT.md"]
recovery = docs["07_NEW_CHAT_RECOVERY.md"]

for required in [
    "01_CURRENT_STATE.md",
    "02_CURRICULUM_INDEX.md",
    "03_MASTER_PLAN.md",
    "04_CONTINUITY_RULES.md",
]:
    must_contain("00_BOOT.md", boot, required)

must_contain(
    "00_BOOT.md",
    boot,
    "Do NOT use the Library Control Center copies as the live study authority.",
)
must_contain(
    "00_BOOT.md",
    boot,
    "this boot file only defines startup routing and must not duplicate live state or detailed operating rules.",
)

for stale in [
    "TS18003",
    "## Exact next action",
    "## Current saved checkpoint",
    "Immediate next action:",
]:
    must_not_contain("00_BOOT.md", boot, stale)

must_contain("07_NEW_CHAT_RECOVERY.md", recovery, "01_CURRENT_STATE.md")
must_contain("07_NEW_CHAT_RECOVERY.md", recovery, "04_CONTINUITY_RULES.md")
must_contain(
    "07_NEW_CHAT_RECOVERY.md",
    recovery,
    "The live checkpoint is always read from `01_CURRENT_STATE.md` at recovery time.",
)
must_contain(
    "07_NEW_CHAT_RECOVERY.md",
    recovery,
    "Do not store a copied checkpoint in this recovery file.",
)

for stale in [
    "TS18003",
    "## Current saved checkpoint",
    "Immediate next action:",
    "## Exact next action",
]:
    must_not_contain("07_NEW_CHAT_RECOVERY.md", recovery, stale)


# ---------------------------------------------------------------------------
# Derived handover checks
# ---------------------------------------------------------------------------

short = docs["05_SHORT_HANDOVER.md"]
long = docs["06_LONG_HANDOVER.md"]

for name, text in [
    ("05_SHORT_HANDOVER.md", short),
    ("06_LONG_HANDOVER.md", long),
]:
    must_contain(name, text, "**Derived record — not authoritative.**")
    must_contain(name, text, "01_CURRENT_STATE.md")
    must_not_contain(name, text, "## Single-authority principle")
    must_not_contain(name, text, "## Safe GitHub write protocol")
    must_not_contain(name, text, "## Terminal teaching rule")

if state_version:
    for name, text in [
        ("05_SHORT_HANDOVER.md", short),
        ("06_LONG_HANDOVER.md", long),
    ]:
        must_contain(name, text, f"Canonical state version: {state_version}")

if day and hour:
    day_hour = f"Day {day} / Hour {hour}"
    must_contain("05_SHORT_HANDOVER.md", short, day_hour)
    must_contain("06_LONG_HANDOVER.md", long, day_hour)

if topic:
    must_contain("05_SHORT_HANDOVER.md", short, topic)
    must_contain("06_LONG_HANDOVER.md", long, topic)

must_contain("05_SHORT_HANDOVER.md", short, "## SHORT HANDOVER — CURRENT")
must_contain("06_LONG_HANDOVER.md", long, "## LONG HANDOVER — CURRENT RECORD")
must_contain("05_SHORT_HANDOVER.md", short, "Immediate next action:")
must_contain("06_LONG_HANDOVER.md", long, "## Exact resume action")


# ---------------------------------------------------------------------------
# Prevent obvious cross-authority duplication
# ---------------------------------------------------------------------------

for name in [
    "00_BOOT.md",
    "02_CURRICULUM_INDEX.md",
    "03_MASTER_PLAN.md",
    "07_NEW_CHAT_RECOVERY.md",
]:
    must_not_contain(name, docs[name], "## Safe GitHub write protocol")
    must_not_contain(name, docs[name], "## Single-authority principle")

for name in [
    "00_BOOT.md",
    "02_CURRICULUM_INDEX.md",
    "03_MASTER_PLAN.md",
    "05_SHORT_HANDOVER.md",
    "06_LONG_HANDOVER.md",
    "07_NEW_CHAT_RECOVERY.md",
]:
    must_not_contain(name, docs[name], "**State version:**")

for name in ["05_SHORT_HANDOVER.md", "06_LONG_HANDOVER.md"]:
    must_not_contain(name, docs[name], "**State version:**")


# ---------------------------------------------------------------------------
# Repository separation checks
# ---------------------------------------------------------------------------

must_contain("00_BOOT.md", boot, "MFadelRep/QA-study-planner")
must_contain("00_BOOT.md", boot, "separate repository")
must_contain("07_NEW_CHAT_RECOVERY.md", recovery, "different GitHub repository")


# ---------------------------------------------------------------------------
# Final result
# ---------------------------------------------------------------------------

if errors:
    print("CONTROL CENTER VALIDATION: FAIL")
    for item in errors:
        print(f"  - {item}")
    if warnings:
        print("\nWarnings:")
        for item in warnings:
            print(f"  - {item}")
    sys.exit(FAIL)

print("CONTROL CENTER VALIDATION: PASS")
print(f"  - {len(REQUIRED)} required control-center files present")
print("  - Canonical ownership checks passed")
print("  - Safe GitHub write protocol is uniquely defined")
print("  - Curriculum index covers hours 1-45")
print("  - Boot/recovery files do not carry copied live checkpoint state")
print("  - Short/long handovers are marked derived and match canonical state")
print("  - Repository separation checks passed")

if warnings:
    print("\nWarnings:")
    for item in warnings:
        print(f"  - {item}")

sys.exit(0)
