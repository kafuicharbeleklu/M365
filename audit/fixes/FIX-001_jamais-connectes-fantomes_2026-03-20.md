# FIX-001 — Correction NbHumainsJamaisConnectes et NbUtilisateursFantomes
**Date**: 2026-03-20
**Référence audit**: BL-001 / IC-001, IC-003
**Fichiers modifiés**: _Mesures.tmdl

## Problèmes corrigés
- `IC-001`: `NbHumainsJamaisConnectes` ne filtrait pas explicitement `T_Utilisateurs_Dim[TypeCompte] = "Utilisateur"`. Les comptes techniques activés sans `LastSignIn` pouvaient donc être inclus.
- `IC-003`: `NbUtilisateursFantomes` n'était pas cohérent avec le scope produit. La mesure restait globale même quand `T_Produits_Dim` était filtrée.
- En attente, non traités dans ce correctif: `IC-002` (chevauchement conceptuel entre fantômes et actifs) et `IC-004` (périmètre de `CiblesNettoyage` à confirmer avec l'équipe).

## DAX avant / après pour chaque mesure
### NbHumainsJamaisConnectes
**Avant**
```dax
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
```

**Après**
```dax
measure NbHumainsJamaisConnectes =
		VAR _isProductScoped = ISCROSSFILTERED(T_Produits_Dim)
		VAR _base =
			CALCULATE(
				DISTINCTCOUNT(T_Utilisateurs_Dim[UserPrincipalName]),
				T_Utilisateurs_Dim[TypeCompte] = "Utilisateur",
				T_Utilisateurs_Dim[AccountEnabled] = TRUE(),
				ISBLANK(T_Utilisateurs_Dim[LastSignIn])
			)
		VAR _scoped =
			CALCULATE(
				DISTINCTCOUNT(T_Utilisateurs_Dim[UserPrincipalName]),
				T_Utilisateurs_Dim[TypeCompte] = "Utilisateur",
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
```

### NbUtilisateursFantomes
**Avant**
```dax
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
```

**Après**
```dax
measure NbUtilisateursFantomes =
		VAR _isProductScoped = ISCROSSFILTERED(T_Produits_Dim)
		VAR _baseUsersActifsAD =
			CALCULATETABLE(
				VALUES(T_Utilisateurs_Dim[UserPrincipalName]),
				REMOVEFILTERS(T_Utilisateurs_Dim[EtatActivite]),
				T_Utilisateurs_Dim[TypeCompte] = "Utilisateur",
				T_Utilisateurs_Dim[AccountEnabled] = TRUE()
			)
		VAR _scopedUsersActifsAD =
			CALCULATETABLE(
				VALUES(T_Utilisateurs_Dim[UserPrincipalName]),
				REMOVEFILTERS(T_Utilisateurs_Dim[EtatActivite]),
				T_Utilisateurs_Dim[TypeCompte] = "Utilisateur",
				T_Utilisateurs_Dim[AccountEnabled] = TRUE(),
				KEEPFILTERS(
					TREATAS(
						VALUES(T_Affectations_Fact[UserPrincipalName]),
						T_Utilisateurs_Dim[UserPrincipalName]
					)
				)
			)
		VAR UsersAvecActivite =
			CALCULATETABLE(
				VALUES(T_Activite_M365[UserPrincipalName]),
				REMOVEFILTERS(T_Affectations_Fact)
			)
		VAR _base = COUNTROWS(EXCEPT(_baseUsersActifsAD, UsersAvecActivite))
		VAR _scoped = COUNTROWS(EXCEPT(_scopedUsersActifsAD, UsersAvecActivite))
		RETURN
		COALESCE(IF(_isProductScoped, _scoped, _base), 0)
```

## Impact attendu sur les KPIs
- `NbHumainsJamaisConnectes` doit maintenant exclure les comptes techniques et s'aligner sur une lecture strictement humaine du KPI.
- `NbUtilisateursFantomes` doit désormais varier sous filtre produit comme les autres KPI utilisateurs product-scopés, en se limitant aux utilisateurs affectés au produit filtré.
- Les écarts `IC-002` et `IC-004` restent ouverts: les chiffres peuvent encore nécessiter validation métier malgré ce correctif technique.
