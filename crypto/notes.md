
#### Chiffrement [[MonoAlphabetique.html]] & Analyse Fréquentielle

**Principe** : Chaque lettre du texte clair est remplacée de manière unique par une autre lettre fixée dans l'alphabet (ex: César, Substitution simple)

1. **Comptage des fréquences** : On calcule les fréquences d'apparition de chaque caractère dans le texte chiffré.
    
2. **Comparaison statistique** : On compare ces fréquences avec la fréquence théorique des lettres dans la langue supposée du texte (ex. en français : E $\approx$ 14.7%, A $\approx$ 7.6%, S $\approx$ 7.9%).
### Chiffrement de Vigenère (Poly-alphabétique)

- **Principe** : On utilise un mot-clé de longueur $K$. La $1^{\text{ère}}$ lettre du texte est chiffrée avec la $1^{\text{ère}}$ lettre de la clé, la $2^{\text{ème}}$ avec la $2^{\text{ème}}$, ..., la $K+1^{\text{ème}}$ de nouveau avec la $1^{\text{ère}}$ lettre de la clé.
    
- **Conséquence** : Une même lettre du texte clair (par exemple 'E') peut être chiffrée par différentes lettres selon sa position. L'analyse fréquentielle globale échoue.

On cherche à connaître la taille de la clé par l'une des méthodes suivantes :

- **Le test de Kasiski** : Recherche de séquences de lettres identiques dans le texte chiffré et calcul des plus grands communs diviseurs (PGCD) des distances qui les séparent.
    
- **L'indice de coïncidence (Friedman)** : Mesure de la probabilité que deux lettres choisies au hasard dans le texte soient identiques. Plus la période supposée $K$ s'approche de la vraie longueur, plus l'indice de coïncidence du sous-texte se rapproche de celui de la langue naturelle (ex: $IC \approx 0.0778$ en français).
### Déterminer une chaîne de 8 bits dont l'image par le diagramme est elle-même

On cherche un point fixe $(L_0, R_0)$ tel que la sortie du diagramme soit identique à l'entrée :

$$(L_2, R_2) = (L_0, R_0)$$

Exprimons les conditions mathématiquement :

1. **Première condition ($L_2 = L_0$)** : Puisque $L_2 = R_1 = L_0 \oplus f_1(R_0)$, on veut :
    
    $$L_0 \oplus f_1(R_0) = L_0 \implies f_1(R_0) = 0$$
    
    Or, $f_1(R_0) = R_0 \oplus 1011 = 0 \implies R_0 = 1011$.
    
2. **Seconde condition ($R_2 = R_0$)** : Puisque $R_2 = L_1 \oplus f_2(R_1)$ avec $L_1 = R_0$ et $R_1 = L_0$, on a :
    
    $$R_0 \oplus f_2(L_0) = R_0 \implies f_2(L_0) = 0$$
    
    Or, $f_2(L_0) = \overline{L_0} \oplus 0101 = 0 \implies \overline{L_0} = 0101 \implies L_0 = 1010$.
    

**Réponse 2 :** En combinant les deux moitiés trouvées ($L_0 = 1010$ et $R_0 = 1011$), la chaîne de 8 bits recherchée est **`10101011`**


### **Concept (CFB) :**

on ne chiffre pas le message directement. On chiffre le bloc précédent avec le Feistel, puis on le XOR avec le clair :

C₀ = IV, Cᵢ = Pᵢ ⊕ E(Cᵢ₋₁)





