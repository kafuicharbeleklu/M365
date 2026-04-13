# FIX-103 - Raise KPI title font sizes and fix page 3 disabled title

## Summary
- Increased KPI title font sizes on the three main pages and on the user drillthrough.
- Corrected the broken page 3 `Desactives` title that was rendered with malformed characters.

## Why
- KPI labels had become visually too small compared with the metric values.
- The page 3 disabled KPI title exposed an encoding issue that reduced readability and visual trust.

## Scope
- `M365_UI.Report/definition/pages/a4497031bb9f4bfb6556/visuals/*.json`
- `M365_UI.Report/definition/pages/54f9d470ac60b85b18da/visuals/*.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/*.json`
- `M365_UI.Report/definition/pages/page_drillthrough_detail_user/visuals/*.json`

## Details
- Page 1 KPI titles: `11D` -> `13D`
- Page 2 KPI titles: `11D` -> `13D`
- Page 3 large KPI titles: `13D` -> `14D`
- Page 3 compact technical KPI titles: `10D` -> `12D`
- Drillthrough KPI titles: `11D` -> `13D`
- Page 3 disabled KPI title fixed from malformed text to `Desactives`

## Validation
- Static source validation completed on the edited visual JSON files.
- Manual validation required in Power BI Desktop:
  - confirm KPI titles are more legible without wrapping regressions
  - confirm the page 3 disabled KPI title now renders cleanly
