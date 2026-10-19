### Pourquoi ce concept ?

C’est **l’outil qui calcule la borne** dans le B&B (ingrédient 3). Sans lui, pas d’évaluation.

---

### 1️⃣ Définition

$$(P)\;\; \min \sum_{j=1}^{n} c_j x_j \quad \text{s.c.} \quad \sum_{j=1}^{n} a_{ij}x_j = b_i,\;\; x_j \ge 0,\; \boxed{x_j \in \mathbb{Z}}$$

**Relaxation** $(\bar P)$ : on **enlève** la contrainte d’intégralité :

$$\boxed{x_j \in \mathbb{Z}} \;\;\longrightarrow\;\; x_j \ge 0 \quad(\text{réels autorisés})$$

||$(P)$ PLNE|$(\bar P)$ Relaxation|
|---|---|---|
|Variables|entières|réelles|
|Difficulté|NP-complet |**Simplexe**, rapide |

---

### 2️⃣ Propriété clé : la borne

$$F(P) \subset F(\bar P) \;\;\Longrightarrow\;\; \boxed{c^\top \bar x \;\le\; c^\top x^*}$$

avec $x^*$ optimum de $(P)$ et $\bar x$ optimum de $(\bar P)$.

```
 Valeur de z (minimisation)
 ──────────────────────────────────────────────▶
      z̄ (relaxé)        z* (entier)
        ●─────────────────●
   borne inférieure     vrai optimum
   (optimiste)
```

> 💡 Domaine **plus grand** ⟹ on a plus de choix ⟹ le minimum ne peut qu’être **meilleur ou égal**.

---

### 3️⃣ Exemple numérique

$$\min z = -3x_1 - 2x_2 \quad \text{s.c.} \quad 2x_1 + x_2 \le 6.5,\;\; x_1, x_2 \ge 0$$

||Solution|$z$|
|---|---|---|
|**Relaxation** $(\bar P)$|$x_1 = 0,\; x_2 = 6.5$ _(non entière)_|$\bar z = -13$|
|**Entier** $(P)$|$x_1 = 0,\; x_2 = 6$|$z^* = -12$|

$$\bar z = -13 \;\le\; z^* = -12 \quad ✅$$

**Écart** (gap) $= 1$ : c’est ce que B&B va réduire en séparant.

---

### 4️⃣ Les 3 conséquences utiles pour B&B

|Résultat de $(\bar P)$|Conclusion sur $(P)$|
|---|---|
|$(\bar P)$ **non réalisable** ($F=\emptyset$)|$(P)$ non réalisable ⟹ ❌ élaguer|
|Solution $\bar x$ **entière**|$\bar x$ est **optimale** pour ce sous-problème ⟹ ✅ feuille|
|Solution $\bar x$ **non entière**|$\bar z$ sert de **borne** ⟹ comparer à $b_0$, puis 🔀 séparer si $\bar z < b_0$|

---

### 🧠 À retenir

$$\boxed{\text{Relaxation} = \text{PLNE sans l'intégralité} \;\Rightarrow\; \text{borne inférieure (min) calculable par le simplexe}}$$