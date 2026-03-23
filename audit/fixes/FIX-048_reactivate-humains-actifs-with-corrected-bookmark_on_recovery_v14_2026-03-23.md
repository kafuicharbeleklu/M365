# FIX-048 - Reactivate Nav_HumainsActifs with corrected bookmark on recovery V14
**Date**: 2026-03-23

## Context
- `RECOVERY_UI_SAFE_V13` is the current stable recovery baseline.
- `Nav_HumainsActifs` is one of the repository-known suspect bookmarks because the legacy recovery copy still references deleted visual `04a9392b160996ab9007`.
- The current `M365_UI.Report` already contains a corrected copy of bookmark `02c501e8d87d63d0078c` with `targetVisualNames: []`.

## Decision
- Create `RECOVERY_UI_SAFE_V14` from `RECOVERY_UI_SAFE_V13`.
- Replace the legacy `02c501e8d87d63d0078c.bookmark.json` with the corrected version from the current report.
- Reactivate only button `kpi_actifs_btn_001`.

## Explicitly Not Changed
- `Nav_TechniquesActives`
- `Nav_TechniquesInactives`
- `Nav_UtilisateursFantomes`

## Expected Result
- The `Humains Actifs` KPI regains its bookmark action without reintroducing the deleted target visual reference.
- If `V14` stays stable, the same repair pattern can be applied to the two remaining broken technical-account bookmarks.
