# M365 Power BI Dashboard (PBIP)

Tableau de bord Power BI pour le suivi des utilisateurs Microsoft 365, des licences et des risques de capacite.

## Projet actif

Le projet de travail valide est :

- `RECOVERY_UI_SAFE_V17/M365_UI.pbip`

Les copies PBIP obsoletes du root ont ete retirees pour limiter les doublons et travailler uniquement sur la base ouvrable.

## Structure

- `RECOVERY_UI_SAFE_V17/M365_UI.pbip` : point d'entree PBIP actif.
- `RECOVERY_UI_SAFE_V17/M365_UI.Report/` : pages, visuels, bookmarks, theme.
- `RECOVERY_UI_SAFE_V17/M365_UI.SemanticModel/` : modele tabulaire (TMDL), mesures DAX, relations.
- `audit/` : historique des audits et correctifs.

## Ouvrir le projet

1. Ouvrir `RECOVERY_UI_SAFE_V17/M365_UI.pbip` dans Power BI Desktop.
2. Verifier les parametres du modele dans :
   `RECOVERY_UI_SAFE_V17/M365_UI.SemanticModel/definition/expressions.tmdl`
3. S'assurer que les valeurs sensibles restent remplacees par des placeholders avant tout commit.

## Zones fonctionnelles

- **Vue d'ensemble** : KPI globaux + synthese activite.
- **Analyse Utilisateur** : segmentation comptes, drillthrough vers detail.
- **Analyse Licences** : stock, affectations, depassements, niveau de risque.
- **Detail Utilisateur** : profil 360, activite applicative, licences affectees.

## Notes

- Les secrets ne doivent jamais etre commites dans Git.
- Le drillthrough utilisateur est configure pour transmettre uniquement le contexte utilisateur.
