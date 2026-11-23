### Concept 1 : Problème d'optimisation combinatoire

**Explication.** Un problème d'OC consiste à trouver, dans un ensemble **fini** $S$ de solutions réalisables, celle qui minimise (ou maximise) une fonction objectif $f$ :

$$s^* = \arg\min_{s\in S} f(s)$$

Le piège : $S$ est fini mais **gigantesque** (croissance exponentielle ou factorielle en la taille $n$ du problème). On ne peut donc pas l'énumérer.

**Visuel : la taille de $S$ selon le problème**

| Problème                   | Solution                | $\lvert S\rvert$ | $n=20$                       |
| -------------------------- | ----------------------- | ---------------- | ---------------------------- |
| Sac à dos (0-1)            | vecteur $x\in\{0,1\}^n$ | $2^n$            | $\approx 10^6$               |
| Affectation                | permutation             | $n!$             | $\approx 2{,}4\times10^{18}$ |
| Voyageur de commerce (TSP) | permutation circulaire  | $\approx n!$     | $\approx 2{,}4\times10^{18}$ |
### Concept 2 : Méthodes exactes vs méthodes approchées

**Explication.** Deux familles pour résoudre un problème d'OC :

||Exactes|Approchées (heuristiques)|
|---|---|---|
|Garantie|optimum **prouvé**|aucune garantie d'optimalité|
|Temps|explose avec la taille|raisonnable|
|Qualité|$f(s)=f(s^*)$|$f(s)\ge f(s^*)$ (minimisation), souvent proche|
|Exemples (cours)|simplexe, B&B, coupes, hongroise|gloutons, recherche locale, tabou, RVV|

### Concept 4 : Heuristique vs métaheuristique

**Explication.**

- **Heuristique** : algorithme spécifique à un type de problème, qui ne fournit pas forcément l'optimum. On en attend : complexité raisonnable, solution souvent proche de l'optimum, rarement mauvaise, et simplicité d'implémentation.
- **Métaheuristique** : méthode **générique** (une "boîte à outils") qui guide une heuristique et s'adapte à des problèmes très différents avec peu de modifications. Elle est en général **stochastique** et vise à explorer et exploiter tout l'espace de recherche.

||Heuristique|Métaheuristique|
|---|---|---|
|Portée|un problème précis|beaucoup de problèmes|
|Idée|règle gloutonne / ad hoc|stratégie qui **pilote** une heuristique|
|Exemple|plus proche voisin (TSP)|recherche tabou, RVV, GRASP|
|Ce qui change d'un problème à l'autre|tout l'algorithme|représentation, voisinage, fonction objectif|

### Concept 5 : Diversification, intensification, mémoire

**Explication.** Toute métaheuristique s'articule autour de 3 notions :

|Notion|Rôle|Question posée|
|---|---|---|
|**Diversification** (exploration)|explorer de nouvelles régions, **échapper aux optima locaux**|"Où n'ai-je pas encore cherché ?"|
|**Intensification** (exploitation)|fouiller en détail les zones **prometteuses** déjà trouvées|"Autour de la meilleure solution, y a-t-il mieux ?"|
|**Mémoire**|support de l'apprentissage : retient ce qui a été visité ou fréquent|"Qu'ai-je déjà vu ?"|

Les deux premières sont **opposées** : il faut les alterner. Trop de diversification gaspille du temps (on ne converge jamais), trop d'intensification bloque dans un optimum local.

**Mémoire : court terme vs long terme** (vu dans la recherche tabou)

| Mémoire     | Contenu                                             | Sert à            |
| ----------- | --------------------------------------------------- | ----------------- |
| Court terme | liste tabou (derniers mouvements interdits)         | éviter les cycles |
| Moyen terme | durée de présence des éléments dans la solution     | intensification   |
| Long terme  | fréquences des éléments dans les solutions visitées | diversification   |
### Concept 6 : Parcours vs population

**Explication.** On classe les métaheuristiques selon ce qu'elles font évoluer à chaque itération :

||Parcours (trajectoire)|Population|
|---|---|---|
|Objet manipulé|**une seule** solution|un **ensemble** de solutions en parallèle|
|Notion clé|le **voisinage** $N(s)$|l'interaction entre solutions (croisement, phéromones, ...)|
|Exemples|recuit simulé, recherche tabou, RVV, GRASP, bruitage|algorithmes génétiques, essaims particulaires, colonies de fourmis|

**Schéma d'une itération**

$$\text{Parcours : } s_k \;\longrightarrow\; s_{k+1}\in N(s_k)$$ $$\text{Population : } \{s^1_k,\dots,s^p_k\} \;\longrightarrow\; \{s^1_{k+1},\dots,s^p_{k+1}\}$$
### Concept 7 : Classes de métaheuristiques

**Explication.** Le cours distingue 3 classes selon la façon de produire les solutions :

| Classe               | Principe                                                                                                               | Exemples                                                            |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Constructive**     | part d'une solution **vide** et ajoute une composante à chaque étape ; la décision n'est **jamais remise en question** | glouton, plus proche voisin, Kruskal, GRASP (phase de construction) |
| **Recherche locale** | part d'une solution **complète** et la modifie par mouvements élémentaires dans un voisinage                           | descente, recuit simulé, tabou, RVV, bruitage                       |
| **Évolutive**        | fait évoluer une **population** avec des principes d'évolution naturelle, pour améliorer la qualité moyenne            | algorithmes génétiques, colonies de fourmis                         |
