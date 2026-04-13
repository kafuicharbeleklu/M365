# FIX-101 - Increase left-nav section spacing, square drillthrough cards, and raise KPI font sizes

## Summary
- Increased the vertical spacing between the logo, navigation buttons, and slicer groups in the left rail of the 3 main pages.
- Removed remaining rounded borders from the drillthrough page cards and table container.
- Increased KPI font sizes on the top KPI rows of pages 1 and 2, and on the 3 KPI cards of the user drillthrough page.

## Why
- The left navigation rail felt visually compressed and the 3 sections were not clearly separated.
- The drillthrough page still kept rounded cards while the main pages had already been flattened.
- KPI text had become too small, especially on pages 1, 2, and in the drillthrough header KPIs.

## Scope
- `M365_UI.Report/definition/pages/a4497031bb9f4bfb6556/visuals/*/visual.json`
- `M365_UI.Report/definition/pages/54f9d470ac60b85b18da/visuals/*/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/*/visual.json`
- `M365_UI.Report/definition/pages/page_drillthrough_detail_user/visuals/*/visual.json`

## Details
- Left rail spacing:
  - navigation buttons moved down from `96/146/196` to `112/162/212`
  - slicer blocks moved down from `264/370/466/562/658` to `292/398/494/590/686`
- Drillthrough:
  - card and table `radius` normalized to `0D`
- KPI typography:
  - page 1 and 2 top KPI cards: `18D -> 20D`, titles `10D -> 11D`
  - drillthrough KPI cards: `16D -> 18D`, titles `10D -> 11D`

## Validation
- Static source validation completed:
  - left-rail target positions match the intended spacing
  - drillthrough `radius` is now `0D` on the affected containers
  - sampled KPI cards now expose the intended font sizes
- Manual validation required in Power BI Desktop:
  - confirm the left rail breathes more without creating overlap
  - confirm the drillthrough page renders fully squared
  - confirm larger KPI text remains readable and not truncated
