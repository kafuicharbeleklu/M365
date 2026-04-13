# FIX-106 - Replace page 3 KPI click bookmarks with right-side analysis segments

## Summary
- Removed bookmark-driven click behavior from the five top KPI cards on `Analyse Utilisateur`.
- Kept the three right-side alert KPI cards visible, but made them informational only.
- Added explicit slicers below those three alert cards for `TypeCompte`, `EtatActivite`, `Statut AD`, `StatutLicence`, and `NiveauRisqueStock`.
- Extended the `Nav_Reset` bookmark so `Reinitialiser filtres` also clears the new right-side slicers.

## Why
- Product filtering on page 3 is now meaningful for the main table, but bookmark clicks were still forcing rigid business subsets on top of the current page state.
- The resulting user experience was confusing because page 2 talks in license counts while page 3 talks mostly in distinct account counts.
- Replacing KPI-click navigation with explicit slicers makes the combinations visible, additive, and easier to reason about under a current `NomProduit` selection.

## Scope
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/kpi_actifs_row_001/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ce70ef9e7866cc72b78d/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/d0f2e5dc55d345c41720/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ce426e14c617550ccd13/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/40e7ac536e9864857177/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/kpi_actifs_btn_001/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/bc689230263b260580e0/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/7a8b216031e010e2d1b4/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/1a2f23d55a380141ed88/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/b407bc3fe477ae00b21e/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_*_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_filter_panel_title_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_population_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_activite_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_statut_ad_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_licence_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_seg_risque_p3/visual.json`
- `M365_UI.Report/definition/bookmarks/1661112e2198ecabde3e.bookmark.json`

## Layout
- Right-side alert KPI cards kept visible at:
  - `Comptes desactives avec licence`: `x=300`, `y=276`, `w=300`, `h=120`
  - `Utilisateurs fantomes`: `x=300`, `y=412`, `w=300`, `h=120`
  - `Produits en depassement`: `x=300`, `y=548`, `w=300`, `h=120`
- Right-side slicers moved below the alert cards:
  - title banner: `x=300`, `y=686`, `w=300`, `h=42`
  - `Population`: `x=300`, `y=736`, `w=300`, `h=56`
  - `Activite`: `x=300`, `y=798`, `w=300`, `h=56`
  - `Statut AD`: `x=300`, `y=860`, `w=300`, `h=56`
  - `Statut licence`: `x=300`, `y=922`, `w=300`, `h=56`
  - `Risque stock`: `x=300`, `y=984`, `w=300`, `h=56`
- Transparent overlay buttons for the old alert bookmarks stay off-canvas so they no longer intercept the pointer.
- Top KPI overlays were pushed behind the cards and the cards themselves no longer serialize bookmark links.

## Expected behavior
- Selecting `Produit = Office 365 E1`, then refining with the right-side segments below the alert cards, now keeps the logic visible:
  - `Population = Utilisateur`
  - `Activite = Inactif > seuil`
  - `Statut AD = Desactive`
  - `Statut licence = ON/OFF`
  - `Risque stock = Depassement`
- The five KPI cards on top are now informational only.
- The three alert KPI cards on the right remain visible, but are no longer clickable.
- `Reinitialiser filtres` clears both the left slicers and the new right-side segments.

## Validation
- Static source validation completed:
  - top KPI cards no longer serialize bookmark links
  - top transparent overlay buttons were demoted behind the cards
  - new right-side slicers exist in page source
  - `Nav_Reset` contains empty slicer states for the new segment visuals
- Manual validation required in Power BI Desktop:
  - confirm the five top KPI cards no longer trigger bookmark filtering
  - confirm the three right-side alert KPI cards remain visible but do not filter on click
  - confirm the new right-side segments below those cards filter the main table under a current `Produit`
  - confirm `Reinitialiser filtres` clears the new segment selections
