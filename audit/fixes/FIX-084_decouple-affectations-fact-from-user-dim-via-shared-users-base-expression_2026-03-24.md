# FIX-084 - Decouple T_Affectations_Fact from T_Utilisateurs_Dim via shared users base expression
**Date**: 2026-03-24

## Diagnostic
- `T_Affectations_Fact` etait source directement depuis `T_Utilisateurs_Dim`.
- Cette forme couplait la table de faits a toute la structure de la dimension utilisateurs, alors que la table de faits n'a besoin en amont que de `UserPrincipalName` et `Licences_Brutes`.
- Ce couplage rendait les refactorings de `T_Utilisateurs_Dim` plus risqués et entretenait une confusion entre source technique et enrichissements metier.

## Fix applique
- Ajout d'une expression M partagee `GetUsersBaseTable` dans `M365_UI.SemanticModel/definition/expressions.tmdl`.
- `GetUsersBaseTable` centralise la lecture Graph des utilisateurs, l'expansion des colonnes brutes utiles, le calcul de `LastSignIn` et le typage initial.
- `T_Affectations_Fact` repart maintenant de `GetUsersBaseTable` au lieu de `T_Utilisateurs_Dim`.
- `T_Utilisateurs_Dim` est egalement rebranchee sur `GetUsersBaseTable` pour ses corrections geographiques et enrichissements aval, ce qui aligne l'amont des deux tables sans toucher aux colonnes metier du modele.
- Le preambule Graph devenu mort dans la partition de `T_Utilisateurs_Dim` a ete retire pour ne conserver qu'un seul point d'entree technique amont.

## Resultat attendu
- `T_Affectations_Fact` n'est plus source depuis la dimension utilisateurs.
- Les deux tables reutilisent le meme socle technique amont pour les utilisateurs bruts.
- Les futurs refactorings de `T_Utilisateurs_Dim` seront moins susceptibles de casser la table de faits.
- La partition utilisateurs ne porte plus de logique Graph dupliquee ni de variables M inutilisees.

## Validation manuelle requise
- Ouvrir le projet dans Power BI Desktop.
- Rafraichir le modele.
- Verifier que `T_Utilisateurs_Dim` et `T_Affectations_Fact` se chargent sans erreur.
- Verifier que les pages `Analyse Utilisateur`, `Analyse Licences` et le drillthrough utilisateur restent coherentes.
