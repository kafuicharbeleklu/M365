# FIX-062 - Indicateur cache pour comptes desactives avec licence
**Date**: 2026-03-23

## Diagnostic
- Le fallback `FIX-061` (`StatutLicence = ON`) n'a pas suffi: la vue `Comptes desactives avec licence` continuait a afficher des comptes desactives sans licence.
- Le filtre avance sur mesure `LicencesAffectees > 0` reste exclu car il a deja provoque une regression d'ouverture en page blanche.
- Il fallait donc une cle de filtre stable, calculee au refresh, mais plus precise que `StatutLicence` seul.

## Fix applique
- Ajout de la colonne calculee cachee `T_Utilisateurs_Dim[EstDesactiveAvecLicence]`.
- La colonne calcule directement:
  - `TypeCompte = "Utilisateur"`
  - `AccountEnabled = FALSE()`
  - `DISTINCTCOUNT(T_Affectations_Fact[AffectationID]) > 0`
- Le bookmark `dacdeaf07eb2d1577049` filtre maintenant `EstDesactiveAvecLicence = true`.

## Resultat attendu
- Le clic sur `Comptes desactives avec licence` n'affiche plus les comptes desactives sans licence.
- La coloration rouge du tableau reste coherente avec les lignes visibles.
- Le projet conserve une strategie de filtrage stable, sans retour au filtre de mesure qui cassait l'ouverture.
