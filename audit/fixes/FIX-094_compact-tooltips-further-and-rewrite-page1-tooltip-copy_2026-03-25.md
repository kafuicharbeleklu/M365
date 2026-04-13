# FIX-094 — Compact tooltips further and rewrite page1 tooltip copy

## Summary
- Reduced all `ttv_*` pages again to a smaller tooltip footprint.
- Reduced tooltip card size and font size again for all tooltip pages.
- Rewrote the page 1 tooltip texts to be shorter and more action-oriented.
- Localized page 1 tooltip card titles from generic labels to short French labels.

## Why
- The previous tooltip size was still visually too large for the amount of information displayed.
- Page 1 tooltips were technically correct but too verbose and not action-oriented enough for quick reading.

## Scope
- All `M365_UI.Report/definition/pages/ttv_*/page.json`
- All `M365_UI.Report/definition/pages/ttv_*/visuals/*/visual.json`
- `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`

## Validation
- Static validation only in source.
- Manual validation required in Power BI Desktop:
  - Confirm page 1 tooltips remain readable without truncation.
  - Confirm hover still opens the tooltip on all page 1 KPI cards.
  - Confirm the smaller tooltip footprint feels proportionate on Desktop.
