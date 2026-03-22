# FIX-023b - BL-002 safe reapply
**Date**: 2026-03-21
**Reference**: BL-002

## Contexte
- Le commit `ea3bb8d` a ete revert car il introduisait une corruption semantique du report.
- Le risque principal venait de metadonnees ajoutees manuellement avec de nouveaux identifiants ou noms hors pattern Power BI attendu.
- Cette reapplique limitee reutilise uniquement des IDs bookmark hex 20 caracteres valides et n'ajoute aucun nouveau dossier visuel.

## Reapplique en securite
- `Nav_ProduitsDepassement` corrige:
  `TypeCompte='Technique'` remplace par `T_Produits_Dim[NiveauRisqueStock]='Depassement'`.
- `Nav_UtilisateursFantomes` corrige:
  `TypeCompte='Technique'` remplace par `TypeCompte='Utilisateur'` + `AccountEnabled=true`.
- `Nav_HumainsActifs`, `Nav_TechniquesActives`, `Nav_TechniquesInactives` nettoyes:
  suppression de `04a9392b160996ab9007` dans `targetVisualNames`.
- Nouveau bookmark `Nav_TousDesactives` ajoute avec ID hex valide:
  `a5f1d2c3b4e506172840`.
- Nouveau bookmark `Nav_CiblesNettoyage` ajoute avec ID hex valide:
  `a5f1d2c3b4e506172841`.
- Bouton overlay `7a8b216031e010e2d1b4` retargete vers `Nav_TousDesactives`.
- Bouton `ux_action_ghost_btn_p3` retargete vers `Nav_UtilisateursFantomes`.

## Deferred
- Aucun bouton overlay existant ne couvre actuellement la card `0781849f42b2a3099ac6` (`CiblesNettoyage`).
- Aucun nouveau dossier visuel n'a ete cree dans ce commit.
- Ajout de l'overlay `CiblesNettoyage` a faire manuellement dans Power BI Desktop si necessaire.

## Notes
- `page.json` de `3c4cbe0b2835dc22b7e2` ne contenait pas de valeurs de filtre serializees a supprimer au moment de la reapplique.
- `expressions.tmdl` n'est pas touche par ce fix.
