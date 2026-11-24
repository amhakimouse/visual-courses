# la Recherche Locale, Carences et Naissance de la Recherche Tabou (RT)



|**Caractéristique**|**Descente Locale Pure (Hill Climbing)**|**Recherche Tabou (RT)**|
|---|---|---|
|**Sélection du voisin**|Strictement améliorant ($f(s') < f(s)$)|Meilleur voisin non tabou (même dégradant)|
|**Condition d'arrêt**|Premier optimum local rencontré|Limite d'itérations, temps ou stagnation|
|**Gestion de la mémoire**|Amnésique (sans mémoire)|Mémoire à court terme (Liste Taboue FIFO)|
|**Gestion du cyclage**|Vulnérable aux boucles infinies dès qu'on dégrade|Interdiction temporaire des mouvements inverses|

![[Pasted image 20261124115809.png]]