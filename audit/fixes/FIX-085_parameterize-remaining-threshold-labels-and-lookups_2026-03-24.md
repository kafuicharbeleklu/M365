# FIX-085 - Parameterize remaining threshold labels and lookups
**Date**: 2026-03-24

## Diagnostic
- Les parametres techniques existaient deja dans `expressions.tmdl` et `T_Parametres_Dim`.
- En revanche, plusieurs residus restaient semi-durs dans le modele :
  - libelles M de type `Inactif (>90j)`
  - comparaisons DAX sur ce libelle fige
  - mesures et tooltips lisant encore `T_Parametres_Dim` avec des valeurs de secours codees en dur
  - textes exposes mentionnant encore `90 jours`, `10%` ou `180 derniers jours`
- Cette situation entretenait un ecart entre parametres reels et texte/metadonnees visibles.

## Fix applique
- `T_Activite_M365` construit maintenant un libelle d'inactivite dynamique a partir de `Param_SeuilInactiviteJours`, puis le reutilise dans `NiveauUtilisation` et `CategorieActivite`.
- `T_Utilisateurs_Dim` ne compare plus `CategorieActivite` a la chaine fixe `Inactif (>90j)` ; la comparaison est maintenant reconstruite depuis le seuil courant.
- Les calculs DAX concernes lisent directement `T_Parametres_Dim` via `MAX(...)` ou `MAXX(...)` au lieu de retomber silencieusement sur `90`, `10`, `25`, `50`, `7`, `4` ou `1`.
- Les tooltips exposes ont ete rendus dynamiques pour les seuils d'inactivite, le seuil critique stock et la periode d'activite.
- La synonymie culture `fr-FR` ne mentionne plus `inactifs 90 jours`.

## Resultat attendu
- Le seuil d'inactivite visible s'adapte au parametre sans desalignement entre M, DAX et tooltips.
- Les mentions de seuil critique stock s'alignent sur `SeuilStockCritiquePct`.
- Le texte relatif aux utilisateurs fantomes suit `PeriodeActivite` au lieu de rester fige sur `180 jours`.

## Validation manuelle requise
- Ouvrir le projet dans Power BI Desktop.
- Rafraichir le modele.
- Verifier que `T_Activite_M365` se charge sans erreur.
- Verifier que les labels `Inactif` et les tooltips sur `Analyse Utilisateur` et `Analyse Licences` refletent bien les valeurs parametrees.
