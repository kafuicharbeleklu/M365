# FIX-057 - Alignement des libelles UI avec les seuils parametrables
**Date**: 2026-03-23

## Diagnostic
- Le modele utilisait deja des seuils parametrables pour l'inactivite et le stock critique.
- Plusieurs libelles visibles dans le report restaient figes sur `>90j`, `<=10%`, `<=25%` et `<=50%`.
- Les bookmarks existants filtrent encore sur les libelles techniques `Inactif (>90j)` et `Stock critique <=10%`.

## Fix applique
- Mise a jour des mesures de lecture pour afficher les seuils reels actifs:
  - `UX_BandeauRisqueLicences`
  - `DT_NiveauUtilisation`
  - `TT_p1_lic_dispo_lect`
  - `TT_p2_dispo_lect`
  - `TT_p3_actifs_ctx`
- Mise a jour des titres statiques les plus visibles du report:
  - carte P1 `Utilisateurs Inactifs`
  - carte P2 `Stock critique`
  - legende de disponibilite P2

## Compatibilite volontaire
- Les valeurs techniques suivantes ne changent pas:
  - `Inactif (>90j)`
  - `Stock critique <=10%`
- Elles restent necessaires pour la compatibilite des bookmarks et filtres existants.
- L'alignement porte donc sur l'affichage utilisateur, pas sur les libelles de categorisation internes.

## Resultat attendu
- L'UI n'affiche plus de seuils faux quand les parametres changent.
- Le comportement des bookmarks existants reste stable.
