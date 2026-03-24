# FIX-072 - Exposition de StatutLicence comme filtre de page sur Analyse Utilisateur
**Date**: 2026-03-24

## Diagnostic
- Le bookmark `Nav_CompteDesactivesAvecLicence` contenait bien un filtre `StatutLicence = ON`
- Mais `StatutLicence` n'etait pas declare comme filtre utilisateur dans `Analyse Utilisateur`
- Resultat: le panneau `Filters on this page` n'affichait que `TypeCompte`, `Statut AD`, `EtatActivite` et `AccountEnabled`

## Fix applique
- Ajout de `T_Utilisateurs_Dim[StatutLicence]` dans `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/page.json`
- Le filtre utilisateur reutilise l'identifiant `0702cdef1ed5a9113ad1` deja present dans le bookmark `Nav_CompteDesactivesAvecLicence`

## Resultat attendu
- Le panneau `Filters on this page` de `Analyse Utilisateur` doit maintenant exposer `StatutLicence`
- Le bookmark `Nav_CompteDesactivesAvecLicence` doit afficher et appliquer les deux filtres :
  - `Statut AD = Désactivé`
  - `StatutLicence = ON`
