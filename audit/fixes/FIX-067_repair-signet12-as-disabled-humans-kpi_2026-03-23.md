# FIX-067 - Reparation de Signet 12 pour le KPI Desactives
**Date**: 2026-03-23

## Diagnostic
- Le bouton [7a8b216031e010e2d1b4/visual.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/7a8b216031e010e2d1b4/visual.json) recouvrait la carte [d0f2e5dc55d345c41720/visual.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/d0f2e5dc55d345c41720/visual.json), basee sur la mesure `NbHumainsDesactives`.
- Ce bouton pointait vers [fc8c08bf78c2215aa501.bookmark.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/bookmarks/fc8c08bf78c2215aa501.bookmark.json), encore nomme `Signet 12`.
- Le bookmark ne filtrait que `TypeCompte = Technique`, ce qui etait incoherent avec la carte `Désactivés`.

## Fix applique
- Conservation de l'ID bookmark `fc8c08bf78c2215aa501` pour eviter un retarget inutile du bouton.
- Renommage du displayName en `Nav_HumainsDesactivesKPI`.
- Remplacement du filtre `TypeCompte = Technique` par:
  - `TypeCompte = Utilisateur`
  - `Statut AD = Désactivé`
- Ajout de `suppressDisplay = true` pour en faire un bookmark d'action non ambigu.

## Resultat attendu
- Le clic sur la carte `Désactivés` applique un filtre coherent avec la mesure `NbHumainsDesactives`.
- `Signet 12` ne reste plus un bookmark orphelin et non documente.
