# FIX-051 - Reactivate Nav_UtilisateursFantomes with corrected bookmark on recovery V17
**Date**: 2026-03-23

## Context
- `RECOVERY_UI_SAFE_V16` remains stable after refresh.
- `Nav_UtilisateursFantomes` is the last repository-known suspect bookmark still disabled in the recovery line.
- The legacy recovery copy is still `Signet 11` with incorrect filter `TypeCompte='Technique'`.
- The current `M365_UI.Report` already contains a corrected copy of bookmark `ca5213839361d51050a4` with:
  - `displayName = Nav_UtilisateursFantomes`
  - `TypeCompte = 'Utilisateur'`
  - `AccountEnabled = true`

## Decision
- Create `RECOVERY_UI_SAFE_V17` from `RECOVERY_UI_SAFE_V16`.
- Replace the legacy `ca5213839361d51050a4.bookmark.json` with the corrected version from the current report.
- Reactivate only button `ux_action_ghost_btn_p3`.

## Expected Result
- The `Utilisateurs Fantomes` KPI regains its bookmark action with the intended filter logic.
- If `V17` stays stable, the recovery line has fully restored the interactive layer, including all previously suspect bookmarks, using corrected definitions only.
