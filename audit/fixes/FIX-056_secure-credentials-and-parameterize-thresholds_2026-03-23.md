# FIX-056 - Redaction des credentials Git et parametrage des seuils metier
**Date**: 2026-03-23

## Diagnostic
- `M365_UI.SemanticModel/definition/expressions.tmdl` contenait encore des valeurs reelles pour `Param_TenantId`, `Param_ClientId` et `Param_Secret`.
- Les seuils d'inactivite, de criticite stock et les bandes de score etaient hardcodes dans Power Query et dans DAX.
- Les artefacts report actuels filtrent encore sur les libelles historiques `Inactif (>90j)` et `Stock critique <=10%`.

## Fix applique
- Remplacement des trois credentials par des placeholders explicites dans `expressions.tmdl`.
- Ajout des parametres versionnes:
  - `Param_SeuilInactiviteJours`
  - `Param_SeuilStockCritiquePct`
  - `Param_SeuilStockAlertePct`
  - `Param_SeuilStockSurveillancePct`
  - `Param_ScoreBandPowerUser`
  - `Param_ScoreBandStandard`
  - `Param_ScoreBandMinimal`
  - `Param_PeriodeActivite`
- Ajout de la table masquee `T_Parametres_Dim` pour exposer ces valeurs a DAX sans duplication de constantes.
- Remplacement des seuils hardcodes dans:
  - `T_Utilisateurs_Dim[EtatActivite]`
  - `T_Activite_M365` (M)
  - `T_Produits_Dim` (M)
  - `_Mesures` (`NiveauAlerteDisponibilite`, `UX_ProduitsStockCritique`, `DT_NiveauUtilisation`)

## Compatibilite volontaire
- Les libelles report sensibles restent inchanges:
  - `Inactif (>90j)`
  - `Stock critique <=10%`
- Cette decision evite de casser les bookmarks et filtres visuels deja relies a ces chaines.
- Si les parametres sont modifies hors des valeurs par defaut, une passe report/bookmarks sera necessaire pour aligner les libelles affiches.

## Actions requises
- Rotation immediate du secret Entra/Azure expose precedemment dans Git et dans l'historique local.
- Re-renseigner localement `Param_TenantId`, `Param_ClientId` et `Param_Secret` avant tout refresh Desktop.
