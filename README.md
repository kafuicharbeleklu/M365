# M365 Power BI Dashboard (PBIP)

Tableau de bord Power BI pour le suivi des utilisateurs Microsoft 365, des licences et des risques de capacite.

## Projet actif

Le projet de travail valide est :

- `M365_UI.pbip`

La baseline validee de `RECOVERY_UI_SAFE_V17` a ete promue au root pour travailler sur un seul chemin projet.

## Structure

- `M365_UI.pbip` : point d'entree PBIP actif.
- `M365_UI.Report/` : pages, visuels, bookmarks, theme.
- `M365_UI.SemanticModel/` : modele tabulaire (TMDL), mesures DAX, relations.
- `audit/` : historique des audits et correctifs.

## Ouvrir le projet

1. Ouvrir `M365_UI.pbip` dans Power BI Desktop.
2. Verifier les parametres du modele dans :
   `M365_UI.SemanticModel/definition/expressions.tmdl`
3. S'assurer que les valeurs sensibles restent remplacees par des placeholders avant tout commit.

## Zones fonctionnelles

- **Vue d'ensemble** : KPI globaux + synthese activite.
- **Analyse Utilisateur** : segmentation comptes, drillthrough vers detail.
- **Analyse Licences** : stock, affectations, depassements, niveau de risque.
- **Detail Utilisateur** : profil 360, activite applicative, licences affectees.

## Notes

- Les secrets ne doivent jamais etre commites dans Git.
- Le drillthrough utilisateur est configure pour transmettre uniquement le contexte utilisateur.

## Garde-fou pre-commit

- Un hook repo-managed est disponible dans `.githooks/pre-commit`.
- Pour l'activer localement dans ce workspace :
  `powershell -ExecutionPolicy Bypass -File scripts/install-git-hooks.ps1`
- Le hook controle la version stagee de `M365_UI.SemanticModel/definition/expressions.tmdl`
  et bloque le commit si `Param_TenantId`, `Param_ClientId` ou `Param_Secret`
  ne sont pas des placeholders du type `__...__`.
