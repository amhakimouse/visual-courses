

### 1. Idée en une phrase

On cherche le maximum d'une fonction linéaire sur un polyèdre convexe. L'optimum est toujours atteint en un **sommet**, donc le simplexe **se déplace de sommet en sommet** en améliorant Z à chaque pas, jusqu'à l'optimum.

```
 Problème (PL)                    Forme standard
 max Z = c·x                      max Z = c·x
 sous A·x ≤ b        ──────►      sous A·x + e = b
 x ≥ 0                            x, e ≥ 0   (e = variables d'écart)
```

### 2. Vocabulaire

|Terme|Sens|
|---|---|
|**Variables de base**|Celles qui sont ≠ 0 (une par contrainte)|
|**Variables hors base**|Fixées à 0|
|**Solution de base**|Un sommet du polyèdre|
|**Variable entrante**|Hors base → entre en base (améliore Z)|
|**Variable sortante**|En base → sort (la première contrainte qui "bloque")|
|**Pivot**|Élément à l'intersection colonne entrante / ligne sortante|

### 3. Les 4 étapes de l'algorithme

```
┌──────────────────────────────────────────────────────────┐
│ 0. Tableau initial (base = variables d'écart, x = 0)     │
└───────────────────────────┬──────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────┐
│ 1. TEST D'OPTIMALITÉ (max)                               │
│    Tous les coeffs de la ligne Z sont ≥ 0 ?              │
│        OUI ──► STOP : solution optimale                  │
│        NON ──► étape 2                                   │
└───────────────────────────┬──────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────┐
│ 2. VARIABLE ENTRANTE                                     │
│    Colonne du coeff le plus NÉGATIF de la ligne Z        │
└───────────────────────────┬──────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────┐
│ 3. VARIABLE SORTANTE (test du ratio minimum)             │
│    min { bᵢ / aᵢⱼ  |  aᵢⱼ > 0 }                          │
│    Aucun aᵢⱼ > 0 ──► problème NON BORNÉ                  │
└───────────────────────────┬──────────────────────────────┘
                            ▼
┌──────────────────────────────────────────────────────────┐
│ 4. PIVOTAGE (Gauss-Jordan)                               │
│    ligne pivot ÷ pivot, puis annuler le reste de la      │
│    colonne  ──► retour à l'étape 1                       │
└──────────────────────────────────────────────────────────┘
```