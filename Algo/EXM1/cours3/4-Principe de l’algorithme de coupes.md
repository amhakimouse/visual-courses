## Inégalité valide, plan coupant, coupe

> **Idée clé** : pour « couper » la solution fractionnaire sans casser le problème, il faut des contraintes **sûres**. Trois notions les décrivent.

---

### 1️⃣ Les 3 définitions

```
 Soit P un PLNE, F(P) ses points entiers réalisables,
 et  π·x ≤ π₀  une inégalité linéaire.
```

|Notion|Définition|Condition|
|---|---|---|
|**Inégalité valide**|`π·x ≤ π₀`|satisfaite par **tous** les `x ∈ F(P)`|
|**Plan coupant**|l’hyperplan `π·x = π₀`|issu d’une inégalité valide|
|**Coupe**|inégalité valide **qui élimine** `x̄`|**violée** par `x̄` (optimum de `RP`)|

```
 Coupe  =  valide pour F(P)   +   violée par x̄
           (ne perd rien)         (progresse)
```

---

### 2️⃣ Test sur l’exemple

`F(P) = {(0,0),(1,0),(2,0),(0,1),(1,1),(2,1),(0,2)}` et `x̄ = (2 ; 1,8)`

| Inégalité        | Valide ?            | Violée par `x̄` ?   | Verdict                             |
| ---------------- | ------------------- | ------------------- | ----------------------------------- |
| `x₁ ≤ 2`         | ✅ tous les points   | ❌ `2 ≤ 2`           | valide, **pas une coupe** (inutile) |
| `x₂ ≤ 1`         | ❌ `(0,2)` : `2 > 1` | ✅                   | **invalide** (perd l’optimum)       |
| **x₁ + 2x₂ ≤ 4** | ✅                   | ✅ `2+3,6 = 5,6 > 4` | **coupe** 🎯                        |


Vérification de la coupe sur les points entiers :

```
 (0,0)→0  (1,0)→1  (2,0)→2  (0,1)→2  (1,1)→3  (2,1)→4  (0,2)→4
                                                  tous ≤ 4 ✅
```

---

### 4️⃣ Les 3 cas

```
 Inégalité π·x ≤ π₀
     │
     ├─ perd un point entier de F(P) ──► ❌ INVALIDE   (dangereuse)
     │
     ├─ valide mais satisfaite par x̄ ──► 💤 inutile     (ne change rien)
     │
     └─ valide ET violée par x̄ ────────► ✂️ COUPE       (progrès)
```

---

![[Pasted image 20261011115201.png|637]]

## Principe de l’algorithme de coupes

> **Idée clé** : on ne touche **pas** à `F(P)` (les points ●). On **rabote** `F(RP)` (la zone verte) avec des coupes jusqu’à ce que son optimum devienne entier.

---

### 1️⃣ Les deux conditions sur le problème modifié `PA`

```
 ① F(PA)  =  F(P)       ← mêmes points entiers (aucune perte)
 ② F(RPA) ⊂  F(RP)      ← polygone strictement plus petit (progrès)
```

| Condition | Rôle                           | Sur le graphe                                  |
| --------- | ------------------------------ | ---------------------------------------------- |
| **①**     | la coupe est **valide**        | les 7 points ● restent tous dans la zone verte |
| **②**     | la coupe est **violée par x̄** | le sommet rouge `(2 ; 1,8)` est retiré         |

---

### 2️⃣ La boucle

```
 ┌──────────────────────────────────────┐
 │  ① Résoudre RP  →  solution x̄       │◄──────────┐
 └──────────────────┬───────────────────┘           │
                    ▼                               │
            ┌───────────────┐                       │
            │ x̄ est entier ? │                      │
            └───┬───────┬───┘                       │
            OUI │       │ NON                       │
                ▼       ▼                           │
         ┌─────────┐  ┌───────────────────────┐     │
         │ ✅ FIN  │  │ ② Générer une coupe   │     │
         │ x̄ opt.  │  │   valide, violée par x̄│     │
         │ de P    │  └──────────┬────────────┘     │
         └─────────┘             ▼                  │
                       ┌───────────────────┐        │
                       │ ③ L'ajouter à P   │────────┘
                       │   (RP devient RP')│
                       └───────────────────┘
```

---

### 3️⃣ Déroulement sur l’exemple

|Itération|Problème|Optimum|z|Entier ?|
|---|---|---|---|---|
|**0**|`RP`|`(2 ; 1,8)`|−11|❌|
|**1**|`RP'` = `RP` + `x₁ + 2x₂ ≤ 4`|`(0 ; 2)`|**−10**|✅ **stop**|

Vérification de la coupe sur `x̄` : `2 + 2·1,8 = 5,6 > 4` ➜ **violée** ✅  
Sur le point `(0,2)` : `0 + 4 = 4 ≤ 4` ➜ **respectée** ✅

---

### 4️⃣ Pourquoi ça converge ?

```
 Chaque coupe rend x̄ infaisable  ➜  F(RP) rétrécit
                                  ➜  on tend vers l'enveloppe convexe de F(P)
```

⚠️ Le nombre de coupes peut être grand ; en pratique on combine avec le **Branch-and-Bound** (= Branch-and-Cut).

---
