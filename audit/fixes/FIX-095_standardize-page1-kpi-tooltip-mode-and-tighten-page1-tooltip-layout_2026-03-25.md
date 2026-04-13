# FIX-095 - Standardize page1 KPI tooltip mode and tighten page1 tooltip layout

## Summary
- Standardized the main KPI tooltips on page 1 to the same tooltip mode already used by the working `Comptes` card.
- Reduced only the `ttv_p1_*` tooltip pages again to a tighter footprint than the global tooltip size.
- Shortened page 1 tooltip copy again to reduce wrapping and improve scan speed.

## Why
- Screenshot review showed inconsistent hover behavior on page 1:
  - `Comptes` opened the intended custom tooltip.
  - `Utilisateurs Actifs` fell back to the default measure tooltip.
- Screenshot review also showed that the page 1 tooltip container was still visually too large relative to the amount of text displayed.

## Scope
- `M365_UI.Report/definition/pages/a4497031bb9f4bfb6556/visuals/*/visual.json`
- `M365_UI.Report/definition/pages/ttv_p1_*/page.json`
- `M365_UI.Report/definition/pages/ttv_p1_*/visuals/*/visual.json`
- `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`

## Validation
- Static validation only in source.
- Manual validation required in Power BI Desktop:
  - Confirm all page 1 KPI cards now open the intended custom tooltip.
  - Confirm no page 1 tooltip text is truncated.
  - Confirm the smaller page 1 tooltip footprint feels proportionate on Desktop.
