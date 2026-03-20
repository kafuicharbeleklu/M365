# FIX-002 — Tooltips explicatifs Fantômes vs Jamais Connectés
**Date**: 2026-03-20
**Référence audit**: BL-001 / IC-002
**Fichiers modifiés**: _Mesures.tmdl

## Décision équipe
Les deux mesures coexistent. Des tooltips explicatifs différencient
clairement les deux populations pour éviter toute confusion.

## Définitions officielles
| KPI | Définition |
|-----|-----------|
| Utilisateurs Fantômes | Actifs AD, absents de T_Activite_M365 (180j) |
| Jamais Connectés | LastSignIn vide — jamais authentifiés sur Azure AD |

## DAX avant / après (4 mesures)

### TT_p3_fantomes_ctx
```dax
-- Avant
measure TT_p3_fantomes_ctx = "AD actif mais zero activite M365 depuis 180 jours"

-- Après
measure TT_p3_fantomes_ctx = "Actifs AD sans activité M365"
```

### TT_p3_fantomes_lect
```dax
-- Avant
measure TT_p3_fantomes_lect = "Action : contacter l'utilisateur ou desactiver le compte"

-- Après
measure TT_p3_fantomes_lect = "Utilisateurs dont le compte Azure AD est actif mais qui n'apparaissent dans aucune donnée d'activité Microsoft 365 sur les 180 derniers jours. Distinct des utilisateurs jamais connectés à AD."
```

### TT_p3_inactifs_ctx
```dax
-- Avant
measure TT_p3_inactifs_ctx = "Aucune activite M365 depuis plus de 90 jours"

-- Après
measure TT_p3_inactifs_ctx = "Jamais connectés à Azure AD"
```

### TT_p3_inactifs_lect
```dax
-- Avant
measure TT_p3_inactifs_lect = "Candidats a la desactivation ou revue manageur"

-- Après
measure TT_p3_inactifs_lect = "Utilisateurs dont le champ LastSignIn est vide : ils ne se sont jamais authentifiés sur Azure AD. Un utilisateur fantôme peut s'être connecté à AD sans jamais utiliser une application M365."
```

## Nouveaux gaps identifiés — à traiter dans DQ-001
- Utilisateur non mappé dans T_Affectations_Fact
- TypeCompte potentiellement trop agressif (1383 Technique / ~4000)
- Sous-catégorisation de la population Exclu
