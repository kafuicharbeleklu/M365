# UI-001 — Chevauchements et alignements visuels
**Date**: 2026-03-20
**Statut**: ✅ Résolu
**Périmètre**: Pages Vue d'ensemble (a4497031bb9f4bfb6556)
              et Analyse Utilisateur (3c4cbe0b2835dc22b7e2)

## Résultats de l'audit bounding-box

### Vue d'ensemble — aucun chevauchement détecté
Le source PBIP sérialise 8 cartes sur cette page. Aucune zone ne se chevauche.

| Visual ID | Type | x | y | width | height |
|-----------|------|---|---|-------|--------|
| `e01617238ac009dd6693` | `card` | 300 | 92 | 186 | 120 |
| `32f0782d609024c5ddeb` | `card` | 502 | 92 | 186 | 120 |
| `5a57e51bd95d62c2f1c8` | `card` | 704 | 92 | 186 | 120 |
| `ebe08689cd1cb3339e74` | `card` | 906 | 92 | 186 | 120 |
| `ed4f3b6ef5234a8c7a7e` | `card` | 1108 | 92 | 186 | 120 |
| `dfb6bb22621287a516f5` | `card` | 1310 | 92 | 186 | 120 |
| `d3b401179a9644ebfef4` | `card` | 1512 | 92 | 186 | 120 |
| `97ff1f41db18c4fc211a` | `card` | 1714 | 92 | 186 | 120 |

### Analyse Utilisateur — désalignement pixel détecté
- Visual `8030dbc87ab90506be3e` (`NbHumainsActifs`) : coordonnées fractionnaires `x=93.9367` `y=109.33` — corrigé vers `x=94` `y=92`

## Correction appliquée
- Fichier modifié : `visual.json` de `8030dbc87ab90506be3e`
- Coordonnées avant / après

| Champ | Avant | Après |
|-------|-------|-------|
| `x` | `93.9367128266182` | `94` |
| `y` | `109.33617394573594` | `92` |
| `width` | `186.33347954132464` | `186` |
| `height` | `103.17638949808885` | `104` |
