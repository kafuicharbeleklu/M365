# FIX-096 - Standardize page2 KPI tooltip mode and compact page2 tooltips

## Summary
- Standardized the 6 main KPI tooltips on page 2 to `Canvas` mode for consistent custom hover behavior.
- Reduced the `ttv_p2_*` pages to the same compact layout now used successfully on page 1.
- Renamed the two tooltip blocks to `Perimetre` and `Action`.
- Shortened the page 2 tooltip copy to reduce wrapping and improve quick reading.

## Why
- Page 2 still used larger tooltip pages than page 1 after the last compact pass.
- Page 1 showed that inconsistent tooltip mode can lead to the raw measure tooltip appearing instead of the intended custom tooltip.
- Page 2 tooltip texts were still more explanatory than action-oriented.

## Scope
- `M365_UI.Report/definition/pages/54f9d470ac60b85b18da/visuals/*/visual.json`
- `M365_UI.Report/definition/pages/ttv_p2_*/page.json`
- `M365_UI.Report/definition/pages/ttv_p2_*/visuals/*/visual.json`
- `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`

## Validation
- Static validation only in source.
- Manual validation required in Power BI Desktop:
  - Confirm all 6 KPI cards on page 2 open the intended custom tooltip.
  - Confirm the compact tooltip format remains readable.
  - Confirm no page 2 tooltip text is truncated.
