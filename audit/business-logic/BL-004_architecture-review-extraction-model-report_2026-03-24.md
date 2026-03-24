# BL-004 - Revue architecture extraction -> modele -> mesures -> report
**Date**: 2026-03-24
**Statut**: Audite
**Perimetre**: `expressions.tmdl`, `T_Utilisateurs_Dim.tmdl`, `T_Produits_Dim.tmdl`, `T_Affectations_Fact.tmdl`, `_Mesures.tmdl`, `M365_UI.Report/definition`

## Resume executif
La structure generale du projet est exploitable, mais elle s'est complexifiee autour de trois zones:
- la logique d'extraction Graph est dupliquee dans plusieurs requetes Power Query
- la logique metier d'activite utilisateur est calculee a la fois en colonnes et reconsommee en DAX
- le stock de mesures est devenu trop dense pour etre maintenu sereinement sans classement ni purge

Le projet n'a pas un probleme unique de "mauvais calcul", mais un probleme de repartition de responsabilites entre extraction, modele semantique et report.

## Findings

### 1. Risque critique de securite dans `expressions.tmdl`
- Les parametres `Param_TenantId`, `Param_ClientId` et `Param_Secret` contiennent actuellement de vraies valeurs dans le working tree local.
- C'est un risque de fuite immediate si un commit ou un export est fait en l'etat.
- Ce point doit etre corrige avant tout commit, meme si aucun refactoring fonctionnel n'est fait.

### 2. Couplage fort entre extraction utilisateurs et fait licences
- `T_Affectations_Fact` est derivee de `T_Utilisateurs_Dim[Licences_Brutes]`, pas d'une source d'affectation autonome.
- Cela simplifie l'obtention d'un snapshot courant, mais couple le fait licences a la forme interne de la dimension utilisateurs.
- Consequence: toute evolution de l'extraction utilisateurs peut avoir un effet de bord sur le fait licences.

### 3. Duplication de logique metier sur l'activite
- `EtatActivite` et `CodeEtatActivite` recalculent quasiment la meme logique metier avec deux sorties differentes: label visible et code stable.
- Le besoin UI justifie les deux representations, mais pas la duplication integrale de la formule.
- La maintenance est fragile: un changement oublie dans l'une des deux colonnes recree des incoherences entre KPI, filtres et bookmarks.

### 4. `TypeCompte` reste la zone la plus fragile du modele
- La colonne combine un bon signal primaire (`UserType`, `#EXT#`) avec un grand nombre de heuristiques `CONTAINSSTRING`.
- Meme apres les bornages precedents, cette logique reste sensible aux faux positifs et difficile a faire evoluer proprement.
- C'est une logique de classification qui devrait a terme etre externalisee ou au minimum gouvernee comme une table de regles.

### 5. `_Mesures.tmdl` concentre trop de responsabilites
- 122 mesures sont centralisees dans un seul fichier.
- 82 mesures sont referencees directement dans le report.
- 40 mesures ne sont pas referencees par le report.
- 37 mesures n'ont ni reference directe dans le report ni dependance detectee dans les autres mesures.
- Le fichier melange KPI metier, mesures UX, tooltips, detail, diagnostic et reliquats de tests.

### 6. Duplication de pattern DAX sur le scope produit
- Le pattern `ISCROSSFILTERED(T_Produits_Dim)` + `TREATAS(VALUES(T_Affectations_Fact[UserPrincipalName]))` est repete sur plusieurs KPI utilisateurs.
- Cette repetition rend les evolutions lentes et augmente le risque de divergence de comportement entre KPI voisins.
- Sans calculation group ni table canonique intermediaire, il n'y a pas de mutualisation propre aujourd'hui.

### 7. Le report est moins le probleme que le symptome
- Le report est fortement pilote par cartes, slicers et bookmarks, avec 15 bookmarks actifs et une densite importante de cartes.
- Les incidents recents venaient surtout d'un decalage entre champs caches, champs visibles et mesures branchees, pas d'un schema visuel fondamentalement mauvais.
- Les pages principales restent relativement simples en nombre de visuels: 38, 32 et 29 pour les trois pages majeures.

## Evaluation par couche

### Extraction
- Point fort: les parametres metier existent et couvrent deja plusieurs seuils.
- Point faible: authentification Graph dupliquee, mapping produit code en dur, classification partiellement poussee trop tot.

### Modele
- Point fort: schema metier lisible autour de `T_Utilisateurs_Dim`, `T_Produits_Dim`, `T_Affectations_Fact`, `T_Activite_M365`.
- Point faible: `T_Affectations_Fact` n'est pas un vrai fait independant, et la logique d'activite est repartie entre colonnes calculees paralleles.

### Mesures
- Point fort: les KPI essentiels existent et les plus critiques sont maintenant alignes.
- Point faible: densite trop forte, faible classement, presence de reliquats morts, et duplication de patterns.

### Report
- Point fort: interactions principales recuperables et maintenant plus coherentes.
- Point faible: dependance historique forte aux bookmarks pour porter de la logique de filtre.

## Recommandations
1. Securiser immediatement `expressions.tmdl` avant tout commit.
2. Refactoriser l'organisation des mesures sans toucher aux calculs comme premiere passe sure.
3. Ouvrir une passe dediee de suppression/archivage des mesures mortes apres validation Desktop.
4. Extraire a terme la logique Graph commune dans des fonctions M partagees.
5. Repenser `TypeCompte` comme une classification gouvernee, pas seulement codee en dur.
6. A moyen terme, unifier la logique `EtatActivite`/`CodeEtatActivite` autour d'un noyau canonique unique.
