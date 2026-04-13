# FIX-107 - Restore page 3 table product grain from affectations fact

## Summary
- Rebound the `NomProduit` column of the main table on `Analyse Utilisateur` to `T_Affectations_Fact[NomProduit]`.
- Preserved the rest of the table layout and measures, including `NomUtilisateurAffiche` and `LicencesAffectees`.

## Why
- The current page 3 table was showing many user rows with `LicencesAffectees = 0` under a current product filter.
- This happened because the table projected `T_Produits_Dim[NomProduit]`, which let the visual keep user rows from the dimension grain while the measure dropped to `0`.
- The older `Lab` version anchored the product column on `T_Affectations_Fact[NomProduit]`, which is closer to the real assignment grain and better suited to a product-filtered user list.

## Scope
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/87d3521e0b96312bffb0/visual.json`

## Expected behavior
- With `Produit = Office 365 E1`, the table should now list only rows backed by actual E1 assignment facts instead of keeping users with `LicencesAffectees = 0`.
- The product column shown in the table now reflects the assignment fact grain, aligned with the selected product.

## Validation
- Static source validation completed:
  - the table projection now uses `T_Affectations_Fact.NomProduit`
  - the visual-level filter binding on `T_Affectations_Fact.NomProduit` remains intact
- Manual validation required in Power BI Desktop:
  - filter `Produit = Office 365 E1`
  - verify that rows with `LicencesAffectees = 0` disappear from the table
  - verify that the remaining row count matches the in-scope user list for the selected product
