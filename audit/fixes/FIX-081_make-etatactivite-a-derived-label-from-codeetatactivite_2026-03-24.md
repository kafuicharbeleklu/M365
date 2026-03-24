# FIX-081 - Faire de EtatActivite un libelle derive de CodeEtatActivite
**Date**: 2026-03-24

## Diagnostic
- `T_Utilisateurs_Dim[EtatActivite]` et `T_Utilisateurs_Dim[CodeEtatActivite]` recalculaient la meme logique metier avec deux sorties differentes.
- Cette duplication augmentait le risque d'ecart entre filtres visibles, KPI, bookmarks et logique technique.
- Les mesures s'appuient deja majoritairement sur `CodeEtatActivite`, tandis que l'UI utilise `EtatActivite`.

## Fix applique
- Conservation de `CodeEtatActivite` comme source canonique de la classification d'activite.
- Simplification de `EtatActivite` pour qu'il derive uniquement de `CodeEtatActivite`.
- Conservation du libelle dynamique `Inactif >Nj` via `Param_SeuilInactiviteJours`.
- Aucun bookmark ni aucune mesure n'ont ete modifies dans cette passe.

## Resultat attendu
- Une seule logique metier d'activite au niveau du modele.
- Les evolutions futures se feront dans `CodeEtatActivite`, pas dans deux colonnes paralleles.
- L'UI continue d'afficher les libelles metier attendus sans changer les filtres visibles existants.

## Validation manuelle requise
- Rafraichir le modele dans Power BI Desktop.
- Verifier que les segments et filtres sur `EtatActivite` continuent d'afficher `Actif`, `Inactif >90j`, `Jamais Connecte`, `Inactif M365` et `Exclu`.
- Verifier que les KPI utilisateurs et bookmarks P3 restent coherents avec ces libelles visibles.
