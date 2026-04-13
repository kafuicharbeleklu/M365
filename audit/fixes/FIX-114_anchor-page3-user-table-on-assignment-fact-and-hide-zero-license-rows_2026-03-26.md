# FIX-114 - Anchor page 3 user table on assignment fact and hide zero-license rows

## Summary
- Added a dedicated measure `LicencesConsommeesTableau` that returns `BLANK()` when the current row has no real license assignment.
- Rebound the `UserPrincipalName` column of the main `Analyse Utilisateur` table to `T_Affectations_Fact[UserPrincipalName]`.
- Replaced the last table measure with `LicencesConsommeesTableau`.
- Updated the table title to reflect consumed licenses rather than raw cross-filtered license states.

## Why
- Under user filters and drillthrough-style navigation, the page-3 table could still show product rows with `0` where the selected user had no actual assignment.
- The requirement is to expose only the licenses really consumed by the filtered user or user subset.
- Anchoring the row grain on `T_Affectations_Fact` and blanking zero rows makes the table behavior align with the business expectation.

## Scope
- `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/87d3521e0b96312bffb0/visual.json`

## Expected behavior
- With a country filter and a search on a specific user, `Analyse Utilisateur` should list only the products actually assigned to that user.
- The last column now represents consumed licenses in the current row context and hides zero-value rows more aggressively.
- The drillthrough to `Detail Utilisateur` remains the detailed follow-up page, but the page-3 table should already be cleaner before the drillthrough.

## Validation
- Static source validation completed:
  - `UserPrincipalName` is now projected from `T_Affectations_Fact`
  - the last table measure now binds `LicencesConsommeesTableau`
  - the new measure returns `BLANK()` when `LicencesAffectees = 0`
- Manual validation required in Power BI Desktop:
  - filter `Pays = Togo`
  - search the target profile on `Analyse Utilisateur`
  - confirm only assigned products remain in the table
  - confirm the drillthrough `Detail Utilisateur` still shows the expected 5 assigned licenses
