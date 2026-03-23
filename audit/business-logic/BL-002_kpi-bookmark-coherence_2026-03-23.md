# BL-002 - Audit coherence KPI -> bouton -> bookmark
**Date**: 2026-03-23

## Portee
Audit des boutons transparents relies a des bookmarks sur:
- `Vue d'ensemble`
- `Analyse Licences`
- `Analyse Utilisateur`
- `Detail Utilisateur`

## Findings

### 1. Bookmark live non documente sur P3
- Le bouton [7a8b216031e010e2d1b4/visual.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/7a8b216031e010e2d1b4/visual.json) pointe vers [fc8c08bf78c2215aa501.bookmark.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/bookmarks/fc8c08bf78c2215aa501.bookmark.json), affiche sous le nom `Signet 12`.
- Ce bookmark n'est pas nomme metierement et ne porte qu'un filtre `TypeCompte = Technique`.
- C'est un risque eleve: action utilisateur visible, intention fonctionnelle non explicite, maintenance fragile.

### 2. Deux bookmarks P3 gardent un `targetVisualNames` incoherent
- [66e80f63e44eee7812b9.bookmark.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/bookmarks/66e80f63e44eee7812b9.bookmark.json) (`Nav_HumainsInactifs`) cible `kpi_actifs_btn_001`.
- [f4a061ed23da49a09717.bookmark.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/bookmarks/f4a061ed23da49a09717.bookmark.json) (`Nav_TechniquesActives`) cible aussi `kpi_actifs_btn_001`.
- Ce ciblage ne correspond pas au bouton qui les declenche et ressemble a une capture de bookmark faite avec le mauvais visuel selectionne.

### 3. `Nav_HumainsInactifs` reste couple a un libelle metier
- [66e80f63e44eee7812b9.bookmark.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/bookmarks/66e80f63e44eee7812b9.bookmark.json) filtre `EtatActivite = 'Inactif >90j'`.
- A l'inverse, [02c501e8d87d63d0078c.bookmark.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/bookmarks/02c501e8d87d63d0078c.bookmark.json) et [33c262bf35d2d40b3aa8.bookmark.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/bookmarks/33c262bf35d2d40b3aa8.bookmark.json) utilisent le code stable `CodeEtatActivite`.
- Tant que `Nav_HumainsInactifs` reste sur `EtatActivite`, il depend du libelle et du seuil affiche, pas du code technique stable.

### 4. Le KPI "Comptes desactives avec licence" est maintenant correctement isole
- [ux_action_disabled_btn_p3/visual.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/pages/3c4cbe0b2835dc22b7e2/visuals/ux_action_disabled_btn_p3/visual.json) pointe vers [150a82ee4e0523134131.bookmark.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/bookmarks/150a82ee4e0523134131.bookmark.json).
- Ce bookmark applique `StatutLicence = ON` et `Statut AD = Desactive`, sans recycler `Nav_HumainsDesactives`.
- C'est le premier chemin P3 aligne correctement entre intention KPI et filtres reels.

### 5. Les quick filters P2 sont structurellement coherents
- [btn_filtre_critique_p2/visual.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/pages/54f9d470ac60b85b18da/visuals/btn_filtre_critique_p2/visual.json), [btn_filtre_depassement_p2/visual.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/pages/54f9d470ac60b85b18da/visuals/btn_filtre_depassement_p2/visual.json) et [btn_filtre_epuise_p2/visual.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/pages/54f9d470ac60b85b18da/visuals/btn_filtre_epuise_p2/visual.json) pointent tous vers des bookmarks P2 dedies.
- Les bookmarks [a5f1d2c3b4e50617283b.bookmark.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/bookmarks/a5f1d2c3b4e50617283b.bookmark.json), [a5f1d2c3b4e506172839.bookmark.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/bookmarks/a5f1d2c3b4e506172839.bookmark.json) et [a5f1d2c3b4e50617283a.bookmark.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/bookmarks/a5f1d2c3b4e50617283a.bookmark.json) ciblent le quickfilter `ux_risk_quickfilter_p2`.
- Je ne releve pas d'anomalie majeure de cablage sur ce groupe.

### 6. Quelques bookmarks P3 restent presents sans bouton metier visible
- [33c262bf35d2d40b3aa8.bookmark.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/bookmarks/33c262bf35d2d40b3aa8.bookmark.json) (`Nav_HumainsJamaisConnectes`)
- [1b1924d8900ee938d84a.bookmark.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/bookmarks/1b1924d8900ee938d84a.bookmark.json) (`Nav_LicencesGaspillees`)
- [dacdeaf07eb2d1577049.bookmark.json](C:/Users/eklu/Downloads/111/M365_V7/M365_UI.Report/definition/bookmarks/dacdeaf07eb2d1577049.bookmark.json) (`Nav_HumainsDesactives`, ancien chemin)
- Ils ne sont pas forcement faux, mais ils ne sont plus clairement relies a un bouton KPI actif dans l'etat local observe.

## Recommandations
1. Corriger en priorite `Signet 12` et lui donner soit un nom metier explicite, soit le retirer des actions live.
2. Nettoyer les `targetVisualNames` parasites sur `Nav_HumainsInactifs` et `Nav_TechniquesActives`.
3. Aligner `Nav_HumainsInactifs` sur `CodeEtatActivite = 'INACTIF'`.
4. Faire ensuite une passe de nettoyage des bookmarks P3 orphelins ou redondants.
