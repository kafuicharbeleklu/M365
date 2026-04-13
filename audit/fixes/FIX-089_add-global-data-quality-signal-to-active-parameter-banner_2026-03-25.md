# FIX-089 — Add global data quality signal to active parameter banner

## Summary
- Added `UX_QualiteDonnees` to surface a compact global DQ signal in the header.
- Updated `UX_ParametresActifs` to use a shorter format and append the DQ status.

## Why
- The new parameter banner exposed active thresholds, but it still lacked an operational health signal.
- Users need a fast indication when the model still contains `Non defini`, `Non synchronisé`, or unclassified rows.

## Scope
- `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`

## Validation
- Static validation only in source.
- Manual validation required in Power BI Desktop:
  - Confirm the parameter banner still fits on the three main pages.
  - Confirm the DQ suffix shows `DQ OK` when no anomaly exists, otherwise the expected compact counts.
