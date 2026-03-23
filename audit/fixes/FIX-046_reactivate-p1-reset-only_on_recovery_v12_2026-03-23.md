# FIX-046 - Reactivate P1 reset only on recovery V12
**Date**: 2026-03-23

## Context
- `RECOVERY_UI_SAFE_V11` remains stable after refresh.
- `Nav_Reset_P1` (`a5f1d2c3b4e50617283d`) is structurally similar to the already stable `Nav_Reset_P2`.
- The 5 slicer targets referenced by the bookmark still exist in the recovery shell.

## Decision
- Create `RECOVERY_UI_SAFE_V12` from `RECOVERY_UI_SAFE_V11`.
- Add only bookmark `a5f1d2c3b4e50617283d`.
- Reactivate only `ux_reset_filters_p1`.

## Explicitly Not Changed
- `Nav_HumainsActifs`
- `Nav_TechniquesActives`
- `Nav_TechniquesInactives`
- `Nav_UtilisateursFantomes`
- drillthrough reset

## Expected Result
- `P1` regains its reset action in addition to the already stable interactions.
- If `V12` stays stable, the remaining unrecovered surface is mainly drillthrough reset plus the known-suspect bookmarks.
