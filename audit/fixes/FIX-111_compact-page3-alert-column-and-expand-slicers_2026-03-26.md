# FIX-111 - Compact page 3 alert column and expand slicers

## Summary
- Renamed the left alert KPI for disabled users so it no longer reads like a duplicate of the top-row disabled KPI.
- Moved the three left alert cards upward on page 3 to free more vertical space for the segment area.
- Removed the visible segment-comment textbox by moving it off-canvas.
- Increased the height of the four visible slicers on page 3 to make the filter panel easier to use.

## Why
- On `Analyse Utilisateur`, `Utilisateurs desactives` already exists in the first KPI row.
- The left alert KPI is still useful because it isolates disabled accounts that still carry a license, but its wording created visual redundancy with the global KPI.
- The slicer stack had become too compressed after the recent alert-panel additions and the explanatory textbox consumed space without adding much value.

## Scope
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_disabled_card_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_ghost_card_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_overuse_card_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_disabled_btn_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_ghost_btn_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_overuse_btn_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_filter_panel_title_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_population_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_activite_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_statut_ad_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_licence_p3/visual.json`

## Layout
- Alert cards now sit at:
  - `Desactives avec licence a retirer`: `y=228`
  - `Utilisateurs fantomes`: `y=356`
  - `Jamais connectes`: `y=484`
- The segment-comment textbox is hidden off-canvas.
- Visible slicers now sit at:
  - `Population`: `y=620`, `height=80`
  - `Activite`: `y=716`, `height=80`
  - `Statut AD`: `y=812`, `height=80`
  - `Statut licence`: `y=908`, `height=80`

## Expected behavior
- The left alert column should feel less repetitive because the disabled alert now expresses the cleanup action rather than repeating the top KPI label.
- The right filter panel should breathe more, with larger dropdown slicers and no extra comment box.
- The alert cards remain grouped close to the table and preserve the existing three-alert workflow.

## Validation
- Static source validation completed:
  - page 3 alert cards now serialize the updated `y` positions
  - the segment title textbox is off-canvas
  - all four visible slicers serialize the new `height=80`
- Manual validation required in Power BI Desktop:
  - confirm the new disabled alert title wraps cleanly
  - confirm the left alert column does not overlap the table or top KPI row
  - confirm the slicers are easier to open and read on desktop
