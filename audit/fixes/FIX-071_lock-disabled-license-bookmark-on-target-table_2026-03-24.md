# FIX-071 - Verrouillage du bookmark comptes desactives avec licence sur le tableau cible
**Date**: 2026-03-24

## Diagnostic
- Le bookmark `Nav_CompteDesactivesAvecLicence` appliquait deja `Statut AD = Desactive` et `StatutLicence = ON` au niveau global
- Le resultat du tableau restait toutefois different du filtrage manuel valide via segments
- Le tableau `87d3521e0b96312bffb0` n'avait pas encore ses propres filtres categoriels verrouilles pour ce cas d'usage

## Fix applique
- Ajout dans `150a82ee4e0523134131.bookmark.json` de deux filtres categoriels directement sur le tableau cible :
  - `Statut AD = Desactive`
  - `StatutLicence = ON`

## Resultat attendu
- Le clic sur `Comptes desactives avec licence` doit produire le meme resultat que le filtrage manuel via segments
- Le tableau ne doit plus melanger les comptes sans licence avec les comptes desactives ayant une licence
