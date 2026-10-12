# Study Control Center Validation

The Study Control Center uses one canonical source per information type. Read `study-control-center/04_CONTINUITY_RULES.md` for the authoritative batch-first workflow and safe GitHub write protocol.

## Validator

Run from the repository root:

    python3 tools/validate_control_center.py

The validator is read-only and exits non-zero when required study-control files, consistency rules, or anti-drift checks fail.

It verifies:
- the required control-center and ISTQB portfolio files exist, including `study-control-center/08_ISTQB_TESTING_PORTFOLIO.md`;
- canonical source ownership is not duplicated;
- the safe GitHub write protocol and batch-first workflow are defined only in the continuity rules;
- all 45 curriculum hours remain present;
- the accelerated seven-day plan and ISTQB coverage map remain present;
- boot/recovery files do not contain copied live checkpoints;
- short/long handovers match canonical state version, Day/Hour, topic, and resume direction;
- legacy micro-step teaching instructions do not reappear;
- repository separation and current next-action requirements remain intact.

## Self-tests

Run:

    python3 -m unittest discover -s tests -v

Tests use temporary fixtures, confirm that the validator is read-only, and inject errors for duplicated authority, legacy workflow drift, missing curriculum hours/ISTQB scope, stale handover versions, and missing next actions.

## GitHub Actions

`.github/workflows/control-center-validation.yml` runs the self-tests and real validator on pushes to `main` and pull requests.

The validator and tests never edit canonical documents. A failure blocks the workflow; only explicit, verified changes to the control-center files may resolve it.
