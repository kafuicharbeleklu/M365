# FIX-050 - Reactivate Nav_TechniquesInactives with corrected bookmark on recovery V16
**Date**: 2026-03-23

## Context
- `RECOVERY_UI_SAFE_V15` remains stable after refresh.
- `Nav_TechniquesInactives` is a repository-known suspect bookmark because the legacy recovery copy still references deleted visual `04a9392b160996ab9007`.
- The current `M365_UI.Report` already contains a corrected copy of bookmark `bab47829329722d7d720` with `targetVisualNames: []`.

## Decision
- Create `RECOVERY_UI_SAFE_V16` from `RECOVERY_UI_SAFE_V15`.
- Replace the legacy `bab47829329722d7d720.bookmark.json` with the corrected version from the current report.
- Reactivate only button `b407bc3fe477ae00b21e`.

## Explicitly Not Changed
- `Nav_UtilisateursFantomes`

## Expected Result
- The `Techniques Inactives` KPI regains its bookmark action without reintroducing the deleted target visual reference.
- If `V16` stays stable, the only remaining disabled case is `Nav_UtilisateursFantomes`.
