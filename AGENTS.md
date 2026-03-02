# Repository Guidelines

## Project Structure & Module Organization
`M365_UI.pbip` is the project entry point and links the report to the semantic model.

- `M365_UI.Report/definition/` contains report metadata (`pages/`, `bookmarks/`, `report.json`).
- `M365_UI.Report/StaticResources/` stores theme and image assets.
- `M365_UI.SemanticModel/definition/` contains TMDL model sources (`model.tmdl`, `relationships.tmdl`, `expressions.tmdl`, `tables/*.tmdl`).

Keep shared business measures in `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`. Continue table naming patterns already used in the model: `T_<Domain>_Dim` and `T_<Domain>_Fact`.

## Build, Test, and Development Commands
This repository has no compiled build pipeline; development is PBIP source editing.

- `start .\M365_UI.pbip` - Open the project in Power BI Desktop.
- `rg --files M365_UI.SemanticModel\definition` - List model source files quickly.
- `git diff -- M365_UI.SemanticModel M365_UI.Report` - Review serialized changes before commit.

## Coding Style & Naming Conventions
- Preserve serializer output formatting (tabs in `.tmdl`, 2-space indentation in JSON).
- Do not rename generated IDs (visual folders, page IDs, lineage tags) unless doing an intentional refactor.
- Keep business naming consistent with current model vocabulary (for example `NbHumainsActifs`, `LicencesAffectees`).
- Place reusable DAX measures in `_Mesures.tmdl` instead of duplicating logic across visuals.

## Testing Guidelines
No automated tests are currently defined. Validate changes manually in Power BI Desktop:

1. Refresh data and confirm model loads without errors.
2. Check affected pages, bookmarks, and drillthrough behavior (`page_drillthrough_detail_user`).
3. Verify measure outputs under expected slicer/filter combinations, especially `EtatActivite` logic.

## Commit & Pull Request Guidelines
Git history is not available in this workspace snapshot, so use Conventional Commit style:

- `feat(report): add inactivity trend visual`
- `fix(model): prevent slicer exclusion for disabled accounts`

For PRs, include a short scope summary, changed paths, screenshots for visual/layout changes, and notes about data/model impact.

## Security & Configuration Tips
- Never commit credentials or tenant secrets.
- Keep machine-specific files in ignored `.pbi` artifacts (`**/.pbi/localSettings.json`, `**/.pbi/cache.abf`).
- Treat parameter-like values (`Param_TenantId`, `Param_ClientId`, `Param_Secret`) as environment-specific and externalized.
