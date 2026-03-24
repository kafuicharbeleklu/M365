# BL-003 - Verification HEAD des liaisons bouton -> bookmark
**Date**: 2026-03-24

## Portee
Verification des boutons interactifs sur la page `Analyse Utilisateur` (`3c4cbe0b2835dc22b7e2`) a partir du `HEAD` Git, pour distinguer les vrais problemes du depot des reserialisations locales de Power BI Desktop.

## Boutons KPI verifies comme coherents
- `kpi_actifs_btn_001` -> `Nav_HumainsActifs`
- `bc689230263b260580e0` -> `Nav_HumainsInactifs`
- `7a8b216031e010e2d1b4` -> `Nav_HumainsDesactivesKPI`
- `1a2f23d55a380141ed88` -> `Nav_TechniquesActives`
- `b407bc3fe477ae00b21e` -> `Nav_TechniquesInactives`
- `ux_action_disabled_btn_p3` -> `Nav_CompteDesactivesAvecLicence`
- `ux_action_ghost_btn_p3` -> `Nav_UtilisateursFantomes`
- `ux_action_overuse_btn_p3` -> `Nav_UsersProduitsDepassement`

## Faux positifs observes precedemment
- `Nav_HumainsInactifs` a deja `targetVisualNames: []` dans le `HEAD`
- `Nav_TechniquesActives` a deja `targetVisualNames: []` dans le `HEAD`
- `Nav_HumainsInactifs` filtre deja `CodeEtatActivite = INACTIF` dans le `HEAD`
- Les incoherences relevees sur ces points provenaient du working tree local reserialise par Power BI Desktop, pas du depot Git

## Verification complementaire
- Le bouton `79259f2e49cae54295a9` de P3 est bien configure en action `Back`
- Il ne pointe pas vers un bookmark KPI dans le `HEAD`
- Le bookmark `Nav_HumainsJamaisConnectes` existe encore, mais aucun bouton de la page `Analyse Utilisateur` ne l'appelle

## Conclusion
- Les boutons KPI actifs de P3 sont maintenant globalement coherents dans le depot
- La prochaine decision utile concerne surtout `Nav_HumainsJamaisConnectes`:
  - soit le recabler a un bouton KPI dedie
  - soit l'assumer comme bookmark orphelin et le documenter comme tel
