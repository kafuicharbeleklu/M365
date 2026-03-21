# FIX-014 — Correction schéma bookmark Nav_UsersProduitsDepassement
**Date**: 2026-03-21
**Référence**: erreur d'ouverture PBIP post-FIX-013

## Problème
Le bookmark `a5f1d2c3b4e50617283c` ne respectait pas le schéma attendu.
La section contenait un filtre de page mais pas de propriété `visualContainers`.

## Correction appliquée
Ajout de `visualContainers: {}` dans
`Nav_UsersProduitsDepassement`.

## Impact
Le PBIP peut à nouveau être chargé par Power BI Desktop.
