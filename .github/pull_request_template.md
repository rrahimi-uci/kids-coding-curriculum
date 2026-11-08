## Summary

<!-- What changed and why? Link the issue, epic or milestone. -->

## What changed

<!-- Group by area: lessons / workbook / homework / answers / exercises / project / tooling / docs. -->

## Approach and key decisions

<!-- Why this approach; important pedagogical, architectural or implementation decisions. -->

## Tests and validation

- [ ] `make test` passes (exercise checks against solutions + repository quality gate).
- [ ] `make smoke` passes on a Mac (every turtle program opens in a real window).
- [ ] `make pdf` builds every document in both editions without errors.
- [ ] New/changed exercises fail against their untouched starter (`KIDCODE_TARGET=starter`).
- [ ] Ran `git diff --check`.
- [ ] Checked for personal data, secrets, unrelated changes, and generated-file drift (`python3 tools/coverage.py --check`).

Validation commands and results:

## Risks and follow-up

<!-- Risks, limitations, side effects, and what to verify when teaching it. -->

## Documentation, configuration and deployment implications

<!-- Docs updated? New setup steps for the Macs? Anything parents must re-print? -->
