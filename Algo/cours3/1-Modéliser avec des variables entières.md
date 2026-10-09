
> **Idée clé** : une variable binaire `y ∈ {0,1}` traduit une **décision oui/non** ou une **condition logique** dans un modèle linéaire.

---

### 1️⃣ Sac à dos (knapsack)

Choisir des objets de valeur `vᵢ` et poids `pᵢ`, capacité `P`.

```
 xᵢ = 1 si objet i pris, 0 sinon

 Max  Σ vᵢ xᵢ          ← valeur totale
 s.c. Σ pᵢ xᵢ ≤ P      ← capacité du sac
      xᵢ ∈ {0,1}
```

---

### 2️⃣ Stable de poids max

Choisir des sommets d'un graphe, **sans deux voisins**.

```
   1 ───── 2          xᵥ = 1 si sommet v choisi
   │ ╲     │
   │   ╲   │          Max  Σ wᵥ xᵥ
   4 ───── 3          s.c. xᵤ + xᵥ ≤ 1   pour toute arête (u,v)
                           xᵥ ∈ {0,1}
```

Si l'arête `(u,v)` existe, `xᵤ + xᵥ ≤ 1` interdit de prendre les deux.

---

### 3️⃣ Localisation (modèle **mixte**)

Où construire des usines pour servir des clients au moindre coût ?

|Symbole|Sens|
|---|---|
|`aᵢ`|coût de construction du site _i_|
|`uᵢ`|capacité du site _i_|
|`bᵢ`|coût de production unitaire|
|`cᵢⱼ`|coût de transport _i → j_|
|`dⱼ`|demande du client _j_|
|**`yᵢ ∈ {0,1}`**|1 si usine construite en _i_|
|**`xᵢⱼ ≥ 0`** (réel)|quantité envoyée de _i_ à _j_|

```
 Min  Σ aᵢ yᵢ  +  Σ (bᵢ + cᵢⱼ) xᵢⱼ
      └─ fixe ─┘   └──── variable ────┘

 s.c. Σᵢ xᵢⱼ = dⱼ         ∀ j   ← demande satisfaite
      Σⱼ xᵢⱼ ≤ uᵢ yᵢ      ∀ i   ← 🔑 contrainte logique
      yᵢ ∈ {0,1},  xᵢⱼ ≥ 0
```

**🔑 Le lien `Σⱼ xᵢⱼ ≤ uᵢ yᵢ` :**

```
 yᵢ = 0  →  Σⱼ xᵢⱼ ≤ 0   →  aucun flux (pas d'usine)
 yᵢ = 1  →  Σⱼ xᵢⱼ ≤ uᵢ  →  flux limité par la capacité
```

---

### 4️⃣ Contraintes mutuellement exclusives (méthode **Big-M**)

On veut : **soit** `3x₁+2x₂ ≤ 18`, **soit** `x₁+4x₂ ≤ 16`.

On introduit `y ∈ {0,1}` et un très grand `M` :

```
 3x₁ + 2x₂ ≤ 18 + M·y
  x₁ + 4x₂ ≤ 16 + M·(1 − y)
```

|`y`|Contrainte 1|Contrainte 2|
|---|---|---|
|**0**|`≤ 18` ✅ active|`≤ 16 + M` 💤 inutile|
|**1**|`≤ 18 + M` 💤 inutile|`≤ 16` ✅ active|

➜ `M` « désactive » une contrainte en la rendant toujours vraie.  
⚠️ Le modèle impose **au moins une** des deux ; l'autre peut aussi être vérifiée.

---

### 5️⃣ Fonction à N valeurs possibles

`f(x) = d₁ **ou** d₂ **ou** … **ou** d_N`

```
 f(x) = Σ dⱼ yⱼ
 Σ yⱼ = 1          ← exactement une valeur choisie
 yⱼ ∈ {0,1}
```

**Exemple du cours** : temps de production = 6 h, 12 h ou 18 h

```
 3x₁ + 2x₂ = 6y₁ + 12y₂ + 18y₃
 y₁ + y₂ + y₃ = 1

 y = (0,1,0)  →  3x₁ + 2x₂ = 12 ✅
```

---

### ✅ À retenir

| Besoin                   | Outil                    |
| ------------------------ | ------------------------ |
| Choisir / ne pas choisir | `x ∈ {0,1}`              |
| Coût fixe + flux         | `Σ xᵢⱼ ≤ uᵢ yᵢ`          |
| « Soit A soit B »        | Big-M + `y`              |
| « Valeur parmi N »       | `N` binaires, `Σ yⱼ = 1` |