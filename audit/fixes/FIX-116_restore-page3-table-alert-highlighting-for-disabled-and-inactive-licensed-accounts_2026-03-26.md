# FIX-116 - Restore page 3 table alert highlighting for disabled and inactive licensed accounts

## Summary
- Reintroduced visual highlighting on the page-3 consumed-license table after the switch to the drillthrough-based table visual.
- Reused `FlagLigneCompteDesactive` to highlight disabled accounts that still carry at least one license.
- Added `FlagLigneActiviteSousLicence` to distinguish licensed accounts that are still enabled but `INACTIF`, `INACTIF_M365`, or `JAMAIS_CONNECTE`.
- Applied conditional formatting on `DisplayName`, `Statut AD`, `EtatActivite`, and `LastSignIn`.

## Why
- The drillthrough-based table fixed the filtering issue, but the old visual cues for operational cleanup had been lost in the process.
- Page 3 is an action page, so accounts that are disabled with license should stand out immediately.
- A softer second-level cue is useful for licensed accounts that are inactive or never connected, without visually competing with the disabled-account priority.

## Scope
- `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`
- `M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/2110cfd8ad8ca81897f9/visual.json`

## Expected behavior
- Disabled accounts with license are highlighted in red on the user name and AD status cells.
- Licensed accounts that are inactive or never connected are highlighted with softer amber tones on activity-related cells.
- The table remains readable and still lists only real license assignments.

## Validation
- Static source validation completed:
  - `FlagLigneActiviteSousLicence` added in `_Mesures.tmdl`
  - page-3 table JSON parses correctly
  - conditional formatting targets `DisplayName`, `Statut AD`, `EtatActivite`, and `LastSignIn`
- Manual validation required in Power BI Desktop:
  - confirm disabled accounts with licenses appear in red
  - confirm inactive / never-connected licensed accounts appear in amber
  - confirm active licensed accounts keep the neutral styling
