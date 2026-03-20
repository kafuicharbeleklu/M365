# FIX-003 — Réécriture CiblesNettoyage via IsCible
**Date**: 2026-03-20
**Référence audit**: BL-001 / IC-004, DQ-001 / Section C
**Fichiers modifiés**: _Mesures.tmdl

## Définition IsCible
```dax
column IsCible =
		
		// Colonne calculée : identifie les comptes cibles pour le nettoyage
		// Cible = Humain actif AD mais dormant (>90j ou jamais connecté) OU tout compte désactivé AD
		(
		    T_Utilisateurs_Dim[TypeCompte] = "Utilisateur" &&
		    T_Utilisateurs_Dim[Statut AD] = "Activé" &&
		    T_Utilisateurs_Dim[EtatActivite] IN {"Inactif (>90j)", "Jamais Connecté"}
		)
		||
		T_Utilisateurs_Dim[Statut AD] = "Désactivé"
```

## Couverture confirmée
- `TypeCompte = "Utilisateur" AND AccountEnabled = FALSE()` : couvert via `Statut AD = "Désactivé"`
- `EtatActivite = "Inactif (>90j)"` : couvert pour les utilisateurs actifs AD
- `EtatActivite = "Jamais Connecté"` : couvert pour les utilisateurs actifs AD
- `TypeCompte = "Technique" AND AccountEnabled = FALSE()` : couvert via `Statut AD = "Désactivé"`

## CiblesNettoyage — avant / après
```dax
-- Avant
measure CiblesNettoyage =
		
		[NbHumainsInactifs] + [NbHumainsJamaisConnectes] + [NbHumainsDesactives] + [NbBoitesInactives]

-- Après
measure CiblesNettoyage =
		CALCULATE(
			COUNTROWS(T_Utilisateurs_Dim),
			T_Utilisateurs_Dim[IsCible] = TRUE()
		)
```
