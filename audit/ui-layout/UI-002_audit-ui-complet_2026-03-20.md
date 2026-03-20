# UI-002 — Audit UI complet
**Date**: 2026-03-20
**Statut**:  En cours
**Périmètre**: 4 pages principales

## A — Boutons transparents désalignés
| Page | Button ID | Card cible ID | Δx | Δy | Statut |
|------|-----------|---------------|----|----|--------|
| Vue d'ensemble | `f006d16cea357fa216ad` | — | — | — | `NO_OVERLAY` |
| Vue d'ensemble | `39e489804ad79b14f1e3` | — | — | — | `NO_OVERLAY` |
| Vue d'ensemble | `fcf527b13b528b4cce49` | — | — | — | `NO_OVERLAY` |
| Analyse Licences | `ed9801a6641e69784d39` | — | — | — | `NO_OVERLAY` |
| Analyse Licences | `09d6c423bf6f0a295554` | — | — | — | `NO_OVERLAY` |
| Analyse Licences | `b2dc3498181f205c50bc` | — | — | — | `NO_OVERLAY` |
| Analyse Utilisateur | `79259f2e49cae54295a9` | — | — | — | `NO_OVERLAY` |
| Analyse Utilisateur | `ux_reset_filters_p3` | — | — | — | `NO_OVERLAY` |
| Analyse Utilisateur | `7b1496a23db63d581614` | `8030dbc87ab90506be3e` | `74` | `4` | `MISALIGNED` |
| Analyse Utilisateur | `bc689230263b260580e0` | `ce70ef9e7866cc72b78d` | `0` | `0` | `OK` |
| Analyse Utilisateur | `47d6cec71d3710a42e63` | `b5e7555e9ed80b014183` | `0` | `0` | `OK` |
| Analyse Utilisateur | `7a8b216031e010e2d1b4` | `d0f2e5dc55d345c41720` | `0` | `0` | `OK` |
| Analyse Utilisateur | `1a2f23d55a380141ed88` | `ce426e14c617550ccd13` | `0` | `0` | `OK` |
| Analyse Utilisateur | `b407bc3fe477ae00b21e` | `40e7ac536e9864857177` | `0` | `0` | `OK` |
| Analyse Utilisateur | `0a49bad639711380db9c` | `8030dbc87ab90506be3e` | `74` | `52` | `MISALIGNED` |
| Analyse Utilisateur | `6ec49b4eb05935f1b117` | — | — | — | `NO_OVERLAY` |
| Analyse Utilisateur | `7855b7f60d52cd95b580` | — | — | — | `NO_OVERLAY` |
| Analyse Utilisateur | `ux_action_disabled_btn_p3` | `ux_action_disabled_card_p3` | `0` | `0` | `OK` |
| Analyse Utilisateur | `ux_action_overuse_btn_p3` | `ux_action_overuse_card_p3` | `0` | `0` | `OK` |
| Analyse Utilisateur | `ux_action_ghost_btn_p3` | `ux_action_ghost_card_p3` | `0` | `0` | `OK` |
| Detail Utilisateur | `dt_back_btn_001` | — | — | — | `NO_OVERLAY` |

Constat principal :
- Les pages `Vue d'ensemble`, `Analyse Licences` et `Detail Utilisateur` n'ont pas de boutons transparents recouvrant des cartes KPI.
- `Analyse Utilisateur` contient deux boutons de navigation partiellement posés sur la carte `NbHumainsActifs` : `7b1496a23db63d581614` et `0a49bad639711380db9c`.
- Le bouton bookmark `7855b7f60d52cd95b580` (`Nav_HumainsActifs`) n'est plus sur la carte KPI et ne recouvre aucune carte.

## B — Doublons KPI / Slicer (Analyse Utilisateur)
### Inventaire KPI
| Card KPI | Mesure | Button couvrant | Cible |
|----------|--------|-----------------|-------|
| `8030dbc87ab90506be3e` | `NbHumainsActifs` | `0a49bad639711380db9c`, `7b1496a23db63d581614` | `PageNavigation` vers `Analyse Licences` / `Vue d'ensemble` |
| `678ebb458a124b23d8b3` | `NbHumainsTotal` | — | — |
| `ce70ef9e7866cc72b78d` | `NbHumainsInactifs` | `bc689230263b260580e0` | `Nav_HumainsInactifs` |
| `b5e7555e9ed80b014183` | `NbUtilisateursFantomes` | `47d6cec71d3710a42e63` | `Nav_HumainsJamaisConnectes` |
| `d0f2e5dc55d345c41720` | `NbHumainsDesactives` | `7a8b216031e010e2d1b4` | `Nav_HumainsDesactives` |
| `d8558517a5af0608ba18` | `NbBoitesTotal` | — | — |
| `ce426e14c617550ccd13` | `NbBoitesActives` | `1a2f23d55a380141ed88` | `Nav_TechniquesActives` |
| `40e7ac536e9864857177` | `NbBoitesInactives` | `b407bc3fe477ae00b21e` | `Nav_LicencesGaspillees` |
| `0781849f42b2a3099ac6` | `CiblesNettoyage` | — | — |
| `ux_action_disabled_card_p3` | `LicencesComptesBloques` | `ux_action_disabled_btn_p3` | `Nav_HumainsDesactives` |
| `ux_action_overuse_card_p3` | `UX_ProduitsEnDepassement` | `ux_action_overuse_btn_p3` | `PageNavigation` vers `Analyse Licences` |
| `ux_action_ghost_card_p3` | `NbUtilisateursFantomes` | `ux_action_ghost_btn_p3` | `Nav_HumainsJamaisConnectes` |

### Inventaire filtres
| Visual ID | Type | Champ(s) |
|-----------|------|----------|
| `ac1767da87f9554d5519` | `slicer` | `WhenCreated` |
| `a41382b807b0d8afd3a6` | `slicer` | `CountryOrRegion` |
| `13b24c306ab625400ecd` | `slicer` | `TypeCompte` |
| `cff18eebc6e8ac5a4392` | `slicer` | `Statut AD` |
| `7998d7938a65e4cbd1cd` | `slicer` | `Department` |
| `78c3a585a38d21cb56a8` | `slicer` | `NomProduit` |
| `d8f1ebe5daefcb4ea661` | `slicer` | `TypeLicence` |
| `256a79fcfd1a1485f625` | `advancedSlicerVisual` | `EtatActivite`, `UserPrincipalName` |
| `d590c2deb480ca846ab9` | `advancedSlicerVisual` | `StatutLicence` |

### Inventaire boutons bookmark
| Button ID | Cible |
|-----------|-------|
| `bc689230263b260580e0` | `Nav_HumainsInactifs` |
| `47d6cec71d3710a42e63` | `Nav_HumainsJamaisConnectes` |
| `7a8b216031e010e2d1b4` | `Nav_HumainsDesactives` |
| `1a2f23d55a380141ed88` | `Nav_TechniquesActives` |
| `b407bc3fe477ae00b21e` | `Nav_LicencesGaspillees` |
| `7855b7f60d52cd95b580` | `Nav_HumainsActifs` |
| `ux_reset_filters_p3` | `Nav_Reset` |
| `ux_action_disabled_btn_p3` | `Nav_HumainsDesactives` |
| `ux_action_ghost_btn_p3` | `Nav_HumainsJamaisConnectes` |

### Doublons détectés
| Population | KPI + Button ID | Slicer ID | Recommandation |
|------------|------------------|-----------|----------------|
| Humains inactifs | `ce70ef9e7866cc72b78d` + `bc689230263b260580e0` | `13b24c306ab625400ecd`, `cff18eebc6e8ac5a4392`, `256a79fcfd1a1485f625` | `KEEP KPI+button, REMOVE slicer` |
| Humains jamais connectés | `b5e7555e9ed80b014183` + `47d6cec71d3710a42e63` | `13b24c306ab625400ecd`, `cff18eebc6e8ac5a4392`, `256a79fcfd1a1485f625` | `KEEP KPI+button, REMOVE slicer` |
| Humains désactivés | `d0f2e5dc55d345c41720` + `7a8b216031e010e2d1b4` | `13b24c306ab625400ecd`, `cff18eebc6e8ac5a4392` | `KEEP KPI+button, REMOVE slicer` |

Notes utiles :
- `Humains actifs` n'entre pas dans les doublons exploitables car le bouton `7855b7f60d52cd95b580` (`Nav_HumainsActifs`) ne recouvre plus la KPI.
- `NbUtilisateursFantomes` et `NbBoitesInactives` ont des boutons recouvrants, mais les bookmarks déclenchés ne correspondent pas à la mesure affichée ; ce sont des mismatches, pas des doublons.

## C — Cards tronquées (Detail Utilisateur)
| Card | Mesure | Width actuelle | Truncation risk | Width recommandée |
|------|--------|----------------|-----------------|-------------------|
| `dt_card_displayname` | `DT_Nom` | `323` | `Non` | `Conserver` |
| `dt_card_upn` | `DT_Email` | `323` | `Non` | `Conserver` |
| `dt_card_dept` | `DT_Departement` | `323` | `Non` | `Conserver` |
| `dt_card_statut` | `DT_StatutAD` | `323` | `Non` | `Conserver` |
| `dt_card_etat` | `DT_EtatActivite` | `324` | `Non` | `Conserver` |

Constat :
- Aucune carte de la rangée identité n'est sous le seuil de `250px`.
- Le risque de troncature structurelle vient plutôt du contenu des labels/valeurs que de la largeur du container.

## D — Disclaimer fraîcheur données
| Visual DateDerniereActivite | Position actuelle | Disclaimer existant | Position suggérée |
|-----------------------------|------------------|---------------------|-------------------|
| `dt_profile_last_activity` | `(1137, 332, 323, 112)` | `Aucun textbox/shape voisin` | `(1137, 444, 663, 16)` |

Justification :
- La rangée profil se termine à `y=444`.
- La table commence à `y=460`.
- Un textbox de faible hauteur entre ces deux zones n'empiète ni sur les cartes ni sur la table.

## E — Cohérence hauteurs KPI
| Page | Heights trouvées | Écarts détectés |
|------|------------------|-----------------|
| Vue d'ensemble | `[120, 120, 120, 120, 120, 120, 120, 120]` | `Aucun` |
| Analyse Licences | `[120, 120, 120, 120, 120, 120]` | `Aucun` |
| Analyse Utilisateur | `[104, 104, 104, 104, 104, 104, 104, 104, 104]` | `Aucun` |

## Plan de corrections priorisé
1. Repositionner `7b1496a23db63d581614` et `0a49bad639711380db9c` pour qu'ils n'empiètent plus sur `NbHumainsActifs`.
2. Re-ancrer `7855b7f60d52cd95b580` sur la KPI `NbHumainsActifs`, sinon le parcours bookmark `Nav_HumainsActifs` reste inutilisable.
3. Corriger les mismatches KPI/bookmark de `NbUtilisateursFantomes` et `NbBoitesInactives` avant toute simplification de filtres.
4. Après correction des overlays, supprimer les slicers redondants de populations déjà couvertes par KPI + bookmark sur `Analyse Utilisateur`.
5. Ajouter un disclaimer de fraîcheur sous `dt_profile_last_activity`.
6. Ne rien changer sur les largeurs de la rangée identité ni sur les hauteurs KPI : elles sont cohérentes à ce stade.
