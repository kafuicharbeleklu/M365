# FIX-075 - Alignement des bookmarks P2 de risque avec le filtre visible NiveauRisqueStock
**Date**: 2026-03-24

## Diagnostic
- Sur `Analyse Licences`, les bookmarks `Nav_FiltreCritique`, `Nav_FiltreDepassement` et `Nav_FiltreEpuise` pilotaient uniquement le slicer `ux_risk_quickfilter_p2`.
- La page `54f9d470ac60b85b18da` n'exposait pas clairement ce filtre dans `Filters on this page`, ce qui rendait l'etat des quick filters peu lisible.
- `Nav_Reset_P2` ne reinitialisait que l'etat des slicers cibles et pas un filtre de page visible equivalent.

## Fix applique
- Ajout de `T_Produits_Dim[NiveauRisqueStock]` comme filtre de page utilisateur dans `M365_UI.Report/definition/pages/54f9d470ac60b85b18da/page.json`.
- Normalisation des bookmarks P2 suivants pour qu'ils appliquent aussi un vrai filtre de page sur `NiveauRisqueStock`:
  - `Nav_FiltreCritique` -> `Stock critique`
  - `Nav_FiltreDepassement` -> `Depassement`
  - `Nav_FiltreEpuise` -> `Stock epuise`
- `Nav_Reset_P2` vide maintenant aussi ce filtre de page via une entree `expression` sans valeur.
- L'etat du slicer `ux_risk_quickfilter_p2` est conserve dans les bookmarks pour garder la coherence visuelle du quick filter.

## Resultat attendu
- Les quick filters P2 doivent maintenant restaurer un etat visible dans `Filters on this page`.
- Le reset P2 doit effacer a la fois le filtre visible `NiveauRisqueStock` et l'etat du quickfilter.

## Controle de portee
- Aucun changement de logique metier sur `NiveauRisqueStock`.
- Les autres slicers P2 restent inchanges.
