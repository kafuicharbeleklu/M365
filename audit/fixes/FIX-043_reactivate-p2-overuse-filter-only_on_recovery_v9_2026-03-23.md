# FIX-043 - Reactivate P2 overuse filter only on recovery V9
**Date**: 2026-03-23

## Context
- `RECOVERY_UI_SAFE_V8` remains stable after refresh.
- Incremental reactivation is still limited to one interaction per step.
- `Nav_FiltreDepassement` (`a5f1d2c3b4e506172839`) targets only `ux_risk_quickfilter_p2`.

## Decision
- Create `RECOVERY_UI_SAFE_V9` from `RECOVERY_UI_SAFE_V8`.
- Add only bookmark `a5f1d2c3b4e506172839`.
- Reactivate only `btn_filtre_depassement_p2`.

## Explicitly Not Changed
- `Nav_HumainsActifs`
- `Nav_TechniquesActives`
- `Nav_TechniquesInactives`
- `Nav_UtilisateursFantomes`
- P2 exhausted filter and reset
- P1 and drillthrough bookmark reactivations

## Expected Result
- P2 regains only the "Depassement" quick filter action in addition to the already stable actions.
- If `V9` stays stable, the remaining risk is likely concentrated in reset behavior or the still-disabled suspect bookmarks.
