
# Compte Rendu de TP1 : Implémentation du KNN (from scratch et avec scikit-learn)sur Iris

Réalisation Par: **OUSLIMANE ABDELHAKIM**

## Partie 1 : Préparation des données

### 1. Charger le fichier iris.csv

Nous importons d'abord les bibliothèques requises, puis nous chargeons les données depuis le fichier CSV de l'Iris.
```python

import pandas as pd

from sklearn.model_selection import train_test_split

```
```python

iris = pd.read_csv("/content/iris - iris.csv")

iris.shape

```

**Sortie :**

```

(150, 6)

```

### 2. Afficher les premières lignes du dataset (head)

Voici un aperçu des 5 premières lignes du jeu de données pour vérifier la structure :

```python

iris.head(5)

```
**Sortie :**
```

   Id  SepalLengthCm  SepalWidthCm  PetalLengthCm  PetalWidthCm      Species

0   1            5.1           3.5            1.4           0.2  Iris-setosa

1   2            4.9           3.0            1.4           0.2  Iris-setosa

2   3            4.7           3.2            1.3           0.2  Iris-setosa

3   4            4.6           3.1            1.5           0.2  Iris-setosa

4   5            5.0           3.6            1.4           0.2  Iris-setosa

```
### 3. Séparer les variables explicatives (X) et la variable cible (y)

Nous extrayons les caractéristiques (en excluant les colonnes `Id` et `Species`) et la cible `Species`.
```pytho

X, Y = iris.drop(columns=['Id', 'Species']), iris["Species"]

```
### 4. Diviser le dataset en train et test (70% / 30%)

Nous divisons les données avec un état aléatoire fixé à `12` pour assurer la reproductibilité des indices.  

```python

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=12)

```

---

  

## Partie 2 : Implémentation de KNN from scratch

### 1) Écrire une fonction pour calculer la distance euclidienne entre deux vecteurs

  
```python

from numpy import sqrt

def distance_euc(v1, v2):

  return sqrt(((v1 - v2) ** 2).sum())

```

### 2) Implémenter une fonction knn_predict(x_new, k)

Cette fonction calcule la distance entre un nouvel exemple et tous les points d'entraînement, sélectionne les $k$ plus proches, puis détermine la classe majoritaire par vote.

```python

def knn_predict(x_new, k):

  distances = []

  for i in range(len(X_train)):

      distance = distance_euc(x_new, X_train.iloc[i])

      distances.append((distance, Y_train.iloc[i]))

  distances.sort(key=lambda x: x[0])

  k_nearest = distances[:k]

  classes = {}

  for distance, label in k_nearest:

      if label in classes:

          classes[label] += 1

      else:

          classes[label] = 1

  prediction = max(classes, key=classes.get)
  return prediction

```

### 3) Tester la fonction sur un seul exemple du dataset test

Test de prédiction sur le premier échantillon de notre jeu de test avec $k=3$ :
```python

example_Y_predict = knn_predict(X_test.iloc[0], 3)

print(example_Y_predict)

```

**Sortie :**

```

Iris-setosa

```

### 4) Évaluer le modèle sur tout le jeu de test en calculant le taux d’erreur

```python

k = 3

  

errors = 0

  

for i in range(len(X_test)):

    prediction = knn_predict(X_test.iloc[i], k)

  

    if prediction != Y_test.iloc[i]:

        errors += 1

  

error_rate = errors / len(X_test)

  

print("Nombre d'erreurs :", errors)

print("Taux d'erreur :", error_rate)

print("Taux d'erreur (%) :", error_rate * 100)

```


**Sortie :**

```

Nombre d'erreurs : 1

Taux d'erreur : 0.022222222222222223

Taux d'erreur (%) : 2.2222222222222223

```

### 5) Répéter l’expérience pour plusieurs valeurs de k (de 1 à 15)

  
Nous évaluons l'erreur pour chaque valeur de $k$ afin de trouver le paramètre optimal.

  

```python

k_values = range(1, 16)

error_rates = []

for k in k_values:

  

    errors = 0

  

    for i in range(len(X_test)):

        prediction = knn_predict(X_test.iloc[i], k)

  

        if prediction != Y_test.iloc[i]:

            errors += 1

  

    error_rate = errors / len(X_test)

  

    error_rates.append(error_rate)

print(list(k_values))

print(error_rates)

```

**Sortie :**

```

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

[0.022222222222222223, 0.022222222222222223, 0.022222222222222223, 0.022222222222222223, 0.022222222222222223, 0.022222222222222223, 0.022222222222222223, 0.0, 0.022222222222222223, 0.0, 0.0, 0.0, 0.022222222222222223, 0.022222222222222223, 0.022222222222222223]

```

### 6) Tracer un graphique Erreur vs k

  
```python

import matplotlib.pyplot as plt

  

plt.plot(k_values, error_rates, marker='o')

  

plt.xlabel("k")

plt.ylabel("Taux d'erreur")

plt.title("Taux d'erreur en fonction de k")

  

plt.xticks(range(1, 16))

plt.grid()

  

plt.show()

```

  ![[Pasted image 20261012113059.png]]

---

  
## Partie 3 : Implémentation avec scikit-learn

  
### 1. Utiliser KNeighborsClassifier de sklearn.neighbors

  

```python

from sklearn.neighbors import KNeighborsClassifier

```

  

### 2. Entraîner un modèle pour différentes valeurs de k


```python

#prediction = knn_predict(X_test.iloc[i], k)

model = KNeighborsClassifier(n_neighbors=k)

```

```python

model.fit(X_train, Y_train)

```

```python

Y_pred = model.predict(X_test)

```


```python

print(Y_pred)

```


**Sortie :**

```

['Iris-setosa' 'Iris-virginica' 'Iris-setosa' 'Iris-versicolor'

 'Iris-virginica' 'Iris-virginica' 'Iris-virginica' 'Iris-setosa'

 'Iris-virginica' 'Iris-setosa' 'Iris-versicolor' 'Iris-setosa'

 'Iris-setosa' 'Iris-setosa' 'Iris-versicolor' 'Iris-virginica'

 'Iris-virginica' 'Iris-versicolor' 'Iris-setosa' 'Iris-versicolor'

 'Iris-setosa' 'Iris-versicolor' 'Iris-virginica' 'Iris-versicolor'

 'Iris-setosa' 'Iris-virginica' 'Iris-virginica' 'Iris-versicolor'

 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-versicolor'

 'Iris-virginica' 'Iris-setosa' 'Iris-virginica' 'Iris-setosa'

 'Iris-versicolor' 'Iris-versicolor' 'Iris-setosa' 'Iris-versicolor'

 'Iris-versicolor' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa' 'Iris-setosa']

```

  

### 3. Calculer le taux d’erreur pour chaque k

  

```python

errors = 0

  

for i in range(len(Y_test)):

    if Y_pred[i] != Y_test.iloc[i]:

        errors += 1

  

error_rate = errors / len(Y_test)

  

print("Taux d'erreur :", error_rate)

print("Taux d'erreur (%) :", error_rate * 100)

```

  

**Sortie :**

```

Taux d'erreur : 0.022222222222222223

Taux d'erreur (%) : 2.2222222222222223

```

  

Évaluation du taux d'erreur de scikit-learn pour $k$ variant de 1 à 15 :

  

```python

sklearn_error_rates = []

  

for k in range(1, 16):

  

    model = KNeighborsClassifier(n_neighbors=k)

  

    model.fit(X_train, Y_train)

  

    Y_pred = model.predict(X_test)

  

    errors = 0

  

    for i in range(len(Y_test)):

        if Y_pred[i] != Y_test.iloc[i]:

            errors += 1

  

    error_rate = errors / len(Y_test)

  

    sklearn_error_rates.append(error_rate)

  

sklearn_error_rates

```

  

**Sortie :**

```

[0.022222222222222223, 0.022222222222222223, 0.022222222222222223, 0.022222222222222223, 0.022222222222222223, 0.0, 0.022222222222222223, 0.0, 0.022222222222222223, 0.022222222222222223, 0.0, 0.022222222222222223, 0.022222222222222223, 0.022222222222222223, 0.022222222222222223]

```

  

### 4. Stocker les résultats dans un tableau et les comparer avec la version from scratch

  

```python

results = pd.DataFrame({

    "k": range(1, 16),

    "Erreur_from_scratch": error_rates,

    "Erreur_sklearn": sklearn_error_rates

})

  

print(results)

```

  

**Sortie :**

```

     k  Erreur_from_scratch  Erreur_sklearn

0    1             0.022222        0.022222

1    2             0.022222        0.022222

2    3             0.022222        0.022222

3    4             0.022222        0.022222

4    5             0.022222        0.022222

5    6             0.022222        0.000000

6    7             0.022222        0.022222

7    8             0.000000        0.000000

8    9             0.022222        0.022222

9   10             0.000000        0.022222

10  11             0.000000        0.000000

11  12             0.000000        0.022222

12  13             0.022222        0.022222

13  14             0.022222        0.022222

14  15             0.022222        0.022222

```

  

### 5. Tracer le graphique Erreur vs k avec scikit-learn

  

Graphique superposant notre implémentation et celle de scikit-learn :

  

```python

plt.figure(figsize=(8, 5))

  

plt.plot(

    range(1, 16),

    error_rates,

    marker='o',

    label="KNN from scratch"

)

  

plt.plot(

    range(1, 16),

    sklearn_error_rates,

    marker='s',

    label="KNN scikit-learn"

)

  

plt.xlabel("k")

plt.ylabel("Taux d'erreur")

plt.title("Comparaison du KNN from scratch et scikit-learn")

  

plt.xticks(range(1, 16))

plt.legend()

plt.grid()

  

plt.show()

```


![[Pasted image 20261012113011.png]]
