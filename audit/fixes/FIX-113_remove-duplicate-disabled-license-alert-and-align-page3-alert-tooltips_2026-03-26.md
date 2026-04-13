# FIX-113 - Remove duplicate disabled-license alert and align page 3 alert tooltips

## Summary
- Removed the duplicated `desactives avec licence` alert card from the page-3 alert column by moving its card and overlay off-canvas.
- Kept only `Utilisateurs fantomes` and `Jamais connectes` in the alert stack and moved them upward.
- Switched the remaining alert-card tooltips and overlays to the same `Canvas` tooltip mode used by the other page-3 KPI hovers.
- Replaced the malformed top-row label with a plain ASCII title: `Utilisateurs desactives`.

## Why
- The page already exposes disabled users in the first KPI row, so the extra disabled-with-license alert felt redundant.
- The alert overlays were capturing pointer events, but their tooltip mode was not aligned with the top KPI row.
- The serialized title `Utilisateurs D\\u00E9sactiv\\u00E9s` could surface as a malformed label.

## Scope
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/d0f2e5dc55d345c41720/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_disabled_card_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_disabled_btn_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_ghost_card_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_ghost_btn_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_overuse_card_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_overuse_btn_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_population_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_activite_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_statut_ad_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_licence_p3/visual.json`

## Expected behavior
- The first-row disabled KPI remains the single disabled-account summary on page 3.
- The alert column now focuses on the two remaining cleanup signals.
- Hovering the remaining alert cards should use the same tooltip mode as the other KPI cards on the page.

## Validation
- Static source validation completed:
  - duplicate disabled alert card and overlay are off-canvas
  - ghost and never-connected alerts are repositioned upward
  - remaining alert tooltips now use `Canvas`
- Manual validation required in Power BI Desktop:
  - confirm the top-row label renders correctly
  - confirm the disabled-with-license alert no longer appears
  - confirm `Fantomes` and `Jamais connectes` show their tooltip on hover
