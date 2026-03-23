# FIX-055 - Export de V17 vers le root et nettoyage
**Date**: 2026-03-23

## Contexte
- `RECOVERY_UI_SAFE_V17` etait la seule base PBIP validee et ouvrable.
- Le workspace avait ete refactorise autour de ce dossier recovery.
- Besoin utilisateur : remettre directement cette baseline au root du depot.

## Fix applique
- Deplacement Git de `RECOVERY_UI_SAFE_V17/M365_UI.pbip` vers `M365_UI.pbip`.
- Deplacement Git de `RECOVERY_UI_SAFE_V17/M365_UI.Report/` vers `M365_UI.Report/`.
- Deplacement Git de `RECOVERY_UI_SAFE_V17/M365_UI.SemanticModel/` vers `M365_UI.SemanticModel/`.
- Suppression du conteneur recovery residuel `RECOVERY_UI_SAFE_V17/`.
- Mise a jour de la documentation pour pointer de nouveau vers le root.

## Resultat attendu
- Le projet actif est de nouveau le root du depot.
- Le workspace ne contient plus de doublon PBIP recovery.
- Aucun contenu fonctionnel du modele ou du report n'est modifie par cette promotion.
