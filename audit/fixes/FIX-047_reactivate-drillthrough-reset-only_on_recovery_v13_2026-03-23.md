# FIX-047 - Reactivate drillthrough reset only on recovery V13
**Date**: 2026-03-23

## Context
- `RECOVERY_UI_SAFE_V12` remains stable after refresh.
- `Nav_Reset_DT` (`a5f1d2c3b4e50617283f`) is the last non-suspect reset not yet restored.
- Unlike the page resets, this bookmark serializes no target visuals and no page visual state.

## Decision
- Create `RECOVERY_UI_SAFE_V13` from `RECOVERY_UI_SAFE_V12`.
- Add only bookmark `a5f1d2c3b4e50617283f`.
- Reactivate only `ux_reset_filters_dt`.

## Explicitly Not Changed
- `Nav_HumainsActifs`
- `Nav_TechniquesActives`
- `Nav_TechniquesInactives`
- `Nav_UtilisateursFantomes`

## Expected Result
- The drillthrough page regains its reset action.
- If `V13` stays stable, all non-suspect bookmark actions have been restored and only the repository-known suspect bookmarks remain disabled.
