# FIX-100 - Harmonize tooltip section font hierarchy and remove rounded main-page borders

## Summary
- Harmonized the `ttv_*` tooltip typography so section titles use a consistent size above body text.
- Removed rounded corners from cards and overlay buttons on the 3 main report pages.

## Why
- Tooltip compactness had already been validated, but the section hierarchy still felt visually inconsistent.
- Rounded corners were still mixed across pages 1, 2 and 3, especially on KPI cards and transparent overlay buttons.

## Scope
- `M365_UI.Report/definition/pages/ttv_*/visuals/*/visual.json`
- `M365_UI.Report/definition/pages/a4497031bb9f4bfb6556/visuals/*/visual.json`
- `M365_UI.Report/definition/pages/54f9d470ac60b85b18da/visuals/*/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/*/visual.json`

## Details
- Tooltip body text stays at `7D`.
- Tooltip section titles `Perimetre` and `Action` now use `8D`.
- `radius` is normalized to `0D` on the affected main-page visuals.
- `roundEdge` is normalized to `0L` on the affected main-page visuals.

## Validation
- Static source validation completed:
  - no `ttv_*` section title remains at a size other than `8D`
  - no `radius` / `roundEdge` remains non-zero on the main pages 1, 2 and 3
- Manual validation required in Power BI Desktop:
  - confirm tooltip titles/body remain readable
  - confirm squared cards/buttons still render cleanly on pages 1, 2 and 3
