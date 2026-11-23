## Pourquoi l'analyse post-optimale ?

### 1. Le problème : les données du modèle sont des estimations

Dans un PL, les coefficients **c** (coûts/profits), **b** (ressources) et **A** (consommations) viennent de prévisions ou de mesures, donc ils sont **incertains** et **changent** dans le temps.

```
 Modèle résolu une fois        Réalité
 ┌─────────────────────┐       ┌─────────────────────────────┐
 │ max 5x₁ + 4,5x₂ ... │  ≠    │ prix qui bougent            │
 │ b = (60, 150, 8)    │       │ stock qui change            │
 │ solution x*         │       │ nouveau produit, nouvelle   │
 └─────────────────────┘       │ contrainte                  │
                               └─────────────────────────────┘
        ▼
  Question : x* reste-t-elle optimale ? Sinon, comment la corriger ?
```

### 2. Les deux objectifs (selon le cours)

|Objectif|Sens|
|---|---|
|**Mesurer l'influence**|De combien peut-on modifier un coefficient avant que la solution optimale change ?|
|**Guider l'effort**|Repérer les coefficients **critiques**, ceux qu'il faut estimer avec le plus de précision|

### 3. Sommes-nous limités aux autres méthodes ?

Non, mais elles sont inefficaces ici. On pourrait **tout recalculer depuis zéro**, mais on perdrait du temps et de l'information.

```
 ┌──────────────────────────┬──────────────────────────────┐
 │ Re-résoudre depuis zéro  │ Analyse post-optimale        │
 ├──────────────────────────┼──────────────────────────────┤
 │ Repart du tableau initial│ Repart du TABLEAU OPTIMAL    │
 │ Tout le travail refait   │ On réutilise B⁻¹, π, c_B     │
 │ Donne UNE solution       │ Donne une PLAGE de validité  │
 │ Aucune idée de stabilité │ Mesure la sensibilité        │
 └──────────────────────────┴──────────────────────────────┘
```

**Idée clé :** le tableau optimal contient déjà tout (**B⁻¹**, les multiplicateurs **πᵀ = c_BᵀB⁻¹**). Une petite modification n'oblige pas à tout refaire : on **met à jour** le tableau, puis on reprend le simplexe quelques pivots seulement.

### 4. Ce qui peut casser après une modification

```
              Tableau optimal :  b ≥ 0  ✔   et   coûts relatifs ≥ 0  ✔
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        ▼                              ▼                              ▼
   on change c                    on change b                  on change A /
   (ou nouvelle variable)         (ou nouvelle contrainte)     colonne
        │                              │                              │
  perd l'OPTIMALITÉ              perd l'ADMISSIBILITÉ           l'un ou l'autre
        │                              │
        ▼                              ▼
  reprise : simplexe PRIMAL      reprise : simplexe DUAL
```

C'est ici que les deux algorithmes vus avant servent.

### 5. Plan du chapitre (les 5 cas du cours)

| #   | Modification                               | Ce qui est touché | Reprise        |
| --- | ------------------------------------------ | ----------------- | -------------- |
| 1   | Coefficients de la fonction économique (c) | Optimalité        | Primal         |
| 2   | Termes de droite (b)                       | Admissibilité     | Dual           |
| 3   | Contraintes (A)                            | Selon le cas      | Primal ou dual |
| 4   | Nouvelle variable                          | Optimalité        | Primal         |
| 5   | Nouvelle contrainte                        | Admissibilité     | Dual           |