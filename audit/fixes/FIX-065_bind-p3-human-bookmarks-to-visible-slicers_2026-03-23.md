# FIX-065 - Liaison des bookmarks P3 humains aux segments visibles
**Date**: 2026-03-23

## Diagnostic
- Les segments copies sur `Analyse Utilisateur` filtrent correctement le tableau quand ils sont manipules manuellement.
- Les bookmarks KPI P3 continuaient d'appliquer des filtres de page sans etre relies aux nouveaux segments visibles.
- Cette divergence rendait le comportement difficile a comprendre et a deboguer, surtout sur `Comptes desactives avec licence`.

## Fix applique
- Ajout des segments visibles suivants dans les bookmarks P3 humains:
  - `18e02ee723e342995a61` -> `TypeCompte`
  - `7c987dd0a69bc50ae8d6` -> `Statut AD`
  - `e0d8483582d3ec82b9bc` -> `StatutLicence`
- Bookmarks alignes:
  - `02c501e8d87d63d0078c` (`Nav_HumainsActifs`)
  - `66e80f63e44eee7812b9` (`Nav_HumainsInactifs`)
  - `33c262bf35d2d40b3aa8` (`Nav_HumainsJamaisConnectes`)
  - `dacdeaf07eb2d1577049` (`Nav_HumainsDesactives`)
  - `1661112e2198ecabde3e` (`Nav_Reset`)
- Les segments deviennent ainsi la couche visible de pilotage pour ces bookmarks, au lieu de laisser uniquement des filtres implicites de page.

## Resultat attendu
- Les KPI humains P3 restaurent aussi l'etat visible des segments associes.
- `Comptes desactives avec licence` suit la meme logique de filtrage que les segments manuels.
- Le reset P3 remet egalement a zero les segments `TypeCompte`, `Statut AD` et `StatutLicence`.

## Limite connue
- Les cas `Utilisateurs fantomes` et `Produits en depassement` ne sont pas encore entierement exprimables par ces trois segments seuls.
- Pour une parite complete, il faudra ajouter un segment dedie a l'etat d'activite/categorie cible ou accepter un mode hybride bookmark + segment.
