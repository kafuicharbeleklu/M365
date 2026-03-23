# FIX-041 - Reactivate Nav_UsersProduitsDepassement only on recovery V7
**Date**: 2026-03-23

## Context
- `RECOVERY_UI_SAFE_V6` is stable after refresh.
- The next step is to continue reactivation one interaction at a time.
- `Nav_UsersProduitsDepassement` (`a5f1d2c3b4e50617283c`) is the corrected users-context bookmark, distinct from the known-suspect `Nav_ProduitsDepassement`.

## Decision
- Create `RECOVERY_UI_SAFE_V7` from `RECOVERY_UI_SAFE_V6`.
- Add only bookmark `a5f1d2c3b4e50617283c` to the recovery bookmark metadata.
- Reactivate only `ux_action_overuse_btn_p3`.

## Explicitly Not Changed
- `Nav_HumainsActifs`
- `Nav_TechniquesActives`
- `Nav_TechniquesInactives`
- `Nav_UtilisateursFantomes`
- All P1, P2, and drillthrough bookmark reactivations

## Expected Result
- P3 regains only the "produits en dépassement" user navigation.
- If `V7` stays stable, the issue is narrower than the full `a5f1...` family and likely tied to a smaller subset of reintroduced interactions.
