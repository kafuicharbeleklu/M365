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

## Threshold Parameterization Status
The main threshold families below are parameterized as of `2026-03-24`. When editing these flows, preserve the linkage to `Param_*` and do not reintroduce hardcoded fallbacks silently:

| Location | Status | Parameter source |
|----------|--------|------------------|
| `T_Utilisateurs_Dim[EtatActivite]` / `CodeEtatActivite` | Parameterized | `Param_SeuilInactiviteJours` |
| `DT_NiveauUtilisation` | Parameterized | `Param_SeuilInactiviteJours`, `Param_ScoreBand*` |
| `NiveauAlerteDisponibilite` | Parameterized | `Param_SeuilStockCritiquePct`, `Param_SeuilStockAlertePct`, `Param_SeuilStockSurveillancePct` |
| `UX_ProduitsStockCritique` | Parameterized | `Param_SeuilStockCritiquePct` |
| `getM365AppUserDetail` | Parameterized | `Param_PeriodeActivite` |

## Known Report Artifacts Needing Repair
Do not work around these silently; flag them in your response:

- No currently tracked report artifact remains open in source after the `2026-03-24` bookmark and tooltip audit.

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

---

## Codex / AI Agent Operating Constraints

This section is specifically for AI coding agents (Codex, Gemini, etc.) operating on this repository in a sandboxed environment.

### What you CAN do
- Read and edit all `.tmdl`, `.json`, and `.md` files.
- Create, modify, and delete DAX measures in `_Mesures.tmdl`.
- Add or edit Power Query (M) expressions in `expressions.tmdl`.
- Add, reorder, or modify report pages and visuals by editing their JSON definitions under `M365_UI.Report/definition/pages/`.
- Create and manage bookmark JSON files under `M365_UI.Report/definition/bookmarks/`.
- Create and update audit records under `audit/`.
- Run `git` commands and file-search tools (`rg`, `fd`, `grep`).

### What you CANNOT do
- Open Power BI Desktop or refresh the semantic model. All visual validation must be deferred to the human operator.
- Execute DAX queries or Power Query (M) code. You can only write and lint them statically.
- Test drillthrough, slicer interactions, or cross-filter behavior. Flag these for manual validation.
- Access external APIs (Microsoft Graph, Azure AD). Do not attempt HTTP calls.

### Operating principles
1. **Explore before editing.** Read the target file in full before proposing changes. For structural changes, list the directory tree first.
2. **One concern per commit.** Group related `.tmdl` and `.json` edits together, but do not mix unrelated changes.
3. **Flag, don't fix silently.** If you encounter a known issue from "Known Report Artifacts Needing Repair" or "Hardcoded Thresholds", report it and ask for confirmation.
4. **Respect serialization formats.** `.tmdl` files use tabs for indentation. JSON files use 2-space indentation. Never reformat an entire file.
5. **Audit trail is mandatory.** Every `.tmdl` or report JSON change must have a corresponding `FIX-*` record in `audit/fixes/`.

## File Inventory

### Semantic Model Tables (`M365_UI.SemanticModel/definition/tables/`)

| File | Purpose |
|------|---------|
| `_Mesures.tmdl` | All shared DAX measures (~45 KB). Primary editing target. |
| `T_Utilisateurs_Dim.tmdl` | User dimension: accounts, TypeCompte classification, EtatActivite. |
| `T_Produits_Dim.tmdl` | License product dimension: SKU, stock, thresholds. |
| `T_Activite_M365.tmdl` | M365 app usage activity (source: `getM365AppUserDetail`). |
| `T_Affectations_Fact.tmdl` | Current-state license assignments (no date column). |
| `T_Parametres_Dim.tmdl` | Dashboard parameters and configuration. |
| `DateTableTemplate_*.tmdl` | Auto-generated. **Do not edit.** |
| `LocalDateTable_*.tmdl` (×5) | Auto-generated. **Do not edit.** |

### Key Model Files

| File | Purpose |
|------|---------|
| `expressions.tmdl` | Power Query (M) data sources and parameters. **Contains secrets — never commit real values.** |
| `relationships.tmdl` | All model relationships. |
| `model.tmdl` | Model-level settings (culture, compatibility). |

### Report Pages (`M365_UI.Report/definition/pages/`)

| Folder | Type | Description |
|--------|------|-------------|
| `3c4cbe0b2835dc22b7e2` | Main page | Primary dashboard page (hash ID). |
| `54f9d470ac60b85b18da` | Main page | Secondary dashboard page (hash ID). |
| `a4497031bb9f4bfb6556` | Main page | Tertiary dashboard page (hash ID). |
| `page_drillthrough_detail_user` | Drillthrough | User 360° detail page. |
| `ttv_p1_*` (×8) | Tooltip | Page 1 tooltip overlays (actifs, comptes, desactives, inactifs, licences). |
| `ttv_p2_*` (×6) | Tooltip | Page 2 tooltip overlays (actives, affectees, dispo, inactives, produits, stock). |
| `ttv_p3_*` (×7) | Tooltip | Page 3 tooltip overlays (actifs, boites, cibles, desactives, fantomes, inactifs). |

### Other Key Paths

| Path | Purpose |
|------|---------|
| `M365_UI.Report/StaticResources/` | Theme JSON and image assets. |
| `M365_UI.Report/definition/bookmarks/` | Bookmark definitions (see "Known Report Artifacts Needing Repair"). |
| `audit/AUDIT_INDEX.md` | Master audit index. |
| `audit/fixes/` | FIX records for code changes. |
| `audit/business-logic/` | BL audit records. |
| `audit/data-quality/` | DQ audit records. |
| `audit/ui-layout/` | UI audit records. |
| `Lab/` | Experimental fork of the project. Not the active working copy. |

## Quick-Start Checklist (for AI Agents)

When starting a new task on this repo:

1. Read this `AGENTS.md` in full.
2. Identify which files are affected by the request.
3. Read each affected file before editing.
4. For DAX measure changes → edit `_Mesures.tmdl`.
5. For visual/page changes → edit JSON under `M365_UI.Report/definition/pages/<page_id>/`.
6. For data source changes → edit `expressions.tmdl` (never commit secrets).
7. Create a `FIX-*` audit record in `audit/fixes/` for every change.
8. Run `git diff -- M365_UI.SemanticModel/definition/expressions.tmdl` to verify no secrets leak.
9. Flag any items from "Known Report Artifacts Needing Repair" or "Hardcoded Thresholds" encountered during the task.
