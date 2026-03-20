# UI-003 â€” Audit layout pixel-perfect
**Date**: 2026-03-20
**Statut**:  En cours
**PÃ©rimÃ¨tre**: 4 pages principales

## A â€” Constantes canvas et navigation
| Page | Canvas W | Canvas H | Content Start X | Content End X |
|------|----------|----------|-----------------|---------------|
| Vue d'ensemble | 1920 | 1080 | 200 | 1910 |
| Analyse Licences | 1920 | 1080 | 200 | 1910 |
| Analyse Utilisateur | 1920 | 1080 | 200 | 1910 |
| Detail Utilisateur | 1920 | 1080 | 120 | 1910 |

- `LEFT_NAV_WIDTH = 190` sur les 3 pages principales. Les visuels Ã  `x < 200` sont en conflit avec le chrome natif Power BI.
- `CONTENT_END_X = 1910` (`canvas_width - 10`).
- `HEADER_HEIGHT = 92` sur les 4 pages : premiÃ¨re ligne de contenu sous le titre.
- RÃ©glages background / wallpaper :
  - Vue d'ensemble : background: theme(0,-0.1) / transparency 7D; wallpaper: none
  - Analyse Licences : background: theme(0,-0.1) / transparency 0D; wallpaper: none
  - Analyse Utilisateur : background: theme(0,-0.1) / transparency 0D; wallpaper: none
  - Detail Utilisateur : background: theme(0,-0.1) / transparency 0D; wallpaper: none

## B â€” Inventaire complet des visuels
### Vue d'ensemble â€” a4497031bb9f4bfb6556
| Visual ID | Type | Mesure / Champ | x | y | width | height | Right edge | Bottom edge |
|-----------|------|----------------|---|---|-------|--------|------------|-------------|
| 9626e5c75f9e8f5c08ab | group | - | 0 | 0 | 280 | 1080 | 280 | 1080 |
| 0d0f2c648c01c1f648a7 | shape | - | 0 | 0 | 280 | 1080 | 280 | 1080 |
| 57cd12a3c5c073767919 | textbox | Vue d'ensemble / Adoption globale, activite et couverture des licences | 296 | 8 | 1608 | 72 | 1904 | 80 |
| b3a44db816229d136326 | image | - | 20 | 16 | 240 | 56 | 260 | 72 |
| ux_refresh_banner_p1 | card | _Mesures.UX_DerniereMiseAJour | 1610 | 32 | 290 | 36 | 1900 | 68 |
| f006d16cea357fa216ad | actionButton | Page:a4497031bb9f4bfb6556 | 20 | 88 | 240 | 44 | 260 | 132 |
| e01617238ac009dd6693 | card | _Mesures.TotalUtilisateurs | 300 | 92 | 186 | 120 | 486 | 212 |
| 32f0782d609024c5ddeb | card | _Mesures.NbHumainsActifs | 502 | 92 | 186 | 120 | 688 | 212 |
| 5a57e51bd95d62c2f1c8 | card | _Mesures.NbHumainsInactifs | 704 | 92 | 186 | 120 | 890 | 212 |
| ebe08689cd1cb3339e74 | card | _Mesures.NbHumainsDesactives | 906 | 92 | 186 | 120 | 1092 | 212 |
| ed4f3b6ef5234a8c7a7e | card | _Mesures.StockLicences | 1108 | 92 | 186 | 120 | 1294 | 212 |
| dfb6bb22621287a516f5 | card | _Mesures.LicencesActives | 1310 | 92 | 186 | 120 | 1496 | 212 |
| d3b401179a9644ebfef4 | card | _Mesures.LicencesInactives | 1512 | 92 | 186 | 120 | 1698 | 212 |
| 97ff1f41db18c4fc211a | card | _Mesures.LicencesDisponibles | 1714 | 92 | 186 | 120 | 1900 | 212 |
| 39e489804ad79b14f1e3 | actionButton | Page:54f9d470ac60b85b18da | 20 | 144 | 240 | 44 | 260 | 188 |
| fcf527b13b528b4cce49 | actionButton | Page:3c4cbe0b2835dc22b7e2 | 20 | 200 | 240 | 44 | 260 | 244 |
| d9407e41b932cde22e6b | hundredPercentStackedBarChart | T_Produits_Dim.NomProduit, _Mesures.LicencesActives, _Mesures.LicencesInactives, _Mesures.LicencesDisponibles | 300 | 228 | 1196 | 388 | 1496 | 616 |
| 3f8e3ca22bd94e8d2782 | gauge | _Mesures.TauxUtilisation | 1512 | 228 | 392 | 186 | 1904 | 414 |
| 7576df232a88a5e13d21 | slicer | T_Utilisateurs_Dim.WhenCreated | 20 | 268 | 240 | 100 | 260 | 368 |
| 13993fe2e745b349a9d5 | slicer | T_Utilisateurs_Dim.CountryOrRegion | 20 | 384 | 240 | 90 | 260 | 474 |
| 16a2195710bfb1beb12c | gauge | _Mesures.TauxActiviteUtilisateurs | 1512 | 430 | 392 | 186 | 1904 | 616 |
| 8ba9d0f5579e41d05b89 | slicer | T_Utilisateurs_Dim.Department | 20 | 490 | 240 | 90 | 260 | 580 |
| b2f94b5f4d87f60a7629 | slicer | T_Produits_Dim.NomProduit | 20 | 596 | 240 | 90 | 260 | 686 |
| d2942203372b41a1e52c | azureMap | T_Utilisateurs_Dim.CountryOrRegion, _Mesures.TotalUtilisateurs | 300 | 632 | 792 | 376 | 1092 | 1008 |
| 82e9038bf2275194b4f7 | columnChart | T_Utilisateurs_Dim.CountryOrRegion, _Mesures.LicencesAffectees, _Mesures.LicencesInactives | 1108 | 632 | 796 | 376 | 1904 | 1008 |
| 7cd221b2685275681dc8 | slicer | T_Produits_Dim.TypeLicence | 20 | 702 | 240 | 120 | 260 | 822 |
| ffb33c5d97e0ade0c492 | ScrollingTextVisual1448795304508 | T_Utilisateurs_Dim.CountryOrRegion, _Mesures.LicencesInactives | 300 | 1024 | 1604 | 40 | 1904 | 1064 |

### Analyse Licences â€” 54f9d470ac60b85b18da
| Visual ID | Type | Mesure / Champ | x | y | width | height | Right edge | Bottom edge |
|-----------|------|----------------|---|---|-------|--------|------------|-------------|
| 144feccfa5fbea4db9e4 | group | - | 0 | 0 | 280 | 1080 | 280 | 1080 |
| f47cab793550000da57d | shape | - | 0 | 0 | 280 | 1080 | 280 | 1080 |
| 4e1a01705b45b2070499 | textbox | Analyse Licences / Stock, affectation et utilisation des licences | 296 | 8 | 1608 | 72 | 1904 | 80 |
| 0db51d0a4236116c3872 | image | - | 20 | 16 | 240 | 56 | 260 | 72 |
| ux_context_banner_p2 | card | _Mesures.UX_ContexteFiltres | 960 | 32 | 640 | 36 | 1600 | 68 |
| ux_refresh_banner_p2 | card | _Mesures.UX_DerniereMiseAJour | 1610 | 32 | 290 | 36 | 1900 | 68 |
| ed9801a6641e69784d39 | actionButton | Page:a4497031bb9f4bfb6556 | 20 | 88 | 240 | 44 | 260 | 132 |
| 2c5997a1c165a6f8f1ae | card | _Mesures.NombreProduits | 300 | 92 | 254 | 120 | 554 | 212 |
| 6f1df5859617b98c1562 | card | _Mesures.StockLicences | 570 | 92 | 254 | 120 | 824 | 212 |
| e1b3be0487c3ace443a4 | card | _Mesures.LicencesAffectees | 840 | 92 | 254 | 120 | 1094 | 212 |
| 40db69b7a2dd5b305e58 | card | _Mesures.LicencesActives | 1110 | 92 | 254 | 120 | 1364 | 212 |
| 746add9e9b3de7697cf0 | card | _Mesures.LicencesDisponibles | 1380 | 92 | 254 | 120 | 1634 | 212 |
| 3c5834c05e73a26ef3ce | card | _Mesures.LicencesInactives | 1650 | 92 | 254 | 120 | 1904 | 212 |
| 09d6c423bf6f0a295554 | actionButton | Page:54f9d470ac60b85b18da | 20 | 144 | 240 | 44 | 260 | 188 |
| b2dc3498181f205c50bc | actionButton | Page:3c4cbe0b2835dc22b7e2 | 20 | 200 | 240 | 44 | 260 | 244 |
| legend_licences_dispo_001 | textbox | Legende disponibilite: / Critique (<0) / / / Elevee (<=10%) / / / Moderee (<=25%) / / / Surveiller (<=50%) | 300 | 228 | 1604 | 28 | 1904 | 256 |
| 3626dc072b6e376f3a86 | slicer | T_Utilisateurs_Dim.WhenCreated | 20 | 268 | 240 | 100 | 260 | 368 |
| ux_l2_overuse_card | card | _Mesures.UX_ProduitsEnDepassement | 300 | 272 | 389 | 78 | 689 | 350 |
| ux_l2_exhausted_card | card | _Mesures.UX_ProduitsStockEpuise | 705 | 272 | 389 | 78 | 1094 | 350 |
| ux_l2_critical_card | card | _Mesures.UX_ProduitsStockCritique | 1110 | 272 | 389 | 78 | 1499 | 350 |
| ux_l2_risklevel_card | card | _Mesures.UX_NiveauRisqueLicences | 1515 | 272 | 389 | 78 | 1904 | 350 |
| 51a8fe4679139854ecc5 | donutChart | _Mesures.LicencesAffectees, _Mesures.LicencesActives, _Mesures.LicencesDisponibles | 300 | 366 | 450 | 264 | 750 | 630 |
| 9bdea977b2b328ae4ce4 | pivotTable | T_Produits_Dim.NomProduit, _Mesures.StockLicences, _Mesures.LicencesAffectees, _Mesures.LicencesActives, _Mesures.LicencesInactives, _Mesures.LicencesDisponibles, _Mesures.TauxUtilisation | 766 | 366 | 1138 | 694 | 1904 | 1060 |
| 9be3f2f347da33375eb0 | slicer | T_Utilisateurs_Dim.CountryOrRegion | 20 | 384 | 240 | 90 | 260 | 474 |
| 86770fbf6fe57e94e998 | slicer | T_Utilisateurs_Dim.Department | 20 | 490 | 240 | 90 | 260 | 580 |
| 90319ee1bdd377ebb01a | slicer | T_Produits_Dim.NomProduit | 20 | 596 | 240 | 90 | 260 | 686 |
| ux_risk_quickfilter_p2 | slicer | T_Produits_Dim.NiveauRisqueStock | 300 | 646 | 450 | 170 | 750 | 816 |
| 2e4b80c68d53a65fee7c | slicer | T_Produits_Dim.TypeLicence | 20 | 702 | 240 | 120 | 260 | 822 |

### Analyse Utilisateur â€” 3c4cbe0b2835dc22b7e2
| Visual ID | Type | Mesure / Champ | x | y | width | height | Right edge | Bottom edge |
|-----------|------|----------------|---|---|-------|--------|------------|-------------|
| 321cf8d0d5d0be093468 | shape | - | 0 | 0 | 280 | 1080 | 280 | 1080 |
| 3a2e0f8584503a88dcbf | group | - | 0 | 0 | 280 | 1080 | 280 | 1080 |
| 855861f892a1da7eccbf | textbox | Analyse Utilisateur / Annuaire, activite et nettoyage des comptes | 356 | 8 | 1548 | 72 | 1904 | 80 |
| 4ef11891f58da3f6fa5b | image | - | 20 | 16 | 240 | 56 | 260 | 72 |
| 79259f2e49cae54295a9 | actionButton | Button | 296 | 20 | 44 | 44 | 340 | 64 |
| ux_reset_filters_p3 | actionButton | Bookmark:1661112e2198ecabde3e | 1700 | 20 | 204 | 40 | 1904 | 60 |
| ux_context_banner_p3 | card | _Mesures.UX_ContexteFiltres | 760 | 36 | 640 | 32 | 1400 | 68 |
| ux_refresh_banner_p3 | card | _Mesures.UX_DerniereMiseAJour | 1410 | 36 | 280 | 32 | 1690 | 68 |
| 7b1496a23db63d581614 | actionButton | Page:a4497031bb9f4bfb6556 | 20 | 88 | 240 | 44 | 260 | 132 |
| 7855b7f60d52cd95b580 | actionButton | Bookmark:02c501e8d87d63d0078c | 97 | 92 | 187 | 104 | 284 | 196 |
| 8030dbc87ab90506be3e | card | _Mesures.NbHumainsActifs | 97 | 92 | 187 | 104 | 284 | 196 |
| 678ebb458a124b23d8b3 | card | _Mesures.NbHumainsTotal | 300 | 92 | 187 | 104 | 487 | 196 |
| bc689230263b260580e0 | actionButton | Bookmark:66e80f63e44eee7812b9 | 503 | 92 | 187 | 104 | 690 | 196 |
| ce70ef9e7866cc72b78d | card | _Mesures.NbHumainsInactifs | 503 | 92 | 187 | 104 | 690 | 196 |
| b5e7555e9ed80b014183 | card | _Mesures.NbUtilisateursFantomes | 706 | 92 | 187 | 104 | 893 | 196 |
| 47d6cec71d3710a42e63 | actionButton | Bookmark:ca5213839361d51050a4 | 706 | 92 | 187 | 104 | 893 | 196 |
| d0f2e5dc55d345c41720 | card | _Mesures.NbHumainsDesactives | 909 | 92 | 187 | 104 | 1096 | 196 |
| 7a8b216031e010e2d1b4 | actionButton | Bookmark:dacdeaf07eb2d1577049 | 909 | 92 | 187 | 104 | 1096 | 196 |
| d8558517a5af0608ba18 | card | _Mesures.NbBoitesTotal | 1112 | 92 | 187 | 104 | 1299 | 196 |
| 1a2f23d55a380141ed88 | actionButton | Bookmark:f4a061ed23da49a09717 | 1315 | 92 | 187 | 104 | 1502 | 196 |
| ce426e14c617550ccd13 | card | _Mesures.NbBoitesActives | 1315 | 92 | 187 | 104 | 1502 | 196 |
| b407bc3fe477ae00b21e | actionButton | Bookmark:bab47829329722d7d720 | 1518 | 92 | 187 | 104 | 1705 | 196 |
| 40e7ac536e9864857177 | card | _Mesures.NbBoitesInactives | 1518 | 92 | 187 | 104 | 1705 | 196 |
| 0781849f42b2a3099ac6 | card | _Mesures.CiblesNettoyage | 1721 | 92 | 189 | 104 | 1910 | 196 |
| 0a49bad639711380db9c | actionButton | Page:54f9d470ac60b85b18da | 20 | 144 | 240 | 44 | 260 | 188 |
| 6ec49b4eb05935f1b117 | actionButton | Page:3c4cbe0b2835dc22b7e2 | 20 | 200 | 240 | 44 | 260 | 244 |
| ac1767da87f9554d5519 | slicer | T_Utilisateurs_Dim.WhenCreated | 20 | 268 | 240 | 100 | 260 | 368 |
| 87d3521e0b96312bffb0 | tableEx | _Mesures.NomUtilisateurAffiche, T_Utilisateurs_Dim.UserPrincipalName, T_Utilisateurs_Dim.CountryOrRegion, T_Utilisateurs_Dim.Statut AD, T_Utilisateurs_Dim.EtatActivite, T_Utilisateurs_Dim.LastSignIn, _Mesures.LicencesAffectees | 776 | 268 | 1128 | 792 | 1904 | 1060 |
| a41382b807b0d8afd3a6 | slicer | T_Utilisateurs_Dim.CountryOrRegion | 20 | 384 | 240 | 90 | 260 | 474 |
| 13b24c306ab625400ecd | slicer | T_Utilisateurs_Dim.TypeCompte | 300 | 488 | 220 | 96 | 520 | 584 |
| cff18eebc6e8ac5a4392 | slicer | T_Utilisateurs_Dim.Statut AD | 536 | 488 | 224 | 96 | 760 | 584 |
| 7998d7938a65e4cbd1cd | slicer | T_Utilisateurs_Dim.Department | 20 | 490 | 240 | 90 | 260 | 580 |
| 78c3a585a38d21cb56a8 | slicer | T_Produits_Dim.NomProduit | 20 | 596 | 240 | 90 | 260 | 686 |
| d8f1ebe5daefcb4ea661 | slicer | T_Produits_Dim.TypeLicence | 20 | 702 | 240 | 120 | 260 | 822 |
| ux_action_disabled_btn_p3 | actionButton | Bookmark:dacdeaf07eb2d1577049 | 300 | 702 | 380 | 80 | 680 | 782 |
| ux_action_disabled_card_p3 | card | _Mesures.LicencesComptesBloques | 300 | 702 | 380 | 80 | 680 | 782 |
| ux_action_overuse_card_p3 | card | _Mesures.UX_ProduitsEnDepassement | 300 | 798 | 380 | 80 | 680 | 878 |
| ux_action_overuse_btn_p3 | actionButton | Page:54f9d470ac60b85b18da | 300 | 798 | 380 | 80 | 680 | 878 |
| ux_action_ghost_btn_p3 | actionButton | Bookmark:33c262bf35d2d40b3aa8 | 300 | 894 | 380 | 80 | 680 | 974 |
| ux_action_ghost_card_p3 | card | _Mesures.NbUtilisateursFantomes | 300 | 894 | 380 | 80 | 680 | 974 |

### Detail Utilisateur â€” page_drillthrough_detail_user
| Visual ID | Type | Mesure / Champ | x | y | width | height | Right edge | Bottom edge |
|-----------|------|----------------|---|---|-------|--------|------------|-------------|
| dt_title_001 | textbox | Detail Utilisateur / Identite, activite et licences de l'utilisateur selectionne | 296 | 8 | 1504 | 72 | 1800 | 80 |
| ux_refresh_banner_dt | card | _Mesures.UX_DerniereMiseAJour | 1610 | 8 | 290 | 36 | 1900 | 44 |
| dt_back_btn_001 | actionButton | Button | 120 | 20 | 160 | 40 | 280 | 60 |
| dt_card_displayname | card | _Mesures.DT_Nom | 120 | 92 | 323 | 108 | 443 | 200 |
| dt_card_upn | card | _Mesures.DT_Email | 459 | 92 | 323 | 108 | 782 | 200 |
| dt_card_dept | card | _Mesures.DT_Departement | 798 | 92 | 323 | 108 | 1121 | 200 |
| dt_card_statut | card | _Mesures.DT_StatutAD | 1137 | 92 | 323 | 108 | 1460 | 200 |
| dt_card_etat | card | _Mesures.DT_EtatActivite | 1476 | 92 | 324 | 108 | 1800 | 200 |
| dt_kpi_licences | card | _Mesures.LicencesAffectees | 120 | 216 | 549 | 100 | 669 | 316 |
| dt_kpi_actives | card | _Mesures.LicencesActives | 685 | 216 | 549 | 100 | 1234 | 316 |
| dt_kpi_inactives | card | _Mesures.LicencesInactives | 1250 | 216 | 550 | 100 | 1800 | 316 |
| dt_profile_niveau | card | _Mesures.DT_NiveauUtilisation | 120 | 332 | 323 | 112 | 443 | 444 |
| dt_profile_score | card | _Mesures.DT_ScoreUtilisation | 459 | 332 | 323 | 112 | 782 | 444 |
| dt_profile_apps | card | _Mesures.DT_NbAppsUtilisees | 798 | 332 | 323 | 112 | 1121 | 444 |
| dt_profile_last_activity | card | _Mesures.DT_DateDerniereActivite | 1137 | 332 | 323 | 112 | 1460 | 444 |
| dt_profile_last_signin | card | _Mesures.DT_DateDerniereAuthentification | 1476 | 332 | 324 | 112 | 1800 | 444 |
| dt_freshness_disclaimer_001 | textbox | Ã¢Å¡ Ã¯Â¸Â ActivitÃƒÂ© M365 : donnÃƒÂ©es issues du rapport Microsoft avec 48-72h de dÃƒÂ©calage structurel. | 1137 | 444 | 663 | 16 | 1800 | 460 |
| dt_table_licences | tableEx | T_Utilisateurs_Dim.DisplayName, T_Utilisateurs_Dim.UserPrincipalName, T_Affectations_Fact.CodeSKU, T_Affectations_Fact.NomProduit, T_Affectations_Fact.TypeLicence, T_Utilisateurs_Dim.Statut AD, T_Utilisateurs_Dim.EtatActivite, T_Utilisateurs_Dim.Department | 120 | 460 | 1680 | 600 | 1800 | 1060 |

## C â€” Analyse grille horizontale
### Vue d'ensemble
| Row Y | Visual | x | width | Right edge | Gap aprÃ¨s | Gap idÃ©al | Statut |
|-------|--------|---|-------|------------|-----------|-----------|--------|
| 0 | 0d0f2c648c01c1f648a7 | 0 | 280 | 280 | -280 | 1150 | Nav |
| 0 | 9626e5c75f9e8f5c08ab | 0 | 280 | 280 | - | 1150 | Nav |
| 92 | f006d16cea357fa216ad | 20 | 240 | 260 | 40 | -2.25 | Nav, Top, Gap |
| 92 | e01617238ac009dd6693 | 300 | 186 | 486 | 16 | -2.25 | OK |
| 92 | 32f0782d609024c5ddeb | 502 | 186 | 688 | 16 | -2.25 | OK |
| 92 | 5a57e51bd95d62c2f1c8 | 704 | 186 | 890 | 16 | -2.25 | OK |
| 92 | ebe08689cd1cb3339e74 | 906 | 186 | 1092 | 16 | -2.25 | OK |
| 92 | ed4f3b6ef5234a8c7a7e | 1108 | 186 | 1294 | 16 | -2.25 | OK |
| 92 | dfb6bb22621287a516f5 | 1310 | 186 | 1496 | 16 | -2.25 | OK |
| 92 | d3b401179a9644ebfef4 | 1512 | 186 | 1698 | 16 | -2.25 | OK |
| 92 | 97ff1f41db18c4fc211a | 1714 | 186 | 1900 | - | -2.25 | OK |
| 228 | d9407e41b932cde22e6b | 300 | 1196 | 1496 | 16 | 122 | OK |
| 228 | 3f8e3ca22bd94e8d2782 | 1512 | 392 | 1904 | - | 122 | OK |
| 632 | d2942203372b41a1e52c | 300 | 792 | 1092 | 16 | 122 | OK |
| 632 | 82e9038bf2275194b4f7 | 1108 | 796 | 1904 | - | 122 | OK |

### Analyse Licences
| Row Y | Visual | x | width | Right edge | Gap aprÃ¨s | Gap idÃ©al | Statut |
|-------|--------|---|-------|------------|-----------|-----------|--------|
| 0 | f47cab793550000da57d | 0 | 280 | 280 | -280 | 1150 | Nav |
| 0 | 144feccfa5fbea4db9e4 | 0 | 280 | 280 | - | 1150 | Nav |
| 32 | ux_context_banner_p2 | 960 | 640 | 1600 | 10 | 780 | OK |
| 32 | ux_refresh_banner_p2 | 1610 | 290 | 1900 | - | 780 | OK |
| 92 | ed9801a6641e69784d39 | 20 | 240 | 260 | 40 | -9 | Nav, Top, Gap |
| 92 | 2c5997a1c165a6f8f1ae | 300 | 254 | 554 | 16 | -9 | OK |
| 92 | 6f1df5859617b98c1562 | 570 | 254 | 824 | 16 | -9 | OK |
| 92 | e1b3be0487c3ace443a4 | 840 | 254 | 1094 | 16 | -9 | OK |
| 92 | 40db69b7a2dd5b305e58 | 1110 | 254 | 1364 | 16 | -9 | OK |
| 92 | 746add9e9b3de7697cf0 | 1380 | 254 | 1634 | 16 | -9 | OK |
| 92 | 3c5834c05e73a26ef3ce | 1650 | 254 | 1904 | - | -9 | OK |
| 272 | 3626dc072b6e376f3a86 | 20 | 240 | 260 | 40 | -21.5 | Nav, Top, Gap |
| 272 | ux_l2_overuse_card | 300 | 389 | 689 | 16 | -21.5 | OK |
| 272 | ux_l2_exhausted_card | 705 | 389 | 1094 | 16 | -21.5 | OK |
| 272 | ux_l2_critical_card | 1110 | 389 | 1499 | 16 | -21.5 | OK |
| 272 | ux_l2_risklevel_card | 1515 | 389 | 1904 | - | -21.5 | OK |
| 366 | 51a8fe4679139854ecc5 | 300 | 450 | 750 | 16 | 122 | OK |
| 366 | 9bdea977b2b328ae4ce4 | 766 | 1138 | 1904 | - | 122 | OK |

### Analyse Utilisateur
| Row Y | Visual | x | width | Right edge | Gap aprÃ¨s | Gap idÃ©al | Statut |
|-------|--------|---|-------|------------|-----------|-----------|--------|
| 0 | 3a2e0f8584503a88dcbf | 0 | 280 | 280 | -280 | 1150 | Nav |
| 0 | 321cf8d0d5d0be093468 | 0 | 280 | 280 | - | 1150 | Nav |
| 20 | 4ef11891f58da3f6fa5b | 20 | 240 | 260 | 36 | 611 | Nav, Top, Gap |
| 20 | 79259f2e49cae54295a9 | 296 | 44 | 340 | 1360 | 611 | OK |
| 20 | ux_reset_filters_p3 | 1700 | 204 | 1904 | - | 611 | OK |
| 36 | ux_context_banner_p3 | 760 | 640 | 1400 | 10 | 790 | OK |
| 36 | ux_refresh_banner_p3 | 1410 | 280 | 1690 | - | 790 | OK |
| 92 | 7b1496a23db63d581614 | 20 | 240 | 260 | -163 | -89.133 | Nav, Top, Gap |
| 92 | 8030dbc87ab90506be3e | 97 | 187 | 284 | -187 | -89.133 | Nav, Gap |
| 92 | 7855b7f60d52cd95b580 | 97 | 187 | 284 | 16 | -89.133 | Nav |
| 92 | 678ebb458a124b23d8b3 | 300 | 187 | 487 | 16 | -89.133 | OK |
| 92 | ce70ef9e7866cc72b78d | 503 | 187 | 690 | -187 | -89.133 | Gap |
| 92 | bc689230263b260580e0 | 503 | 187 | 690 | 16 | -89.133 | OK |
| 92 | 47d6cec71d3710a42e63 | 706 | 187 | 893 | -187 | -89.133 | Gap |
| 92 | b5e7555e9ed80b014183 | 706 | 187 | 893 | 16 | -89.133 | OK |
| 92 | 7a8b216031e010e2d1b4 | 909 | 187 | 1096 | -187 | -89.133 | Gap |
| 92 | d0f2e5dc55d345c41720 | 909 | 187 | 1096 | 16 | -89.133 | OK |
| 92 | d8558517a5af0608ba18 | 1112 | 187 | 1299 | 16 | -89.133 | OK |
| 92 | ce426e14c617550ccd13 | 1315 | 187 | 1502 | -187 | -89.133 | Gap |
| 92 | 1a2f23d55a380141ed88 | 1315 | 187 | 1502 | 16 | -89.133 | OK |
| 92 | 40e7ac536e9864857177 | 1518 | 187 | 1705 | -187 | -89.133 | Gap |
| 92 | b407bc3fe477ae00b21e | 1518 | 187 | 1705 | 16 | -89.133 | OK |
| 92 | 0781849f42b2a3099ac6 | 1721 | 189 | 1910 | - | -89.133 | OK |
| 268 | ac1767da87f9554d5519 | 20 | 240 | 260 | 516 | 342 | Nav |
| 268 | 87d3521e0b96312bffb0 | 776 | 1128 | 1904 | - | 342 | OK |
| 488 | 7998d7938a65e4cbd1cd | 20 | 240 | 260 | 40 | 513 | Nav, Gap |
| 488 | 13b24c306ab625400ecd | 300 | 220 | 520 | 16 | 513 | OK |
| 488 | cff18eebc6e8ac5a4392 | 536 | 224 | 760 | - | 513 | OK |
| 702 | d8f1ebe5daefcb4ea661 | 20 | 240 | 260 | 40 | 355 | Nav, Gap |
| 702 | ux_action_disabled_card_p3 | 300 | 380 | 680 | -380 | 355 | OK |
| 702 | ux_action_disabled_btn_p3 | 300 | 380 | 680 | - | 355 | OK |
| 798 | ux_action_overuse_btn_p3 | 300 | 380 | 680 | -380 | 950 | OK |
| 798 | ux_action_overuse_card_p3 | 300 | 380 | 680 | - | 950 | OK |
| 894 | ux_action_ghost_card_p3 | 300 | 380 | 680 | -380 | 950 | OK |
| 894 | ux_action_ghost_btn_p3 | 300 | 380 | 680 | - | 950 | OK |

### Detail Utilisateur
| Row Y | Visual | x | width | Right edge | Gap aprÃ¨s | Gap idÃ©al | Statut |
|-------|--------|---|-------|------------|-----------|-----------|--------|
| 8 | dt_title_001 | 296 | 1504 | 1800 | -190 | -4 | OK |
| 8 | ux_refresh_banner_dt | 1610 | 290 | 1900 | - | -4 | OK |
| 92 | dt_card_displayname | 120 | 323 | 443 | 16 | 43.5 | OK |
| 92 | dt_card_upn | 459 | 323 | 782 | 16 | 43.5 | OK |
| 92 | dt_card_dept | 798 | 323 | 1121 | 16 | 43.5 | OK |
| 92 | dt_card_statut | 1137 | 323 | 1460 | 16 | 43.5 | OK |
| 92 | dt_card_etat | 1476 | 324 | 1800 | - | 43.5 | OK |
| 216 | dt_kpi_licences | 120 | 549 | 669 | 16 | 71 | OK |
| 216 | dt_kpi_actives | 685 | 549 | 1234 | 16 | 71 | OK |
| 216 | dt_kpi_inactives | 1250 | 550 | 1800 | - | 71 | OK |
| 332 | dt_profile_niveau | 120 | 323 | 443 | 16 | 43.5 | OK |
| 332 | dt_profile_score | 459 | 323 | 782 | 16 | 43.5 | OK |
| 332 | dt_profile_apps | 798 | 323 | 1121 | 16 | 43.5 | OK |
| 332 | dt_profile_last_activity | 1137 | 323 | 1460 | 16 | 43.5 | OK |
| 332 | dt_profile_last_signin | 1476 | 324 | 1800 | - | 43.5 | OK |

## D â€” Analyse espacement vertical
| Page | Row A | Row B | Gap actuel | Gap recommandÃ© | Statut |
|------|-------|-------|------------|-----------------|--------|
| Vue d'ensemble | 0 | 8 | -1072 | 16 | Too tight, Inconsistent |
| Vue d'ensemble | 8 | 16 | -64 | 16 | Too tight, Inconsistent |
| Vue d'ensemble | 16 | 32 | -40 | 16 | Too tight, Inconsistent |
| Vue d'ensemble | 32 | 92 | 24 | 16 | OK |
| Vue d'ensemble | 92 | 144 | -68 | 16 | Too tight, Inconsistent |
| Vue d'ensemble | 144 | 200 | 12 | 16 | OK |
| Vue d'ensemble | 200 | 228 | -16 | 16 | Too tight, Inconsistent |
| Vue d'ensemble | 228 | 268 | -348 | 16 | Too tight, Inconsistent |
| Vue d'ensemble | 268 | 384 | 16 | 16 | OK |
| Vue d'ensemble | 384 | 430 | -44 | 16 | Too tight, Inconsistent |
| Vue d'ensemble | 430 | 490 | -126 | 16 | Too tight, Inconsistent |
| Vue d'ensemble | 490 | 596 | 16 | 16 | OK |
| Vue d'ensemble | 596 | 632 | -54 | 16 | Too tight, Inconsistent |
| Vue d'ensemble | 632 | 702 | -306 | 16 | Too tight, Inconsistent |
| Vue d'ensemble | 702 | 1024 | 202 | 16 | Too loose, Inconsistent |
| Analyse Licences | 0 | 8 | -1072 | 16 | Too tight, Inconsistent |
| Analyse Licences | 8 | 16 | -64 | 16 | Too tight, Inconsistent |
| Analyse Licences | 16 | 32 | -40 | 16 | Too tight, Inconsistent |
| Analyse Licences | 32 | 92 | 24 | 16 | OK |
| Analyse Licences | 92 | 144 | -68 | 16 | Too tight, Inconsistent |
| Analyse Licences | 144 | 200 | 12 | 16 | OK |
| Analyse Licences | 200 | 228 | -16 | 16 | Too tight, Inconsistent |
| Analyse Licences | 228 | 272 | 16 | 16 | OK |
| Analyse Licences | 272 | 366 | -2 | 16 | Too tight, Inconsistent |
| Analyse Licences | 366 | 384 | -676 | 16 | Too tight, Inconsistent |
| Analyse Licences | 384 | 490 | 16 | 16 | OK |
| Analyse Licences | 490 | 596 | 16 | 16 | OK |
| Analyse Licences | 596 | 646 | -40 | 16 | Too tight, Inconsistent |
| Analyse Licences | 646 | 702 | -114 | 16 | Too tight, Inconsistent |
| Analyse Utilisateur | 0 | 8 | -1072 | 12 | Too tight, Inconsistent |
| Analyse Utilisateur | 8 | 20 | -60 | 12 | Too tight, Inconsistent |
| Analyse Utilisateur | 20 | 36 | -36 | 12 | Too tight, Inconsistent |
| Analyse Utilisateur | 36 | 92 | 24 | 12 | Inconsistent |
| Analyse Utilisateur | 92 | 144 | -52 | 12 | Too tight, Inconsistent |
| Analyse Utilisateur | 144 | 200 | 12 | 12 | OK |
| Analyse Utilisateur | 200 | 268 | 24 | 12 | Inconsistent |
| Analyse Utilisateur | 268 | 384 | -676 | 12 | Too tight, Inconsistent |
| Analyse Utilisateur | 384 | 488 | 14 | 12 | OK |
| Analyse Utilisateur | 488 | 596 | 12 | 12 | OK |
| Analyse Utilisateur | 596 | 702 | 16 | 12 | OK |
| Analyse Utilisateur | 702 | 798 | -24 | 12 | Too tight, Inconsistent |
| Analyse Utilisateur | 798 | 894 | 16 | 12 | OK |
| Detail Utilisateur | 8 | 20 | -60 | 0 | Too tight, Inconsistent |
| Detail Utilisateur | 20 | 92 | 32 | 0 | Inconsistent |
| Detail Utilisateur | 92 | 216 | 16 | 0 | Inconsistent |
| Detail Utilisateur | 216 | 332 | 16 | 0 | Inconsistent |
| Detail Utilisateur | 332 | 444 | 0 | 0 | Too tight |
| Detail Utilisateur | 444 | 460 | 0 | 0 | Too tight |

## E â€” Grille proposÃ©e et corrections
| Page | Constante | Valeur proposÃ©e |
|------|-----------|-----------------|
| Vue d'ensemble | MARGIN_TOP | 92 |
| Vue d'ensemble | MARGIN_LEFT | 300 |
| Vue d'ensemble | MARGIN_RIGHT | 16 |
| Vue d'ensemble | STANDARD_GAP_H | 16 |
| Vue d'ensemble | STANDARD_GAP_V | 16 |
| Vue d'ensemble | KPI_ROW_HEIGHT | 120 |
| Analyse Licences | MARGIN_TOP | 92 |
| Analyse Licences | MARGIN_LEFT | 300 |
| Analyse Licences | MARGIN_RIGHT | 16 |
| Analyse Licences | STANDARD_GAP_H | 16 |
| Analyse Licences | STANDARD_GAP_V | 16 |
| Analyse Licences | KPI_ROW_HEIGHT | 120 |
| Analyse Utilisateur | MARGIN_TOP | 92 |
| Analyse Utilisateur | MARGIN_LEFT | 200 |
| Analyse Utilisateur | MARGIN_RIGHT | 10 |
| Analyse Utilisateur | STANDARD_GAP_H | 16 (hors overlays) |
| Analyse Utilisateur | STANDARD_GAP_V | 12 |
| Analyse Utilisateur | KPI_ROW_HEIGHT | 104 |
| Detail Utilisateur | MARGIN_TOP | 92 |
| Detail Utilisateur | MARGIN_LEFT | 120 |
| Detail Utilisateur | MARGIN_RIGHT | 20 |
| Detail Utilisateur | STANDARD_GAP_H | 16 |
| Detail Utilisateur | STANDARD_GAP_V | 0 |
| Detail Utilisateur | KPI_ROW_HEIGHT | 108 |

### Corrections requises
| Page | Visual ID | Mesure | x actuel | y actuel | w actuel | h actuel | x proposÃ© | y proposÃ© | w proposÃ© | h proposÃ© | Raison |
|------|-----------|--------|----------|----------|----------|----------|-----------|-----------|-----------|-----------|--------|
| Vue d'ensemble | 9626e5c75f9e8f5c08ab | - | 0 | 0 | 280 | 1080 | 200 | 0 | 280 | 1080 | x<200 / conflit panneau natif |
| Vue d'ensemble | 0d0f2c648c01c1f648a7 | - | 0 | 0 | 280 | 1080 | 200 | 0 | 280 | 1080 | x<200 / conflit panneau natif |
| Vue d'ensemble | b3a44db816229d136326 | - | 20 | 16 | 240 | 56 | 200 | 16 | 240 | 56 | x<200 / conflit panneau natif |
| Vue d'ensemble | f006d16cea357fa216ad | Page:a4497031bb9f4bfb6556 | 20 | 88 | 240 | 44 | 200 | 92 | 240 | 44 | x<200 / conflit panneau natif; haut non alignÃ© Ã  la ligne |
| Vue d'ensemble | 39e489804ad79b14f1e3 | Page:54f9d470ac60b85b18da | 20 | 144 | 240 | 44 | 200 | 144 | 240 | 44 | x<200 / conflit panneau natif |
| Vue d'ensemble | fcf527b13b528b4cce49 | Page:3c4cbe0b2835dc22b7e2 | 20 | 200 | 240 | 44 | 200 | 200 | 240 | 44 | x<200 / conflit panneau natif |
| Vue d'ensemble | 7576df232a88a5e13d21 | T_Utilisateurs_Dim.WhenCreated | 20 | 268 | 240 | 100 | 200 | 268 | 240 | 100 | x<200 / conflit panneau natif |
| Vue d'ensemble | 13993fe2e745b349a9d5 | T_Utilisateurs_Dim.CountryOrRegion | 20 | 384 | 240 | 90 | 200 | 384 | 240 | 90 | x<200 / conflit panneau natif |
| Vue d'ensemble | 8ba9d0f5579e41d05b89 | T_Utilisateurs_Dim.Department | 20 | 490 | 240 | 90 | 200 | 490 | 240 | 90 | x<200 / conflit panneau natif |
| Vue d'ensemble | b2f94b5f4d87f60a7629 | T_Produits_Dim.NomProduit | 20 | 596 | 240 | 90 | 200 | 596 | 240 | 90 | x<200 / conflit panneau natif |
| Vue d'ensemble | 7cd221b2685275681dc8 | T_Produits_Dim.TypeLicence | 20 | 702 | 240 | 120 | 200 | 702 | 240 | 120 | x<200 / conflit panneau natif |
| Analyse Licences | 144feccfa5fbea4db9e4 | - | 0 | 0 | 280 | 1080 | 200 | 0 | 280 | 1080 | x<200 / conflit panneau natif |
| Analyse Licences | f47cab793550000da57d | - | 0 | 0 | 280 | 1080 | 200 | 0 | 280 | 1080 | x<200 / conflit panneau natif |
| Analyse Licences | 0db51d0a4236116c3872 | - | 20 | 16 | 240 | 56 | 200 | 16 | 240 | 56 | x<200 / conflit panneau natif |
| Analyse Licences | ed9801a6641e69784d39 | Page:a4497031bb9f4bfb6556 | 20 | 88 | 240 | 44 | 200 | 92 | 240 | 44 | x<200 / conflit panneau natif; haut non alignÃ© Ã  la ligne |
| Analyse Licences | 09d6c423bf6f0a295554 | Page:54f9d470ac60b85b18da | 20 | 144 | 240 | 44 | 200 | 144 | 240 | 44 | x<200 / conflit panneau natif |
| Analyse Licences | b2dc3498181f205c50bc | Page:3c4cbe0b2835dc22b7e2 | 20 | 200 | 240 | 44 | 200 | 200 | 240 | 44 | x<200 / conflit panneau natif |
| Analyse Licences | 3626dc072b6e376f3a86 | T_Utilisateurs_Dim.WhenCreated | 20 | 268 | 240 | 100 | 200 | 272 | 240 | 100 | x<200 / conflit panneau natif; haut non alignÃ© Ã  la ligne |
| Analyse Licences | 9be3f2f347da33375eb0 | T_Utilisateurs_Dim.CountryOrRegion | 20 | 384 | 240 | 90 | 200 | 384 | 240 | 90 | x<200 / conflit panneau natif |
| Analyse Licences | 86770fbf6fe57e94e998 | T_Utilisateurs_Dim.Department | 20 | 490 | 240 | 90 | 200 | 490 | 240 | 90 | x<200 / conflit panneau natif |
| Analyse Licences | 90319ee1bdd377ebb01a | T_Produits_Dim.NomProduit | 20 | 596 | 240 | 90 | 200 | 596 | 240 | 90 | x<200 / conflit panneau natif |
| Analyse Licences | 2e4b80c68d53a65fee7c | T_Produits_Dim.TypeLicence | 20 | 702 | 240 | 120 | 200 | 702 | 240 | 120 | x<200 / conflit panneau natif |
| Analyse Utilisateur | 321cf8d0d5d0be093468 | - | 0 | 0 | 280 | 1080 | 200 | 0 | 280 | 1080 | x<200 / conflit panneau natif |
| Analyse Utilisateur | 3a2e0f8584503a88dcbf | - | 0 | 0 | 280 | 1080 | 200 | 0 | 280 | 1080 | x<200 / conflit panneau natif |
| Analyse Utilisateur | 4ef11891f58da3f6fa5b | - | 20 | 16 | 240 | 56 | 200 | 20 | 240 | 56 | x<200 / conflit panneau natif; haut non alignÃ© Ã  la ligne |
| Analyse Utilisateur | 7b1496a23db63d581614 | Page:a4497031bb9f4bfb6556 | 20 | 88 | 240 | 44 | 200 | 92 | 240 | 44 | x<200 / conflit panneau natif; haut non alignÃ© Ã  la ligne |
| Analyse Utilisateur | 7855b7f60d52cd95b580 | Bookmark:02c501e8d87d63d0078c | 97 | 92 | 187 | 104 | 200 | 92 | 187 | 104 | x<200 / conflit panneau natif; nÃ©cessite recomposition de la ligne KPI |
| Analyse Utilisateur | 8030dbc87ab90506be3e | _Mesures.NbHumainsActifs | 97 | 92 | 187 | 104 | 200 | 92 | 187 | 104 | x<200 / conflit panneau natif; nÃ©cessite recomposition de la ligne KPI |
| Analyse Utilisateur | 0a49bad639711380db9c | Page:54f9d470ac60b85b18da | 20 | 144 | 240 | 44 | 200 | 144 | 240 | 44 | x<200 / conflit panneau natif |
| Analyse Utilisateur | 6ec49b4eb05935f1b117 | Page:3c4cbe0b2835dc22b7e2 | 20 | 200 | 240 | 44 | 200 | 200 | 240 | 44 | x<200 / conflit panneau natif |
| Analyse Utilisateur | ac1767da87f9554d5519 | T_Utilisateurs_Dim.WhenCreated | 20 | 268 | 240 | 100 | 200 | 268 | 240 | 100 | x<200 / conflit panneau natif |
| Analyse Utilisateur | a41382b807b0d8afd3a6 | T_Utilisateurs_Dim.CountryOrRegion | 20 | 384 | 240 | 90 | 200 | 384 | 240 | 90 | x<200 / conflit panneau natif |
| Analyse Utilisateur | 7998d7938a65e4cbd1cd | T_Utilisateurs_Dim.Department | 20 | 490 | 240 | 90 | 200 | 490 | 240 | 90 | x<200 / conflit panneau natif |
| Analyse Utilisateur | 78c3a585a38d21cb56a8 | T_Produits_Dim.NomProduit | 20 | 596 | 240 | 90 | 200 | 596 | 240 | 90 | x<200 / conflit panneau natif |
| Analyse Utilisateur | d8f1ebe5daefcb4ea661 | T_Produits_Dim.TypeLicence | 20 | 702 | 240 | 120 | 200 | 702 | 240 | 120 | x<200 / conflit panneau natif |
| Detail Utilisateur | ux_refresh_banner_dt | _Mesures.UX_DerniereMiseAJour | 1610 | 8 | 290 | 36 | 1510 | 8 | 290 | 36 | hors zone titre; aligner Ã  droite dans dt_title_001 |

## F â€” ProblÃ¨mes spÃ©cifiques
1. **Analyse Utilisateur â€” `NbHumainsActifs`**
   - Oui. 8030dbc87ab90506be3e est Ã  x=97, donc < 200.
   - Sous la contrainte nav native (`x >= 200`), le premier slot KPI valide est `x=200`. Avec 9 cartes sur une ligne, cela impose une recomposition complète de la rangée KPI avec un gap théorique de `3.125` px.
   - SÃ©quence KPI recomposÃ©e Ã  y=92 : 8030dbc87ab90506be3e=200, 678ebb458a124b23d8b3=390.125, ce70ef9e7866cc72b78d=580.25, b5e7555e9ed80b014183=770.375, d0f2e5dc55d345c41720=960.5, d8558517a5af0608ba18=1150.625, ce426e14c617550ccd13=1340.75, 40e7ac536e9864857177=1530.875, 0781849f42b2a3099ac6=1721.
2. **Detail Utilisateur â€” `dt_title_001` et `ux_refresh_banner_dt`**
   - dt_title_001 = (x=296, y=8, w=1504, h=72).
   - Pour rester dans la zone titre et sâ€™aligner Ã  droite sans sortir du bloc header, ux_refresh_banner_dt doit Ãªtre placÃ© Ã  (x=1510, y=8, w=290, h=36). La position actuelle (x=1610, y=8) dÃ©borde du bloc titre jusquâ€™Ã  x=1900 alors que dt_title_001 se termine Ã  x=1800.
3. **DÃ©passements globaux**
   - Visuels avec `right edge > CONTENT_END_X` : aucun
   - Visuels avec `bottom edge > canvas height` : aucun
