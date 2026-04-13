# FIX-105 - Preserve page 3 slicer context when KPI bookmarks apply user filters

## Summary
- Removed the five left-side slicer visual states from the page 3 KPI bookmarks.
- Removed extra page-level placeholder filters from `Nav_CompteDesactivesAvecLicence`.
- Kept the business filters serialized by each bookmark (`TypeCompte`, `EtatActivite`, `Statut AD`, `StatutLicence`) so KPI clicks still drive the intended user subset.

## Why
- Page 3 started filtering the main table correctly by product only after `NomProduit` was added to the table.
- KPI clicks were still replaying the serialized slicer state from the bookmark, which cleared the current product selection and made the KPI action look inconsistent.
- The expected behavior is additive: the user keeps the current slicer context, then applies the KPI subset on top of it.

## Scope
- `M365_UI.Report/definition/bookmarks/02c501e8d87d63d0078c.bookmark.json`
- `M365_UI.Report/definition/bookmarks/66e80f63e44eee7812b9.bookmark.json`
- `M365_UI.Report/definition/bookmarks/fc8c08bf78c2215aa501.bookmark.json`
- `M365_UI.Report/definition/bookmarks/f4a061ed23da49a09717.bookmark.json`
- `M365_UI.Report/definition/bookmarks/bab47829329722d7d720.bookmark.json`
- `M365_UI.Report/definition/bookmarks/ca5213839361d51050a4.bookmark.json`
- `M365_UI.Report/definition/bookmarks/150a82ee4e0523134131.bookmark.json`

## Details
- Removed serialized states for these page 3 slicers from the KPI bookmarks:
  - `TypeLicence`
  - `NomProduit`
  - `Department`
  - `CountryOrRegion`
  - `WhenCreated`
- Removed page-level placeholder filters with `howCreated = 5` from `Nav_CompteDesactivesAvecLicence` for:
  - `EtatActivite`
  - `NomProduit`
  - `LastSignIn`
  - `Statut AD`
  - `CountryOrRegion`
  - `UserPrincipalName`
  - `DisplayName`
- Resulting behavior:
  - selecting `E3` in the product slicer keeps the table filtered to `E3`
  - clicking `Humains Inactifs`, `Humains Actifs`, `Utilisateurs Fantomes`, `Techniques`, or `Comptes desactives avec licence` now applies the KPI subset without resetting the current slicers

## Validation
- Static source validation completed:
  - the five slicer visual ids are no longer serialized in the seven KPI bookmarks
  - the extra `howCreated = 5` page placeholders are no longer present in `Nav_CompteDesactivesAvecLicence`
- Manual validation required in Power BI Desktop:
  - choose a product in the left slicer on `Analyse Utilisateur`
  - click each KPI bookmark
  - confirm the table stays filtered to the selected product while the KPI subset is applied
