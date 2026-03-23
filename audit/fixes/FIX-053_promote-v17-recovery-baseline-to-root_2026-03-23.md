# FIX-053 - Promote V17 recovery baseline to root project
**Date**: 2026-03-23

## Context
- `RECOVERY_UI_SAFE_V17` was manually validated in Power BI Desktop as the first fully interactive recovery baseline.
- The root project `M365_UI` was still the intended main entry point for day-to-day work.
- A structural compare showed the root `M365_UI.Report` and `M365_UI.SemanticModel` payload already matched `RECOVERY_UI_SAFE_V17`.

## Diagnostic
- The remaining root-only differences were local `.pbi` artifacts:
  - `M365_UI.Report/.pbi/localSettings.json`
  - `M365_UI.SemanticModel/.pbi/cache.abf`
  - `M365_UI.SemanticModel/.pbi/localSettings.json`
  - `M365_UI.SemanticModel/.pbi/editorSettings.json`
- `RECOVERY_UI_SAFE_V17` does not contain these `.pbi` artifacts and opens correctly.
- `M365_UI.pbip` was also normalized with `enableAutoRecovery=false`, consistent with the working recovery line.

## Fix Applied
- Created a local safeguard snapshot in `ROOT_PREPROMOTION_2026-03-23/` containing:
  - `M365_UI.pbip`
  - `M365_UI.Report`
  - `M365_UI.SemanticModel`
- Moved the root `.pbi` folders out of `M365_UI.Report` and `M365_UI.SemanticModel` into that backup area.
- Kept the semantic model/report payload intact because it already matched `RECOVERY_UI_SAFE_V17`.

## Expected Result
- Opening root `M365_UI.pbip` now uses the same report/model source payload as the validated `RECOVERY_UI_SAFE_V17` baseline.
- The root project no longer carries local `.pbi` session artifacts that were absent from the working recovery snapshot.
- The pre-promotion root state remains preserved locally for rollback if needed.
