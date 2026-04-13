# FIX-117 - Clarify page-3 account-vs-license KPI reading and human-total label

## Summary
- Renamed the first page-3 KPI from `Total` to `Humains Totaux`.
- Clarified the page-3 help banner to state that the top KPI row counts distinct accounts, not license stock.
- Verified by source inspection that the page-3 technical KPIs already follow the product scope in the current model.

## Why
- The label `Total` was too generic and encouraged direct comparison with stock KPIs from the other pages.
- On page 3, the correct reconciliation under a product filter is `Humains Totaux + Tech. Totaux = Licences affectees`.
- The mismatch reported by the user was therefore a reading issue on the report page, not a missing product-scope branch in the current measure logic.

## Scope
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/678ebb458a124b23d8b3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/p3-drill-instruction/visual.json`

## Expected behavior
- The first KPI is clearly read as the total of human accounts in the current perimeter.
- The instruction banner explains that, under a product filter, `Humains Totaux + Tech. Totaux = Licences affectees`.
- Page 3 is less likely to be interpreted as a stock page.

## Validation
- Static source validation completed:
  - page-3 first KPI title updated to `Humains Totaux`
  - instruction banner updated with the reconciliation rule
  - current `_Mesures.tmdl` inspected: `NbBoitesActives`, `NbBoitesInactives`, and `CiblesNettoyage` already align with the product-filtered perimeter in the working tree
- Manual validation required in Power BI Desktop:
  - confirm the new `Humains Totaux` title fits cleanly
  - confirm the banner remains readable
  - confirm a single-product filter gives `Humains Totaux + Tech. Totaux = Licences affectees`
