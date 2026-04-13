# Audit Index â€” M365 Dashboard

This folder tracks all audits and fixes performed on the M365_UI.pbip project.
Each file follows the naming convention: `{TYPE}-{NNN}_{subject}_{YYYY-MM-DD}.md`

Types: BL (Business Logic) | UI (UI Layout) | DQ (Data Quality) | FIX (Fix Record)

## Registry

| ID | Type | Subject | Date | Status |
|----|------|---------|------|--------|
| BL-001 | Business Logic | CohÃ©rence des mesures utilisateurs et licences | 2026-03-20 | âœ… RÃ©solu â€” IC-004 seul en attente dÃ©cision Ã©quipe |
| FIX-001 | Fix | Correction NbHumainsJamaisConnectes + NbUtilisateursFantomes | 2026-03-20 | âœ… AppliquÃ© |
| UI-001 | UI Layout | Chevauchements visuels Vue d'ensemble | 2026-03-20 | âœ… RÃ©solu â€” dÃ©salignement pixel corrigÃ© |
| FIX-002 | Fix | Tooltips FantÃ´mes vs Jamais ConnectÃ©s | 2026-03-20 | âœ… AppliquÃ© |
| DQ-001 | Data Quality | Gaps jointure + TypeCompte + population Exclu | 2026-03-20 | âœ… RÃ©solu â€” Exchange niveau 2 en attente lundi |
| FIX-003 | Fix | RÃ©Ã©criture CiblesNettoyage via IsCible | 2026-03-20 | âœ… AppliquÃ© |
| FIX-004 | Fix | Bornage patterns TypeCompte risquÃ©s | 2026-03-20 | âœ… AppliquÃ© |
| FIX-005 | Fix | Bandeau MAJ toutes pages | 2026-03-20 | âœ… AppliquÃ© |
| UI-002 | UI Layout | Audit UI complet | 2026-03-20 | âœ… RÃ©solu â€” corrections appliquÃ©es |
| FIX-006 | Fix | Corrections UI boutons mismatches disclaimer | 2026-03-20 | âœ… AppliquÃ© |
| FIX-007 | Fix | Layout nav panel + header banner | 2026-03-20 | âœ… AppliquÃ© |
| UI-003 | UI Layout | Audit layout pixel-perfect | 2026-03-20 | âœ… RÃ©solu â€” grille pixel-perfect appliquÃ©e |
| FIX-008 | Fix | Layout pixel-perfect KPI row + header | 2026-03-20 | âœ… AppliquÃ© |
| FIX-009 | Fix | Restructuration layout Analyse Utilisateur | 2026-03-20 | âœ… AppliquÃ© |
| FIX-010 | Fix | Alignement hauteur tableau/action cards | 2026-03-20 | âœ… AppliquÃ© |
| FIX-011 | Fix | Extension canvas action cards + tableau | 2026-03-20 | âœ… AppliquÃ© |
| FIX-012 | Fix | Dimensionnement dÃ©finitif Analyse Utilisateur | 2026-03-20 | âœ… AppliquÃ© |
| FIX-013 | Fix | Smart filters + nav spacing + UI polish | 2026-03-20 | âœ… AppliquÃ© |
| FIX-014 | Fix | Correction schÃ©ma bookmark Nav_UsersProduitsDepassement | 2026-03-21 | âœ… AppliquÃ© |
| FIX-015 | Fix | Smart filters + nav spacing + DT refonte | 2026-03-21 | ? Appliqué |
| FIX-016 | Fix | Header alignment + nav spacing | 2026-03-21 | ? Appliqué |
| FIX-017 | Fix | Filtres persistants + titres + Detail polish | 2026-03-21 | ? Appliqué |
| FIX-018 | Fix | DT header + spacing + filtre désactivés | 2026-03-21 | ? Appliqué |
| FIX-019 | Fix | Detail Utilisateur layout final | 2026-03-21 | ? Appliqué |
| FIX-020 | Fix | Header reset alignment 3 pages | 2026-03-21 | âœ… AppliquÃ© |
| FIX-021 | Fix | Harmonisation espacement global | 2026-03-21 | âœ… AppliquÃ© |
| FIX-022 | Fix | Filtre dÃ©sactivÃ©s avec licence â€” LicencesAffectees>0 | 2026-03-21 | âœ… AppliquÃ© |
| FIX-040 | Fix | Reactivation minimale des bookmarks legacy P3 sur recovery V6 | 2026-03-23 | ? Appliqué |
| FIX-041 | Fix | Reactivation uniquement de Nav_UsersProduitsDepassement sur recovery V7 | 2026-03-23 | ? Appliqué |
| FIX-042 | Fix | Reactivation uniquement du filtre critique P2 sur recovery V8 | 2026-03-23 | ? Appliqué |
| FIX-043 | Fix | Reactivation uniquement du filtre depassement P2 sur recovery V9 | 2026-03-23 | ? Appliqué |
| FIX-044 | Fix | Reactivation uniquement du filtre epuise P2 sur recovery V10 | 2026-03-23 | ? Appliqué |
| FIX-045 | Fix | Reactivation uniquement du reset P2 sur recovery V11 | 2026-03-23 | ? Appliqué |
| FIX-046 | Fix | Reactivation uniquement du reset P1 sur recovery V12 | 2026-03-23 | ? Appliqué |
| FIX-047 | Fix | Reactivation uniquement du reset drillthrough sur recovery V13 | 2026-03-23 | ? Appliqué |
| FIX-048 | Fix | Reactivation de Nav_HumainsActifs avec bookmark corrige sur recovery V14 | 2026-03-23 | ? Appliqué |
| FIX-049 | Fix | Reactivation de Nav_TechniquesActives avec bookmark corrige sur recovery V15 | 2026-03-23 | ? Appliqué |
| FIX-050 | Fix | Reactivation de Nav_TechniquesInactives avec bookmark corrige sur recovery V16 | 2026-03-23 | ? Appliqué |
| FIX-051 | Fix | Reactivation de Nav_UtilisateursFantomes avec bookmark corrige sur recovery V17 | 2026-03-23 | ? Appliqué |
| FIX-052 | Fix | Finalisation de V17 comme baseline recovery interactive complete | 2026-03-23 | ? Appliqué |
| FIX-053 | Fix | Promotion de V17 comme baseline root et purge des artefacts .pbi locaux | 2026-03-23 | ? Appliqué |
| FIX-054 | Fix | Refactor workspace autour de V17 et suppression des doublons PBIP obsoletes | 2026-03-23 | ? Appliqué |
| FIX-055 | Fix | Export de V17 vers le root et nettoyage du workspace | 2026-03-23 | ? Appliqué |
| FIX-056 | Fix | Redaction des credentials Git et parametrage des seuils metier | 2026-03-23 | ? Appliqué |
| FIX-057 | Fix | Alignement des libelles UI avec les seuils parametrables | 2026-03-23 | ? Appliqué |
| FIX-058 | Fix | Decouplage des bookmarks des libelles de seuil | 2026-03-23 | ? Appliqué |
| FIX-059 | Fix | Clarification du bandeau de contexte pour les comptes desactives avec licence | 2026-03-23 | ? Appliqué |
| FIX-061 | Fix | Filtre de secours desactives avec licence via StatutLicence=ON | 2026-03-23 | ? Appliqué |
| FIX-062 | Fix | Indicateur cache desactives avec licence pour bookmark stable | 2026-03-23 | ? Appliqué |
| FIX-063 | Fix | Filtrage explicite par UPN pour les comptes desactives avec licence | 2026-03-23 | ? Appliqué |
| FIX-064 | Fix | Alignement du bookmark desactives avec licence sur StatutLicence='ON' | 2026-03-23 | ? Appliqué |
| FIX-065 | Fix | Liaison des bookmarks P3 humains aux segments visibles | 2026-03-23 | ? Appliqué |

| FIX-066 | Fix | Bookmark dedie pour le KPI comptes desactives avec licence | 2026-03-23 | ? Appliqué |
| BL-002 | Business Logic | Audit coherence KPI -> bouton -> bookmark | 2026-03-23 | ? Audité |
| FIX-067 | Fix | Reparation de Signet 12 pour le KPI Désactivés | 2026-03-23 | ? Appliqué |
| BL-003 | Business Logic | Verification HEAD des liaisons bouton -> bookmark | 2026-03-24 | ? Audité |
| FIX-068 | Fix | Nettoyage des bookmarks legacy non appeles | 2026-03-24 | ? Appliqué |
| FIX-069 | Fix | Restauration de l'etat des segments visibles pour le KPI comptes desactives avec licence | 2026-03-24 | ? Appliqué |
| FIX-070 | Fix | Restauration de la navigation KPI P1 et du bouton P3 comptes desactives avec licence | 2026-03-24 | ? Appliqué |
| FIX-071 | Fix | Verrouillage du bookmark comptes desactives avec licence sur le tableau cible | 2026-03-24 | ? Appliqué |
| FIX-072 | Fix | Exposition de StatutLicence comme filtre de page sur Analyse Utilisateur | 2026-03-24 | ? Appliqué |
| FIX-073 | Fix | Realignement des bookmarks humains Actifs/Inactifs avec le filtre visible EtatActivite | 2026-03-24 | ? Appliqué |
| FIX-074 | Fix | Exposition de NiveauRisqueStock comme filtre de page sur Analyse Utilisateur | 2026-03-24 | ? Appliqué |
| FIX-075 | Fix | Alignement des bookmarks P2 de risque avec le filtre visible NiveauRisqueStock | 2026-03-24 | ? Appliqué |
| FIX-076 | Fix | Alignement des KPI utilisateurs avec des comptes distincts sur Analyse Utilisateur | 2026-03-24 | ? Appliqué |
| BL-004 | Business Logic | Revue architecture extraction -> modele -> mesures -> report | 2026-03-24 | ? Audité |
| FIX-077 | Fix | Organisation des mesures partagees par dossiers metier | 2026-03-24 | ? Appliqué |
| FIX-078 | Fix | Factorisation de l'auth Graph dans une expression Power Query partagee | 2026-03-24 | ? Appliqué |
| FIX-079 | Fix | Deduplication du nombre de licences par utilisateur dans une colonne cachee | 2026-03-24 | ? Appliqué |
| FIX-080 | Fix | Redaction des credentials Graph locaux avant commit | 2026-03-24 | ? Appliqué |
| FIX-081 | Fix | Faire de EtatActivite un libelle derive de CodeEtatActivite | 2026-03-24 | ? Appliqué |
| FIX-082 | Fix | Refactor TypeCompte en colonne de regle diagnostique + sortie fine | 2026-03-24 | ? Appliqué |
| FIX-083 | Fix | Suppression des mesures partagees clairement sans usage dans _Mesures | 2026-03-24 | ? Appliqué |
| FIX-084 | Fix | Decouplage de T_Affectations_Fact via une expression partagee users base | 2026-03-24 | ? Appliqué |
| FIX-085 | Fix | Parametrage des derniers libelles et comparaisons de seuils | 2026-03-24 | ? Appliqué |
| FIX-086 | Fix | Mise a jour des notes AGENTS sur seuils et bookmarks apres audit source | 2026-03-24 | ? Appliqué |
| FIX-087 | Fix | Suppression des mesures tooltip P2 orphelines et cloture de l'alerte doc | 2026-03-24 | ? Appliqué |
| FIX-088 | Fix | Exposition des parametres actifs dans le header des pages principales | 2026-03-25 | ? Appliqué |
| FIX-089 | Fix | Ajout d'un signal global de qualite des donnees dans le bandeau de parametres actifs | 2026-03-25 | ? Appliqué |
| FIX-090 | Fix | Exposition de la regle diagnostique TypeCompte sur le drillthrough utilisateur | 2026-03-25 | ? Appliqué |
| FIX-091 | Fix | Ajout d'un controle pre-commit gere par le repo pour les secrets de expressions.tmdl | 2026-03-25 | ? Appliqué |
| FIX-092 | Fix | Refonte des tooltips P3 et liaison des cartes d'action a des report-page tooltips | 2026-03-25 | ? Appliqué |
| FIX-093 | Fix | Deplacement du hover P3 sur les boutons transparents et compactage global des tooltips | 2026-03-25 | ? Appliqué |
| FIX-094 | Fix | Reduction supplementaire des tooltips et reecriture du contenu P1 | 2026-03-25 | ? Appliqué |
| FIX-095 | Fix | Uniformisation du mode tooltip des KPI P1 et compactage specifique des tooltips P1 | 2026-03-25 | ? Appliqué |
| FIX-096 | Fix | Uniformisation du mode tooltip des KPI P2 et compactage des tooltips P2 | 2026-03-25 | ? Appliqué |
| FIX-097 | Fix | Compactage des tooltips P3 et routage du hover des KPI hauts via boutons overlay | 2026-03-25 | ? Appliqué |
| FIX-098 | Fix | Deplacement du clic bookmark P3 sur les cartes pour eviter le hover natif CTRL+click | 2026-03-25 | ? Appliqué |
| FIX-099 | Fix | Ajout d'un tooltip dedie pour la carte Total de la page 3 | 2026-03-25 | ? Appliqué |
| FIX-100 | Fix | Harmonisation des tailles de titres de sections dans les tooltips et suppression des bordures arrondies sur les pages principales | 2026-03-25 | ? Appliqué |
| FIX-101 | Fix | Espacement accru des sections du nav lateral, suppression des arrondis du drillthrough et augmentation des polices KPI | 2026-03-25 | ? Appliqué |
| FIX-102 | Fix | Renommage du KPI Cibles Nettoyage et refonte visuelle des tooltips ttv_* | 2026-03-25 | ? Appliqué |
| FIX-103 | Fix | Augmentation des tailles de titres KPI et correction du titre Desactives sur la page 3 | 2026-03-25 | ? Appliqué |
| FIX-104 | Fix | Ajout d'une recherche utilisateur sur la page 3 et alignement du libelle Utilisateurs Désactivés | 2026-03-25 | ? Appliqué |
| FIX-105 | Fix | Preservation du contexte des slicers P3 lors de l'application des bookmarks KPI | 2026-03-25 | ? Applique |
| FIX-106 | Fix | Remplacement des KPI cliquables P3 par un panneau de segments d'analyse a droite | 2026-03-25 | ? Applique |
| FIX-107 | Fix | Realignement du tableau P3 sur le grain produit de T_Affectations_Fact pour eliminer les lignes a 0 sous filtre produit | 2026-03-25 | ? Appliqué |
| FIX-108 | Fix | Restauration d'une logique utilisateur pour Licences Actives/Inactives et scope produit sur les KPI techniques P3 | 2026-03-25 | ? Appliqué |
| FIX-109 | Fix | Clarification des tooltips Licences Inactives et Comptes a traiter | 2026-03-26 | Applique |
| FIX-110 | Fix | Remplacement de l'alerte depassement P3 par Jamais connectes et resserrement du panneau d'alerte | 2026-03-26 | Applique |
| FIX-111 | Fix | Compactage du panneau d alertes P3 et agrandissement des segments | 2026-03-26 | Applique |
| FIX-112 | Fix | Recalage du hover des alertes P3 et correction du KPI desactives | 2026-03-26 | Applique |


| FIX-113 | Fix | Suppression de l alerte dupliquee desactives avec licence et alignement des tooltips P3 | 2026-03-26 | Applique |
| FIX-114 | Fix | Ancrage du tableau P3 sur les affectations et masquage des lignes de licence a 0 | 2026-03-26 | Applique |
| FIX-115 | Fix | Affinage du tableau P3 de licences consommees apres reutilisation du visuel drillthrough | 2026-03-26 | Applique |
| FIX-116 | Fix | Restauration du surlignage d alerte du tableau P3 pour comptes desactives et inactifs sous licence | 2026-03-26 | Applique |

| FIX-117 | Fix | Clarification de lecture des KPI P3 comptes vs licences et renommage du total humain | 2026-04-07 | Applique |