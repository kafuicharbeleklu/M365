# FIX-086 - Refresh stale AGENTS bookmark and threshold notes from current source audit
**Date**: 2026-03-24

## Diagnostic
- `AGENTS.md` contenait encore des notes de travail devenues obsoletes apres les refactorings et realignements faits sur le projet.
- Deux familles d'information etaient stale :
  - le backlog de parametrisation de seuils, alors que les points principaux etaient deja relies a `Param_*`
  - les artefacts report connus sur les bookmarks, alors que l'audit statique courant ne retrouve plus ni visuel mort, ni mismatch sur les signets cites, ni `Signet 12`
- Ces notes obsoletes risquaient de faire repartir un agent futur sur de faux positifs.

## Fix applique
- Mise a jour de `AGENTS.md` pour faire passer la section seuils d'un backlog de parametrisation a un statut courant de parametrisation.
- Mise a jour de la section des artefacts report connus pour refleter l'etat reel observe dans les sources a la date du controle.
- Conservation du seul point encore ouvert dans cette section : les mesures tooltip `TT_p2_*` orphelines.

## Resultat attendu
- Les prochaines interventions partent d'un etat documentaire coherent avec le depot actuel.
- Les futurs agents ne perdront plus de temps a investiguer des anomalies de bookmarks deja levees.

## Validation manuelle requise
- Aucune validation Power BI Desktop requise pour cette passe documentaire.
- Si de nouveaux signets sont modifies plus tard, refaire un controle statique equivalent avant de reintroduire une note d'alerte dans `AGENTS.md`.
