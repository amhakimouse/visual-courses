    un contour (edge) = un changement brutal d’intensité

```
Coupe d'une image (1D) traversant un contour :

Intensité
   255 ┤              ╭──────────────
       │              │
       │              │  ← changement BRUTAL = CONTOUR
       │              │
     0 ┤──────────────╯
       └───────────────────────────► position (x)
         fond noir      objet clair

La dérivée (gradient) de cette courbe :
   pic ┤              ▲
       │              │  ← pic de dérivée = ici se trouve le contour
     0 ┤──────────────┴──────────────
       └───────────────────────────► position (x)
```

**Principe** : un contour = un **maximum du gradient** (dérivée 1ère) ou un **passage par zéro** de la dérivée 2nde. Tous les détecteurs de contours reposent sur ça.
#### 1️ Sobel — le gradient directionnel

```
Deux kernels séparés : un pour les contours VERTICAUX, un pour les HORIZONTAUX

   Sobel X (Gx)              Sobel Y (Gy)
   détecte les contours      détecte les contours
   VERTICAUX                 HORIZONTAUX
   ┌────┬────┬────┐          ┌────┬────┬────┐
   │ -1 │  0 │ +1 │          │ -1 │ -2 │ -1 │
   ├────┼────┼────┤          ├────┼────┼────┤
   │ -2 │  0 │ +2 │          │  0 │  0 │  0 │
   ├────┼────┼────┤          ├────┼────┼────┤
   │ -1 │  0 │ +1 │          │ +1 │ +2 │ +1 │
   └────┴────┴────┘          └────┴────┴────┘
```

```
Image test :          Gx (contours verticaux)    Gy (contours horizontaux)
┌───────────┐         ┌───────────┐               ┌───────────┐
│ ▓▓▓ │ ░░░ │         │    ┃      │               │           │
│ ▓▓▓ │ ░░░ │   →     │    ┃      │      +        │           │
│ ▓▓▓ │ ░░░ │         │    ┃      │               │           │
└───────────┘         └───────────┘               └───────────┘
 bord VERTICAL         Gx réagit fort              Gy ≈ 0 (rien
 entre 2 zones         ici (changement             d'horizontal
                       horizontal → il              à détecter)
                       DÉTECTE le vertical)
```

Combinaison finale — magnitude du gradient (intensité du contour, toutes directions) :

```
Magnitude = √(Gx² + Gy²)      Direction = arctan(Gy / Gx)
   ▲                              ▲
"à quel point c'est          "dans quelle direction
 un contour"                  pointe le contour"
```

#### 2️ Laplacian — la dérivée seconde (sans direction)

```
Kernel Laplacian (une seule matrice, pas de X/Y séparés) :

   ┌────┬────┬────┐
   │  0 │  1 │  0 │
   ├────┼────┼────┤
   │  1 │ -4 │  1 │
   ├────┼────┼────┤
   │  0 │  1 │  0 │
   └────┴────┴────┘

Dérivée 1ère (Sobel)          Dérivée 2nde (Laplacian)
     ▲                             ▲
     │      pic                    │      ╱╲
     │     ╱  ╲                    │     ╱  ╲
     │    ╱    ╲                   │────╱────╲────  ← passe par 0
     │───╱      ╲───               │           ╲  ╱   PILE au contour
                                    │            ╲╱
   contour = SOMMET               contour = PASSAGE PAR ZÉRO
```

⚠️ Le Laplacian est **très sensible au bruit** (dérivée seconde = amplifie les petites variations) → on le combine presque toujours avec un flou Gaussian d’abord (technique “LoG” = Laplacian of Gaussian).

#### 3️ Canny — l’algorithme “complet” (le plus utilisé en pratique)

```
┌─────────────────────────────────────────────────────────┐
│              PIPELINE CANNY (4 étapes)                   │
├─────────────────────────────────────────────────────────┤
│  1. GaussianBlur    → réduire le bruit avant tout         │
│           ↓                                                │
│  2. Sobel (Gx, Gy)  → calculer magnitude + direction       │
│           ↓                                                │
│  3. Non-Maximum     → affiner : ne garder que le pixel     │
│     Suppression        LE PLUS FORT le long du contour     │
│           ↓            (contours fins d'1 pixel, pas flous)│
│  4. Double seuillage → deux seuils (bas, haut) :           │
│     + hystérésis                                            │
└─────────────────────────────────────────────────────────┘
```

```
Double seuillage avec hystérésis (l'étape clé) :

   gradient > seuil_HAUT   →  contour FORT (gardé à coup sûr)
   gradient < seuil_BAS    →  pas un contour (rejeté)
   entre les deux          →  contour FAIBLE, gardé SEULEMENT
                               s'il est CONNECTÉ à un contour fort

   ████████████░░░░░░░░░░░░░░░░░░████████
   FORT (gardé) │  FAIBLE      │  FORT (gardé)
                │  (gardé SI   │
                │   connecté)  │
   0 ──────────seuil_bas───seuil_haut────► gradient
```

Ça évite deux problèmes opposés : trop de bruit détecté comme contour (seuil trop bas) ou des contours coupés/incomplets (seuil trop haut).

---

#### Comparatif rapide

```
╔══════════╦═══════════════════════╦══════════════════╦═══════════════════╗
║  Méthode ║  Robustesse bruit     ║  Contours fins ? ║  Usage réel       ║
╠══════════╬═══════════════════════╬══════════════════╬═══════════════════╣
║  Sobel   ║  Moyenne              ║  Non (épais)     ║  Étape interne    ║
║  Laplacian║  Faible              ║  Non             ║  Détails fins     ║
║  Canny   ║  Forte (intégré)      ║  ✅ Oui (1px)    ║  Standard pro     ║
╚══════════╩═══════════════════════╩══════════════════╩═══════════════════╝
```

#### Exemple concret : détecter les bords d’un document sur une photo (étape clé avant un “scanner de document” mobile — projet Fiverr classique)

```python
import cv2

img = cv2.imread("document_photo.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# --- Sobel : gradient dans chaque direction séparément ---
# ddepth=CV_64F : on garde des valeurs négatives (float) au lieu de
# uint8, sinon les gradients négatifs seraient coupés à 0 (perte d'info).
sobel_x = cv2.Sobel(gray, cv2.CV_64F, dx=1, dy=0, ksize=3)  # contours verticaux
sobel_y = cv2.Sobel(gray, cv2.CV_64F, dx=0, dy=1, ksize=3)  # contours horizontaux

# --- Laplacian : dérivée seconde, une seule passe ---
# On floute d'abord pour limiter la sensibilité au bruit (LoG).
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
laplacian = cv2.Laplacian(blurred, cv2.CV_64F, ksize=3)

# --- Canny : LE choix standard pour la détection de bords de document ---
# threshold1 = seuil bas, threshold2 = seuil haut (règle empirique : ratio 1:2 ou 1:3)
edges = cv2.Canny(gray, threshold1=75, threshold2=200)

cv2.imwrite("doc_canny_edges.jpg", edges)
```


```python
import cv2
import numpy as np

# Cas réel complet : isoler le contour EXTÉRIEUR du document
# (première étape avant la correction de perspective, vue en Stage 2.7)
img = cv2.imread("document_photo.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Flou léger pour éviter que Canny ne détecte la texture du papier
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)

# Dilatation légère (aperçu de Stage 2.6) pour refermer les petits
# trous dans le contour détecté avant de chercher les formes fermées.
kernel = np.ones((3, 3), np.uint8)
edges_dilated = cv2.dilate(edges, kernel, iterations=1)

cv2.imwrite("doc_edges_ready.jpg", edges_dilated)
```

**Pourquoi c’est important pour de vrais projets** : Canny est **LE** détecteur de contours utilisé en production (scanner de document, détection de forme, préparation avant `findContours` en Stage 3.1). Sobel et Laplacian sont surtout des briques pédagogiques/internes — mais comprendre leur logique (gradient, dérivée seconde) explique exactement pourquoi Canny fonctionne aussi bien.
