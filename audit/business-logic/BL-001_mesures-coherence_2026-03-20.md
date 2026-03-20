# BL-001 ? Coh?rence des mesures utilisateurs et licences
**Date**: 2026-03-20
**Statut**:  En cours
**P?rim?tre**: _Mesures.tmdl, T_Utilisateurs_Dim, T_Activite_M365, T_Affectations_Fact

## R?sum? ex?cutif
Audit de coh?rence des d?finitions DAX li?es aux populations utilisateurs, aux licences et aux jointures entre activit? M365 et affectations.
Les d?finitions montrent trois ?carts principaux : `NbHumainsJamaisConnectes` ne filtre pas explicitement les comptes humains, `NbUtilisateursFantomes` peut chevaucher la population `Actif`, et cette mesure ne suit pas le m?me comportement de scope produit que les autres KPI utilisateurs.
Sur la page `Analyse Utilisateur`, aucun chevauchement de cartes/KPI n'a ?t? d?tect? d'apr?s les bounding boxes s?rialis?es.

## A ? D?finitions exactes des mesures cl?s
### 1. NbUtilisateursFantomes
````dax
measure NbUtilisateursFantomes =
			VAR UsersActifsAD =
				CALCULATETABLE(
					VALUES(T_Utilisateurs_Dim[UserPrincipalName]),
					REMOVEFILTERS(T_Utilisateurs_Dim[EtatActivite]),
					T_Utilisateurs_Dim[TypeCompte] = "Utilisateur",
					T_Utilisateurs_Dim[AccountEnabled] = TRUE()
				)
			VAR UsersAvecActivite =
				CALCULATETABLE(
					VALUES(T_Activite_M365[UserPrincipalName]),
					REMOVEFILTERS(T_Affectations_Fact)
				)
			RETURN
			COALESCE(COUNTROWS(EXCEPT(UsersActifsAD, UsersAvecActivite)), 0)
````

### 2. NbHumainsJamaisConnectes
````dax
measure NbHumainsJamaisConnectes =
			VAR _isProductScoped = ISCROSSFILTERED(T_Produits_Dim)
			VAR _base =
				CALCULATE(
					DISTINCTCOUNT(T_Utilisateurs_Dim[UserPrincipalName]),
					T_Utilisateurs_Dim[AccountEnabled] = TRUE(),
					ISBLANK(T_Utilisateurs_Dim[LastSignIn])
				)
			VAR _scoped =
				CALCULATE(
					DISTINCTCOUNT(T_Utilisateurs_Dim[UserPrincipalName]),
					T_Utilisateurs_Dim[AccountEnabled] = TRUE(),
					ISBLANK(T_Utilisateurs_Dim[LastSignIn]),
					KEEPFILTERS(
						TREATAS(
							VALUES(T_Affectations_Fact[UserPrincipalName]),
							T_Utilisateurs_Dim[UserPrincipalName]
						)
					)
				)
			RETURN
				COALESCE(IF(_isProductScoped, _scoped, _base), 0)
````

### 3. NbHumainsInactifs
````dax
measure NbHumainsInactifs =
			VAR _isProductScoped = ISCROSSFILTERED(T_Produits_Dim)
			VAR _base =
				CALCULATE(
					DISTINCTCOUNT(T_Utilisateurs_Dim[UserPrincipalName]),
					FILTER(
						T_Utilisateurs_Dim,
						TRIM(T_Utilisateurs_Dim[EtatActivite]) = "Inactif (>90j)"
					)
				)
			VAR _scoped =
				CALCULATE(
					DISTINCTCOUNT(T_Utilisateurs_Dim[UserPrincipalName]),
					FILTER(
						T_Utilisateurs_Dim,
						TRIM(T_Utilisateurs_Dim[EtatActivite]) = "Inactif (>90j)"
					),
					KEEPFILTERS(
						TREATAS(
							VALUES(T_Affectations_Fact[UserPrincipalName]),
							T_Utilisateurs_Dim[UserPrincipalName]
						)
					)
				)
			RETURN
				COALESCE(IF(_isProductScoped, _scoped, _base), 0)
````

### 4. NbHumainsActifs
````dax
measure NbHumainsActifs =
			VAR _isProductScoped = ISCROSSFILTERED(T_Produits_Dim)
			VAR _base =
				CALCULATE(
					DISTINCTCOUNT(T_Utilisateurs_Dim[UserPrincipalName]),
					FILTER(
						T_Utilisateurs_Dim,
						TRIM(T_Utilisateurs_Dim[EtatActivite]) = "Actif"
					)
				)
			VAR _scoped =
				CALCULATE(
					DISTINCTCOUNT(T_Utilisateurs_Dim[UserPrincipalName]),
					FILTER(
						T_Utilisateurs_Dim,
						TRIM(T_Utilisateurs_Dim[EtatActivite]) = "Actif"
					),
					KEEPFILTERS(
						TREATAS(
							VALUES(T_Affectations_Fact[UserPrincipalName]),
							T_Utilisateurs_Dim[UserPrincipalName]
						)
					)
				)
			RETURN
				COALESCE(IF(_isProductScoped, _scoped, _base), 0)
````

### 5. NbHumainsDesactives
````dax
measure NbHumainsDesactives =
			VAR _isProductScoped = ISCROSSFILTERED(T_Produits_Dim)
			VAR _base =
				CALCULATE(
					DISTINCTCOUNT(T_Utilisateurs_Dim[UserPrincipalName]),
					REMOVEFILTERS(T_Utilisateurs_Dim[EtatActivite]),
					T_Utilisateurs_Dim[TypeCompte] = "Utilisateur",
					T_Utilisateurs_Dim[AccountEnabled] = FALSE()
				)
			VAR _scoped =
				CALCULATE(
					DISTINCTCOUNT(T_Utilisateurs_Dim[UserPrincipalName]),
					REMOVEFILTERS(T_Utilisateurs_Dim[EtatActivite]),
					T_Utilisateurs_Dim[TypeCompte] = "Utilisateur",
					T_Utilisateurs_Dim[AccountEnabled] = FALSE(),
					KEEPFILTERS(
						TREATAS(
							VALUES(T_Affectations_Fact[UserPrincipalName]),
							T_Utilisateurs_Dim[UserPrincipalName]
						)
					)
				)
			RETURN
				COALESCE(IF(_isProductScoped, _scoped, _base), 0)
````

### 6. EtatActivite
````dax
column EtatActivite =
			
			VAR EstTechnique = [TypeCompte] = "Technique"
			VAR EstDesactive = [AccountEnabled] = FALSE()
			VAR UserEmail    = [UserPrincipalName]
			
			// Catégorie issue des données d'activité Microsoft 365
			VAR CategorieM365 =
			    LOOKUPVALUE(
			        T_Activite_M365[CategorieActivite],
			        T_Activite_M365[UserPrincipalName], UserEmail
			    )
			
			// Connexion Azure AD (authentification, indépendant des apps M365)
			VAR AJamaisConnecteAD = ISBLANK([LastSignIn])
			VAR EstInactif90j     = NOT(ISBLANK([LastSignIn])) && [LastSignIn] < TODAY() - 90
			
			RETURN
			IF(
			    EstTechnique || EstDesactive,
			    "Exclu",	// Remplace BLANK() par une valeur explicite pour eviter les (Blank) dans les filtres
			    IF(
			        NOT(ISBLANK(CategorieM365)),
			        // Nuance : si M365 dit 'Jamais Connecté' mais Azure AD a une connexion
			        // → l'user s'est authentifié mais n'utilise aucune app M365
			        IF(
			            CategorieM365 = "Jamais Connecté" && NOT(AJamaisConnecteAD),
			            "Inactif M365",
			            CategorieM365
			        ),
			        // Fallback sur Azure AD si aucune donnée M365
			        IF(
			            AJamaisConnecteAD,
			            "Jamais Connecté",
			            IF(EstInactif90j, "Inactif (>90j)", "Actif")
			        )
			    )
			)
````

### 7. StatutLicence
````dax
column StatutLicence = ```
			
			IF(
			    // On compte le nombre de lignes dans la table Affectations liées à cet utilisateur
			    COUNTROWS(RELATEDTABLE(T_Affectations_Fact)) > 0, 
			    "ON", 
			    "OFF"
			)
			```
````

### 8. TypeCompte
````dax
column TypeCompte = ```
			
			// Protection contre les valeurs nulles pour eviter les (Blank)
			VAR Nom = LOWER(COALESCE([DisplayName], ""))
			VAR Email = LOWER(COALESCE([UserPrincipalName], ""))
			VAR _estVide = ISBLANK([DisplayName]) && ISBLANK([UserPrincipalName])
			RETURN
			IF(_estVide, "Non defini",
			SWITCH(
			    TRUE(),
			
			    // ═══════════════════════════════════════════════════════════════════
			    // 1. COMPTES EXTERNES
			    // ═══════════════════════════════════════════════════════════════════
			    CONTAINSSTRING(Email, "#ext#"), "Technique",
			
			    // ═══════════════════════════════════════════════════════════════════
			    // 2. COMPTES PARTAGÉS / SALLES
			    // ═══════════════════════════════════════════════════════════════════
			    LEFT([DisplayName], 1) = "#", "Technique",
			    CONTAINSSTRING(Nom, "salle"), "Technique",
			    CONTAINSSTRING(Nom, "salon"), "Technique",
			    CONTAINSSTRING(Nom, "meeting"), "Technique",
			    CONTAINSSTRING(Nom, "conference"), "Technique",
			    CONTAINSSTRING(Nom, "conférence"), "Technique",
			    CONTAINSSTRING(Nom, "réunion"), "Technique",
			    CONTAINSSTRING(Nom, "reunion"), "Technique",
			    CONTAINSSTRING(Nom, "room"), "Technique",
			    CONTAINSSTRING(Nom, "boardroom"), "Technique",
			    CONTAINSSTRING(Nom, "bookings"), "Technique",
			    CONTAINSSTRING(Nom, "accueil"), "Technique",
			
			    // ═══════════════════════════════════════════════════════════════════
			    // 3. EMAILS GÉNÉRIQUES / NO-REPLY
			    // ═══════════════════════════════════════════════════════════════════
			    CONTAINSSTRING(Email, "info@"), "Technique",
			    CONTAINSSTRING(Email, "contact@"), "Technique",
			    CONTAINSSTRING(Email, "no-reply"), "Technique",
			    CONTAINSSTRING(Email, "noreply"), "Technique",
			    CONTAINSSTRING(Email, "norepley"), "Technique",
			    CONTAINSSTRING(Email, "nepasrepondre"), "Technique",
			    CONTAINSSTRING(Email, "support@"), "Technique",
			    CONTAINSSTRING(Email, "catchall"), "Technique",
			    CONTAINSSTRING(Email, "facture"), "Technique",
			    CONTAINSSTRING(Email, "export"), "Technique",
			
			    // ═══════════════════════════════════════════════════════════════════
			    // 4. PATTERNS SUPPORT
			    // ═══════════════════════════════════════════════════════════════════
			    CONTAINSSTRING(Email, "support_"), "Technique",
			    CONTAINSSTRING(Nom, "support_"), "Technique",
			    CONTAINSSTRING(Nom, "supportguarani"), "Technique",
			
			    // ═══════════════════════════════════════════════════════════════════
			    // 5. COMPTES IT / INFRASTRUCTURE
			    // ═══════════════════════════════════════════════════════════════════
			    CONTAINSSTRING(Nom, "sql"), "Technique",
			    CONTAINSSTRING(Nom, "proxy"), "Technique",
			    CONTAINSSTRING(Nom, "backup"), "Technique",
			    CONTAINSSTRING(Nom, "sauvegarde"), "Technique",
			    CONTAINSSTRING(Nom, "ldap"), "Technique",
			    CONTAINSSTRING(Nom, "utm"), "Technique",
			    CONTAINSSTRING(Nom, "scan"), "Technique",
			    CONTAINSSTRING(Nom, "sync"), "Technique",
			    CONTAINSSTRING(Nom, "bot"), "Technique",
			    CONTAINSSTRING(Nom, "api"), "Technique",
			    CONTAINSSTRING(Nom, "admin"), "Technique",
			    CONTAINSSTRING(Nom, "svc"), "Technique",
			    CONTAINSSTRING(Nom, "pool"), "Technique",
			    CONTAINSSTRING(Nom, "spapp"), "Technique",
			
			    // ═══════════════════════════════════════════════════════════════════
			    // 6. PRÉFIXES TECHNIQUES
			    // ═══════════════════════════════════════════════════════════════════
			    CONTAINSSTRING(Nom, "app_"), "Technique",
			    CONTAINSSTRING(Nom, "svc_"), "Technique",
			    CONTAINSSTRING(Nom, "srv_"), "Technique",
			    CONTAINSSTRING(Nom, "test"), "Technique",
			    CONTAINSSTRING(Nom, "update"), "Technique",
			    CONTAINSSTRING(Nom, "irium"), "Technique",
			    CONTAINSSTRING(Nom, "mts "), "Technique",
			
			    // ═══════════════════════════════════════════════════════════════════
			    // 7. BUSINESS OBJECTS / BI
			    // ═══════════════════════════════════════════════════════════════════
			    LEFT(Nom, 2) = "bo" && LEN(Nom) < 10, "Technique",
			    CONTAINSSTRING(Nom, "bodev"), "Technique",
			    CONTAINSSTRING(Nom, "boprod"), "Technique",
			    CONTAINSSTRING(Nom, "bosched"), "Technique",
			    CONTAINSSTRING(Nom, "bosql"), "Technique",
			    CONTAINSSTRING(Nom, "businessobject"), "Technique",
			    CONTAINSSTRING(Nom, "powerbi"), "Technique",
			    CONTAINSSTRING(Nom, "pbi "), "Technique",
			    CONTAINSSTRING(Nom, "bi "), "Technique",
			    CONTAINSSTRING(Nom, "ireporting"), "Technique",
			    CONTAINSSTRING(Email, "pbi-"), "Technique",
			    CONTAINSSTRING(Email, "bi."), "Technique",
			
			    // ═══════════════════════════════════════════════════════════════════
			    // 8. OUTILS / APPLICATIONS IT
			    // ═══════════════════════════════════════════════════════════════════
			    CONTAINSSTRING(Nom, "azure"), "Technique",
			    CONTAINSSTRING(Nom, "migration"), "Technique",
			    CONTAINSSTRING(Nom, "migwiz"), "Technique",
			    CONTAINSSTRING(Nom, "veeam"), "Technique",
			    CONTAINSSTRING(Nom, "rubrik"), "Technique",
			    CONTAINSSTRING(Nom, "sophos"), "Technique",
			    CONTAINSSTRING(Nom, "sentinel"), "Technique",
			    CONTAINSSTRING(Nom, "talend"), "Technique",
			    CONTAINSSTRING(Nom, "mulesoft"), "Technique",
			    CONTAINSSTRING(Nom, "matrix42"), "Technique",
			    CONTAINSSTRING(Nom, "m42"), "Technique",
			    CONTAINSSTRING(Nom, "sage"), "Technique",
			    CONTAINSSTRING(Nom, "quest"), "Technique",
			    CONTAINSSTRING(Nom, "coservit"), "Technique",
			    CONTAINSSTRING(Nom, "projeqtor"), "Technique",
			    CONTAINSSTRING(Nom, "wordpress"), "Technique",
			    CONTAINSSTRING(Nom, "systancia"), "Technique",
			    CONTAINSSTRING(Nom, "aquiweb"), "Technique",
			    CONTAINSSTRING(Nom, "automator"), "Technique",
			    CONTAINSSTRING(Nom, "mimecast"), "Technique",
			    CONTAINSSTRING(Nom, "manageengine"), "Technique",
			    CONTAINSSTRING(Nom, "rpmglobal"), "Technique",
			    CONTAINSSTRING(Nom, "svn"), "Technique",
			    CONTAINSSTRING(Nom, "skype"), "Technique",
			
			    // ═══════════════════════════════════════════════════════════════════
			    // 9. INFRASTRUCTURE RÉSEAU
			    // ═══════════════════════════════════════════════════════════════════
			    CONTAINSSTRING(Nom, "xg"), "Technique",
			    CONTAINSSTRING(Nom, "xcc"), "Technique",
			    CONTAINSSTRING(Nom, "firewall"), "Technique",
			    CONTAINSSTRING(Nom, "visor"), "Technique",
			    CONTAINSSTRING(Nom, "winstox"), "Technique",
			    CONTAINSSTRING(Nom, "i80"), "Technique",
			
			    // ═══════════════════════════════════════════════════════════════════
			    // 10. RH / ADMINISTRATION / GÉNÉRIQUES
			    // ═══════════════════════════════════════════════════════════════════
			    CONTAINSSTRING(Nom, "sirh"), "Technique",
			    CONTAINSSTRING(Nom, "formation"), "Technique",
			    CONTAINSSTRING(Nom, "induction"), "Technique",
			    CONTAINSSTRING(Nom, "reservation"), "Technique",
			    CONTAINSSTRING(Nom, "validation"), "Technique",
			    CONTAINSSTRING(Nom, "compta"), "Technique",
			    CONTAINSSTRING(Nom, "congé"), "Technique",
			    CONTAINSSTRING(Nom, "occasion"), "Technique",
			    CONTAINSSTRING(Nom, "interfaces"), "Technique",
			    CONTAINSSTRING(Nom, "intranet"), "Technique",
			    CONTAINSSTRING(Nom, "supervision"), "Technique",
			    CONTAINSSTRING(Nom, "operateur"), "Technique",
			    CONTAINSSTRING(Nom, "gestsup"), "Technique",
			    CONTAINSSTRING(Nom, "signcenter"), "Technique",
			    CONTAINSSTRING(Nom, "stagiaire"), "Technique",
			    CONTAINSSTRING(Nom, "delegues"), "Technique",
			    CONTAINSSTRING(Nom, "visit"), "Technique",
			    CONTAINSSTRING(Nom, "survey"), "Technique",
			
			    // ═══════════════════════════════════════════════════════════════════
			    // 11. PATTERNS EMAIL SPÉCIFIQUES
			    // ═══════════════════════════════════════════════════════════════════
			    CONTAINSSTRING(Email, "sirh@"), "Technique",
			    CONTAINSSTRING(Email, ".sirh@"), "Technique",
			    CONTAINSSTRING(Email, "survey@"), "Technique",
			    CONTAINSSTRING(Email, "alerts@"), "Technique",
			    CONTAINSSTRING(Email, "edi@"), "Technique",
			    CONTAINSSTRING(Email, "-edi@"), "Technique",
			
			    // ═══════════════════════════════════════════════════════════════════
			    // 12. COMPTES COURTS / GÉNÉRIQUES (3-4 lettres majuscules)
			    // ═══════════════════════════════════════════════════════════════════
			    CONTAINSSTRING(Nom, "amt"), "Technique",
			    CONTAINSSTRING(Nom, "cat"), "Technique",
			    CONTAINSSTRING(Nom, "cesu"), "Technique",
			    CONTAINSSTRING(Nom, "dfi"), "Technique",
			    CONTAINSSTRING(Nom, "bissas"), "Technique",
			    CONTAINSSTRING(Nom, "qsec"), "Technique",
			    CONTAINSSTRING(Nom, "scrute"), "Technique",
			    CONTAINSSTRING(Nom, "suwonda"), "Technique",
			    CONTAINSSTRING(Nom, "partswe"), "Technique",
			    CONTAINSSTRING(Nom, "saudequip"), "Technique",
			    
			    // Comptes très courts (2-3 lettres seules)
			    Nom = "su", "Technique",
			    Nom = "sac", "Technique",
			    Nom = "rcc", "Technique",
			    Nom = "ae", "Technique",
			    Nom = "dp", "Technique",
			
			    // ═══════════════════════════════════════════════════════════════════
			    // 13. COMPTES PARTAGÉS / GÉNÉRIQUES
			    // ═══════════════════════════════════════════════════════════════════
			    CONTAINSSTRING(Nom, "polaris"), "Technique",
			    CONTAINSSTRING(Nom, "generique"), "Technique",
			    CONTAINSSTRING(Nom, "partage"), "Technique",
			    CONTAINSSTRING(Nom, "service"), "Technique",
			
			    // ═══════════════════════════════════════════════════════════════════
			    // PAR DÉFAUT : UTILISATEUR HUMAIN
			    // ═══════════════════════════════════════════════════════════════════
			    "Utilisateur"
			))
			```
````

### 9. LicencesInactives
````dax
measure LicencesInactives =
			VAR _affectees = COALESCE([LicencesAffectees], 0)
			VAR _actives = COALESCE([LicencesActives], 0)
			RETURN
			MAX(0, _affectees - _actives)
````

### 10. LicencesActives
````dax
measure LicencesActives =
			VAR _actives =
				CALCULATE(
					[LicencesAffectees],
					TREATAS(
						CALCULATETABLE(
							VALUES(T_Utilisateurs_Dim[UserPrincipalName]),
							FILTER(
								T_Utilisateurs_Dim,
								TRIM(T_Utilisateurs_Dim[EtatActivite]) = "Actif"
							)
						),
						T_Affectations_Fact[UserPrincipalName]
					)
				)
			RETURN
			COALESCE(_actives, 0)
````

### 11. LicencesComptesBloques
````dax
measure LicencesComptesBloques =
			COALESCE(
				CALCULATE(
					[LicencesAffectees],
					REMOVEFILTERS(T_Utilisateurs_Dim[EtatActivite]),
					T_Utilisateurs_Dim[AccountEnabled] = FALSE()
				),
				0
			)
````

### 12. CiblesNettoyage
````dax
measure CiblesNettoyage =
			
			[NbHumainsInactifs] + [NbHumainsJamaisConnectes] + [NbHumainsDesactives] + [NbBoitesInactives]
````

### 13. TauxGaspillage
````dax
measure TauxGaspillage =
			
			DIVIDE([LicencesInactives], [LicencesAffectees], 0)
````

## B ? Matrice de coh?rence

| Concept | Mesure / Colonne | Condition filtre exacte | Seuil hardcod? |
|---------|-----------------|------------------------|----------------|
| Jamais connect? | `NbHumainsJamaisConnectes` | `AccountEnabled = TRUE()` et `ISBLANK(LastSignIn)` ; branche produit via `TREATAS(VALUES(T_Affectations_Fact[UserPrincipalName]))` | Aucun dans la mesure |
| Fant?me | `NbUtilisateursFantomes` | `TypeCompte = "Utilisateur"` et `AccountEnabled = TRUE()` dans `T_Utilisateurs_Dim`, puis exclusion des `UserPrincipalName` pr?sents dans `T_Activite_M365` via `EXCEPT(...)` | Aucun dans la mesure |
| Inactif | `NbHumainsInactifs` | `TRIM(T_Utilisateurs_Dim[EtatActivite]) = "Inactif (>90j)"` ; branche produit via `TREATAS(...)` | `90` jours, port? par `EtatActivite` |
| D?sactiv? AD | `NbHumainsDesactives` | `REMOVEFILTERS(EtatActivite)` + `TypeCompte = "Utilisateur"` + `AccountEnabled = FALSE()` ; branche produit via `TREATAS(...)` | Aucun |
| Exclu | `EtatActivite = "Exclu"` | `TypeCompte = "Technique"` ou `AccountEnabled = FALSE()` | Aucun |
| Licence inactive | `LicencesInactives` | `MAX(0, [LicencesAffectees] - [LicencesActives])` ; `LicencesActives` ne garde que `EtatActivite = "Actif"` | Indirect : `90` jours via `EtatActivite` |
| Licence bloqu?e | `LicencesComptesBloques` | `[LicencesAffectees]` sous `AccountEnabled = FALSE()` et `REMOVEFILTERS(EtatActivite)` | Aucun |
| Cible nettoyage | `CiblesNettoyage` | Somme de `[NbHumainsInactifs] + [NbHumainsJamaisConnectes] + [NbHumainsDesactives] + [NbBoitesInactives]` | Indirect : `90` jours via `NbHumainsInactifs` |

## C ? Incoh?rences d?tect?es

**IC-001 ? `NbHumainsJamaisConnectes` ne filtre pas explicitement les comptes humains**
- Sympt?me : un compte technique activ? sans `LastSignIn` peut ?tre compt? dans `NbHumainsJamaisConnectes`, alors que le nom de la mesure et les commentaires sugg?rent une population humaine.
- Cause probable : la mesure filtre seulement `AccountEnabled = TRUE()` et `ISBLANK(LastSignIn)` ; elle ne filtre ni `TypeCompte = "Utilisateur"` ni `EtatActivite = "Jamais Connect?"`.
- Recommandation : aligner la mesure sur la d?finition m?tier en ajoutant un filtre explicite `TypeCompte = "Utilisateur"` ou en r?utilisant la classification `EtatActivite = "Jamais Connect?"`.

**IC-002 ? `NbUtilisateursFantomes` chevauche la population `Actif`**
- Sympt?me : un utilisateur actif dans Azure AD, absent de `T_Activite_M365`, peut ?tre compt? ? la fois dans `NbUtilisateursFantomes` et dans `NbHumainsActifs`.
- Cause probable : `EtatActivite` retombe sur `Actif` quand `LastSignIn` est r?cent et qu'aucune ligne M365 n'existe, alors que `NbUtilisateursFantomes` compte pr?cis?ment les utilisateurs actifs AD absents de `T_Activite_M365`.
- Recommandation : d?cider si un fant?me doit ?tre une sous-cat?gorie exclusive ; si oui, harmoniser `EtatActivite` et `NbUtilisateursFantomes` pour ?viter le double comptage conceptuel.

**IC-003 ? `NbUtilisateursFantomes` n'est pas coh?rent avec le scope produit**
- Sympt?me : sous filtre produit, `NbHumainsActifs`, `NbHumainsInactifs`, `NbHumainsJamaisConnectes` et `NbHumainsDesactives` deviennent product-scop?s, alors que `NbUtilisateursFantomes` reste global.
- Cause probable : la mesure ne contient ni branche `ISCROSSFILTERED(T_Produits_Dim)` ni `TREATAS(...)` vers `T_Affectations_Fact`, contrairement aux autres KPI utilisateurs.
- Recommandation : soit rendre `NbUtilisateursFantomes` product-scop?e avec la m?me logique de pont, soit documenter explicitement qu'elle reste globale et l'isoler visuellement des KPI filtrables par produit.

**IC-004 ? `CiblesNettoyage` sous-couvre les populations d'action d?j? expos?es sur la page**
- Sympt?me : la mesure n'inclut ni `NbUtilisateursFantomes` ni `NbInactifsM365`, alors que la page `Analyse Utilisateur` expose un bloc d'action sp?cifique pour les fant?mes et que `EtatActivite` g?re `Inactif M365`.
- Cause probable : la formule agr?ge seulement quatre mesures historiques (`Inactifs`, `JamaisConnectes`, `Desactives`, `BoitesInactives`).
- Recommandation : confirmer le p?rim?tre m?tier de `CiblesNettoyage` ; si l'objectif est la totalit? des comptes ? traiter, ?largir la mesure ou documenter explicitement les exclusions.

## D ? Couverture des jointures

- T_Activite_M365 ? T_Affectations_Fact : pas de relation directe ; la jonction se fait uniquement via `T_Utilisateurs_Dim[UserPrincipalName]`, avec des ponts DAX (`TREATAS`) pour certains KPI orient?s produit.
- User dans T_Utilisateurs_Dim absent de T_Activite_M365 : il n'est pas exclu par d?faut. S'il est `Technique` ou `AccountEnabled = FALSE()`, `EtatActivite` le classe `Exclu`. Sinon, la classification retombe sur `LastSignIn` : `Jamais Connect?`, `Inactif (>90j)` ou `Actif`.
- User dans T_Affectations_Fact absent de T_Activite_M365 : oui dans `NbUtilisateursFantomes` s'il existe aussi dans `T_Utilisateurs_Dim`, avec `TypeCompte = "Utilisateur"` et `AccountEnabled = TRUE()`. Non s'il est orphelin d'utilisateur dans la dimension, car l'ensemble de d?part de la mesure vient de `T_Utilisateurs_Dim`.

## E ? Chevauchements visuels (page Analyse Utilisateur)

| Visual ID | Mesure affich?e | x | y | width | height | Overlap avec |
|-----------|----------------|---|---|-------|--------|-------------|
| `0781849f42b2a3099ac6` | `CiblesNettoyage` | 1721 | 92 | 189 | 104 | Aucun |
| `40e7ac536e9864857177` | `NbBoitesInactives` | 1518 | 92 | 187 | 104 | Aucun |
| `678ebb458a124b23d8b3` | `NbHumainsTotal` | 300 | 92 | 187 | 104 | Aucun |
| `8030dbc87ab90506be3e` | `NbHumainsActifs` | 93.9367128266182 | 109.33617394573594 | 186.33347954132464 | 103.17638949808885 | Aucun |
| `b5e7555e9ed80b014183` | `NbUtilisateursFantomes` | 706 | 92 | 187 | 104 | Aucun |
| `ce426e14c617550ccd13` | `NbBoitesActives` | 1315 | 92 | 187 | 104 | Aucun |
| `ce70ef9e7866cc72b78d` | `NbHumainsInactifs` | 503 | 92 | 187 | 104 | Aucun |
| `d0f2e5dc55d345c41720` | `NbHumainsDesactives` | 909 | 92 | 187 | 104 | Aucun |
| `d8558517a5af0608ba18` | `NbBoitesTotal` | 1112 | 92 | 187 | 104 | Aucun |
| `ux_action_disabled_card_p3` | `LicencesComptesBloques` | 300 | 702 | 380 | 80 | Aucun |
| `ux_action_ghost_card_p3` | `NbUtilisateursFantomes` | 300 | 894 | 380 | 80 | Aucun |
| `ux_action_overuse_card_p3` | `UX_ProduitsEnDepassement` | 300 | 798 | 380 | 80 | Aucun |
| `ux_context_banner_p3` | `UX_ContexteFiltres` | 760 | 36 | 640 | 32 | Aucun |
| `ux_refresh_banner_p3` | `UX_DerniereMiseAJour` | 1410 | 36 | 280 | 32 | Aucun |

## Prochaines ?tapes
- [ ] Confirmer les d?finitions correctes avec l'?quipe
- [ ] Corriger les mesures incoh?rentes ? cr?er FIX-001
- [ ] Param?trer les seuils hardcod?s ? cr?er FIX-002
