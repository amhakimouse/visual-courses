#### C'est quoi un histogramme d'image ?

C'est simplement : **combien de pixels ont chaque niveau de gris** (0 à 255).

```
H(k) = nombre de pixels ayant l'intensité k

Nombre
de pixels
   ▲
   │      ▄▄
   │     ████▄
   │    ██████▄▄
   │  ▄████████████▄▄        ▄▄▄
   │▄████████████████▄▄▄▄▄▄▄████▄
   └──────────────────────────────► intensité (0 → 255)
   0        sombre    milieu    clair  255
```

```
Histogramme NORMALISÉ  Hn(k) = H(k) / N
   → c'est une PROBABILITÉ : "quelle chance qu'un pixel pris
     au hasard ait l'intensité k ?"  (N = nombre total de pixels)

Histogramme CUMULÉ  Hc(k) = somme de H(i) pour i ≤ k
   → "quelle proportion de pixels a une intensité ≤ k ?"
   → C'EST LA CLÉ de l'égalisation (on y revient plus bas)

   Hc(k)
   1.0 ┤                          ╭────────
       │                     ╭────╯
       │               ╭─────╯
       │         ╭─────╯
   0.0 ┤─────────╯
       └──────────────────────────────► k
         courbe TOUJOURS croissante
```

#### Diagnostic visuel : lire un histogramme

```
┌─────────────────────────┬─────────────────────────┐
│  IMAGE SOUS-EXPOSÉE     │  IMAGE SURE-EXPOSÉE      │
│  (trop sombre)          │  (trop claire)           │
│                         │                          │
│  █▄▄                    │                    ▄▄█   │
│  ████▄                  │                  ▄████   │
│  ███████▄               │              ▄███████    │
│0 ────────────────255    │0 ────────────────────255 │
│  tout collé à gauche    │  tout collé à droite     │
└─────────────────────────┴─────────────────────────┘
┌─────────────────────────┬─────────────────────────┐
│  FAIBLE CONTRASTE       │  BON CONTRASTE           │
│  (image "plate")        │  (bien étalée)           │
│         ▄█▄             │  ▄█    ▄█▄       ▄█      │
│        ████             │ ███  ▄██████▄  ▄███      │
│0 ────────────────255    │0 ────────────────────255 │
│  tassé au centre        │  utilise TOUTE la plage  │
└─────────────────────────┴─────────────────────────┘
```

⚠️ Piège classique du cours : **deux images totalement différentes peuvent avoir le même histogramme** — l'histogramme ne dit rien sur la _position_ des pixels, seulement leur _quantité_ par niveau.

---

#### Amélioration 1 : Étirement (stretching) — "utiliser toute la plage"

```
AVANT (plage étroite : 60→180)     APRÈS (étiré sur 0→255)
   ▄█▄                                ▄█▄
  █████                             █████
0    60      180    255          0                  255
     └──┬──┘                        └────────┬────────┘
    zone utilisée                    même forme, mais ÉTALÉE
    (contraste faible)                (contraste amélioré)
```

Formule (transformation **linéaire**) :

```
Im2 = 255 × (Im1 − Imin) / (Imax − Imin)

  Imin devient 0, Imax devient 255,
  tout le reste est réparti proportionnellement entre les deux.
```

---

#### Amélioration 2 : Égalisation (equalization) — "répartir uniformément"

```
Étirement = étale la forme existante (linéaire, simple)
Égalisation = VA PLUS LOIN : rend la répartition UNIFORME
              en utilisant l'histogramme CUMULÉ Hc comme fonction
              de transformation.

Im2(i,j) = round( 255 × Hc(Im1(i,j)) / (N×M) )
                          ▲
              histogramme cumulé de l'image originale
              (N×M = nombre total de pixels)
```

```
AVANT égalisation              APRÈS égalisation
(pic concentré, contraste faible)  (répartition étalée = contraste fort)

   ▄██▄                          ▄  █    ▄█  ▄  █   ▄
  ██████                        ██ ██  ▄████ ██  █ ██
0 ──────────255                0 ──────────────────255
```

**Effet secondaire** : l'égalisation peut amplifier le bruit dans les zones où l'histogramme est faible (elle "gonfle" les petites variations).

---

#### Amélioration 3 : Correction Gamma — transformation NON-linéaire

```
disp = pix^γ

γ > 1  →  image plus SOMBRE            γ < 1  →  image plus CLAIRE

Courbe de transformation (pix en entrée → disp en sortie) :

255 ┤                    ╱          255 ┤        ╱‾‾‾‾‾
    │                 ╱              │      ╱
    │              ╱                 │   ╱
    │          ╱                     │ ╱
    │      ╱                         │╱
  0 ┤──╱─────────────────255       0 ┤────────────────255
      γ > 1 : courbe SOUS la          γ < 1 : courbe AU-DESSUS
      diagonale → assombrit les       de la diagonale →
      tons moyens                     éclaircit les tons moyens
```

Contrairement à stretching/égalisation (qui traitent tous les pixels de façon linéaire ou globale), gamma permet de **cibler** les tons sombres ou clairs différemment — très utilisé pour corriger l'affichage écran ou "réveiller" une photo terne.

---

#### Exemple concret : corriger une photo scannée sombre avant OCR (usage réel très fréquent)

python

```python
import cv2
import numpy as np

img = cv2.imread("scan_sombre.jpg", cv2.IMREAD_GRAYSCALE)

# --- 1. Étirement d'histogramme (stretching) ---
# On récupère les valeurs min/max réellement présentes dans l'image.
i_min, i_max = img.min(), img.max()

# Conversion en float pour éviter l'overflow (vu en 1.1) pendant le calcul.
stretched = (img.astype(np.float32) - i_min) * 255.0 / (i_max - i_min)

# On reconvertit en uint8 avec clip -> valeurs forcées entre 0 et 255.
stretched = np.clip(stretched, 0, 255).astype(np.uint8)

# --- 2. Égalisation d'histogramme (equalization) ---
# equalizeHist fait TOUT le calcul (histogramme cumulé + transformation) en une ligne.
# Fonctionne uniquement sur une image en NIVEAUX DE GRIS (1 canal).
equalized = cv2.equalizeHist(img)

cv2.imwrite("scan_stretched.jpg", stretched)
cv2.imwrite("scan_equalized.jpg", equalized)
```

python

```python
import cv2
import numpy as np

# --- 3. Correction Gamma ---
img = cv2.imread("photo_terne.jpg")

def correction_gamma(image, gamma=1.0):
    # On construit une "lookup table" (LUT) : pour chaque valeur possible
    # de pixel (0 à 255), on précalcule le résultat de la formule gamma.
    # C'est BEAUCOUP plus rapide que de recalculer pixel par pixel.
    inv_gamma = 1.0 / gamma
    table = np.array([
        ((i / 255.0) ** inv_gamma) * 255
        for i in range(256)
    ]).astype("uint8")

    # cv2.LUT applique la table à chaque pixel de l'image en une seule opération.
    return cv2.LUT(image, table)

# gamma < 1 -> éclaircit l'image (utile pour une photo trop sombre)
photo_claire = correction_gamma(img, gamma=0.5)
cv2.imwrite("photo_eclaircie.jpg", photo_claire)
```

**Pourquoi c'est important pour de vrais projets** : c'est l'étape de **prétraitement** juste avant l'OCR, la détection de contours ou le thresholding (Stage 2.5) — une image mal exposée fait échouer ces étapes même avec le meilleur algorithme derrière. `equalizeHist` + gamma sont les deux réflexes rapides pour "sauver" une image mal exposée côté client.