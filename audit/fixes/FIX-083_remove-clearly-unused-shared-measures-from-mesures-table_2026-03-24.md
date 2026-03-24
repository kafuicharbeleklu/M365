# FIX-083 - Remove clearly unused shared measures from _Mesures
**Date**: 2026-03-24

## Diagnostic
- `_Mesures.tmdl` contenait encore un stock de mesures sans aucune reference detectee ni dans le report, ni dans les autres mesures.
- Ces mesures mortes rendaient la table partagee plus difficile a lire et entretenaient des familles de logique non materialisees dans le report:
  - legacy E3 (`UsersOffice365E3`, `UsersMicrosoft365E3`, `UsersAvecLesDeuxE3`)
  - surcapacite legacy (`DepassementCapacite`, `DepassementCapaciteFlag`, `UX_BandeauRisqueLicences`)
  - detail produit non materialise (`DT_Produit_*`)
  - historique utilisateur non materialise (`DT_Historique_*`)
  - adoption non exposee (`NbUtilisateursStandards`, `NbUtilisateursMinimaux`, `NbNonUtilisateurs`, `ScoreMoyenUtilisation`, `TauxAdoptionWord`, `TauxAdoptionExcel`, `TauxAdoptionPowerPoint`, `TauxAdoptionOneNote`, `TauxUtilisationWindows`, `TauxUtilisationMac`, `TauxUtilisationMobile`, `TauxUtilisationWeb`)
  - legacy licence bloquee (`LicencesComptesBloques`)

## Fix applique
- Suppression de 24 mesures clairement mortes dans `M365_UI.SemanticModel/definition/tables/_Mesures.tmdl`.
- Nettoyage des commentaires et annotations orphelins laisses par ces suppressions pour garder un TMDL coherent.
- Correction post-validation de deux annotations `SummarizationSetBy` orphelines qui provoquaient l'erreur Desktop `TMDL objects cannot be merged because both declare the same property: value`.
- Conservation explicite de `NbLignesNonClassifiees`, car c'est une mesure de diagnostic utile.
- Conservation explicite des `TT_p2_critique_*`, `TT_p2_epuise_*`, `TT_p2_depassement_*` et `TT_p2_risque_*`, car `AGENTS.md` les signale comme code mort connu a traiter explicitement et non a supprimer silencieusement.

## Resultat attendu
- `_Mesures.tmdl` passe de 122 a 98 mesures.
- La table partagee est plus lisible et le stock de logique non branchee est reduit.
- Le prochain nettoyage pourra se concentrer sur les cas restants connus et assumes (`TT_p2_*`) ou sur des diagnostics volontairement conserves.

## Validation manuelle requise
- Rafraichir le modele dans Power BI Desktop.
- Verifier que les pages `Analyse Utilisateur`, `Analyse Licences`, `Analyse Globale` et le drillthrough utilisateur restent fonctionnels.
- Verifier que les tooltips P1, P2 et P3 encore exposes s'affichent toujours correctement.
