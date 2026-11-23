### Problème et tableau optimal de `RP`

```
 Max Z = 9x₁ + 2x₂ + 5x₃
 s.c.   4x₁ + 2x₂ − 4x₃ ≤ 4
        2x₁ −  x₂ + 8x₃ ≤ 4
        2x₁ + 4x₂ +  x₃ ≤ 3        x ≥ 0 entiers
```

```
 XB │ x1  x2  x3 │   t1     t2     t3  │  Sol
 ───┼────────────┼─────────────────────┼──────
 x1 │  1   0   0 │ 11/48   1/8   −1/12 │  7/6
 x2 │  0   1   0 │ −7/72  −1/12   5/18 │  1/9
 x3 │  0   0   1 │ −5/72   1/12   1/18 │  2/9
 zj │  0   0   0 │ 73/48  11/8    1/12 │ 71/6
```

Solution de `RP` : `(7/6 ; 1/9 ; 2/9)`, `z = 71/6 ≈ 11,83` ➜ fractionnaire.

![[Pasted image 20261011123451.png]]

```
 Coupe :  −(67/72)t₁ − (1/12)t₂ − (1/18)t₃  ≤  −2/9
 Écart  :  −(67/72)t₁ − (1/12)t₂ − (1/18)t₃ + t₄ = −2/9
```

Nouvelle ligne du tableau : **`t₄ = −2/9 < 0`** ➜ infaisable ➜ dual simplexe.

### 4️⃣ Dual simplexe

```
 Ligne sortante : t₄ (second membre négatif)

 Test du ratio (colonnes à coefficient < 0) :  zⱼ / |coef|
   t₁ : (73/48) / (67/72) ≈ 1,63
   t₂ : (11/8)  / (1/12)  = 16,5
   t₃ : (1/12)  / (1/18)  = 1,5   ← minimum ✅  (t₃ entre)
```

Après ce 1ᵉʳ pivot, `x₂ = −1 < 0` ➜ 2ᵉ pivot (x₂ sort, t₁ entre). Résultat :

```
 XB │  x2     t2     t4  │  Sol
 ───┼────────────────────┼───────
 x1 │ 13/38   3/38   4/19│ 22/19
 t1 │ −4/19   2/19 −20/19│  4/19
 x3 │ −4/19   2/19  −1/19│  4/19
 t3 │ 67/19  −5/19  −7/19│  9/19
 zj │  1/38  47/38  31/19│ 218/19
```

Solution : `x = (22/19 ; 0 ; 4/19)`, `z = 218/19 ≈ 11,47` : toujours fractionnaire ➜ **nouvelle coupe**.

### 5️⃣ La boucle jusqu’au bout

Avec la même règle, chaque coupe fait **baisser** la borne supérieure :

```
 coupe 0 (RP)  11,83 ████████████████████████
 coupe 1       11,47 ███████████████████████
 coupe 2       10,83 ██████████████████████
 coupe 3       10,68 █████████████████████
 coupe 4       10,25 ████████████████████
 coupe 5        9,73 ███████████████████
 coupe 6        9,69 ███████████████████
 coupe 7        9,04 ██████████████████
 coupe 8        9,00 ██████████████████  ✅ entier : STOP
```

**Optimum entier : `x = (1, 0, 0)`, `Z = 9`**  
Vérif : `4 ≤ 4` ✅ · `2 ≤ 4` ✅ · `2 ≤ 3` ✅.

⚠️ Gomory converge, mais souvent **lentement** (ici 8 coupes pour 3 variables), d’où l’intérêt des coupes de structure et du Branch-and-Cut.

---

## 📘 Concept 10 : Coupes de structure (stable max)

> **Idée** : au lieu de coupes génériques (Gomory), on utilise des inégalités **propres au problème**.

### 1️⃣ Le problème

```
 Max  Σ c(u) x(u)                   x(u) = 1 si le sommet u est choisi
 s.c. x(u) + x(v) ≤ 1   ∀ arête uv ∈ E
      x(u) ∈ {0,1}      ∀ u ∈ V
```

La relaxation est **non entière** (sinon le stable serait polynomial). Exemple, un triangle avec poids 1 :

```
        1
       ╱ ╲          x = (½, ½, ½) respecte  ½ + ½ ≤ 1  sur chaque arête
      2───3         valeur RP = 3/2   |   vrai optimum = 1 (un seul sommet)
      
```

### 2️⃣ Inégalité de clique

Une **clique** `K` = sommets tous reliés entre eux.

$$\sum_{u\in K} x(u) \le 1$$

```
 Pourquoi valide : 2 sommets d'une clique sont voisins
                   ⇒ au plus 1 dans un stable.
 Triangle K = {1,2,3} :  x₁ + x₂ + x₃ ≤ 1
 Test sur x̄ = (½,½,½)  :  3/2 > 1  ⇒ violée ✅ (c'est une coupe)
```

### 3️⃣ Inégalité de cycle impair

Un **cycle impair** `C` : cycle de longueur impaire (3, 5, 7…).

$$\sum_{u\in V(C)} x(u) \le \frac{|C|-1}{2}$$

```
 Exemple C₅ (5 sommets, aucun triangle) :
           1
         ╱   ╲
        5     2        Contrainte : x₁+x₂+x₃+x₄+x₅ ≤ (5−1)/2 = 2
        │     │
        4 ─── 3        x̄ = (½,½,½,½,½)  ⇒  5/2 > 2  ⇒ violée ✅
```

```
 Pourquoi valide : dans un cycle de longueur 2k+1, on peut prendre
                   au plus k sommets non adjacents.
 Les cliques ne coupent PAS C₅ (pas de triangle) : il faut les cycles impairs.
```

### 4️⃣ Comparaison

|Coupes|Principe|Avantage|Limite|
|---|---|---|---|
|**Gomory**|tirées du tableau|marche pour tout PLNE|nombreuses, converge lentement|
|**Structurelles**|inégalités du problème (clique, cycle impair)|fortes, peu nombreuses|spécifiques à chaque problème|

---

### ✅ À retenir (9 + 10)

1. **Gomory** : choisir la ligne de plus grande `{bᵢ}`, coupe `Σ(⌊t⌋−t)x ≤ ⌊b⌋−b`, dual simplexe, répéter
2. Chaque coupe fait baisser la borne (Max) : `11,83 → … → 9`
3. **Clique** : `Σ_{K} x ≤ 1` · **Cycle impair** : `Σ_{C} x ≤ (|C|−1)/2`
4. Ces inégalités sont **valides** et **violées** par `x = (½,…,½)`