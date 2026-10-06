
> **Situation** : `RP` donne une solution fractionnaire (Concept 4). Comment obtenir quand même l'optimum entier ?

```
                    PLNE (P)
                       │
     ┌─────────┬───────┴───────┬──────────────┐
     ▼         ▼               ▼              ▼
  ① TU      ② Coupes     ③ Branch & Bound  ④ Branch & Cut
 (résoudre   (ajouter     (énumérer         (② + ③
  RP seul)   des contr.)   intelligemment)   combinés)
```

---

### ① Unimodularité totale (TU)

Si on sait **à l'avance** que `RP` a un optimum entier, on résout seulement `RP`.

```
 A totalement unimodulaire  (tous ses déterminants ∈ {−1, 0, +1})
 + b entier
        ⟹  tous les sommets de F(RP) sont entiers
        ⟹  le simplexe donne directement l'optimum entier ✅
```

Exemples classiques : problèmes de **flot**, de **transport**, d'**affectation**.

---

### ② Algorithme de coupes

On **ajoute des contraintes** à `P` pour obtenir `P'` dont l'optimum de `RP'` est **entier**.

```
 x₂                                x₂
 2 ●╲                              2 ●╲        coupe
   │ ╲                               │ ╲       x₁ + 2x₂ ≤ 4
 1.8│  ★  ← fractionnaire            │  ╲
 1 ●──●──●                         1 ●──●──●
   │░░░░░░│                           │░░░░│
 0 ●──●──●─► x₁                    0 ●──●──●─► x₁

 F(RP) avec ★ coupé  ──►  nouvel optimum = (0,2), z = −10 ✅
```

La coupe **retire ★** mais **aucun point entier** de `F(P)`.

---

### ③ Branch-and-Bound (B&B)

On **divise** le problème en sous-problèmes et on **élimine** ceux qui ne peuvent pas être meilleurs.

Exemple : `RP` donne `x₂ = 1,8` ➜ on branche sur `x₂ ≤ 1` / `x₂ ≥ 2`.

```
                  RP : (2 ; 1,8)  z = −11
                  /                       \
           x₂ ≤ 1                       x₂ ≥ 2
              /                             \
      (2 ; 1)  z = −7              (0 ; 2)  z = −10
      entier ✅                    entier ✅  ← meilleur
```

Les deux feuilles sont entières, on garde la meilleure : **`(0,2)`, `z = −10`**.

**Élagage (bound)** : si la borne d'un nœud est **pire** que la meilleure solution entière connue, on abandonne cette branche.

---

### ④ Branch-and-Cut (B&C)

```
 Branch-and-Cut  =  Branch-and-Bound  +  Coupes à chaque nœud
```

Les coupes **resserrent les bornes**, donc on élague **plus tôt**.

> 🏭 Les solveurs modernes (**CPLEX**, Gurobi…) utilisent le Branch-and-Cut en interne.

---

### 📊 Comparaison

|Méthode|Principe|Point fort|Limite|
|---|---|---|---|
|**TU**|résoudre `RP`|très rapide|seulement certaines structures|
|**Coupes**|resserrer `F(RP)`|formulation plus serrée|nombreuses coupes possibles|
|**B&B**|diviser + borner|toujours exact|arbre parfois énorme|
|**B&C**|B&B + coupes|meilleur compromis|plus complexe|

---

### ✅ À retenir

1. **TU** : sommets entiers garantis ⟹ `RP` suffit
2. **Coupes** : on ajoute des contraintes qui retirent la solution fractionnaire
3. **B&B** : on énumère par division, on élague avec les bornes
4. **B&C** : les deux ensemble, c'est ce que font les solveurs
5. Ce cours se concentre sur les **méthodes de coupes**