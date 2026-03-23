# FIX-042 - Reactivate P2 critical filter only on recovery V8
**Date**: 2026-03-23

## Context
- `RECOVERY_UI_SAFE_V7` remains stable after refresh.
- Reactivation is being resumed in single-interaction increments.
- `Nav_FiltreCritique` (`a5f1d2c3b4e50617283b`) targets only `ux_risk_quickfilter_p2`.

## Decision
- Create `RECOVERY_UI_SAFE_V8` from `RECOVERY_UI_SAFE_V7`.
- Add only bookmark `a5f1d2c3b4e50617283b`.
- Reactivate only `btn_filtre_critique_p2`.

## Explicitly Not Changed
- `Nav_HumainsActifs`
- `Nav_TechniquesActives`
- `Nav_TechniquesInactives`
- `Nav_UtilisateursFantomes`
- Other P2 filters and reset
- P1 and drillthrough bookmark reactivations

## Expected Result
- P2 regains only the "Stock critique <=10%" quick filter action.
- If `V8` stays stable, P2 can be restored incrementally using the same isolation strategy.
