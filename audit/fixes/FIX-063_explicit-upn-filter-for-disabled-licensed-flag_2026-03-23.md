# FIX-063 - Filtrage explicite par UPN pour les comptes desactives avec licence
**Date**: 2026-03-23

## Diagnostic
- Le bookmark `dacdeaf07eb2d1577049` filtrait bien `EstDesactiveAvecLicence = true`, mais le tableau continuait a afficher des comptes desactives sans licence.
- La coloration de ligne restait correcte, ce qui pointait vers un probleme de calcul dans les colonnes derivees `StatutLicence` et `EstDesactiveAvecLicence`, pas vers le visuel.
- Les deux colonnes comptaient `T_Affectations_Fact[AffectationID]` sans filtre explicite sur `UserPrincipalName`, ce qui pouvait remonter un total trop large au refresh.

## Fix applique
- Correction de `T_Utilisateurs_Dim[StatutLicence]` avec un comptage explicite des affectations par `UserPrincipalName`.
- Correction de `T_Utilisateurs_Dim[EstDesactiveAvecLicence]` avec la meme logique explicite, normalisee par `LOWER(TRIM())`.
- Aucun changement du tableau ni du bookmark: le filtre existant reste `EstDesactiveAvecLicence = true`, mais il s'appuie maintenant sur une colonne fiable.

## Resultat attendu
- Le clic sur `Comptes desactives avec licence` ne doit plus afficher de comptes a `LicencesAffectees = 0`.
- `StatutLicence` redevient coherent pour les slicers et vues qui l'utilisent.
- La coloration rouge du tableau et les lignes visibles convergent enfin sur le meme perimetre metier.
