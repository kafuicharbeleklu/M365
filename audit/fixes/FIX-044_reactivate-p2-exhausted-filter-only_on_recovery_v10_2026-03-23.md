# FIX-044 - Reactivate P2 exhausted filter only on recovery V10
**Date**: 2026-03-23

## Context
- `RECOVERY_UI_SAFE_V9` remains stable after refresh.
- Single-interaction reactivation is still the operating rule.
- `Nav_FiltreEpuise` (`a5f1d2c3b4e50617283a`) targets only `ux_risk_quickfilter_p2`.

## Decision
- Create `RECOVERY_UI_SAFE_V10` from `RECOVERY_UI_SAFE_V9`.
- Add only bookmark `a5f1d2c3b4e50617283a`.
- Reactivate only `btn_filtre_epuise_p2`.

## Explicitly Not Changed
- `Nav_HumainsActifs`
- `Nav_TechniquesActives`
- `Nav_TechniquesInactives`
- `Nav_UtilisateursFantomes`
- P2 reset
- P1 and drillthrough bookmark reactivations

## Expected Result
- P2 regains only the "Stock epuise" quick filter action in addition to the already stable actions.
- If `V10` stays stable, the remaining interactive risk is likely concentrated in reset behavior and the known-suspect bookmarks.
