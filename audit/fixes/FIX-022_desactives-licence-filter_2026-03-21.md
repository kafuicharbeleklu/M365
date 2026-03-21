# FIX-022 — Filtre Comptes désactivés avec licence
**Date**: 2026-03-21

## Diagnostic
- StatutLicence = "ON" est calculé au refresh (snapshot statique)
- LicencesAffectees est une mesure sensible au contexte
- Divergence possible : StatutLicence=ON mais LicencesAffectees=0
  sous filtre actif → lignes sans licence apparaissaient dans le tableau

## Fix appliqué
Ajout d'un filtre visuel LicencesAffectees > 0 (ComparisonKind=1)
sur le visuel table 87d3521e0b96312bffb0 dans le bookmark
dacdeaf07eb2d1577049.

## Résultat attendu
- Seules les lignes avec LicencesAffectees > 0 apparaissent
- Ces lignes sont toutes surlignées en rouge (FlagLigneCompteDesactive)
- Aucune ligne sans licence visible
