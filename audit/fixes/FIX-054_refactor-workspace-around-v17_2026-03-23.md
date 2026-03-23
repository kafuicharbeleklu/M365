# FIX-054 - Refactor workspace around V17 active project
**Date**: 2026-03-23

## Context
- `RECOVERY_UI_SAFE_V17` is the only PBIP path that opens correctly in Power BI Desktop.
- The root `M365_UI` copy remained unusable despite matching payload files and after a full Power BI Desktop profile reset.
- The repository still contained multiple duplicated PBIP trees from the recovery process.

## Fix Applied
- Kept `RECOVERY_UI_SAFE_V17` as the single active PBIP tree.
- Removed obsolete duplicated PBIP trees:
  - root `M365_UI.pbip`
  - root `M365_UI.Report/`
  - root `M365_UI.SemanticModel/`
  - `RECOVERY_UI_SAFE_V13/`
- Kept documentation and audit history.
- Updated top-level documentation to point explicitly to `RECOVERY_UI_SAFE_V17/M365_UI.pbip`.

## Expected Result
- The workspace has a single clear PBIP base to maintain.
- Old mirrored PBIP trees no longer create ambiguity during edits or tests.
- Future report/model changes should target `RECOVERY_UI_SAFE_V17` only.
