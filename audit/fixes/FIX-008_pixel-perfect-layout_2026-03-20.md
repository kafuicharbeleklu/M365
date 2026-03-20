# FIX-008 — Corrections layout pixel-perfect
**Date**: 2026-03-20
**Référence audit**: UI-003
**Fichiers modifiés**: pages 3c4cbe0b2835dc22b7e2,
  page_drillthrough_detail_user

## Décision NbHumainsActifs
Conservé hors de la rangée principale à y=212 (position dédiée)
plutôt que supprimé ou compressé dans la rangée.

## Grille appliquée — Analyse Utilisateur
| Constante | Valeur |
|-----------|--------|
| CONTENT_START_X | 300 |
| CARD_WIDTH | 187 |
| GAP_H | 16 |
| KPI_ROW_Y | 92 |
| KPI_ROW_HEIGHT | 104 |

## Tableau des corrections
| Visual ID | Description | Avant | Après |
|-----------|-------------|-------|-------|
| 0781849f42b2a3099ac6 | CiblesNettoyage | (1721, 92, 189, 104) | (1721, 92, 187, 104) |
| 8030dbc87ab90506be3e | NbHumainsActifs | (97, 92, 187, 104) | (300, 212, 187, 104) |
| 7855b7f60d52cd95b580 | Overlay bouton NbHumainsActifs | (97, 92, 187, 104) | (300, 212, 187, 104) |
| ux_refresh_banner_dt | Bandeau MAJ détail utilisateur | (1610, 8, 290, 36) | (1510, 8, 290, 36) |
| dt_freshness_disclaimer_001 | Disclaimer fraîcheur | (1137, 444, 663, 16) | (1137, 452, 663, 16) |
| dt_table_licences | Table licences | (120, 460, 1680, 600) | (120, 476, 1680, 600) |

## Leçon documentée
Les visuels du panneau nav custom (x=0–280) ne doivent pas
être confondus avec des conflits x<200. Seuls les visuels
de contenu principal hors du panneau doivent respecter
CONTENT_START_X >= 300.
