# FIX-066 - Bookmark dedie pour le KPI Comptes desactives avec licence
**Date**: 2026-03-23

## Diagnostic
- Le KPI `Comptes desactives avec licence` etait branche sur un bookmark humain desactive, pas sur un bookmark dedie au cas metier attendu.
- Ce branchement imposait une logique `TypeCompte = Utilisateur`, ce qui ne correspondait pas au besoin reel du KPI.
- Le comportement valide constate dans Desktop est: `StatutLicence = ON` et `Statut AD = Desactive`, sans restreindre artificiellement `TypeCompte`.

## Fix applique
- Ajout du bookmark dedie `Nav_CompteDesactivesAvecLicence` (`150a82ee4e0523134131`).
- Rebranchement du bouton [ux_action_disabled_btn_p3](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_disabled_btn_p3/visual.json) sur ce nouveau bookmark.
- Enregistrement du bookmark dans [bookmarks.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/bookmarks/bookmarks.json).

## Resultat attendu
- Le clic sur le KPI `Comptes desactives avec licence` applique bien:
  - `StatutLicence = ON`
  - `Statut AD = Desactive`
- Le resultat n'est plus derive du bookmark `Nav_HumainsDesactives`.
- Le filtre est maintenant aligne avec le comportement valide observe dans Power BI Desktop.
