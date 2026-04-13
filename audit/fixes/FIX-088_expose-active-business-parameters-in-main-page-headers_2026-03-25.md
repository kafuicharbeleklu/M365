# FIX-088 — Expose active business parameters in main page headers

## Summary
- Added a shared UX measure `UX_ParametresActifs` to surface the active business thresholds directly in the report header.
- Added a lightweight parameter banner to the three main pages:
  - `a4497031bb9f4bfb6556` (`ux_param_banner_p1`)
  - `54f9d470ac60b85b18da` (`ux_param_banner_p2`)
  - `3c4cbe0b2835dc22b7e2` (`ux_param_banner_p3`)

## Why
- The model thresholds were parameterized, but they remained invisible in the report UX.
- Users had no direct way to see which inactivity threshold, stock thresholds, and activity period were currently active.

## Scope
- `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`
- `M365_UI.Report/definition/pages/a4497031bb9f4bfb6556/visuals/ux_param_banner_p1/visual.json`
- `M365_UI.Report/definition/pages/54f9d470ac60b85b18da/visuals/ux_param_banner_p2/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_param_banner_p3/visual.json`

## Validation
- Static validation only in source.
- Manual validation required in Power BI Desktop:
  - Open the three main pages.
  - Confirm the new header banner is visible and does not overlap the title or header controls.
  - Confirm the displayed values match `T_Parametres_Dim`.
