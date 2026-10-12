> **Idée clé** : on prend **une ligne du tableau optimal** dont le second membre est fractionnaire, et on en déduit **automatiquement** une coupe.

---

### 1️⃣ Point de départ

Tableau optimal de `RP`. Une variable de base `xₖ` a une valeur **non entière** :

```
 xₖ + Σ  tᵢⱼ xⱼ  =  bᵢ          (1)       bᵢ ∉ ℤ
     j∈J
 J = indices des variables HORS base      (valent 0 dans la solution actuelle)
```

Notation : `⌊d⌋` = **partie entière** (plus grand entier ≤ d). Exemples : `⌊10/3⌋ = 3`, `⌊−1/3⌋ = −1`, `⌊2/3⌋ = 0`.

---

### 2️⃣ Construction en 4 étapes

```
 (1)  xₖ + Σ tᵢⱼ xⱼ  =  bᵢ
              │
              ▼  ① xⱼ ≥ 0  ⇒  ⌊tᵢⱼ⌋ xⱼ ≤ tᵢⱼ xⱼ
 (2)  xₖ + Σ ⌊tᵢⱼ⌋ xⱼ  ≤  bᵢ
              │
              ▼  ② le membre de gauche est ENTIER (variables entières)
                    donc ≤ bᵢ  ⇒  ≤ ⌊bᵢ⌋
 (3)  xₖ + Σ ⌊tᵢⱼ⌋ xⱼ  ≤  ⌊bᵢ⌋          ← valide pour tout point de F(P)
              │
              ▼  ③ (3) − (1)
 (4)  Σ (⌊tᵢⱼ⌋ − tᵢⱼ) xⱼ  ≤  ⌊bᵢ⌋ − bᵢ   ← la coupe de Gomory
```

|Étape|Pourquoi c’est permis|
|---|---|
|①|`xⱼ ≥ 0` et `⌊t⌋ ≤ t`|
|②|la seule étape qui utilise l’**intégralité**|
|③|soustraction : on élimine `xₖ`|

---

### 3️⃣ Pourquoi (4) est bien une coupe ?

```
 Valide  : (4) découle de (1) et (3), que tout point entier de P satisfait
           ➜ aucun point de F(P) n'est retiré ✅

 Violée  : à la solution actuelle, xⱼ = 0  ∀ j ∈ J
           ➜ le membre de gauche vaut 0
           ➜ mais le membre de droite ⌊bᵢ⌋ − bᵢ < 0
           ➜ 0 ≤ (nombre négatif)  est FAUX  ⇒  x̄ est éliminé ✅
```

**Forme équivalente** (avec la partie fractionnaire `{d} = d − ⌊d⌋`) :

$$\sum_{j\in J} \{t_{ij}\}\, x_j \;\ge\; \{b_i\}$$

---

### 4️⃣ Exemple du cours

Tableau optimal :

```
 XB │ x1  x2  x3 │  t1    t2  │ Sol
 ───┼────────────┼────────────┼──────
 x1 │  1   0   1 │  2/3  −1/3 │ 10/3
 x2 │  0   1   1 │ −1/3   2/3 │ 10/3
 z  │  0   0   7 │   0     3  │  30
```

**Ligne de `x₁`** : `x₁ + x₃ + (2/3)t₁ − (1/3)t₂ = 10/3`

|Terme|`x₃`|`t₁`|`t₂`|second membre|
|---|---|---|---|---|
|coefficient `t`|1|2/3|−1/3|10/3|
|`⌊t⌋`|1|0|**−1**|3|
|`⌊t⌋ − t`|0|−2/3|**−2/3**|−1/3|

Coupe (4) :

```
 −(2/3) t₁ − (2/3) t₂  ≤  −1/3     ⟺     t₁ + t₂ ≥ 1/2
```

⚠️ Piège : `⌊−1/3⌋ = −1` (pas 0), le plancher d’un négatif descend.

**Ligne de `x₂`** : mêmes parties fractionnaires (`2/3`, `2/3`, `1/3`) ➜ **même coupe** `t₁ + t₂ ≥ 1/2`.

---

### 5️⃣ Après la coupe : variable d’écart et dual simplexe

```
 −(2/3) t₁ − (2/3) t₂ + t₃ = −1/3          t₃ ≥ 0 : écart, coût nul
```

```
 Nouvelle ligne du tableau :  t₃ = −1/3 < 0   ➜ solution NON réalisable
                                              ➜ on continue avec le DUAL SIMPLEXE
```

Le dual simplexe corrige l’infaisabilité en gardant l’optimalité, puis on retest l’intégralité (Concept 7).

---

### ✅ À retenir

1. On choisit une ligne avec `bᵢ` **fractionnaire**
2. Coupe : `Σ (⌊tᵢⱼ⌋ − tᵢⱼ) xⱼ ≤ ⌊bᵢ⌋ − bᵢ`, soit `Σ {tᵢⱼ} xⱼ ≥ {bᵢ}`
3. **Valide** (grâce à l’intégralité) et **violée** par `x̄` (0 contre un négatif)
4. On ajoute une variable d’écart ➜ **dual simplexe**
5. Cas spécial : si tous les `tᵢⱼ` sont **entiers** et `bᵢ` fractionnaire ➜ `P` est **infaisable** (un entier ne peut pas égaler une fraction)