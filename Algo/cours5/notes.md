
Le **problème d'affectation** consiste à assigner un ensemble de $m$ candidats (ou ressources) à $m$ postes (ou tâches) selon une approche univoque (**un à un**), de manière à **minimiser le coût total** (ou maximiser un profit).

C'est un cas particulier du problème de transport où chaque source ne dispose que d'un seul candidat et chaque destination ne demande qu'un seul candidat.

#### 📝 Modélisation mathématique (PLNE) :

- Soit $c_{ij}$ le coût d'affectation du candidat $i$ au poste $j$.
    
- Soit $x_{ij}$ une variable binaire ($x_{ij} \in \{0, 1\}$) :
    
    - $x_{ij} = 1$ si le candidat $i$ est affecté au poste $j$.
        
    - $x_{ij} = 0$ sinon.
        

Le programme linéaire s'écrit :

$$\min \sum_{i=1}^{m} \sum_{j=1}^{m} c_{ij} x_{ij}$$

Sous les contraintes :

- Chaque candidat est affecté à un seul poste : $\sum_{j=1}^{m} x_{ij} = 1 \quad (\forall i = 1, \dots, m)$
    
- Chaque poste est comblé par un seul candidat : $\sum_{i=1}^{m} x_{ij} = 1 \quad (\forall j = 1, \dots, m)$
    
- Binarité : $x_{ij} \in \{0, 1\}$
    

#### ⚠️ Les Pièges & Astuces (Cas particuliers) :

1. **Problème non carré (dimensions différentes)** : Si le nombre de candidats est différent du nombre de postes, on ajoute des **lignes ou colonnes fictives** avec des coûts d'affectation nuls ($c_{ij} = 0$) pour équilibrer la matrice.
    
2. **Affectation interdite** : Si un candidat $i$ ne peut absolument pas être affecté à un poste $j$, on pose un coût infiniment grand $c_{ij} = M$ (ou $\infty$)
# Les Transformations 1 et 2 (Réduction des lignes et des colonnes)

**Transformation 1 (Réduction par Ligne)** :

- Pour chaque ligne $i$ (candidat), on repère la valeur minimale : $\mu_i = \min_{j} \{c_{ij}\}$.
    
- On soustrait $\mu_i$ de chaque élément de la ligne $i$ : $c_{ij}^1 = c_{ij} - \mu_i$.
    
- _Effet_ : Chaque ligne contient désormais au moins un zéro.
- 
**Transformation 2 (Réduction par Colonne)** :

- Sur la nouvelle matrice issue de la Transformation 1, on repère pour chaque colonne $j$ (poste) la valeur minimale : $v_j = \min_{i} \{c_{ij}^1\}$.
    
- On soustrait $v_j$ de chaque élément de la colonne $j$ : $c_{ij}^2 = c_{ij}^1 - v_j$.
    
- _Effet_ : Chaque colonne contient désormais au moins un zéro

# Test de Faisabilité et Couverture des Zéros

Une fois les réductions faites (Transformations 1 et 2), on cherche à savoir si on peut trouver une **affectation complète de coût nul**.

Pour vérifier cela rapidement, on applique la règle du **Nombre Minimal de Trait/Lignes de Couverture** (lignes horizontales et/ou verticales) :

- On cherche à "barrer" ou "couvrir" **TOUS les zéros** de la matrice en traçant le **moins de lignes possibles** (soient des lignes horizontales, soient des lignes verticales).
    

#### ⚖️ Règle de décision :

Soit $N$ le nombre minimal de traits (lignes horizontales/verticales) nécessaires pour couvrir tous les $0$, et $m$ la taille de la matrice ($m \times m$) :

1. **Si $N = m$** : Il est possible de réaliser une affectation complète en utilisant uniquement des positions à coût nul. **On a atteint l'optimum !** On passe directement à l'étape finale d'affectation (Concept 5).
    
2. **Si $N < m$** : Il est **impossible** de faire une affectation complète uniquement avec des zéros. Il faut appliquer une transformation supplémentaire (**Transformation 3** / Concept 4) pour créer de nouveaux zéros.

Lorsque le test de faisabilité échoue ($N < m$), c'est qu'il n'y a pas assez de zéros indépendants pour faire une affectation complète. La **Transformation 3** permet de "créer" de nouveaux zéros dans la matrice sans modifier les solutions optimales.

#### ⚙️ L'algorithme de la Transformation 3 en 3 étapes :

1. **Identifier le plus petit élément non couvert** (noté $\rho$ ou $\theta$) : c'est la plus petite valeur parmi toutes les cases de la matrice qui ne sont traversées par **aucun trait** (ni horizontal, ni vertical).
    
2. **Modifier les éléments non couverts** : Soustraire $\rho$ à _tous_ les éléments non couverts.
    
3. **Modifier les intersections** : Ajouter $\rho$ à _tous_ les éléments situés à l'**intersection** de deux traits (une ligne horizontale et une ligne verticale se croisent sur cette case).
    
4. _Règle pour le reste_ : Les éléments couverts par un seul trait restent **exactement inchangés**
# Lecture de la Solution Optimale et Calcul du Coût Final

Une fois que le test de faisabilité est validé ($N = m$, c'est-à-dire que le nombre minimal de traits est égal à la taille de la matrice), cela signifie que nous pouvons enfin trouver une affectation complète en utilisant **uniquement des cases de coût nul**.

#### ⚙️ Méthode pour procéder à l'affectation :

1. **Priorité absolue** : On commence toujours par examiner les lignes ou les colonnes qui ne possèdent **qu'un seul zéro**.
    
2. **Assignation** : On sélectionne ce zéro unique pour faire l'affectation (le candidat est affecté au poste correspondant).
    
3. **Élimination** : Dès qu'une affectation est faite, on **barre/élimine toute la ligne et toute la colonne** correspondantes.
    
4. On répète l'opération jusqu'à ce que tous les candidats/postes soient affectés.