# FIX-102 - Rename cleanup target KPI and refresh tooltip visual style

## Summary
- Renamed the page 3 KPI label from `Cibles Nettoyage` to `Comptes a traiter`.
- Updated the related tooltip wording to use the same business vocabulary.
- Refreshed the visual style of all `ttv_*` tooltip cards with tighter framing and a clearer editorial split between `Perimetre` and `Action`.

## Why
- `Cibles Nettoyage` was ambiguous and too close to an internal technical notion.
- The tooltip system was functionally correct but still visually flat.
- A more explicit and cleaner tooltip treatment makes the KPIs easier to read without increasing the footprint.

## Scope
- `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/0781849f42b2a3099ac6/visual.json`
- `M365_UI.Report/definition/pages/ttv_*/visuals/*/visual.json`

## Details
- KPI wording:
  - `Cibles Nettoyage` -> `Comptes a traiter`
- Tooltip wording:
  - `TT_p3_cibles_lect` now describes an examination/cleanup population instead of a generic cleanup target
  - `TT_p3_total_lect` now references `comptes a traiter`
- Tooltip UI:
  - inner horizontal padding tightened by moving cards from `x=8` to `x=10`
  - card width normalized from `216` to `212`
  - `Perimetre` cards reduced from `58` to `52` height and moved to `y=10`
  - section title size increased from `8D` to `9D`
  - `Perimetre` palette refreshed to `#163B63` on `#F3F8FF`
  - `Action` palette refreshed to `#A85600` on `#FFF7EC`

## Validation
- Static source validation completed on representative P1 and P3 tooltip visuals.
- Manual validation required in Power BI Desktop:
  - confirm the new tooltip style remains readable
  - confirm no text is truncated after the card width reduction
  - confirm the page 3 KPI now reads `Comptes a traiter`
