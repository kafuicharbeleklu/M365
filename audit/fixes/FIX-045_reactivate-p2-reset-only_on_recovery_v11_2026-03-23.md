# FIX-045 - Reactivate P2 reset only on recovery V11
**Date**: 2026-03-23

## Context
- `RECOVERY_UI_SAFE_V10` remains stable after refresh.
- `Nav_Reset_P2` (`a5f1d2c3b4e50617283e`) is the first reset action being reintroduced after the isolated quick filters proved stable.
- The bookmark targets 6 slicers on page `54f9d470ac60b85b18da`, all of which still exist in the recovery shell.

## Decision
- Create `RECOVERY_UI_SAFE_V11` from `RECOVERY_UI_SAFE_V10`.
- Add only bookmark `a5f1d2c3b4e50617283e`.
- Reactivate only `ux_reset_filters_p2`.

## Explicitly Not Changed
- `Nav_HumainsActifs`
- `Nav_TechniquesActives`
- `Nav_TechniquesInactives`
- `Nav_UtilisateursFantomes`
- `P1` reset
- drillthrough reset

## Expected Result
- `P2` regains its reset action in addition to the already stable quick filters.
- If `V11` stays stable, resets are not globally broken; the remaining risk is concentrated in the still-disabled suspect bookmarks and any not-yet-reintroduced reset variants.
