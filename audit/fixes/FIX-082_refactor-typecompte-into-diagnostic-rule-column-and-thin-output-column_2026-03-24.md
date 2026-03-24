# FIX-082 - Refactor TypeCompte en colonne de regle diagnostique + sortie fine
**Date**: 2026-03-24

## Diagnostic
- `T_Utilisateurs_Dim[TypeCompte]` concentrait toute la logique heuristique de classification dans une seule formule longue et peu lisible.
- Cette forme rendait les audits difficiles, surtout pour comprendre pourquoi un compte etait classe `Technique`.
- Les regles bornees introduites par `FIX-004` devaient etre preservees, mais la structure devait etre rendue plus maintenable.

## Fix applique
- `TypeCompte` devient une colonne de sortie simple, basee sur une nouvelle colonne cachee `RegleTypeCompte`.
- Toute la logique de classification est deplacee dans `RegleTypeCompte`, avec des codes diagnostiques explicites tels que:
  - `TECH_SIGNAL_GUEST`
  - `TECH_SIGNAL_EXT`
  - `TECH_SHARED_ROOM`
  - `TECH_ADMIN_BOUNDED`
  - `TECH_FORMATION_BOUNDED`
  - `TECH_VISIT_BOUNDED`
  - `USER_DEFAULT`
- Les patterns a risque bornes dans `FIX-004` ont ete conserves.
- Les motifs accentues critiques (`conference`, `reunion`, `conge`) restent couverts via `UNICHAR(...)`.

## Resultat attendu
- La sortie metier `TypeCompte` reste `Technique`, `Utilisateur` ou `Non defini`.
- Le modele gagne une trace de diagnostic exploitable pour les audits de faux positifs.
- Les futures evolutions de classification pourront etre faites dans `RegleTypeCompte` sans alourdir la colonne visible.

## Validation manuelle requise
- Rafraichir le modele dans Power BI Desktop.
- Verifier que les KPI et filtres bases sur `TypeCompte` ne changent pas de comportement.
- Controler sur un echantillon de comptes techniques connus que `RegleTypeCompte` remonte bien une famille de regle attendue.
