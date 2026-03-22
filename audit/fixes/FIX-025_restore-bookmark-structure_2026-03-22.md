# FIX-025 - Restore bookmark structure for autosave stability
**Date**: 2026-03-22

## Diagnostic
- The Power BI Desktop crash persisted after removing manually added bookmark IDs.
- The reused bookmark `fc8c08bf78c2215aa501` had lost multiple `visualContainers` entries compared with the last known working state `12de480`.
- That change was semantic metadata corruption, not invalid JSON syntax.

## Repair
- Restored the full original Power BI-generated bookmark structure for `fc8c08bf78c2215aa501`.
- Reapplied only the intended business logic changes on that existing bookmark:
  - `displayName` -> `Nav_TousDesactives`
  - `TypeCompte = "Utilisateur"`
  - `Statut AD = "Désactivé"`
- Left the schema version and all original `visualContainers` intact.

## Validation
- JSON parse check passed.
- `visualContainers` count now matches `12de480` exactly.
- No new bookmark IDs or visual IDs were introduced in this fix.

## Deferred
- `audit/AUDIT_INDEX.md` was not updated because the file is not valid UTF-8 in the current worktree.
