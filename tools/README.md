# Study Control Center Validation

The Study Control Center is governed by one-authority-per-information-type.

## Validator

Run locally from the repository root:

    python3 tools/validate_control_center.py

The validator is read-only. It checks structural consistency and exits with a non-zero status when the repository violates the control-center rules.

It verifies:

- required control-center files exist;
- canonical ownership is not duplicated;
- the safe GitHub write protocol exists only in 04_CONTINUITY_RULES.md;
- the 45-hour curriculum index remains complete;
- Boot and New Chat Recovery do not contain copied live checkpoints;
- Short and Long Handovers are explicitly derived and match the canonical state version, day/hour, and current topic;
- required routing and repository-separation references remain intact.

## Self-tests

Run the validator test suite locally:

    python3 -m unittest discover -s tests -v

The tests use isolated temporary fixtures and intentionally inject failures for stale state, duplicated authority, missing curriculum hours, stale handover versions, and missing current-state next actions. They also verify that the validator does not modify files.

## GitHub Actions

.github/workflows/control-center-validation.yml runs the self-tests first and then the real validator on pushes to main and pull requests.

The validator and tests never edit control-center files. A failure blocks the workflow; canonical documents remain the only authority.

For semantic decisions, follow study-control-center/04_CONTINUITY_RULES.md.
