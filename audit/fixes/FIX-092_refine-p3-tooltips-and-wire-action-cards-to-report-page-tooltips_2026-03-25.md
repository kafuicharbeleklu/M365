# FIX-092 — Refine P3 tooltips and wire action cards to report-page tooltips

## Summary
- Rewrote `TT_p3_inactifs_*` so the tooltip matches the actual `NbHumainsInactifs` logic.
- Added dedicated tooltip pages for:
  - disabled accounts with license
  - over-capacity products shown from P3
- Wired the three P3 action cards to report-page tooltips:
  - `ux_action_ghost_card_p3` -> `ttv_p3_fantomes`
  - `ux_action_disabled_card_p3` -> `ttv_p3_desactives_lic`
  - `ux_action_overuse_card_p3` -> `ttv_p3_depassement`

## Why
- `Utilisateurs Inactifs` was explained as `Jamais connectes`, which was semantically wrong.
- The action cards on P3 had no tooltip guidance, even though they are high-value decision points.

## Scope
- `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`
- `M365_UI.Report/definition/pages/pages.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_ghost_card_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_disabled_card_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_overuse_card_p3/visual.json`
- `M365_UI.Report/definition/pages/ttv_p3_desactives_lic/*`
- `M365_UI.Report/definition/pages/ttv_p3_depassement/*`

## Validation
- Static validation only in source.
- Manual validation required in Power BI Desktop:
  - Hover `Utilisateurs Inactifs` on P3 and confirm the wording matches inactivity beyond the threshold.
  - Hover the three action cards and confirm the correct tooltip page appears.
  - Confirm the new tooltip pages render correctly in the default tooltip size.
