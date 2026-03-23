# FIX-059 - Clarification du bandeau de contexte sur les comptes desactives avec licence
**Date**: 2026-03-23

## Diagnostic
- Le bookmark `Nav_HumainsDesactives` filtre correctement `TypeCompte = Utilisateur` et `Statut AD = Désactivé`.
- Le bandeau `UX_ContexteFiltres` ne lisait pourtant que `EtatActivite`.
- Dans ce contexte, tous les comptes desactives remontent `EtatActivite = Exclu`, ce qui affichait a tort `Etat: Exclu` dans l'en-tete.

## Fix applique
- Mise a jour de `UX_ContexteFiltres` pour afficher aussi:
  - `Type`
  - `AD`
- Neutralisation du cas technique `EtatActivite = Exclu`:
  - si un filtre `TypeCompte` ou `Statut AD` est deja actif, le bandeau affiche `Etat: Tous`
  - sinon, `Exclu` est degrade en `N/A`

## Resultat attendu
- Un clic sur `Comptes desactives avec licence` affiche un contexte lisible:
  - `Type: Utilisateur`
  - `AD: Désactivé`
  - `Etat: Tous`
- Le bandeau ne suggere plus un faux filtre metier `Exclu`.
