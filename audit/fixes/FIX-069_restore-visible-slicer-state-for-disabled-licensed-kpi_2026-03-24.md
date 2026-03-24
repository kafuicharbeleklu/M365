# FIX-069 - Restauration de l'etat des segments visibles pour le KPI comptes desactives avec licence
**Date**: 2026-03-24

## Diagnostic
- Le bookmark `Nav_CompteDesactivesAvecLicence` conservait bien les filtres de section `Statut AD = Desactive` et `StatutLicence = ON`
- En revanche, l'etat des segments visibles `Statut AD` et `StatutLicence` n'etait plus capture dans le bookmark
- Cette simplification rendait le clic KPI different du filtrage manuel via segments, alors que le cas d'usage valide est celui teste manuellement

## Fix applique
- Ajout dans `150a82ee4e0523134131.bookmark.json` de l'etat des segments visibles :
  - `7c987dd0a69bc50ae8d6` pour `Statut AD = Desactive`
  - `e0d8483582d3ec82b9bc` pour `StatutLicence = ON`
  - `18e02ee723e342995a61` conserve sans selection imposee pour ne pas forcer `TypeCompte`

## Resultat attendu
- Le clic sur `Comptes desactives avec licence` reproduit le meme etat que la selection manuelle des segments
- Le segment `Statut AD` doit afficher `Desactive`
- Le segment `StatutLicence` doit afficher `ON`
- Le tableau doit se comporter comme lors du filtrage manuel valide par l'utilisateur
