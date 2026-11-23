

# Régression Linéaire Simple et Méthodes de Minimisation

### encadré par: `Pr:A.CHAREF`
### Réalisé par: `Ouslimane AbdelHakim`


## Partie 1 : Visualisation des données

```python
import pandas as pd                      

import matplotlib.pyplot as plt        

df = pd.read_excel("/content/donnees_regression_lineaire_simple.xlsx")  

df.head()
x = df["x"]                            
y = df["y"]                              
plt.scatter(x, y)                        

plt.xlabel("x")                          

plt.ylabel("y")                        

plt.title("Nuage de points de y en fonction de x")  

plt.grid(True)                          

plt.show()
```
Sortie:
```
          x          y
0  0.000000  27.450712
1  2.040816  25.068893
2  4.081633  44.001042
3  6.122449  64.274019
4  8.163265  45.059128
```

![[Pasted image 20261106172524.png]]

#### La relation entre x et y est croissante

# Partie 2 : Regression lineaire par la methode des moindres carres

#### 1-calculons a et b
```python
x = df["x"].values                      

y = df["y"].values                      

n = len(x)                              

sum_x  = np.sum(x)                      

sum_y  = np.sum(y)                    

sum_xy = np.sum(x * y)                  

sum_x2 = np.sum(x ** 2)

a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)  

b = (sum_y - a * sum_x) / n  

print(f"a = {a:.4f}, b = {b:.4f}")
```

Sortie: 
`a = 3.4130, b = 20.9666`

### 2-Tracons de la droite sur le nuage de points

```python
y_pred = a * x + b  

plt.scatter(x, y, label="Données")    

plt.plot(x, y_pred, color="red", label=f"y = {a:.2f}x + {b:.2f}")

plt.xlabel("x")                          

plt.ylabel("y")                          

plt.legend()                            

plt.grid(True)                          

plt.show()
```

![[Pasted image 20261106174119.png]]

### 3-Erreur quadratique moyenne

```python
mse = np.mean((y - y_pred) ** 2)
print("la valeur de mse est: ",mse)
```
la valeur de mse est: 185.65690390001063

### Partie 3 - Régression linéaire par descente de gradient

1.Initialisation et hyperparamètres

```python
a, b = 0.0, 0.0                        

alpha = 0.0001                          

n_iter = 1000                          

cost_history = []
```

2- Boucle de descente de gradient
```python
for i in range(n_iter):

    y_pred = a * x + b                  

    error = y - y_pred                  

    da = -(1 / n) * np.sum(x * error)  

    db = -(1 / n) * np.sum(error)        

    a = a - alpha * da                  

    b = b - alpha * db                  

    J = (1 / (2 * n)) * np.sum(error ** 2)

    cost_history.append(J)
```

3- Évolution du coût

```python
plt.plot(cost_history)                  

plt.xlabel("Itération")

plt.ylabel("J(a, b)")

plt.title("Évolution de la fonction de coût")

plt.grid(True)

plt.show()
```

![[Pasted image 20261106204629.png]]

4- Droite finale
```python
plt.scatter(x, y, label="Données")      

plt.plot(x, a * x + b, color="red", label=f"y = {a:.3f}x + {b:.3f}")

plt.legend(); plt.grid(True); plt.show()
```

![[Pasted image 20261106204720.png]]

5- Comparaison avec les moindres carrés
```python
print(f"Gradient : a = {a:.4f}, b = {b:.4f}")

print(f"MC       : a = {a_mc:.4f}, b = {b_mc:.4f}")
```
Gradient : a = 3.7157, b = 0.5869 MC : a = 3.4130, b = 5.8351

### Partie 4 - Analyse comparative

||Moindres carrés|Descente de gradient|
|---|---|---|
|**Résultat**|Solution exacte (formule fermée)|Approchée, dépend de α et des itérations|
|**Rapidité**|Très rapide pour 1 variable|Plus lent (boucle d’itérations)|
|**Complexité**|Simple ici ; en multivariable, inversion de matrice en O(p³)|O(n·p) par itération, adaptée aux gros volumes|
|**Réglages**|Aucun|α, nombre d’itérations, initialisation|
