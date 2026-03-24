# FIX-068 - Nettoyage des bookmarks legacy non appeles
**Date**: 2026-03-24

## Diagnostic
- Verification exhaustive du `HEAD` Git sur les `actionButton` du report
- Cinq bookmarks restaient presents dans `bookmarks.json` sans aucun bouton appelant
- Ces bookmarks n'etaient references nulle part ailleurs dans le report

## Bookmarks retires
- `Nav_HumainsJamaisConnectes` (`33c262bf35d2d40b3aa8`)
- `Nav_HumainsDesactives` (`dacdeaf07eb2d1577049`)
- `Nav_Techniques` (`3c091465604a5742de2e`)
- `Nav_LicencesGaspillees` (`1b1924d8900ee938d84a`)
- `Signet 10` (`53def320d1a3d36a5928`)

## Fix applique
- Suppression des cinq fichiers `.bookmark.json`
- Retrait des cinq entrees correspondantes dans `M365_UI.Report/definition/bookmarks/bookmarks.json`

## Resultat attendu
- Reduction du bruit legacy dans le report
- Inventaire des bookmarks aligne sur les seuls bookmarks encore appeles
- Moins de confusion lors des futurs audits KPI -> bouton -> bookmark
