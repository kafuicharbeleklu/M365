# FIX-004 — Bornage des patterns TypeCompte à risque
**Date**: 2026-03-20
**Référence audit**: DQ-001 / Section A et D
**Fichiers modifiés**: T_Utilisateurs_Dim.tmdl

## Problème corrigé
5 règles CONTAINSSTRING non bornées pouvaient classifier des humains
comme Technique (test, admin, service, formation, visit).

## Règles avant / après

| Pattern | Avant | Après |
|---------|-------|-------|
| `test` | `CONTAINSSTRING(Nom, "test"), "Technique",` | `(Nom = "test" \|\| LEFT(Nom, 5) = "test " \|\| RIGHT(Nom, 5) = " test"), "Technique",` |
| `admin` | `CONTAINSSTRING(Nom, "admin"), "Technique",` | `(Nom = "admin" \|\| LEFT(Nom, 6) = "admin " \|\| CONTAINSSTRING(Email, "admin@") \|\| CONTAINSSTRING(Email, ".admin@")), "Technique",` |
| `service` | `CONTAINSSTRING(Nom, "service"), "Technique",` | `(LEFT(Nom, 8) = "service " \|\| Nom = "service" \|\| CONTAINSSTRING(Email, "service@") \|\| CONTAINSSTRING(Email, ".service@")), "Technique",` |
| `formation` | `CONTAINSSTRING(Nom, "formation"), "Technique",` | `(Nom = "formation" \|\| LEFT(Nom, 10) = "formation " \|\| CONTAINSSTRING(Email, "formation@")), "Technique",` |
| `visit` | `CONTAINSSTRING(Nom, "visit"), "Technique",` | `(Nom = "visit" \|\| LEFT(Nom, 6) = "visit " \|\| Nom = "visitor" \|\| Nom = "visiteur"), "Technique",` |

## Risque résiduel
- Les règles bornées peuvent encore manquer certains vrais comptes
  techniques avec des noms non standards.
- Validation sur données réelles requise après prochain refresh.
- Exchange Online (Lundi) permettra une classification fiable
  des SharedMailbox indépendamment du DisplayName.
