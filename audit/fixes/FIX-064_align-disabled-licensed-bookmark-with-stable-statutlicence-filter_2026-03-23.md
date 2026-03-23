# FIX-064 - Alignement du bookmark desactives avec licence sur le filtre stable StatutLicence
**Date**: 2026-03-23

## Diagnostic
- La version `Lab` a confirme que le comportement historique stable reposait sur un schema de filtrage plus simple que le bookmark courant.
- Le projet actif utilisait pour `dacdeaf07eb2d1577049` un filtre booléen `EstDesactiveAvecLicence = true`, plus fragile a diagnostiquer et different des autres bookmarks stables deja presents sur la page.
- Le bookmark `Nav_LicencesGaspillees` utilise deja avec succes un filtre texte `StatutLicence = 'ON'`.

## Fix applique
- Remplacement dans `dacdeaf07eb2d1577049.bookmark.json` du filtre `EstDesactiveAvecLicence = true` par `StatutLicence = 'ON'`.
- Conservation des autres filtres du bookmark:
  - `TypeCompte = 'Utilisateur'`
  - `Statut AD = 'Desactive'`
- Le calcul de `StatutLicence` reste celui corrige par `FIX-063`, scope explicitement par `UserPrincipalName`.

## Resultat attendu
- Le clic sur `Comptes desactives avec licence` utilise le meme mecanisme stable que les autres vues par licence.
- Les comptes desactives sans licence ne doivent plus remonter dans le tableau.
- Le bookmark reste compatible avec la structure actuelle du report, sans reintroduire le filtre de mesure qui avait casse l'ouverture.
