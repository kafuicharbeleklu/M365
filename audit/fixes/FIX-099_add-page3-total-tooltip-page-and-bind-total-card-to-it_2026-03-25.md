# FIX-099 - Add page3 total tooltip page and bind total card to it

## Summary
- Added dedicated tooltip measures for the `Total` KPI on page 3.
- Added the tooltip page `ttv_p3_total`.
- Bound the `Total` card to this tooltip.

## Why
- The `Total` KPI on page 3 had no custom tooltip while the other main KPI cards were being harmonized.
- The user explicitly requested a proper tooltip on this card as well.

## Scope
- `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`
- `M365_UI.Report/definition/pages/pages.json`
- `M365_UI.Report/definition/pages/ttv_p3_total/**`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/678ebb458a124b23d8b3/visual.json`

## Validation
- Static validation only in source.
- Manual validation required in Power BI Desktop:
  - Hover on `Total` in page 3 should show the new custom tooltip.
  - The tooltip should use the same compact format as the other `ttv_p3*` pages.
