# FIX-010 — Alignement hauteur tableau et action cards
**Date**: 2026-03-20
**Référence**: FIX-009 followup
**Fichiers modifiés**: page 3c4cbe0b2835dc22b7e2

## Correction appliquée
Table height ajustée pour aligner son bord bas
avec le bord bas de la dernière action card (y=848).

## Avant / après
| Visual | Avant | Après |
|--------|-------|-------|
| 87d3521e0b96312bffb0 | (616, 212, 1294, 648) | (616, 212, 1294, 636) |

## Zone y=848–1080
- Aucun visuel de contenu principal ne démarre dans cette zone après correction.
- `321cf8d0d5d0be093468` `(0, 0, 280, 1080)` et `3a2e0f8584503a88dcbf` `(0, 0, 280, 1080)` la traversent, mais ce sont des artefacts structurels du panneau nav gauche.
- `ux_context_banner_p3` est hors de cette zone et déjà correctement positionné en header à `(760, 36, 640, 32)`.
