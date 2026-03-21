# FIX-018 — Detail Utilisateur header + spacing + filtre désactivés
**Date**: 2026-03-21

## A — Filtre Comptes désactivés avec licence
- Investigation:
  `LicencesComptesBloques` filtre déjà `AccountEnabled = FALSE()`
  mais le bookmark utilisait `Statut AD = Désactivé` + `StatutLicence = ON`
- Fix appliqué:
  remplacement du filtre bookmark dérivé `Statut AD`
  par le booléen direct `AccountEnabled = false`
- Alignement modèle:
  `StatutLicence` est recalculé avec `DISTINCTCOUNT(T_Affectations_Fact[AffectationID])`
  pour rester cohérent avec `[LicencesAffectees] > 0`

## B — Header Detail Utilisateur
| Élément | Avant | Après |
|---------|-------|-------|
| dt_title_001 | w=1504 | w=1116 |
| ux_refresh_banner_dt | x=1510 | x=1420 |
| ux_reset_filters_dt | x=1718 | x=1718 |

## C — Espacement harmonisé
| Zone | y avant | y après |
|------|---------|---------|
| Row 2 | 192 | 192 |
| Row 3 | 272 | 272 |
| Disclaimer | 352 | 360 |
| Table | 368 | 384 |
