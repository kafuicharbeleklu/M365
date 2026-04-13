# FIX-090 — Expose TypeCompte diagnostic rule on user drillthrough

## Summary
- Added `DT_DiagnosticClassification` to expose the actual `TypeCompte` rule applied to the selected user.
- Replaced the static delay note on the drillthrough page with a dynamic diagnostic banner bound to that measure.

## Why
- `RegleTypeCompte` existed only in the model, making diagnosis hard from the report UI.
- The user drillthrough is the right place to understand why an account is classified as `Utilisateur` or `Technique`.

## Scope
- `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`
- `M365_UI.Report/definition/pages/page_drillthrough_detail_user/visuals/dt_activity_delay_note_001/visual.json`

## Validation
- Static validation only in source.
- Manual validation required in Power BI Desktop:
  - Open the user drillthrough page.
  - Confirm the diagnostic line appears above the licenses table.
  - Check that it shows `TypeCompte` and `RegleTypeCompte` for a few known human and technical accounts.
