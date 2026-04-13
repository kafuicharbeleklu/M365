# FIX-104 - Add page 3 user search slicer and align disabled KPI label

## Summary
- Added a compact user search slicer above the three alert cards on `Analyse Utilisateur`.
- Shifted the three alert cards and their transparent overlay buttons down to make room.
- Renamed the disabled KPI title to `Utilisateurs Désactivés`.

## Why
- Page 3 needed a direct user lookup entry point without forcing a scan of the main table.
- The alert column had enough vertical room to host a compact slicer if the cards were offset slightly.
- The disabled KPI label needed to use the explicit business wording expected by users.

## Scope
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_user_search_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_*_p3/visual.json`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/d0f2e5dc55d345c41720/visual.json`
- `M365_UI.Report/definition/bookmarks/1661112e2198ecabde3e.bookmark.json`

## Details
- New slicer:
  - field: `T_Utilisateurs_Dim[DisplayName]`
  - mode: `Dropdown`
  - header text: `Recherche utilisateur`
  - position: directly above the three stacked alert cards
- Alert card column layout:
  - first card/button: `y=276`
  - second card/button: `y=412`
  - third card/button: `y=548`
- KPI wording:
  - `Desactives` -> `Utilisateurs Désactivés`

## Validation
- Static source validation completed on the new visual, moved card/button coordinates, and reset bookmark entry.
- Manual validation required in Power BI Desktop:
  - confirm the new slicer appears above the three alert cards
  - confirm typing in the dropdown search filters the page as expected
  - confirm `Réinitialiser filtres` clears the new search selection
  - confirm the disabled KPI title wraps cleanly without overlap
