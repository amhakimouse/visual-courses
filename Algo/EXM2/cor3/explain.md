
# Le Problème de l'Arbre de Steiner

Le **problème de l'arbre de Steiner** dans un graphe non orienté $G = (V, E)$ muni de coûts sur les arêtes $c_e \ge 0$ consiste à trouver un arbre de poids minimal qui relie un sous-ensemble de sommets obligatoires $T \subseteq V$ appelés **terminaux**

*EX*
![[Pasted image 20261124101950.png]]

($S = 0$):
1. **Restriction du graphe** : On conserve uniquement les sommets $T = \{a, b, c\}$.
    
2. **Calcul de l'ARPM (Arbre Recouvrant de Poids Minimum)** sur $\{a, b, c\}$ :
    
    - Pour connecter $a$, $b$ et $c$, il faut sélectionner $2$ arêtes sans créer de cycle.
        
    - On retient l'arête $(a, b)$ de poids $4$ et l'arête $(b, c)$ de poids $4$.
        
3. **Coût total de la solution initial** :
    
    $$\text{Coût}(X = \emptyset) = 4 + 4 = 8$$
`Insertion du sommet S 

L'arbre couvrant le plus économique relie directement les $3$ terminaux au sommet central $s$ via les arêtes $(a,s)$, $(b,s)$ et $(c,s)$.
$$\text{Coût}(X = \{s\}) = 2 + 2 + 2 = 6$$
#### Décision de l'Algorithme

On calcule la variation de la fonction objectif :

$$\Delta \text{Coût} = \text{Coût}(X = \{s\}) - \text{Coût}(X = \emptyset) = 6 - 8 = -2 < 0$$

Puisque $\Delta \text{Coût} < 0$, le mouvement d'insertion du sommet $s$ améliore la solution. L'algorithme **valide le mouvement** et retient la solution $X = \{s\}$ avec un coût optimal de $6$.

