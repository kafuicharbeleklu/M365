# FIX-076 - Alignement des KPI utilisateurs avec des comptes distincts sur Analyse Utilisateur
**Date**: 2026-03-24

## Diagnostic
- Le KPI `Comptes desactives avec licence` etait branche sur la mesure `LicencesComptesBloques`, qui compte des affectations de licences et non des comptes distincts.
- Le KPI `Utilisateurs Inactifs` etait deja correct: il pointait sur `NbHumainsInactifs`, donc sur un distinct count d'utilisateurs.
- L'ecart observe avec le tableau venait du total de `LicencesAffectees`, qui additionnait des licences sur les lignes utilisateurs et donnait une valeur non comparable au KPI utilisateurs.

## Fix applique
- Ajout de la mesure `NbComptesDesactivesAvecLicence` dans [_Mesures.tmdl](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.SemanticModel/definition/tables/_Mesures.tmdl), avec comptage distinct par `UserPrincipalName`, `AccountEnabled = FALSE()` et `StatutLicence = ON`.
- Rebranchement de la carte [ux_action_disabled_card_p3](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_disabled_card_p3/visual.json) sur cette nouvelle mesure.
- Masquage du total du tableau [87d3521e0b96312bffb0](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/87d3521e0b96312bffb0/visual.json) pour ne plus melanger un total de licences avec des KPI de comptes.
- Realignement des bookmarks P3 qui serialisaient encore l'ancienne mesure du KPI.

## Resultat attendu
- Un compte desactive possedant 3 licences vaut `1` dans le KPI `Comptes desactives avec licence`.
- Le KPI `Utilisateurs Inactifs` reste un comptage distinct d'utilisateurs.
- Le tableau continue d'afficher le nombre de licences par utilisateur, mais sans total trompeur en pied de table.
