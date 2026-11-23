> **Idée clé** : si le PLNE est trop dur, on **oublie l'intégralité** et on résout un simple PL. Ça donne une **borne** sur la vraie réponse.

---

### 1️⃣ Définition

```
 (P)  PLNE                          (RP)  Relaxation
 ─────────────────────              ─────────────────────
 Min  cᵀx                           Min  cᵀx
 s.c. Ax = b                        s.c. Ax = b
      x ≥ 0 ET entier  ──────────►       x ≥ 0          ← on enlève "entier"
```

> `RP` = `P` **sans** les contraintes d'intégralité. C'est un **PL** : le simplexe le résout.

---

### 2️⃣ Conséquence sur les domaines

```
 F(P)  ⊂  F(RP)
 (points entiers)   (tout le polygone)
```

`RP` a **plus** de solutions possibles, donc au moins aussi bonne.

---

### 3️⃣ La borne (cas **Min**)

Soit `x*` optimal de `P` et `x̄` optimal de `RP` :

$$\boxed{\;c^T\bar x \;\le\; c^T x^*\;}$$

```
 z
 ──┼───────────┼───────────┼──►
  z(RP)      z(P)        z(point entier quelconque)
  borne      optimum     solutions réalisables
  inférieure vrai
```

|Problème|La relaxation donne une…|
|---|---|
|**Min**|borne **inférieure**|
|**Max**|borne **supérieure**|

---

### 4️⃣ Exemple du cours

```
 Min z = −x₁ − 5x₂
 s.c.  x₁ + 10x₂ ≤ 20 ,  x₁ ≤ 2 ,  x ≥ 0
```

```
 x₂
 2.0 ●╲
     │ ╲
 1.8 │  ╲──★  ← optimum RP : (2 ; 9/5), z = −11
 1.0 ●───●──●      ↑ non entier ❌
     │░░░░░░░│  x₁ = 2
 0   ●───●───●──► x₁
     0   1   2

 ░ = F(RP) (zone continue)      ● = F(P) (points entiers)
```

![[Pasted image 20261006112650.png]]

$$-11 \;\le\; -10 \quad ✅$$

La relaxation donne `−11` : le vrai optimum ne peut **pas** être meilleur que ça.

---

### 5️⃣ Ce que la relaxation permet de conclure

```
 Résoudre RP
     │
     ├─ RP infaisable ───────────► P infaisable aussi
     │
     ├─ x̄ entier ────────────────► x̄ est optimal pour P 🎉
     │
     └─ x̄ fractionnaire ─────────► on obtient seulement une borne
                                   (il faut travailler davantage)
```

C'est le **point de départ** de toutes les méthodes (coupes, Branch-and-Bound).

---

### ✅ À retenir

1. `RP` = `P` sans « entier » ➜ c'est un **PL**
2. `F(P) ⊂ F(RP)`
3. **Min** : `z(RP) ≤ z(P)` (borne inférieure) · **Max** : `z(RP) ≥ z(P)`
4. Si la solution de `RP` est entière ➜ elle est **optimale** pour `P`

## Pourquoi arrondir ne marche pas

> **Idée tentante** : résoudre `RP`, puis arrondir la solution fractionnaire. Simple, mais **faux en général**.

---

### 1️⃣ Rappel de l'exemple

```
 Min z = −x₁ − 5x₂
 s.c.  x₁ + 10x₂ ≤ 20 ,  x₁ ≤ 2 ,  x ≥ 0 entiers
```

Optimum de `RP` : `x̄ = (2 ; 9/5)`, `z = −11`

---

### 2️⃣ Les arrondis possibles

```
 x₂
 2 │ ●(0,2)   ✖(2,2)        ★ = optimum RP (2 ; 1,8)
   │      ╲    │             ● = réalisable
 1.8│       ╲──★
 1 │ ●───●───●(2,1)          ✖ = non réalisable
   │ ░░░░░░░░░│
 0 ●───●───●──────► x₁
   0   1   2
```

|Arrondi de `(2 ; 1,8)`|Point|Réalisable ?|z|
|---|---|---|---|
|**vers le haut**|`(2,2)`|❌ `2 + 20 = 22 > 20`|—|
|**vers le bas**|`(2,1)`|✅|**−7**|
|**vrai optimum**|`(0,2)`|✅|**−10**|

---

### 3️⃣ Comparaison

```
 z :  −11 ──────── −10 ──────── −7
       │             │            │
    optimum RP   optimum P    solution arrondie
    (borne)      (vrai)       (mauvaise)

                 écart = 3 unités ⚠️
```

L'arrondi `(2,1)` est réalisable mais **loin de l'optimum**. Le vrai optimum `(0,2)` est même **à l'opposé** (`x₁` passe de 2 à 0).