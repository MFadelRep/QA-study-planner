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

## GitHub Actions

.github/workflows/control-center-validation.yml runs the validator on pushes to main and pull requests.

The validator can block a change by failing the workflow, but it never edits files and never overrides the canonical control-center documents.

For semantic decisions, follow study-control-center/04_CONTINUITY_RULES.md.
