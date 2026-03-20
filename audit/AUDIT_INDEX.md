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
