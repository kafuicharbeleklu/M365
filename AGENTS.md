# Repository Guidelines

## Project Structure & Module Organization
This repository is a Power BI PBIP project for Microsoft 365 user, license, and capacity-risk tracking.

- `M365_UI.pbip`: project entry point for Power BI Desktop.
- `M365_UI.SemanticModel/definition/`: semantic model source in TMDL, including `expressions.tmdl`, `relationships.tmdl`, and shared measures in `tables/_Mesures.tmdl`.
- `M365_UI.Report/definition/`: report metadata, pages, visuals, bookmarks, and drillthrough definitions.
- `M365_UI.Report/StaticResources/`: theme JSON and image assets.

Treat `LocalDateTable_*.tmdl` files as generated artifacts and avoid manual edits unless regeneration is intentional.

## Build, Test, and Development Commands
There is no compiled build pipeline; development is done by editing PBIP source and validating in Power BI Desktop.

- `start .\M365_UI.pbip`: open the project locally in Power BI Desktop.
- `rg --files M365_UI.SemanticModel\definition`: list semantic model files quickly.
- `git diff -- M365_UI.SemanticModel M365_UI.Report`: review serialized report/model changes before commit.
- `git status --short`: confirm only intended PBIP artifacts are staged.

## Coding Style & Naming Conventions
- Preserve serializer output exactly: tabs in `.tmdl`, 2-space indentation in JSON.
- Keep reusable DAX logic in `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`; do not duplicate logic across visuals.
- Follow existing naming patterns: `T_<Domain>_Dim`, `T_<Domain>_Fact`, and `ttv_*` for tooltip pages.
- Reuse the current French business vocabulary, for example `NbHumainsActifs`, `LicencesAffectees`, and `EtatActivite`.
- Do not rename page IDs, visual folder IDs, bookmark IDs, or lineage tags unless performing an intentional refactor.

## Testing Guidelines
No automated test suite is defined. Validate changes manually in Power BI Desktop:

1. Refresh the model and confirm data loads without errors.
2. Verify affected pages, bookmarks, slicers, and drillthrough behavior.
3. Check tooltip pages (`ttv_*`) and shared measures under expected filter combinations.

## Commit & Pull Request Guidelines
Recent history follows Conventional Commits, typically scoped by area, for example `feat(report): ...`, `feat(ui): ...`, and `chore(report): ...`.

- Keep commit messages in `type(scope): summary` format.
- In pull requests, include a short scope summary, changed paths, model/report impact, and screenshots for layout or visual changes.

## Security & Configuration
Never commit real values for `Param_TenantId`, `Param_ClientId`, or `Param_Secret`. Keep credentials local and review `expressions.tmdl` before every commit.

## Known Model Constraints
- `SKUFamily` does not exist as a column. Use `TypeLicence` + `CodeSKU` + `NomProduit` as substitutes when building E1/E3 over-provisioning logic.
- `T_Affectations_Fact` has no assignment date: the table is current-state only. Do not build historical license trend visuals from this table without first adding a `DateAffectation` column.
- `T_Activite_M365` is sourced from `getM365AppUserDetail(period='D180')`. The period is hardcoded in Power Query; do not change it without explicit instruction.
- `DateTableTemplate_*` and `LocalDateTable_*` are generated artifacts. Never edit them manually and never create relationships to them directly.

## Hardcoded Thresholds - Parameterization Backlog
The following thresholds are currently hardcoded in DAX and Power Query. When editing measures that contain these values, do not silently change them. Flag them as candidates for `Param_*` parameterization:

| Location | Hardcoded value | Intended param name |
|----------|-----------------|---------------------|
| `T_Utilisateurs_Dim[EtatActivite]` | `TODAY() - 90` | `Param_SeuilInactiviteJours` |
| `DT_NiveauUtilisation` | `> 90j`, score bands `7/4/1` | `Param_SeuilInactiviteJours`, `Param_ScoreBands` |
| `NiveauAlerteDisponibilite` | `0.10`, `0.25`, `0.50` | `Param_SeuilAlerteStock` |
| `UX_ProduitsStockCritique` | `<= 0.10` | `Param_SeuilAlerteStock` |
| `getM365AppUserDetail` | `period='D180'` | `Param_PeriodeActivite` |

## Known Report Artifacts Needing Repair
Do not work around these silently; flag them in your response:

- Broken bookmarks: `Nav_HumainsActifs`, `Nav_TechniquesActives`, `Nav_TechniquesInactives` reference visual id `04a9392b160996ab9007` which no longer exists. Do not re-target without explicit instruction.
- Bookmark filter mismatch: `Nav_ProduitsDepassement` and `Nav_UtilisateursFantomes` serialize `TypeCompte=Technique` instead of their intended filter. Do not silently fix; report the discrepancy.
- `Signet 12`: unnamed bookmark with `TypeCompte=Technique`; orphan, purpose unknown. Do not delete without confirmation.
- Orphaned tooltip measures: `TT_p2_critique_*`, `TT_p2_epuise_*`, `TT_p2_depassement_*`, `TT_p2_risque_*` exist in `_Mesures.tmdl` but have no corresponding `ttv_*` tooltip page. Treat as dead code until tooltip pages are created.

## Security - Mandatory Pre-Commit Check
Before every commit, run:

`git diff -- M365_UI.SemanticModel/definition/expressions.tmdl`

Verify `Param_Secret` contains only a placeholder such as `"__REDACTED__"`, never a real secret. The CI gate does not exist yet, so this remains a manual step.

## Classification TypeCompte — Rules and Constraints
- Primary signals (top of chain, reliable):
  `[UserType] = "Guest"` -> `Technique`
  `CONTAINSSTRING([UserPrincipalName], "#EXT#")` -> `Technique`
- Secondary signals (Exchange - pending, requires `Mail.ReadBasic.All`):
  `RecipientTypeDetails = SharedMailbox` -> `Technique` (not yet implemented)
- Fallback rules (`CONTAINSSTRING` on `DisplayName`):
  `132` rules total. The 5 highest false-positive risk patterns have been bounded as of `2026-03-20` (see `DQ-001`, `FIX-004`).
  Never add new unbounded `CONTAINSSTRING(Nom, x)` rules.
  Always prefer: exact match, `LEFT`/`RIGHT` boundary, or `Email` check.
- `UserType` column: added `2026-03-20`, source = Graph `/beta/users` `$select`.
  Values: `"Guest"` | `"Member"` | `null` (probable shared mailbox)

## Audit System
- All audits tracked in `audit/AUDIT_INDEX.md`
- Types: `BL` | `UI` | `DQ` | `FIX`
- Never modify `.tmdl` or report files without creating a `FIX` record
- Run `/explore` before any structural change to verify current state

## UI Layout Constraints
- Power BI left navigation panel occupies approximately `x=0` to `x=190`. Never place visuals with `x < 200` on pages that use the nav panel.
- Page header zone height varies per page. Always inspect `dt_title_001` or equivalent before placing banners on drillthrough pages.
- Source-level coordinate audits cannot detect overlap with native Power BI UI chrome such as the nav panel or toolbar. Visual validation in Power BI Desktop is mandatory after any position change.
