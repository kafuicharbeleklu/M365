# FIX-115 - Refine page 3 consumed-license table layout after drillthrough-table reuse

## Summary
- Kept the new page-3 table based on the drillthrough license-detail visual because it correctly filters only real assignments.
- Reworked the page-3 table column set to match the analysis workflow: `DisplayName`, `UserPrincipalName`, `Department`, `Statut AD`, `EtatActivite`, `LastSignIn`, `NomProduit`, `TypeLicence`.
- Removed the drillthrough-only `CodeSKU` column from the page-3 table.
- Added an explicit sort by `DisplayName` then `NomProduit`.
- Tightened the visual position and renamed the title to `Licences consommees du perimetre filtre`.

## Why
- The copied drillthrough visual solved the row-grain issue on page 3, but its presentation was still optimized for a user-detail page rather than the broader `Analyse Utilisateur` page.
- The page-3 table needs to stay assignment-based while surfacing activity and account-status context useful for cleanup decisions.
- Removing `CodeSKU` frees horizontal space for `LastSignIn`, which is more actionable on the analysis page.

## Scope
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/2110cfd8ad8ca81897f9/visual.json`

## Expected behavior
- Page 3 continues to list only assigned licenses for the filtered perimeter.
- The table is easier to read for operational analysis and not just user drillthrough.
- Sorting stays stable and readable when several users are visible in the same perimeter.

## Validation
- Static source validation completed:
  - page-3 table projections now favor analysis fields over drillthrough-only fields
  - the title reflects consumed licenses in the current filter perimeter
  - sort order is defined on `DisplayName` and `NomProduit`
- Manual validation required in Power BI Desktop:
  - confirm the page-3 table still shows only assigned licenses
  - confirm the removed `CodeSKU` column is no longer shown
  - confirm `LastSignIn` is visible and useful in the available width
