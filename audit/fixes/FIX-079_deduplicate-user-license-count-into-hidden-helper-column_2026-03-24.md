# FIX-079 - Deduplication du nombre de licences par utilisateur dans une colonne cachee
**Date**: 2026-03-24

## Diagnostic
- `T_Utilisateurs_Dim[StatutLicence]` recalculait le nombre de licences affectees par utilisateur.
- `T_Utilisateurs_Dim[EstDesactiveAvecLicence]` recalculait exactement le meme volume avec la meme logique de normalisation UPN.
- Ce doublon augmentait le risque d'incoherence si une seule des deux expressions evoluait plus tard.

## Fix applique
- Ajout de la colonne cachee `NbLicencesAffecteesDistinctes` dans `T_Utilisateurs_Dim`.
- Rebranchement de `StatutLicence` sur cette colonne cachee.
- Rebranchement de `EstDesactiveAvecLicence` sur cette colonne cachee.

## Resultat attendu
- Une seule logique de comptage de licences affectees au niveau utilisateur.
- Une meilleure maintenabilite des colonnes derivees liees aux licences.
- Aucun changement fonctionnel attendu sur les visuels existants, hors correction future plus simple si la regle doit evoluer.

## Validation manuelle requise
- Rafraichir le modele dans Power BI Desktop.
- Verifier que `StatutLicence` continue de retourner `ON/OFF` comme avant.
- Verifier que les filtres et KPI bases sur `EstDesactiveAvecLicence` restent coherents.
