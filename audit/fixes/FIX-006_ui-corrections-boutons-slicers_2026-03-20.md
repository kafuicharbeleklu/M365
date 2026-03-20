# FIX-006 — Corrections UI : boutons, mismatches, disclaimer, slicers
**Date**: 2026-03-20
**Référence audit**: UI-002
**Fichiers modifiés**: page 3c4cbe0b2835dc22b7e2,
  page_drillthrough_detail_user

## A — Boutons réalignés sur NbHumainsActifs
- `7855b7f60d52cd95b580` (`Nav_HumainsActifs`) réaligné sur la carte `8030dbc87ab90506be3e` : `(303.37, 212.51, 186.33, 103.18)` → `(94, 92, 186, 104)`.
- `7b1496a23db63d581614` et `0a49bad639711380db9c` vérifiés puis laissés en place : ce sont des boutons de navigation visibles du rail gauche, pas des hotspots KPI transparents.

## B — Nav_HumainsActifs re-ancré ou supprimé
- `7855b7f60d52cd95b580` conservé et re-ancré sur `NbHumainsActifs`.
- Aucun doublon transparent valide n'était déjà présent sur la carte après vérification sémantique des actions.

## C — Mismatches bookmark corrigés
- `47d6cec71d3710a42e63` : `Nav_HumainsJamaisConnectes` → `Nav_UtilisateursFantomes`.
- `b407bc3fe477ae00b21e` : `Nav_LicencesGaspillees` → `Nav_TechniquesInactives` car le bookmark existe et correspond mieux au KPI `NbBoitesInactives`.

## D — Disclaimer fraîcheur ajouté
- Nouveau textbox `dt_freshness_disclaimer_001` ajouté sur `page_drillthrough_detail_user`.
- Position : `(1137, 444, 663, 16)`.
- Texte : `⚠️ Activité M365 : données issues du rapport Microsoft avec 48-72h de décalage structurel.`

## E — Slicers redondants : décision par slicer
- `256a79fcfd1a1485f625` (`advancedSlicerVisual` sur `EtatActivite`) supprimé.
  Ce visuel n'est pas un récepteur drillthrough ; les filtres drillthrough `EtatActivite` et `UserPrincipalName` restent définis au niveau de la page.
- `d590c2deb480ca846ab9` (`advancedSlicerVisual` sur `StatutLicence`) supprimé.
  Ce visuel n'est pas un récepteur drillthrough et faisait doublon avec la navigation KPI dédiée aux comptes bloqués.
