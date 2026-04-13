# FIX-097 - Compact page3 tooltips and route top KPI hover through overlay buttons

## Summary
- Reduced all `ttv_p3*` pages to the compact tooltip layout now used on pages 1 and 2.
- Standardized the top KPI card tooltips on page 3 to `Canvas`.
- Added explicit report-page tooltips to the top overlay bookmark buttons so hover is not lost on covered KPI cards.
- Shortened most page 3 tooltip texts.
- Added clean replacement measures for the `fantomes` tooltip page and re-bound the tooltip visuals to them.

## Why
- Page 3 still used the older larger tooltip pages and generic tooltip block labels.
- Several top KPI cards are partially or fully covered by transparent bookmark buttons, which can swallow hover without showing the intended tooltip.
- The existing `fantomes` tooltip text contained a source encoding residue and needed a clean display path without relying on the legacy strings.

## Scope
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/*/visual.json`
- `M365_UI.Report/definition/pages/ttv_p3*/page.json`
- `M365_UI.Report/definition/pages/ttv_p3*/visuals/*/visual.json`
- `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`

## Validation
- Static validation only in source.
- Manual validation required in Power BI Desktop:
  - Confirm top page 3 KPI hover works on both card and covered-button areas.
  - Confirm the compact tooltip size remains readable.
  - Confirm the `fantomes` tooltip shows the clean text and no mojibake.
