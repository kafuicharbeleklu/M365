# FIX-058 - Decouplage des bookmarks des libelles de seuil
**Date**: 2026-03-23

## Diagnostic
- Plusieurs bookmarks P3 filtraient directement `T_Utilisateurs_Dim[EtatActivite]`.
- Le filtre critique P2 dependait du libelle texte `Stock critique <=10%`.
- Ces dependances rendaient les interactions fragiles des qu'un libelle visible changeait apres parametrage des seuils.

## Fix applique
- Ajout du champ technique cache `T_Utilisateurs_Dim[CodeEtatActivite]` avec des codes stables:
  - `ACTIF`
  - `INACTIF`
  - `JAMAIS_CONNECTE`
  - `INACTIF_M365`
  - `EXCLU`
- Refactor des mesures modele qui dependaient encore du texte `EtatActivite`:
  - `NbHumainsActifs`
  - `NbHumainsInactifs`
  - `LicencesHumainsActifs`
  - `NbInactifsM365`
  - `IsCible`
- Conversion des bookmarks P3 suivants vers `CodeEtatActivite`:
  - `Nav_HumainsActifs`
  - `Nav_HumainsInactifs`
  - `Nav_HumainsJamaisConnectes`
  - `Nav_LicencesGaspillees`
- Normalisation du libelle produit `NiveauRisqueStock` de `Stock critique <=10%` vers `Stock critique`.
- Mise a jour du bookmark `Nav_FiltreCritique` vers ce libelle stable.

## Compatibilite volontaire
- Les placeholders et visuels lies au slicer `EtatActivite` n'ont pas ete restructures.
- Les bookmarks connus a risque signales dans `AGENTS.md` n'ont pas ete modifies au-dela de ce perimetre cible.
- `T_Activite_M365` conserve encore des libelles internes legacy (`Inactif (>90j)`), mais les bookmarks refactorises n'en dependent plus.

## Resultat attendu
- Les bookmarks refactorises restent stables si le libelle visible d'inactivite change avec le seuil.
- Le filtre critique P2 ne casse plus quand le seuil critique change.
- L'UI P2 n'affiche plus un libelle faux dans le slicer de risque.
