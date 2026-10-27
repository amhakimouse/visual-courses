

Soit le problème de minimisation d'affectation avec la matrice des coûts initiale $C$ (3 candidats et 3 postes) :

$$C = \begin{pmatrix} 2 & 5 & 7 \\ 4 & 2 & 1 \\ 2 & 6 & 5 \end{pmatrix}$$

### 🔄 Étape 1 : Transformation 1 (Réduction par Ligne)

Pour chaque ligne, on trouve le coût minimal ($\mu_i$) et on le soustrait à tous les éléments de la ligne :

- **Ligne 1** : minimum $\mu_1 = 2 \implies (2-2, \; 5-2, \; 7-2) = (0, 3, 5)$
    
- **Ligne 2** : minimum $\mu_2 = 1 \implies (4-1, \; 2-1, \; 1-1) = (3, 1, 0)$
    
- **Ligne 3** : minimum $\mu_3 = 2 \implies (2-2, \; 6-2, \; 5-2) = (0, 4, 3)$
    

On obtient la matrice $C^1$ :

$$C^1 = \begin{pmatrix} 0 & 3 & 5 \\ 3 & 1 & 0 \\ 0 & 4 & 3 \end{pmatrix}$$

### 🔄 Étape 2 : Transformation 2 (Réduction par Colonne)

Pour chaque colonne de la matrice $C^1$, on trouve le coût minimal ($v_j$) et on le soustrait à tous les éléments de la colonne :

- **Colonne 1** : minimum $v_1 = 0 \implies (0, 3, 0)^T$
    
- **Colonne 2** : minimum $v_2 = 1 \implies (3-1, \; 1-1, \; 4-1)^T = (2, 0, 3)^T$
    
- **Colonne 3** : minimum $v_3 = 0 \implies (5, 0, 3)^T$
    

On obtient la matrice $C^2$ :

$$C^2 = \begin{pmatrix} 0 & 2 & 5 \\ 3 & 0 & 0 \\ 0 & 3 & 3 \end{pmatrix}$$

### 🔍 Étape 3 : Test de Faisabilité (Couverture des Zéros)

Essayons de couvrir tous les zéros de $C^2$ avec le **nombre minimal de traits** :

- On trace une ligne horizontale sur la **Ligne 2** (qui contient deux zéros).
    
- On trace une ligne verticale sur la **Colonne 1** (qui contient les deux autres zéros).
    
- **Bilan** : Nous avons besoin de **$N = 2$ traits** en total.
    
- **Comparaison** : La taille de la matrice est $m = 3$. Comme $N = 2 < 3$, il est **impossible** de faire l'affectation tout de suite. Il faut passer à la Transformation 3.
    

### 🔄 Étape 4 : Transformation 3 (Ajustement de la matrice)

1. **Trouver $\rho$ (le plus petit élément non couvert)** :
    
    - Les cases non couvertes par nos deux traits sont : $2, 5, 3, 3$.
        
    - Le plus petit élément est **$\rho = 2$**.
        
2. **Appliquer les règles de modification** :
    
    - **Éléments non couverts** (on leur soustrait $2$) : $2-2=0$, $5-2=3$, $3-2=1$, $3-2=1$.
        
    - **Éléments à l'intersection** (Ligne 2 / Colonne 1, on lui ajoute $2$) : $3+2=5$.
        
    - **Éléments couverts par un seul trait** : restés intacts.
        

On obtient la nouvelle matrice $C^3$ :

$$C^3 = \begin{pmatrix} 0 & 0 & 3 \\ 5 & 0 & 0 \\ 0 & 1 & 1 \end{pmatrix}$$

- **Nouveau test de couverture** : Si on trace les traits sur cette matrice $C^3$, il faut cette fois **$3$ traits** pour couvrir tous les zéros ($N = m = 3$). Le test est validé, on peut procéder à l'affectation.
    

### 🎯 Étape 5 : Lecture de l'Affectation Optimale

On analyse la matrice $C^3$ en privilégiant les lignes ou colonnes qui possèdent un **seul zéro** :

1. La **Ligne 3** a un seul zéro en position $(3, 1)$ $\implies$ **Candidat 3 affecté au Poste 1**.
    
2. La **Ligne 1** a un seul zéro restant en position $(1, 2)$ $\implies$ **Candidat 1 affecté au Poste 2**.
    
3. Pour le **Candidat 2**, il ne reste que le zéro en position $(2, 3)$ $\implies$ **Candidat 2 affecté au Poste 3**.
    

### 💰 Étape 6 : Calcul du Coût Optimal

Rappel : On prend les coûts d'affectation sur la **matrice d'origine** $C$ :

- Affectation $(1 \to 2)$ : coût d'origine $= 5$
    
- Affectation $(2 \to 3)$ : coût d'origine $= 1$
    
- Affectation $(3 \to 1)$ : coût d'origine $= 2$
    

$$\text{Coût Total Optimal} = 5 + 1 + 2 = 8$$


