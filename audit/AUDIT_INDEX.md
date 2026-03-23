# Audit Index — M365 Dashboard

This folder tracks all audits and fixes performed on the M365_UI.pbip project.
Each file follows the naming convention: `{TYPE}-{NNN}_{subject}_{YYYY-MM-DD}.md`

Types: BL (Business Logic) | UI (UI Layout) | DQ (Data Quality) | FIX (Fix Record)

## Registry

| ID | Type | Subject | Date | Status |
|----|------|---------|------|--------|
| BL-001 | Business Logic | Cohérence des mesures utilisateurs et licences | 2026-03-20 | ✅ Résolu — IC-004 seul en attente décision équipe |
| FIX-001 | Fix | Correction NbHumainsJamaisConnectes + NbUtilisateursFantomes | 2026-03-20 | ✅ Appliqué |
| UI-001 | UI Layout | Chevauchements visuels Vue d'ensemble | 2026-03-20 | ✅ Résolu — désalignement pixel corrigé |
| FIX-002 | Fix | Tooltips Fantômes vs Jamais Connectés | 2026-03-20 | ✅ Appliqué |
| DQ-001 | Data Quality | Gaps jointure + TypeCompte + population Exclu | 2026-03-20 | ✅ Résolu — Exchange niveau 2 en attente lundi |
| FIX-003 | Fix | Réécriture CiblesNettoyage via IsCible | 2026-03-20 | ✅ Appliqué |
| FIX-004 | Fix | Bornage patterns TypeCompte risqués | 2026-03-20 | ✅ Appliqué |
| FIX-005 | Fix | Bandeau MAJ toutes pages | 2026-03-20 | ✅ Appliqué |
| UI-002 | UI Layout | Audit UI complet | 2026-03-20 | ✅ Résolu — corrections appliquées |
| FIX-006 | Fix | Corrections UI boutons mismatches disclaimer | 2026-03-20 | ✅ Appliqué |
| FIX-007 | Fix | Layout nav panel + header banner | 2026-03-20 | ✅ Appliqué |
| UI-003 | UI Layout | Audit layout pixel-perfect | 2026-03-20 | ✅ Résolu — grille pixel-perfect appliquée |
| FIX-008 | Fix | Layout pixel-perfect KPI row + header | 2026-03-20 | ✅ Appliqué |
| FIX-009 | Fix | Restructuration layout Analyse Utilisateur | 2026-03-20 | ✅ Appliqué |
| FIX-010 | Fix | Alignement hauteur tableau/action cards | 2026-03-20 | ✅ Appliqué |
| FIX-011 | Fix | Extension canvas action cards + tableau | 2026-03-20 | ✅ Appliqué |
| FIX-012 | Fix | Dimensionnement définitif Analyse Utilisateur | 2026-03-20 | ✅ Appliqué |
| FIX-013 | Fix | Smart filters + nav spacing + UI polish | 2026-03-20 | ✅ Appliqué |
| FIX-014 | Fix | Correction schéma bookmark Nav_UsersProduitsDepassement | 2026-03-21 | ✅ Appliqué |
| FIX-015 | Fix | Smart filters + nav spacing + DT refonte | 2026-03-21 | ? Appliqu� |
| FIX-016 | Fix | Header alignment + nav spacing | 2026-03-21 | ? Appliqu� |
| FIX-017 | Fix | Filtres persistants + titres + Detail polish | 2026-03-21 | ? Appliqu� |
| FIX-018 | Fix | DT header + spacing + filtre d�sactiv�s | 2026-03-21 | ? Appliqu� |
| FIX-019 | Fix | Detail Utilisateur layout final | 2026-03-21 | ? Appliqu� |
| FIX-020 | Fix | Header reset alignment 3 pages | 2026-03-21 | ✅ Appliqué |
| FIX-021 | Fix | Harmonisation espacement global | 2026-03-21 | ✅ Appliqué |
| FIX-022 | Fix | Filtre désactivés avec licence — LicencesAffectees>0 | 2026-03-21 | ✅ Appliqué |
| FIX-040 | Fix | Reactivation minimale des bookmarks legacy P3 sur recovery V6 | 2026-03-23 | ? Appliqu� |
| FIX-041 | Fix | Reactivation uniquement de Nav_UsersProduitsDepassement sur recovery V7 | 2026-03-23 | ? Appliqu� |
| FIX-042 | Fix | Reactivation uniquement du filtre critique P2 sur recovery V8 | 2026-03-23 | ? Appliqu� |
| FIX-043 | Fix | Reactivation uniquement du filtre depassement P2 sur recovery V9 | 2026-03-23 | ? Appliqu� |
| FIX-044 | Fix | Reactivation uniquement du filtre epuise P2 sur recovery V10 | 2026-03-23 | ? Appliqu� |
| FIX-045 | Fix | Reactivation uniquement du reset P2 sur recovery V11 | 2026-03-23 | ? Appliqu� |
| FIX-046 | Fix | Reactivation uniquement du reset P1 sur recovery V12 | 2026-03-23 | ? Appliqu� |
| FIX-047 | Fix | Reactivation uniquement du reset drillthrough sur recovery V13 | 2026-03-23 | ? Appliqu� |
| FIX-048 | Fix | Reactivation de Nav_HumainsActifs avec bookmark corrige sur recovery V14 | 2026-03-23 | ? Appliqu� |
| FIX-049 | Fix | Reactivation de Nav_TechniquesActives avec bookmark corrige sur recovery V15 | 2026-03-23 | ? Appliqu� |
| FIX-050 | Fix | Reactivation de Nav_TechniquesInactives avec bookmark corrige sur recovery V16 | 2026-03-23 | ? Appliqu� |
| FIX-051 | Fix | Reactivation de Nav_UtilisateursFantomes avec bookmark corrige sur recovery V17 | 2026-03-23 | ? Appliqu� |
| FIX-052 | Fix | Finalisation de V17 comme baseline recovery interactive complete | 2026-03-23 | ? Appliqu� |
| FIX-053 | Fix | Promotion de V17 comme baseline root et purge des artefacts .pbi locaux | 2026-03-23 | ? Appliqu� |
| FIX-054 | Fix | Refactor workspace autour de V17 et suppression des doublons PBIP obsoletes | 2026-03-23 | ? Appliqu� |
| FIX-055 | Fix | Export de V17 vers le root et nettoyage du workspace | 2026-03-23 | ? Appliqu� |
| FIX-056 | Fix | Redaction des credentials Git et parametrage des seuils metier | 2026-03-23 | ? Appliqu� |
| FIX-057 | Fix | Alignement des libelles UI avec les seuils parametrables | 2026-03-23 | ? Appliqu� |
