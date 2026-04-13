# FIX-112 - Restore page 3 alert hover overlays and fix disabled KPI display

## Summary
- Restored the three page-3 alert overlay buttons onto their cards so custom hover and click behavior align with the other KPI interactions.
- Expanded the top-row `Utilisateurs Désactivés` KPI card and its overlay hit area.
- Reduced the title font slightly on that KPI to avoid cramped wrapping.

## Why
- The alert cards still showed their tooltip via the card itself, but they no longer behaved like the other KPI zones because their transparent overlay buttons were off-canvas.
- The fourth KPI in the first row had a constrained title area, which could produce an awkward render for `Utilisateurs Désactivés`.

## Scope
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/d0f2e5dc55d345c41720/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/7a8b216031e010e2d1b4/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_disabled_btn_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_ghost_btn_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_overuse_btn_p3/visual.json`

## Layout
- `Utilisateurs Désactivés` now uses `width=220` instead of `187`.
- Its overlay button now matches the card bounds exactly.
- Alert overlay buttons are back on-canvas at:
  - `x=300, y=228`
  - `x=300, y=356`
  - `x=300, y=484`

## Expected behavior
- Hovering the three alert cards should now feel consistent with the other KPI zones on page 3.
- Clicking the alert cards should continue to trigger their existing bookmarks.
- The fourth KPI on the first row should render more cleanly.

## Validation
- Static source validation completed:
  - alert overlay buttons are serialized back on-canvas
  - the disabled KPI card and button now share the same bounds
- Manual validation required in Power BI Desktop:
  - confirm the fourth KPI title no longer looks cramped
  - confirm all three alert cards show the expected custom hover
  - confirm alert-card click behavior still targets the correct bookmarks
