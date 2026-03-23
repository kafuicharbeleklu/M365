# FIX-052 - Finalize V17 as full interactive recovery baseline
**Date**: 2026-03-23

## Context
- `RECOVERY_UI_SAFE_V13` restored the full non-suspect interactive layer and was committed to Git.
- `RECOVERY_UI_SAFE_V14` to `RECOVERY_UI_SAFE_V17` restored the 4 repository-known suspect bookmarks one by one using corrected bookmark definitions from the current `M365_UI.Report`.
- Each step was validated manually in Power BI Desktop after refresh.

## Result
- `RECOVERY_UI_SAFE_V17` is the first recovery snapshot with the full interactive layer restored:
  - `Nav_HumainsActifs`
  - `Nav_TechniquesActives`
  - `Nav_TechniquesInactives`
  - `Nav_UtilisateursFantomes`
  - P1 reset
  - P2 filters + reset
  - P3 actions + reset
  - drillthrough reset

## Important Notes
- The restored suspect bookmarks use corrected definitions:
  - no reference to deleted visual `04a9392b160996ab9007`
  - `Nav_UtilisateursFantomes` uses `TypeCompte='Utilisateur'` + `AccountEnabled=true`
- This fix records `RECOVERY_UI_SAFE_V17` as the recommended working baseline to continue report work.
- The original root `M365_UI` project was not silently overwritten.
