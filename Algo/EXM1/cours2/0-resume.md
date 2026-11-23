#### Principe général : que faire selon la modification ?

Dans un tableau optimal, il y a deux propriétés à surveiller :

- **réalisabilité** : la colonne $b$ doit être $\ge 0$
- **optimalité** : la ligne $z$ doit avoir le bon signe

Chaque modification casse une seule de ces propriétés, et cela décide de la méthode :

| Modification                           | Ce qui change        | À vérifier                 | Si ça casse         |
| -------------------------------------- | -------------------- | -------------------------- | ------------------- |
| $b$ (second membre)                    | $x_B = B^{-1}b$      | $x_B \ge 0$ ?              | simplexe **dual**   |
| $c_j$ (objectif)                       | coûts réduits        | signe de la ligne $z$      | simplexe **primal** |
| colonne $a_j$ d’une variable hors base | seulement sa colonne | son coût réduit            | simplexe **primal** |
| nouvelle contrainte                    | une ligne en plus    | solution actuelle violée ? | simplexe **dual**   |