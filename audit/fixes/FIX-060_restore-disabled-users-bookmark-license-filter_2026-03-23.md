# FIX-060 - Restauration du filtre licence sur le bookmark des comptes desactives
**Date**: 2026-03-23

## Diagnostic
- Le KPI `Comptes desactives avec licence` ouvrait bien le bookmark `dacdeaf07eb2d1577049`.
- Le formatage rouge du tableau etait correct: il depend de `FlagLigneCompteDesactive`.
- En revanche, le filtre visuel du tableau avait perdu sa condition serializee.
- Resultat: le tableau melangeait des comptes desactives avec licence et des comptes desactives sans licence.

## Fix applique
- Restauration du filtre avance `LicencesAffectees > 0` sur le visuel table `87d3521e0b96312bffb0`
  dans le bookmark `dacdeaf07eb2d1577049`.
- La definition restauree utilise:
  - `ComparisonKind = 1`
  - mesure `_Mesures[LicencesAffectees]`
  - comparaison `> 0`

## Resultat attendu
- Le tableau n'affiche plus que les comptes desactives avec au moins une licence.
- Toutes les lignes visibles de ce tableau sont coherentes avec la mise en rouge.
- Les comptes desactives sans licence ne doivent plus apparaitre dans cette vue.
