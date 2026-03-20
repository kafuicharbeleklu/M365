# FIX-007 — Corrections layout : nav panel overlap + header banner
**Date**: 2026-03-20
**Détecté par**: Validation visuelle (non détectable par audit source)
**Fichiers modifiés**: pages 3c4cbe0b2835dc22b7e2 et
  page_drillthrough_detail_user

## Leçon apprise
Les audits source-level ne peuvent pas détecter les overlaps avec le chrome natif Power BI (panneau de navigation ~190px). La validation visuelle dans Power BI Desktop est obligatoire après tout changement de position.

## A — NbHumainsActifs déplacé hors zone nav
Avant : `8030dbc87ab90506be3e` `(94, 92, 186, 104)` et `7855b7f60d52cd95b580` `(94, 92, 186, 104)`

Après : `8030dbc87ab90506be3e` `(97, 92, 187, 104)` et `7855b7f60d52cd95b580` `(97, 92, 187, 104)`

Motif : la rangée KPI suit un pas constant de `203px` (`300, 503, 706, 909, ...`) avec largeur `187px`, ce qui révèle un slot manquant à `x=97` avant `NbHumainsTotal`.

## B — Bandeau MAJ repositionné dans zone titre
Avant : `ux_refresh_banner_dt` `(1610, 32, 290, 36)`

Après : `ux_refresh_banner_dt` `(1610, 8, 290, 36)`

Motif : le bandeau reste ancré à droite (`1920 - 290 - 20`) mais s'aligne désormais sur le `y` du header de `dt_title_001` (`296, 8, 1504, 72`) au lieu d'être trop bas dans la zone titre.
