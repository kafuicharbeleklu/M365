# FIX-005 — Bandeau MAJ étendu à toutes les pages
**Date**: 2026-03-20
**Référence audit**: UI-002
**Fichiers modifiés**: pages a4497031bb9f4bfb6556 et
  page_drillthrough_detail_user (nouveaux visuels)

## Problème corrigé
Le bandeau UX_DerniereMiseAJour n'était présent que sur
Analyse Licences et Analyse Utilisateur. Vue d'ensemble
et Detail Utilisateur n'avaient pas cette information.

## Visuels créés
| Page | Visual ID | Position |
|------|-----------|----------|
| Vue d'ensemble | ux_refresh_banner_p1 | (1610, 32, 290, 36) |
| Detail Utilisateur | ux_refresh_banner_dt | (1610, 32, 290, 36) |

## Statut UX_DerniereMiseAJour
Dynamique. La mesure retourne `MAX(T_Activite_M365[DateRapport])`
avec fallback sur `MAX(T_Utilisateurs_Dim[WhenCreated])`, puis
formate la valeur en `yyyy-MM-dd`. Ce n'est pas une date hardcodée.
