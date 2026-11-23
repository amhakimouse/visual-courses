### problem d'affectation

- $n$ : le nombre d'éléments à affecter ($n = 4$).
    
- $c_{ij}$ : la distance entre le taxi $i$ et le client $j$ ($i, j \in \{1, 2, 3, 4\}$).
    
- $x_{ij}$ : la variable de décision binaire telle que :
$$x_{ij} = \begin{cases} 1 & \text{si le taxi } i \text{ est affecté au client } j \\ 0 & \text{sinon} \end{cases}$$
    

$$\begin{aligned} \text{Min } Z = & \sum_{i=1}^{n} \sum_{j=1}^{n} c_{ij} \cdot x_{ij} \\ \text{s.c. } & \sum_{j=1}^{n} x_{ij} = 1, \quad \forall i \in \{1, \dots, n\} \quad \text{(Chaque taxi transporte exactement 1 client)} \\ & \sum_{i=1}^{n} x_{ij} = 1, \quad \forall j \in \{1, \dots, n\} \quad \text{(Chaque client est servi par exactement 1 taxi)} \\ & x_{ij} \in \{0, 1\}, \quad \forall i, j \in \{1, \dots, n\} \end{aligned}$$

#### Application numérique au cas de la compagnie de taxi

Soit $C$ la matrice des distances $c_{ij}$ donnée par l'énoncé :

$$C = \begin{pmatrix} 6 & 3 & 4 & 5 \\ 4 & 5 & 4 & 6 \\ 3 & 6 & 6 & 7 \\ 4 & 4 & 3 & 5 \end{pmatrix}$$

### Programme Linéaire explicite :

$$\begin{aligned} \text{Min } Z = & \ 6x_{11} + 3x_{12} + 4x_{13} + 5x_{14} \\ & + 4x_{21} + 5x_{22} + 4x_{23} + 6x_{24} \\ & + 3x_{31} + 6x_{32} + 6x_{33} + 7x_{34} \\ & + 4x_{41} + 4x_{42} + 3x_{43} + 5x_{44} \end{aligned}$$

**Sous les contraintes :**

- Taxis :
    
    $$\begin{aligned} x_{11} + x_{12} + x_{13} + x_{14} &= 1 \\ x_{21} + x_{22} + x_{23} + x_{24} &= 1 \\ x_{31} + x_{32} + x_{33} + x_{34} &= 1 \\ x_{41} + x_{42} + x_{43} + x_{44} &= 1 \end{aligned}$$
    
- Clients :
    
    $$\begin{aligned} x_{11} + x_{21} + x_{31} + x_{41} &= 1 \\ x_{12} + x_{22} + x_{32} + x_{42} &= 1 \\ x_{13} + x_{23} + x_{33} + x_{43} &= 1 \\ x_{14} + x_{24} + x_{34} + x_{44} &= 1 \end{aligned}$$
    
- Non-négativité et intégrité : $x_{ij} \in \{0, 1\}, \ \forall i, j \in \{1, 2, 3, 4\}$.


### LE TRUC : Comment déterminer l'ordre des nœuds

$$P(0,0) \longrightarrow P(1,0) \longrightarrow P(2,0) \longrightarrow P(3,0) \text{ puis } P(k,i)$$
### la stratégie « Meilleur d'abord »

À chaque étape, parmi tous les nœuds ouverts (non encore séparés), **on choisit le nœud qui a la plus grande valeur de $Z$ (la plus forte borne supérieure)**


### LE TRUC GÉNÉRAL : La Recette pour construire l'Arbre

### Le truc en 4 réflexes

1. **Relaxer** : résoudre le PL en ignorant “entier”. Sa valeur donne la borne supérieure (pour un max).
2. **Choisir une variable fractionnaire** xⱼ = a, puis créer deux fils : xⱼ ≤ ⌊a⌋ et xⱼ ≥ ⌈a⌉.
3. **Résoudre chaque fils** en ajoutant la contrainte au problème du père.
4. **Élaguer** (arrêter la branche) dans 3 cas :
    - infaisable
    - solution entière (on met à jour la meilleure borne inférieure Z_best)
    - Z du nœud ≤ Z_best (inutile de continuer, pour un max)

On s’arrête quand tous les nœuds sont fermés. La meilleure solution entière trouvée est l’optimum.

### Exemple

Max Z = 5x₁ + 4x₂  
s.c. 6x₁ + 4x₂ ≤ 24 ; x₁ + 2x₂ ≤ 6 ; x₁, x₂ entiers ≥ 0

![[Pasted image 20261029222531.png]]