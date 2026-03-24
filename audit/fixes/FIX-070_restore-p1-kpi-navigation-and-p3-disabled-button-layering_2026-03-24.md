# FIX-070 - Restauration de la navigation KPI P1 et du bouton P3 comptes desactives avec licence
**Date**: 2026-03-24

## Diagnostic
- Le bouton transparent `ux_action_disabled_btn_p3` etait derriere sa carte KPI sur `Analyse Utilisateur`
- Les cartes KPI de `Vue d'ensemble` avaient ete converties en `Drillthrough` au lieu de leur navigation de page attendue
- La page `Analyse Utilisateur` avait perdu son `pageBinding` de type `Drillthrough`

## Fix applique
- Remontee du bouton `ux_action_disabled_btn_p3` au-dessus de `ux_action_disabled_card_p3`
- Restauration des cartes KPI P1 en `PageNavigation` :
  - vers `Analyse Utilisateur` pour les KPI humains
  - vers `Analyse Licences` pour les KPI licences
- Restauration du `pageBinding` `Drillthrough` de `Analyse Utilisateur`

## Resultat attendu
- Le KPI `Comptes desactives avec licence` redevient cliquable
- Les KPI de `Vue d'ensemble` redeviennent navigables
- Les usages legitimes de drillthrough vers `Analyse Utilisateur` restent disponibles
