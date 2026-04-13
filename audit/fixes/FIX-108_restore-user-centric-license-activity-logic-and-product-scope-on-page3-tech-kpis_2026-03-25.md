# FIX-108 - Restore user-centric license activity logic and product scope on page 3 tech KPIs

## Summary
- Restored a user-centric business rule for `LicencesInactives` based on the older `Lab` logic instead of the broad shortcut `LicencesAffectees - LicencesActives`.
- Realigned `LicencesActives` to derive from the restored `LicencesInactives` logic.
- Made `NbBoitesActives`, `NbBoitesInactives`, and `CiblesNettoyage` sensitive to the current product scope on `Analyse Utilisateur`.

## Why
- The current model had drifted away from the older report logic and was classifying every non-`ACTIF` assignment as an inactive license.
- This was inflating page 2 license inactivity versus page 3 user inactivity, especially when comparing a single SKU such as `Office 365 E1`.
- On page 3, some technical KPIs and `Comptes a traiter` were still returning global values under a current product filter, which made the comparison even harder to interpret.

## Logic
- `LicencesInactives` now counts licenses assigned to:
  - disabled human accounts
  - active human accounts whose `CodeEtatActivite` is `INACTIF` or `JAMAIS_CONNECTE`
- `LicencesActives` is again derived as `LicencesAffectees - LicencesInactives`.
- `NbBoitesActives` and `NbBoitesInactives` now use the same product-scoping pattern already used by `NbBoitesTotal`.
- `CiblesNettoyage` is rebuilt from scoped component measures instead of the unscoped `IsCible` row count.

## Scope
- `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`

## Expected behavior
- A single-product comparison between `Analyse Licences` and `Analyse Utilisateur` should now be materially closer and easier to reconcile.
- Page 3 technical KPIs should no longer stay global under a current product filter.
- `Comptes a traiter` should now follow the same current product scope as the rest of the user page.

## Validation
- Static source validation completed:
  - `LicencesInactives` no longer uses the broad complement shortcut
  - `NbBoitesActives`, `NbBoitesInactives`, and `CiblesNettoyage` are now product-aware
- Manual validation required in Power BI Desktop:
  - filter `Produit = Office 365 E1` on page 2 and page 3
  - compare `Licences Inactives` with the user population returned by page 3 under equivalent inactive filters
  - verify that `Tech. Actifs`, `Tech. Inactifs`, and `Comptes a traiter` now change under the product filter
