# FIX-093 — Move P3 hover to transparent buttons and compact all tooltip pages

## Summary
- Added `visualTooltip` to the three transparent action buttons on P3 so hover is handled by the overlay that actually captures the pointer.
- Reduced all tooltip pages `ttv_*` from `320x240` to `288x208`.
- Reduced tooltip card size and font size consistently across all tooltip pages.

## Why
- The transparent overlay buttons on P3 sat above the cards, preventing hover from reaching the card tooltip.
- Tooltip pages were visually oversized for the amount of text they displayed.

## Scope
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_ghost_btn_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_disabled_btn_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_overuse_btn_p3/visual.json`
- All `M365_UI.Report/definition/pages/ttv_*/page.json`
- All `M365_UI.Report/definition/pages/ttv_*/visuals/*/visual.json`

## Validation
- Static validation only in source.
- Manual validation required in Power BI Desktop:
  - Hover the three P3 action buttons and confirm the tooltip appears.
  - Confirm all tooltip pages still render without truncation after the size reduction.
  - Confirm font size remains readable on Desktop.
