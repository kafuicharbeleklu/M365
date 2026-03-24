# FIX-077 - Organisation des mesures partagees par dossiers metier
**Date**: 2026-03-24

## Diagnostic
- `_Mesures.tmdl` concentre 122 mesures dans un seul fichier.
- Une partie importante des mesures partagees n'avait pas de `displayFolder`, ce qui rendait la lecture du modele confuse dans Power BI Desktop.
- Le probleme etait principalement structurel et de maintenabilite, pas un bug de calcul.

## Fix applique
- Ajout de `displayFolder` coherents sur les mesures partagees non classees.
- Dossiers introduits ou renforces:
  - `Comptes`
  - `Utilisateurs`
  - `Comptes Techniques`
  - `Licences`
  - `Adoption`
  - `Diagnostic`
- Aucune formule DAX n'a ete modifiee dans cette passe.

## Resultat attendu
- Le modele devient plus lisible dans Power BI Desktop.
- Les mesures metier, techniques et d'adoption sont mieux separees.
- Cette passe prepare un futur nettoyage des mesures mortes sans changer le comportement fonctionnel du report.
