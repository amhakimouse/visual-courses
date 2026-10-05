Tous ces filtres sont des **convolutions** (vu en 2.1) avec un kernel différent, sauf le médian qui n'en est pas une (filtre non-linéaire).

#### Vue d'ensemble : pourquoi 3 filtres différents ?

```
╔═══════════════════════════════════════════════════════════════════════════╗
║  FILTRE           │  BUT PRINCIPAL                │  PRÉSERVE-T-IL        ║
║                   │                               │LES CONTOURS(edges) ?  ║
╠═══════════════════════════════════════════════════════════════════════════╣
║  Gaussian Blur    │  Flou doux, réaliste          │  ❌ Non              ║
║  Median Blur      │  Enlève le bruit              │  ✅ Oui (assez)      ║
║  (bruit poivre-sel)│  sans flouter                │                       ║
║  Bilateral Filter │  Lisse la peau(skin)/le fond  │  ✅ Oui (fort)       ║
║                   │  MAIS garde les contours      │                       ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

#### 1️⃣ Gaussian Blur — le "flou moyen pondéré"

```
Kernel Gaussien 5x5 (valeurs indicatives, normalisées) :

        ┌─────────────────────────┐
        │ 1   4   6   4   1       │
        │ 4  16  24  16   4       │   ← les poids suivent une
        │ 6  24  36  24   6       │      courbe en cloche (Gauss)
        │ 4  16  24  16   4       │      centrée sur le pixel du milieu
        │ 1   4   6   4   1       │
        └─────────────────────────┘
              (÷ somme totale pour normaliser)

  Vue de profil (coupe) :
        ▁▃▅█▅▃▁     ← pic au centre, décroît doucement
                       vers les bords (courbe de Gauss)
```

Le paramètre clé est **σ (sigma)** — l'écart-type :

```
σ PETIT (ex: 0.5)              σ GRAND (ex: 5)
┌──────────────┐               ┌──────────────┐
│   pic étroit │               │  pic large    │
│      ▄       │               │   ▂▄▆▄▂       │
│    ▄▄█▄▄     │               │  ▂▄▆█▆▄▂      │
└──────────────┘               └──────────────┘
= flou LÉGER                   = flou FORT
(réduction de bruit)           (flou volontaire)
```

---

#### 2️⃣ Median Blur — le "vote de la majorité"

Pas de convolution ici : on prend **la valeur médiane** (pas la moyenne !) des pixels voisins.

```
Voisinage 3x3 avec un pixel BRUITÉ (255, un point blanc parasite) :

   ┌────┬────┬────┐
   │ 10 │ 12 │ 11 │
   ├────┼────┼────┤
   │ 13 │255 │ 14 │   ← 255 = bruit "poivre-sel" (salt & pepper)
   ├────┼────┼────┤
   │ 12 │ 11 │ 13 │
   └────┴────┴────┘

Valeurs triées : [10,11,11,12,12,13,13,14,255]
                              ▲
                          MÉDIANE = 12  ← remplace le pixel central

  Moyenne aurait donné : (10+12+11+13+255+14+12+11+13)/9 ≈ 39.0
                          → résultat encore "pollué" par le 255 !
  Médiane ignore complètement l'outlier → bien plus robuste au bruit.
```

C'est pour ça que le filtre médian est **le meilleur choix contre le bruit "poivre-sel"** (pixels isolés totalement blancs/noirs).

---

#### 3️⃣ Bilateral Filter — le "flou intelligent"

Combine **deux critères** au lieu d'un seul :

```
Gaussian classique :        Bilateral :
poids = f(distance          poids = f(distance spatiale)
          spatiale)                  × f(différence d'intensité)
                                        ▲
                            si le pixel voisin a une intensité
                            TRÈS différente → poids ≈ 0
                            (= "ça doit être un contour, je n'y touche pas")

┌─────────────────────────────────────────────────────┐
│  Zone plate (peau, ciel)  →  flou appliqué fort      │
│  Zone de contour (bord)   →  flou quasi nul          │
│  ═══════●●●●●●●●●●══════  ← le trait de contour      │
│         ↑ reste net         reste NET malgré le flou │
└─────────────────────────────────────────────────────┘
```

C'est plus lent (calcul plus lourd) mais donne un résultat "professionnel" — utilisé dans les filtres beauté (lissage de peau) et la réduction de bruit avant la détection de contours.

---

#### Exemple concret : nettoyer une photo scannée bruitée + un filtre "lissage peau" (real-world : préparation pour OCR, et retouche photo)

python

```python
import cv2

img = cv2.imread("scanned_doc_noisy.jpg")

# GaussianBlur : kernel_size doit être IMPAIR (3,5,7...) pour avoir un centre.
# sigmaX=0 -> OpenCV calcule sigma automatiquement à partir de kernel_size.
gaussian = cv2.GaussianBlur(img, (5, 5), sigmaX=0)

# medianBlur : un seul paramètre = la taille du voisinage (doit être impair).
# Idéal ici car un scan a souvent du bruit "poivre-sel" (points isolés).
median = cv2.medianBlur(img, 5)

# bilateralFilter :
#   d = diamètre du voisinage considéré
#   sigmaColor = tolérance sur la différence d'intensité (grand = plus tolérant,
#                mélange même des couleurs assez différentes)
#   sigmaSpace = influence de la distance spatiale (comme sigma du Gaussian)
bilateral = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

cv2.imwrite("doc_gaussian.jpg", gaussian)
cv2.imwrite("doc_median.jpg", median)      # meilleur choix ici pour un scan
cv2.imwrite("doc_bilateral.jpg", bilateral)
```

python

```python
import cv2

# Cas réel : filtre "lissage de peau" pour une photo portrait
# (garder les yeux/contours nets, lisser les zones de peau).
portrait = cv2.imread("portrait.jpg")

smooth_skin = cv2.bilateralFilter(portrait, d=15, sigmaColor=80, sigmaSpace=80)
cv2.imwrite("portrait_smooth.jpg", smooth_skin)
```

**Pourquoi c'est important pour de vrais projets** : en pratique, avant TOUT traitement (edge detection, thresholding, OCR), on filtre d'abord l'image pour enlever le bruit — le choix du bon filtre (median pour du bruit ponctuel, bilateral pour préserver les contours, gaussian pour un flou général) change directement la qualité du résultat final.