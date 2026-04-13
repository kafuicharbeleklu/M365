# FIX-109 - Clarify inactive-license and cleanup-target tooltips

## Summary
- Clarified the tooltip copy for inactive licenses on pages 1 and 2.
- Corrected the `Comptes a traiter` tooltip on page 3 so it matches the actual `CiblesNettoyage` measure.

## Why
- Users reconciling `Office 365 E1` were seeing an apparent mismatch between `Licences Inactives` and the visible user breakdown on `Analyse Utilisateur`.
- The current tooltip copy was ambiguous on page 2 and incorrect on page 3:
  - inactive licenses were described too broadly
  - `Comptes a traiter` still mentioned `fantomes` even though the measure now uses `jamais connectes` and `boites inactives`
- This wording made it harder to understand that `LicencesInactives` counts:
  - disabled human accounts with an assigned license
  - active human accounts that are `INACTIF` or `JAMAIS_CONNECTE`

## Scope
- `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`

## Expected behavior
- Hovering `Licences Inactives` now states the current business rule explicitly.
- Hovering `Comptes a traiter` now reflects the real `CiblesNettoyage` composition:
  - `Inactifs`
  - `Jamais connectes`
  - `Desactives`
  - `Boites inactives`
- The tooltip no longer implies that `fantomes` are part of `Comptes a traiter`.

## Validation
- Static source validation completed:
  - `TT_p1_lic_inactives_*` and `TT_p2_inactives_*` now describe disabled + inactive/jamais connecte humans only
  - `TT_p3_cibles_*` now matches `CiblesNettoyage`
- Manual validation required in Power BI Desktop:
  - filter `Produit = Office 365 E1`
  - hover `Licences Inactives` on page 2
  - hover `Comptes a traiter` on page 3
  - verify the tooltip wording matches the actual rows returned by the table filters
