# FIX-073 - Realignement des bookmarks humains Actifs/Inactifs avec le filtre visible EtatActivite
**Date**: 2026-03-24

## Diagnostic
- Les captures utilisateur montraient que `Nav_HumainsActifs` et `Nav_HumainsInactifs` n'etaient pas coherents dans le panneau `Filters on this page`.
- Les deux bookmarks reutilisaient bien l'identifiant du filtre de page `331a55ef4d0300c67d45`, mais en le reliant a `T_Utilisateurs_Dim[CodeEtatActivite]` au lieu du champ visible `T_Utilisateurs_Dim[EtatActivite]`.
- Cette etat hybride venait du refactor `FIX-058`: logique stable cote code, mais filtre de page visible reste branche sur `EtatActivite`.
- En pratique, le filtrage manuel via `EtatActivite` fonctionne, alors que la restauration via bookmark n'est plus fiable pour ces deux cas.

## Fix applique
- `Nav_HumainsActifs` aligne maintenant le filtre `331a55ef4d0300c67d45` sur `T_Utilisateurs_Dim[EtatActivite] = 'Actif'`.
- `Nav_HumainsInactifs` aligne maintenant le meme filtre sur `T_Utilisateurs_Dim[EtatActivite] = 'Inactif >90j'`.
- Les autres filtres de ces deux bookmarks restent inchanges:
  - `TypeCompte = Utilisateur`
  - `Statut AD = Active (valeur AD active cote UI)`

## Resultat attendu
- Le clic sur `Utilisateurs Actifs` doit maintenant restaurer un etat visible coherent dans le panneau de filtres.
- Le clic sur `Utilisateurs Inactifs` doit maintenant restaurer `EtatActivite = Inactif >90j` de la meme maniere qu'un reglage manuel du filtre.

## Risque connu
- Ce correctif reintroduit une dependance au libelle visible `Inactif >90j`.
- Si le seuil dynamique d'inactivite change et modifie ce libelle, ce bookmark devra etre reserialize ou bascule vers une autre strategie de navigation.
