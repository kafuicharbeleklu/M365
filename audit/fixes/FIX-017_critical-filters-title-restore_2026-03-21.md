# FIX-017 — Filtres persistants, titres restaurés, Detail fixes
**Date**: 2026-03-21

## A — Filtres persistants supprimés
- Page Analyse Utilisateur : slicer `78c3a585a38d21cb56a8` (`NomProduit = Office 365 E3`) nettoyé
- Page Analyse Utilisateur : filtres page `TypeCompte = Utilisateur` et `Statut AD = Désactivé` retirés du `page.json`
- Page Detail Utilisateur : filtre drillthrough persisté `UserPrincipalName = charbel.eklu@neemba.com` retiré du `page.json`

## B — Bookmark Nav_HumainsDesactives corrigé
- Avant : `TypeCompte = Utilisateur` + `Statut AD = Désactivé`
- Après : ajout de `StatutLicence = ON`
- DAX `FlagLigneCompteDesactive` vérifié : highlight uniquement si `AccountEnabled = FALSE()` et `[LicencesAffectees] > 0`

## C — Largeurs titres restaurées
- Vue d'ensemble : `57cd12a3c5c073767919` restauré à `x=296`, `w=1608`
- Analyse Licences : `4e1a01705b45b2070499` restauré à `x=296`, `w=1608`
- Analyse Utilisateur : `855861f892a1da7eccbf` restauré à `x=356`, `w=1548`

## D — Header éléments repositionnés
- Les bannières `Filtres`, `MAJ`, `Reset` restent sur la ligne `y=22`
- Les positions FIX-016 sont conservées car le texte utile des titres reste visuellement avant `x=772`

## E — Detail Utilisateur
- Espacement header → KPI : première rangée déplacée à `y=96`
- Bouton reset ajouté : `ux_reset_filters_dt`
- Disclaimer élargi : `x=120`, `y=352`, `w=1780`, `h=16`

## F — Tooltip audit
- Toutes les pages `ttv_*` sont actuellement en `312x220`
- Largeur acceptable, hauteur `220 > 200` : revue manuelle Power BI Desktop requise avant redimensionnement
