# DQ-001 — Qualité TypeCompte, population Exclu, périmètre CiblesNettoyage
**Date**: 2026-03-20
**Statut**:  En cours
**Périmètre**: T_Utilisateurs_Dim, _Mesures.tmdl

## A — Analyse faux positifs TypeCompte
### Règles à risque (par pattern)

Contexte de lecture : dans `TypeCompte`, `Nom = LOWER(COALESCE([DisplayName], ""))` et `Email = LOWER(COALESCE([UserPrincipalName], ""))`. Les 5 règles demandées ciblent donc toutes `DisplayName` uniquement, pas `UserPrincipalName`.

| Pattern | Règle DAX exacte | Cible | Peut matcher un humain réel ? | Analyse |
|---------|------------------|-------|-------------------------------|---------|
| `service` | `CONTAINSSTRING(Nom, "service"), "Technique",` | `DisplayName` | Oui | Peut capturer un intitulé métier ou d'organisation : `Service client`, `Service achats`, `Chef de service`. |
| `formation` | `CONTAINSSTRING(Nom, "formation"), "Technique",` | `DisplayName` | Oui | Peut matcher une fonction RH / L&D ou un libellé de service porté par un humain. |
| `admin` | `CONTAINSSTRING(Nom, "admin"), "Technique",` | `DisplayName` | Oui | Très large : peut matcher `Administration`, `Administratif`, `Admin RH`, donc des comptes humains. |
| `test` | `CONTAINSSTRING(Nom, "test"), "Technique",` | `DisplayName` | Oui | Risque lexical élevé car sous-chaîne non bornée. Exemple : `Atestou` ou tout patronyme contenant `test`. |
| `visit` | `CONTAINSSTRING(Nom, "visit"), "Technique",` | `DisplayName` | Oui | Peut matcher des noms/prénoms ou labels de type `Visit`, `Visitor`, `Visitacion`. |

Répartition de risque estimée :
- `admin` et `service` sont les plus susceptibles de sur-classer des humains via des intitulés d'équipe ou de fonction.
- `test` est le plus fragile techniquement car il n'a aucune borne de mot.
- `formation` et `visit` sont moins fréquents mais restent non fiables comme signal autonome.

Peut-on compter les faux positifs réels dans les données ?
- Oui, mais uniquement sur un modèle rafraîchi, pas depuis les fichiers PBIP seuls.
- Il faut rejouer la logique `TypeCompte` dans une requête diagnostique DAX ou Power Query, avec :
  - 5 flags pour les patterns à risque,
  - 1 flag `AutreRegle` couvrant les 127 autres règles,
  - un filtre final sur les lignes où une seule des 5 règles vaut `TRUE()` et `AutreRegle = FALSE()`.
- Le dépôt source ne contient pas de snapshot de données, donc aucun comptage réel n'est dérivable ici.

Exemple de pattern de requête sur modèle rafraîchi :

```dax
EVALUATE
FILTER(
    ADDCOLUMNS(
        VALUES(T_Utilisateurs_Dim[UserPrincipalName]),
        "Nom", LOWER(COALESCE(CALCULATE(SELECTEDVALUE(T_Utilisateurs_Dim[DisplayName])), "")),
        "Hit_service", CONTAINSSTRING(LOWER(COALESCE(CALCULATE(SELECTEDVALUE(T_Utilisateurs_Dim[DisplayName])), "")), "service"),
        "Hit_formation", CONTAINSSTRING(LOWER(COALESCE(CALCULATE(SELECTEDVALUE(T_Utilisateurs_Dim[DisplayName])), "")), "formation"),
        "Hit_admin", CONTAINSSTRING(LOWER(COALESCE(CALCULATE(SELECTEDVALUE(T_Utilisateurs_Dim[DisplayName])), "")), "admin"),
        "Hit_test", CONTAINSSTRING(LOWER(COALESCE(CALCULATE(SELECTEDVALUE(T_Utilisateurs_Dim[DisplayName])), "")), "test"),
        "Hit_visit", CONTAINSSTRING(LOWER(COALESCE(CALCULATE(SELECTEDVALUE(T_Utilisateurs_Dim[DisplayName])), "")), "visit")
    ),
    [Hit_service] + [Hit_formation] + [Hit_admin] + [Hit_test] + [Hit_visit] = 1
)
```

Cette requête ne suffit pas seule : il faut encore exclure toutes les autres règles `TypeCompte` pour obtenir le comptage “solely because of one of these 5 patterns”.

### Verdict : sur-classification estimée

- Les 5 règles sont toutes des `CONTAINSSTRING` non bornés sur `DisplayName`.
- Aucune ne s'appuie sur `UserPrincipalName`, donc elles classent sur un champ plus libre et plus bruité.
- Le risque de faux positifs est structurellement élevé, surtout pour `admin`, `service` et `test`.
- Le volume réel de sur-classification ne peut pas être mesuré depuis le repo seul ; il faut un audit sur modèle rafraîchi avec échantillonnage.

## B — Décomposition population Exclu
### Split Technique vs Désactivés

La colonne `EtatActivite` applique cette logique :
- `Exclu` si `TypeCompte = "Technique"` ;
- `Exclu` si `AccountEnabled = FALSE()` ;
- sinon seulement, dérivation vers `Actif`, `Inactif (>90j)`, `Jamais Connecté` ou `Inactif M365`.

Les mesures de split possibles sans modifier la colonne sont :

```dax
NbExclusTechniques =
CALCULATE(
    DISTINCTCOUNT(T_Utilisateurs_Dim[UserPrincipalName]),
    T_Utilisateurs_Dim[EtatActivite] = "Exclu",
    T_Utilisateurs_Dim[TypeCompte] = "Technique"
)

NbExclusDesactives =
CALCULATE(
    DISTINCTCOUNT(T_Utilisateurs_Dim[UserPrincipalName]),
    T_Utilisateurs_Dim[EtatActivite] = "Exclu",
    T_Utilisateurs_Dim[TypeCompte] = "Utilisateur",
    T_Utilisateurs_Dim[AccountEnabled] = FALSE()
)
```

Lecture structurelle attendue :
- `NbExclusTechniques` couvre tous les comptes techniques, qu'ils soient actifs ou désactivés.
- `NbExclusDesactives` couvre les comptes humains désactivés.
- Un résidu théorique existe si `TypeCompte = "Non defini"` et `AccountEnabled = FALSE()`. Ce cas n'entre dans aucun des deux sous-totaux ci-dessus.

### Gap logique détecté (si applicable)

Question : existe-t-il des lignes où `EtatActivite = "Exclu"` mais `TypeCompte = "Utilisateur"` et `AccountEnabled = TRUE()` ?

Réponse : non, par définition de la colonne.
- Si `TypeCompte = "Utilisateur"` et `AccountEnabled = TRUE()`, alors `EstTechnique = FALSE()` et `EstDesactive = FALSE()`.
- Dans ce cas, la branche `Exclu` n'est jamais atteinte.
- Le compteur attendu est donc `0` tant que la formule `EtatActivite` reste inchangée.

Le seul angle mort structurel est le cas `TypeCompte = "Non defini"` + `AccountEnabled = FALSE()`, théoriquement possible dans la formule mais probablement marginal au vu de la source Graph `users`.

## C — Périmètre CiblesNettoyage (IC-004)
### Analyse des chevauchements

1. `NbUtilisateursFantomes` n'est pas une population indépendante.
   - Sous-ensemble de `NbHumainsJamaisConnectes` si `LastSignIn` est vide.
   - Sous-ensemble de `NbHumainsInactifs` si l'utilisateur est absent de `T_Activite_M365` et que `LastSignIn < TODAY() - 90`.
   - Reste indépendant seulement pour les utilisateurs AD actifs avec `LastSignIn` récent mais sans aucune ligne dans `T_Activite_M365`.

2. `NbInactifsM365` n'est pas couvert par `NbHumainsInactifs`.
   - `NbHumainsInactifs` filtre `EtatActivite = "Inactif (>90j)"`.
   - `NbInactifsM365` filtre `EtatActivite = "Inactif M365"`.
   - Ces deux statuts sont distincts dans la logique de `EtatActivite`.

3. Conséquence sur `CiblesNettoyage`.
   - Ajouter `NbUtilisateursFantomes` par simple somme créerait du double comptage.
   - Ajouter `NbInactifsM365` par simple somme n'introduirait pas de recouvrement direct avec `NbHumainsInactifs`, mais élargirait le périmètre métier actuel.

### Formule recommandée

Recommandation immédiate, sans changement de périmètre métier :
- ne pas sommer des KPI agrégés ;
- compter un ensemble canonique de lignes cibles.

La réécriture la plus sûre, cohérente avec la colonne `IsCible` déjà présente, est :

```dax
CiblesNettoyage_Recommande =
CALCULATE(
    COUNTROWS(T_Utilisateurs_Dim),
    T_Utilisateurs_Dim[IsCible] = TRUE()
)
```

Cette version :
- préserve le périmètre actuel du modèle ;
- évite tout double comptage arithmétique futur ;
- n'intègre pas implicitement `NbUtilisateursFantomes` ;
- n'intègre pas `NbInactifsM365` tant qu'une décision équipe n'a pas élargi le scope.

Si l'équipe souhaite ensuite intégrer les populations “sans usage M365”, il faudra passer à une formule par `DISTINCT(UNION(...))` sur `UserPrincipalName`, et non à une somme de mesures.

## Prochaines étapes
- [ ] Valider les faux positifs TypeCompte avec un échantillon réel
- [ ] Décision équipe sur CiblesNettoyage → créer FIX-003
- [ ] Ajouter NbExclusTechniques / NbExclusDesactives si utile → créer FIX-004

## E — Amélioration extraction : ajout userType
**Date**: 2026-03-20

| Champ | Avant | Après |
|-------|-------|-------|
| userType | Non extrait | Extrait → colonne UserType |
| usageLocation | Extrait, non utilisé | Extrait → colonne UsageLocation |

### Impact sur TypeCompte
- Comptes Guest et #EXT# désormais classés via signal fiable
- Règles CONTAINSSTRING restent actives pour les Member ambigus
- Prochaine étape : Exchange Online pour SharedMailbox (niveau 2)
