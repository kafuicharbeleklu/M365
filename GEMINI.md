# Gemini Context: M365 Power BI Dashboard (PBIP)

This project is a Power BI Desktop project in **PBIP (Power BI Project)** format, used for monitoring Microsoft 365 users, licenses, and capacity risks. It uses **TMDL (Tabular Model Definition Language)** for the semantic model and **JSON** for report definitions.

## Project Overview
- **Main Entry Point**: `M365_UI.pbip`
- **Semantic Model**: Located in `M365_UI.SemanticModel/`. Definitions are in `.tmdl` files.
- **Report Definitions**: Located in `M365_UI.Report/`. Definitions are in `.json` files.
- **Audit System**: All changes must be documented in `audit/fixes/` and indexed in `audit/AUDIT_INDEX.md`.
- **Secondary Automation**: Python scripts in `Reporting/` generate Excel/PDF reports from CSV exports.

## Tech Stack
- **Business Intelligence**: Power BI (PBIP, TMDL, DAX, Power Query/M).
- **Automation**: Python (for side-reporting tasks).
- **Data Source**: Microsoft Graph API (configured in `expressions.tmdl`).

## Development Conventions

### 1. File Formatting
- **TMDL Files** (`.tmdl`): Use **Tabs** for indentation. Preserve existing serializer output.
- **JSON Files** (`.json`): Use **2-space indentation**.
- **Markdown Files** (`.md`): Standard GitHub-flavored Markdown.

### 2. DAX & Semantic Model
- **Centralized Logic**: All shared DAX measures MUST reside in `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`. Do not duplicate logic in visual-level measures.
- **Naming**: Follow existing patterns: `T_<Domain>_Dim`, `T_<Domain>_Fact`, and `ttv_*` for tooltip pages.
- **Generated Artifacts**: Never manually edit `LocalDateTable_*.tmdl` or `DateTableTemplate_*.tmdl`.

### 3. UI & Layout
- **Navigation Panel**: The left nav panel occupies `x=0` to `x=190`. Visuals MUST have `x >= 200` to avoid overlap.
- **Tooltips**: Tooltip pages are prefixed with `ttv_`.
- **Visual Validation**: AI agents cannot run Power BI Desktop. Any UI change MUST be flagged for manual validation by a human operator.

### 4. Security
- **Secrets**: NEVER commit real values for `Param_TenantId`, `Param_ClientId`, or `Param_Secret`.
- **Pre-commit Check**: Use the provided hook in `.githooks/pre-commit` to prevent secret leakage.
- **Verification**: Always run `git diff -- M365_UI.SemanticModel/definition/expressions.tmdl` before committing.

## Mandate: Audit Trail
Every modification to `.tmdl` or report `.json` files REQUIRES:
1.  A new `FIX-XXX_subject_YYYY-MM-DD.md` file in `audit/fixes/`.
2.  An entry in `audit/AUDIT_INDEX.md`.

## Key Commands
- **Open Project**: `start .\M365_UI.pbip` (Manual)
- **Review Changes**: `git diff -- M365_UI.SemanticModel M365_UI.Report`
- **Search Model**: `rg --files M365_UI.SemanticModel\definition`
- **Install Hooks**: `powershell -ExecutionPolicy Bypass -File scripts/install-git-hooks.ps1`

## Known Constraints
- **SKUFamily**: Does not exist; use `TypeLicence` + `CodeSKU` + `NomProduit`.
- **T_Affectations_Fact**: Current-state only (no historical dates).
- **TypeCompte Classification**: Follow rules defined in `AGENTS.md` (Guest/Member/Patterns).
- **Thresholds**: Most are parameterized via `Param_*` in `expressions.tmdl`. Do not hardcode values.
