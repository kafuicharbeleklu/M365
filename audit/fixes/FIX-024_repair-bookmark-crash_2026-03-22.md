# FIX-024 - Repair bookmark crash after BL-002 safe reapply
**Date**: 2026-03-22

## Diagnostic
- Le report ne cassait pas sur du JSON invalide.
- Le crash apparaissait apres `a53c6e8` dans le moteur de document enrichi Power BI.
- Les seuls objets entierement nouveaux introduits par ce commit etaient les bookmarks `a5f1d2c3b4e506172840` et `a5f1d2c3b4e506172841`.
- Pour reduire le risque, la reparation retire tout nouveau bookmark ID ajoute manuellement.

## Reparation
- Suppression des nouveaux bookmarks `a5f1d2c3b4e506172840` et `a5f1d2c3b4e506172841`.
- Suppression de leurs entrees dans `bookmarks.json`.
- Reutilisation du bookmark orphelin existant `fc8c08bf78c2215aa501` comme `Nav_TousDesactives`.
- Retarget du bouton `7a8b216031e010e2d1b4` vers `fc8c08bf78c2215aa501`.

## Differe
- `Nav_CiblesNettoyage` reste differe tant qu'aucun overlay existant ne le consomme.
- Aucun nouveau dossier visuel ni nouveau bookmark ID n'est ajoute dans ce fix.
