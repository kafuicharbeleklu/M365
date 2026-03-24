# FIX-080 - Redaction des credentials Graph locaux avant commit
**Date**: 2026-03-24

## Diagnostic
- `expressions.tmdl` contenait encore des valeurs reelles pour `Param_TenantId`, `Param_ClientId` et `Param_Secret`.
- Cet etat etait incompatible avec un commit securise du projet.

## Fix applique
- Remplacement de `Param_TenantId` par `__SET_TENANT_ID_LOCALLY__`.
- Remplacement de `Param_ClientId` par `__SET_CLIENT_ID_LOCALLY__`.
- Remplacement de `Param_Secret` par `__SET_CLIENT_SECRET_LOCALLY__`.

## Resultat attendu
- Le fichier `expressions.tmdl` redevient commit-safe.
- La configuration locale devra etre remise manuellement avant un refresh local du modele.

## Validation manuelle requise
- Verifier le diff de `expressions.tmdl` avant commit.
- Reinjecter localement les vraies valeurs uniquement dans un contexte de test hors commit si un refresh Desktop est necessaire.
