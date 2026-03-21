# FIX-012 — Dimensionnement définitif Analyse Utilisateur
**Date**: 2026-03-20
**Référence**: FIX-011 followup — calcul rigoureux en une passe

## Principe appliqué
- Action cards : taille fixe convenable (120px) indépendante du tableau
- Tableau : occupe tout l'espace vertical disponible (y=212 à y=1064)
- Les deux zones ne sont plus liées dimensionnellement

## Grille définitive
| Zone | x | y | width | height | Bottom |
|------|---|---|-------|--------|--------|
| KPI row | 300 | 92 | 1610 | 104 | 196 |
| Action card 1 | 300 | 212 | 300 | 120 | 332 |
| Action card 2 | 300 | 348 | 300 | 120 | 468 |
| Action card 3 | 300 | 484 | 300 | 120 | 604 |
| Tableau | 616 | 212 | 1294 | 852 | 1064 |

## Labels KPI renommés
| Avant | Après |
|-------|-------|
| Comptes Tech. Totaux | Tech. Totaux |
| Comptes Tech. Actifs | Tech. Actifs |
| Comptes Tech. Inactifs | Tech. Inactifs |
| Utilisateurs Desactives | Désactivés |
| Utilisateurs Totaux | Total |

## Leçon appliquée
Les dimensions des action cards sont indépendantes
du tableau. Le tableau seul s'adapte à l'espace disponible.
