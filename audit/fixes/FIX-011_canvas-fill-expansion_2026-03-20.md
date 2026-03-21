# FIX-011 — Extension canvas : action cards + tableau
**Date**: 2026-03-20
**Référence**: FIX-010 followup
**Fichiers modifiés**: page 3c4cbe0b2835dc22b7e2

## Corrections appliquées
Action cards et tableau étendus jusqu'à y=892
pour remplir le canvas et éliminer l'espace blanc.

## Grille finale définitive
| Zone | x | y | width | height | Bottom |
|------|---|---|-------|--------|--------|
| KPI row | 300 | 92 | 1610 | 104 | 196 |
| Action card 1 | 300 | 212 | 300 | 216 | 428 |
| Action card 2 | 300 | 444 | 300 | 216 | 660 |
| Action card 3 | 300 | 676 | 300 | 216 | 892 |
| Tableau | 616 | 212 | 1294 | 680 | 892 |

## Labels KPI tronqués
- `d8558517a5af0608ba18`: `title.fontSize 13D -> 10D`, `labels.fontSize 24D -> 16D`
- `ce426e14c617550ccd13`: `title.fontSize 13D -> 10D`, `labels.fontSize 24D -> 16D`
- `40e7ac536e9864857177`: `title.fontSize 13D -> 10D`, `labels.fontSize 24D -> 16D`
