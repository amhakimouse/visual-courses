## Plan du Cours 3 : PLNE & Méthodes de coupes

```
 C1  PLNE : définition, types, forme générale      ◄── on commence ici
 C2  Modélisation (sac à dos, localisation, "ou", N valeurs)
 C3  Relaxation linéaire + borne
 C4  Arrondir ne marche pas
 C5  Idées algorithmiques (TU, coupes, B&B, B&C)
 C6  Inégalité valide / plan coupant / coupe
 C7  Principe de l'algorithme de coupes
 C8  Coupe de Gomory (construction)
 C9  Gomory : exemple complet (dual simplexe)
 C10 Coupes structurelles (stable max)
```

---

## 📘 Concept 1 : Qu'est-ce qu'un PLNE ?

### 1️⃣ Idée

Un **PL** classique accepte `x = 2,7`. Mais certaines décisions sont **discrètes** : 2,7 usines ? 0,5 camion ? ➜ impossible.

> **PLNE** = PL où les variables doivent être **entières**.

### 2️⃣ Forme générale

```
 Min   Σ cⱼ xⱼ                    j = 1..n      ← objectif
 s.c.  Σ aᵢⱼ xⱼ = bᵢ              i = 1..m      ← m contraintes
       xⱼ ≥ 0 ET entier           j = 1..n      ← ⚠️ seule différence avec un PL
```

### 3️⃣ Les 3 types

|Type|Variables|Exemple|
|---|---|---|
|**PLNE pur**|toutes entières|nb de machines|
|**Binaire (0-1)**|`xⱼ ∈ {0,1}`|construire (1) ou non (0)|
|**Mixte (PLNEM)**|certaines entières, d'autres réelles|usine `yᵢ ∈{0,1}` + flux `xᵢⱼ ∈ ℝ`|

### 4️⃣ Exemple du cours : le domaine réalisable `F(P)`

```
 Min z = −x₁ − 5x₂
 s.c.  x₁ + 10x₂ ≤ 20
       x₁ ≤ 2
       x₁, x₂ ≥ 0 entiers
```

On ne garde que les **points à coordonnées entières** :

```
 x₂
  2 │ ●  ·  ·          ●  = point réalisable
  1 │ ●  ●  ●          ·  = entier mais interdit
  0 │ ●  ●  ●             (ex. (1,2) : 1+20 = 21 > 20 ❌)
    └──┴──┴──┴──► x₁
      0  1  2
```

$$F(P)=\{(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2)\}$$

➜ **7 points seulement** : le domaine n'est plus un polygone continu, mais un **ensemble fini de points isolés**.

### 5️⃣ Pourquoi c'est difficile ?

```
 PL   :  domaine convexe  → optimum en un sommet → simplexe efficace ✅
 PLNE :  points isolés    → pas de convexité     → problème NP-difficile ⚠️
```

### ✅ À retenir

1. PLNE = PL **+ contrainte d'intégralité** `xⱼ ∈ ℤ`
2. Binaire (0-1) ⊂ pur ⊂ mixte (selon quelles variables sont entières)
3. `F(P)` = **ensemble de points entiers** réalisables