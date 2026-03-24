# FIX-087 - Remove orphaned TT_p2 tooltip measures and close report artifact note
**Date**: 2026-03-24

## Diagnostic
- Les mesures `TT_p2_critique_*`, `TT_p2_epuise_*`, `TT_p2_depassement_*` et `TT_p2_risque_*` existaient encore dans `_Mesures.tmdl`.
- Le report ne contient pourtant que les pages tooltip P2 suivantes : `ttv_p2_stock`, `ttv_p2_affectees`, `ttv_p2_dispo`, `ttv_p2_inactives`, `ttv_p2_produits`, `ttv_p2_actives`.
- Aucune reference a ces mesures orphelines n'a ete trouvee dans le report, les bookmarks, ni les autres fichiers sources du depot.

## Fix applique
- Suppression des huit mesures tooltip P2 orphelines de `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`.
- Mise a jour de `AGENTS.md` pour fermer cette alerte documentaire devenue sans objet.

## Resultat attendu
- Le modele ne conserve plus de dead code tooltip P2 sans page correspondante.
- La documentation operative du depot ne signale plus un artefact deja purge.

## Validation manuelle requise
- Ouvrir le projet dans Power BI Desktop.
- Verifier que le modele se charge sans erreur.
- Verifier que les tooltips P2 existants (`stock`, `affectees`, `dispo`, `inactives`, `produits`, `actives`) restent fonctionnels.
