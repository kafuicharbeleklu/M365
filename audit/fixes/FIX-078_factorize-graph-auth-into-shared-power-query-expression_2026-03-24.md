# FIX-078 - Factorisation de l'auth Graph dans une expression Power Query partagee
**Date**: 2026-03-24

## Diagnostic
- Le bloc d'authentification Graph etait duplique dans trois extractions:
  - `T_Produits_Dim`
  - `T_Activite_M365`
  - `T_Utilisateurs_Dim`
- Cette duplication augmentait le cout de maintenance et le risque de divergence si l'URL, le scope ou le format du token devaient evoluer.
- Le probleme etait structurel. Les appels API cibles restaient differents, mais le mecanisme d'obtention du token etait identique.

## Fix applique
- Ajout d'une expression partagee `GetGraphAccessToken` dans `expressions.tmdl`.
- Suppression du bloc local `TenantId` / `ClientId` / `ClientSecret` / `GetAccessToken` dans les trois tables concernees.
- Rebranchement des trois requetes sur `AuthToken = GetGraphAccessToken`.

## Resultat attendu
- Une seule source de verite pour l'authentification Graph dans le modele.
- Les futures evolutions de l'auth seront faites une seule fois.
- Aucun changement fonctionnel attendu sur les datasets extraits si la requete partagee est resolue correctement par Power Query.

## Validation manuelle requise
- Rafraichir le modele dans Power BI Desktop.
- Verifier que `T_Produits_Dim`, `T_Activite_M365` et `T_Utilisateurs_Dim` se chargent sans erreur d'authentification.
- Controler qu'aucune regle de confidentialite Power Query ne bloque la reference a l'expression partagee.

## Point de vigilance
- `expressions.tmdl` contient encore des secrets reels dans l'etat local du depot. Aucun commit ne doit etre fait avant remise en placeholders.
