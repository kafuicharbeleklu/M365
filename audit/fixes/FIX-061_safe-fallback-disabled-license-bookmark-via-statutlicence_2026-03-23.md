# FIX-061 - Filtre de secours pour comptes desactives avec licence
**Date**: 2026-03-23

## Diagnostic
- Le bookmark `dacdeaf07eb2d1577049` n'appliquait plus de filtre excluant les comptes desactives sans licence.
- Une tentative de restauration du filtre visuel precis `LicencesAffectees > 0` a provoque une regression critique: ouverture en page blanche dans Power BI Desktop March 2026.
- Le besoin metier reste de rapprocher la vue du KPI `Comptes desactives avec licence` sans reintroduire la regression d'ouverture.

## Fix applique
- Ajout d'un filtre de bookmark au niveau page: `T_Utilisateurs_Dim[StatutLicence] = "ON"` dans `dacdeaf07eb2d1577049.bookmark.json`.
- Aucun filtre avance sur mesure n'a ete reintroduit.
- Le correctif conserve donc la variante d'ouverture stable du projet.

## Limites connues
- `StatutLicence` est un etat snapshot et non un calcul contextuel.
- Sous certains filtres produit, cette solution peut etre moins precise que `LicencesAffectees > 0`.
- Le filtre de mesure precis reste volontairement exclu tant qu'il n'existe pas de serialization Desktop stable.

## Resultat attendu
- Le clic sur `Comptes desactives avec licence` exclut les comptes sans licence dans le cas standard.
- Le projet continue de s'ouvrir normalement, sans retour de page blanche.
