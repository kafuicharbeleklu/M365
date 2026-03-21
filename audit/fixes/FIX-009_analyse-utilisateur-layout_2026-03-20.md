# FIX-009 — Restructuration layout Analyse Utilisateur
**Date**: 2026-03-20
**Référence audit**: UI-003
**Fichiers modifiés**: page 3c4cbe0b2835dc22b7e2

## Décisions appliquées
- NbUtilisateursFantomes retiré de la rangée KPI (doublon action card)
- NbHumainsActifs réintégré dans la rangée KPI (slot 2)
- Slicers TypeCompte + Statut AD supprimés (bookmarks suffisent)
- Action cards reorganisées en colonne gauche verticale
- Tableau élargi à 1294px, démarrant à x=616

## Grille finale
| Zone | x | y | width | height |
|------|---|---|-------|--------|
| KPI row | 300 | 92 | 1610 | 104 |
| Action cards | 300 | 228 | 300 | 636 |
| Tableau | 616 | 212 | 1294 | 648 |

## Visuals supprimés
- 8030dbc87ab90506be3e
- 7855b7f60d52cd95b580
- b5e7555e9ed80b014183
- 47d6cec71d3710a42e63
- 13b24c306ab625400ecd
- cff18eebc6e8ac5a4392

## Visuals créés
- kpi_actifs_row_001
- kpi_actifs_btn_001
