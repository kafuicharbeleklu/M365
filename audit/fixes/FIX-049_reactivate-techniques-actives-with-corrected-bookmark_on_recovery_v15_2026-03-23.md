# FIX-049 - Reactivate Nav_TechniquesActives with corrected bookmark on recovery V15
**Date**: 2026-03-23

## Context
- `RECOVERY_UI_SAFE_V14` remains stable after refresh.
- `Nav_TechniquesActives` is a repository-known suspect bookmark because the legacy recovery copy still references deleted visual `04a9392b160996ab9007`.
- The current `M365_UI.Report` already contains a corrected copy of bookmark `f4a061ed23da49a09717` with `targetVisualNames: []`.

## Decision
- Create `RECOVERY_UI_SAFE_V15` from `RECOVERY_UI_SAFE_V14`.
- Replace the legacy `f4a061ed23da49a09717.bookmark.json` with the corrected version from the current report.
- Reactivate only button `1a2f23d55a380141ed88`.

## Explicitly Not Changed
- `Nav_TechniquesInactives`
- `Nav_UtilisateursFantomes`

## Expected Result
- The `Techniques Actives` KPI regains its bookmark action without reintroducing the deleted target visual reference.
- If `V15` stays stable, the same repair pattern can be applied to `Nav_TechniquesInactives`.
