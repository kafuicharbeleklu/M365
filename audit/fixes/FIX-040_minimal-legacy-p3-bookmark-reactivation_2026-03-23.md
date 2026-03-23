# FIX-040 - Minimal legacy P3 bookmark reactivation
**Date**: 2026-03-23

## Context
- `RECOVERY_UI_SAFE_V4` is the last confirmed stable recovery build.
- `RECOVERY_UI_SAFE_V5` reintroduced a broader bookmark layer and regressed to a blank report after refresh.
- The regression window is therefore the reactivated bookmark/action layer, not the rebuilt report shell.

## Decision
- Create `RECOVERY_UI_SAFE_V6` from `RECOVERY_UI_SAFE_V4`.
- Reactivate only a minimal P3 subset backed by legacy bookmark ids already present in the stable shell.
- Keep all newer `a5f1...` bookmarks excluded from this build.

## Reactivated Controls
- `ux_reset_filters_p3` -> `1661112e2198ecabde3e` (`Nav_Reset`)
- `7a8b216031e010e2d1b4` -> `fc8c08bf78c2215aa501` (`Nav_TousDesactives`)
- `bc689230263b260580e0` -> `66e80f63e44eee7812b9` (`Nav_HumainsInactifs`)
- `ux_action_disabled_btn_p3` -> `dacdeaf07eb2d1577049` (`Nav_HumainsDesactives`)

## Explicitly Left Disabled
- `kpi_actifs_btn_001` -> `Nav_HumainsActifs`
- `1a2f23d55a380141ed88` -> `Nav_TechniquesActives`
- `b407bc3fe477ae00b21e` -> `Nav_TechniquesInactives`
- `ux_action_ghost_btn_p3` -> `Nav_UtilisateursFantomes`
- `ux_action_overuse_btn_p3` -> `Nav_UsersProduitsDepassement`
- All P1, P2, and drillthrough reactivations from `V5`

## Expected Result
- `RECOVERY_UI_SAFE_V6` keeps the stable recovery shell from `V4`.
- Only the oldest P3 navigation/reset interactions are restored.
- If this version remains stable after refresh, the fault is narrowed to the broader bookmark set reintroduced in `V5`.
