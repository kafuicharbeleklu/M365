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
