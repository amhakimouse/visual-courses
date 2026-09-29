
**kernel** (also called a filter or convolution matrix) is ==a small matrix of numbers used to slide across an image and perform a math operation called convolution==
#### C'est quoi une convolution ?

C'est l'opération **fondamentale** derrière le flou(blur), la détection de contours, le renforcement — presque tout le repose là-dessus.

**Idée simple** : on fait glisser une petite matrice (le **kernel**, aussi appelé masque/noyau) sur l'image, et à chaque position on calcule une somme pondérée des pixels voisins.

```
╔══════════════════════════════════════════════════════════╗
║                    IMAGE ORIGINALE                       ║
║  ┌────┬────┬────┬────┬────┐                              ║
║  │ 10 │ 20 │ 30 │ 40 │ 50 │                              ║
║  ├────┼────┼────┼────┼────┤                              ║
║  │ 15 │[A] │[B] │[C] │ 55 │   ← le KERNEL (3x3) se pose  ║
║  ├────┼────┼────┼────┼────┤     ici, centré sur le pixel ║
║  │ 25 │[D] │[E] │[F] │ 65 │     du milieu [E]            ║
║  ├────┼────┼────┼────┼────┤                              ║
║  │ 35 │[G] │[H] │[I] │ 75 │                              ║
║  └────┴────┴────┴────┴────┘                              ║
╚══════════════════════════════════════════════════════════╝
```

#### Le calcul, étape par étape

```
┌─────────────────────┐        ┌─────────────────────┐
│   Voisinage (9 px)  │        │  Kernel (3x3)        │
│   A  B  C           │        │  k1  k2  k3          │
│   D  E  F           │   ×    │  k4  k5  k6          │
│   G  H  I           │        │  k7  k8  k9          │
└─────────────────────┘        └─────────────────────┘
            │
            ▼  multiplication élément par élément, puis somme
            │
   nouveau_pixel = A·k1 + B·k2 + C·k3
                 + D·k4 + E·k5 + F·k6
                 + G·k7 + H·k8 + I·k9
```

Ce nouveau pixel remplace **E** dans l'image résultat. Puis le kernel **glisse** d'une case, et on recommence — pour **chaque pixel** de l'image.

#### Convolution vs Corrélation — la nuance technique

```
┌───────────────────────┬───────────────────────────────────┐
│   CORRÉLATION          │   CONVOLUTION                    │
│   (cross-correlation)  │                                  │
├───────────────────────┼───────────────────────────────────┤
│  kernel appliqué       │  kernel RETOURNÉ (flip 180°)       │
│  directement, sans     │  avant d'être appliqué             │
│  rotation              │                                     │
│                        │                                     │
│  ┌─┬─┬─┐               │  ┌─┬─┬─┐        ┌─┬─┬─┐            │
│  │1│2│3│               │  │1│2│3│  flip → │9│8│7│            │
│  │4│5│6│               │  │4│5│6│         │6│5│4│            │
│  │7│8│9│               │  │7│8│9│         │3│2│1│            │
│  └─┴─┴─┘               │  └─┴─┴─┘        └─┴─┴─┘            │
└───────────────────────┴───────────────────────────────────┘
```

⚠️ **Point important** : `cv2.filter2D()` (utilisé pour le filtrage manuel) fait en réalité une **corrélation**, pas une vraie convolution. Mais si le kernel est **symétrique** (comme le kernel gaussien ou moyenneur), flip ou pas flip → **même résultat**. C'est pourquoi en pratique, dans 90% des cas OpenCV, on dit "convolution" même si c'est techniquement une corrélation.

#### Le problème des bords (border handling)

```
Kernel centré sur un pixel du BORD → il "dépasse" de l'image !

        ??? ??? ???
        ┌───┬───┬───┐
   ???  │ 10│ 20│ 30│  ...
        ├───┼───┼───┤
   ???  │ 15│ X │ 45│  ...     X = pixel de bord, kernel 3x3
        ├───┼───┼───┤            déborde à gauche et en haut
   ???  │ 25│ 35│ 55│  ...

Solutions (paramètre borderType) :
  • BORDER_CONSTANT   → remplir de 0 (noir)
  • BORDER_REFLECT    → effet miroir  [30 20 10 | 10 20 30]
  • BORDER_REPLICATE  → dupliquer le dernier pixel [10 10 | 10 20 30]
```

#### Exemple concret : un kernel de netteté (sharpening) — utile pour améliorer une photo produit avant publication

python

```python
import cv2
import numpy as np

# Charge l'image produit en couleur
img = cv2.imread("product.jpg")

# Définition du kernel de "sharpening" (renforcement des contours).
# Le centre a une grande valeur positive, les voisins sont négatifs.
# Somme des coefficients = 1 -> préserve la luminosité globale.
kernel = np.array([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
])

# cv2.filter2D applique le kernel à CHAQUE pixel de l'image.
# ddepth=-1 signifie : garder la même profondeur (dtype) que l'image source.
sharpened = cv2.filter2D(img, ddepth=-1, kernel=kernel)

cv2.imwrite("product_sharp.jpg", sharpened)
```

python

```python
import cv2
import numpy as np

# Kernel moyenneur (blur) fait "à la main" avec filter2D,
# pour bien voir le lien direct avec la convolution.
img = cv2.imread("photo.jpg")

# Kernel 5x5 où chaque case vaut 1/25 -> moyenne des 25 pixels voisins.
# La somme des coefficients = 1 -> pas de changement de luminosité globale.
kernel = np.ones((5, 5), dtype=np.float32) / 25

# borderType=cv2.BORDER_REFLECT : gère les bords par effet miroir,
# évite d'assombrir artificiellement les contours de l'image.
blurred = cv2.filter2D(img, -1, kernel, borderType=cv2.BORDER_REFLECT)

cv2.imwrite("photo_blurred.jpg", blurred)
```

**Pourquoi c'est important pour de vrais projets** : chaque filtre "prêt à l'emploi" d'OpenCV (`GaussianBlur`, `Sobel`, `Laplacian`...) qu'on verra ensuite n'est qu'un **kernel de convolution spécifique**, déjà optimisé. Comprendre `filter2D` ici, c'est comprendre le mécanisme sous tout Stage 2.