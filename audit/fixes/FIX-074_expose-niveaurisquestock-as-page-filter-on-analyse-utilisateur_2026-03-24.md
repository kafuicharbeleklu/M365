# FIX-074 - Exposition de NiveauRisqueStock comme filtre de page sur Analyse Utilisateur
**Date**: 2026-03-24

## Diagnostic
- Sur `Analyse Utilisateur`, le seul bookmark restant avec un filtre non expose dans `Filters on this page` etait `Nav_UsersProduitsDepassement`.
- Ce bookmark filtre `T_Produits_Dim[NiveauRisqueStock] = 'Depassement'`.
- La page n'exposait pas encore `NiveauRisqueStock` dans son `filterConfig`, ce qui laissait un etat bookmark applique mais peu lisible dans l'UI.

## Fix applique
- Ajout de `T_Produits_Dim[NiveauRisqueStock]` dans `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/page.json`.
- Le filtre utilisateur reutilise l'identifiant `b5f1d2c3b4e50617283c` deja present dans `Nav_UsersProduitsDepassement`.
- Aucun changement de logique sur le bookmark lui-meme.

## Resultat attendu
- `Nav_UsersProduitsDepassement` doit maintenant restaurer un etat visible dans `Filters on this page`.
- Le filtre `NiveauRisqueStock = Depassement` devient inspectable et ajustable manuellement depuis le panneau de filtres.

## Controle de portee
- `Nav_UtilisateursFantomes` a ete relu pendant cette passe et reste aligne sur des filtres deja exposes (`TypeCompte`, `AccountEnabled`).
- Aucun traitement n'a ete applique aux anomalies legacy mentionnees dans `AGENTS.md` au-dela de ce perimetre cible.
