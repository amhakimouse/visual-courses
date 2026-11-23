### Qu'est-ce qu'un Histogramme d'Image ?

L'histogramme représente la distribution de la fréquence des niveaux de gris dans une image.

- **Axe horizontal ($X$)** : Les niveaux de gris, généralement de **0 (Noir parfait)** à gauche jusqu'à **255 (Blanc parfait)** à droite.
    
- **Axe vertical ($Y$)** : Le nombre de pixels possédant cette valeur de gris.


<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 220" style="background-color: #1e1e2e; font-family: Arial, sans-serif; border-radius: 8px;">
  <!-- Titre -->
  <text x="300" y="25" fill="#ffffff" font-size="16" font-weight="bold" text-anchor="middle">Principe de l'Histogramme de Gris</text>
  
  <!-- Axe X et Y -->
  <line x1="80" y1="170" x2="520" y2="170" stroke="#ffffff" stroke-width="2" />
  <line x1="80" y1="170" x2="80" y2="40" stroke="#ffffff" stroke-width="2" />
  
  <!-- Gradient de fond pour l'axe X -->
  <defs>
    <linearGradient id="grayGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#000000" />
      <stop offset="50%" stop-color="#808080" />
      <stop offset="100%" stop-color="#ffffff" />
    </linearGradient>
  </defs>
  <rect x="80" y="175" width="440" height="15" fill="url(#grayGradient)" stroke="#888" stroke-width="1" />

  <!-- Légendes des axes -->
  <text x="80" y="205" fill="#a6adc8" font-size="12" text-anchor="middle">0 (Sombre / Noir)</text>
  <text x="300" y="205" fill="#a6adc8" font-size="12" text-anchor="middle">128 (Moyens / Gris)</text>
  <text x="520" y="205" fill="#a6adc8" font-size="12" text-anchor="middle">255 (Clair / Blanc)</text>
  <text x="35" y="105" fill="#a6adc8" font-size="12" text-anchor="middle" transform="rotate(-90 35,105)">Nombre de Pixels</text>

  <!-- Zones caractéristiques (Zones de distribution) -->
  <!-- Image Sombre -->
  <path d="M 80 170 Q 120 60 180 170 Z" fill="#f38ba8" opacity="0.6" />
  <text x="130" y="110" fill="#f38ba8" font-size="11" font-weight="bold">Image Sombre</text>

  <!-- Image Contrastée / Équilibrée -->
  <path d="M 180 170 Q 300 80 420 170 Z" fill="#a6e3a1" opacity="0.5" />
  <text x="300" y="110" fill="#a6e3a1" font-size="11" font-weight="bold">Moyenne / Normale</text>

  <!-- Image Lumineuse -->
  <path d="M 400 170 Q 480 50 520 170 Z" fill="#89b4fa" opacity="0.6" />
  <text x="470" y="90" fill="#89b4fa" font-size="11" font-weight="bold">Image Claire</text>
</svg>

### Algorithme simple (naïf) pour détecter les contours

- **Parcourir** chaque pixel de l'image de coordonnées $(x, y)$.
    
- **Calculer la différence** absolue entre l'intensité du pixel courant $I(x, y)$ et son voisin de droite $I(x+1, y)$ (et/ou son voisin du bas $I(x, y+1)$).
    
- **Fixer un seuil ($S$)** choisi arbitrairement.
    
- **Décision** :
    
    - Si la différence est **supérieure au seuil $S$**, cela signifie qu'il y a une rupture nette de luminosité : on qualifie ce pixel de **contour** (on lui met la valeur **255 / Blanc**).
        
    - Sinon, c'est une zone homogène (sans contour) : on lui met la valeur **0 / Noir**.

### L'étirement d'histogramme

$$I_{étiré} = \frac{(I - I_{min}) \times 255}{I_{max} - I_{min}}$$