# FIX-110 - Replace page 3 overuse alert with never connected and tighten alert panel

## Summary
- Replaced the right-side alert KPI `Produits en depassement` on page 3 with `Jamais connectes`.
- Renamed the licensed-disabled alert KPI to `Utilisateurs desactives avec licence`.
- Removed the visible `Risque stock` slicer from page 3 by moving it off-canvas.
- Tightened the alert-panel segment stack upward after the slicer removal.
- Added tooltip definitions to the five transparent overlay buttons above the top KPI row so hover behavior stays consistent.

## Why
- On `Analyse Utilisateur`, product overuse is a license-stock alert that belongs more naturally to page 2 than to the user-cleanup workflow on page 3.
- The current reconciliation work for `Office 365 E1` requires direct visibility on `Jamais connectes`, not on stock overuse.
- The right-side segment stack had become overly tall after prior iterations and still exposed `Risque stock`, which is no longer needed on page 3.
- Some KPI hover zones could feel silent because transparent overlay buttons above the top KPI cards had no tooltip payload.

## Scope
- `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_overuse_card_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_disabled_card_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_filter_panel_title_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_population_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_activite_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_statut_ad_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_licence_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_risque_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/kpi_actifs_btn_001/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/bc689230263b260580e0/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/7a8b216031e010e2d1b4/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/1a2f23d55a380141ed88/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/b407bc3fe477ae00b21e/visual.json`
- `M365_UI.Report/definition/pages/ttv_p3_depassement/page.json`

## Layout
- Right-side alert cards remain stacked in place; the third card is now `Jamais connectes`.
- The segment title banner moved from `y=686` to `y=680`.
- Remaining visible segments now sit at:
  - `Population`: `y=732`
  - `Activite`: `y=794`
  - `Statut AD`: `y=856`
  - `Statut licence`: `y=918`
- `Risque stock` was moved off-canvas so it no longer appears on page 3.

## Expected behavior
- Page 3 now exposes `Jamais connectes` directly in the alert column, which helps reconcile inactive licenses for products such as `Office 365 E1`.
- The disabled-with-license alert uses explicit user wording.
- Hovering the top KPI row should consistently show tooltips even if the pointer lands on a transparent overlay button instead of the card itself.
- The right-side panel is shorter and focused on user-analysis filters only.

## Validation
- Static source validation completed:
  - the former overuse alert card now binds `NbHumainsJamaisConnectes`
  - the hidden `Risque stock` slicer is off-canvas
  - all five top KPI overlay buttons now serialize a tooltip section
- Manual validation required in Power BI Desktop:
  - confirm `Jamais connectes` appears in the third right-side alert slot
  - confirm `Risque stock` no longer appears on page 3
  - confirm the alert panel spacing still looks balanced on desktop
  - confirm hovering the top KPI cards always shows the expected tooltip
