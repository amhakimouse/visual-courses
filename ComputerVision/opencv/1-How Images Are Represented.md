A digital image is just a **grid of numbers**. Nothing more. OpenCV loads it as a NumPy array.

#### Grayscale image (2D array)

```
        columns (x) →
      ┌─────────────────────────┐
rows  │  12   45   200  255   0 │
(y)   │  34   90   180  120  60 │
 ↓    │ 255  255  255  255  255 │
      │   0    0    0    0    0 │
      └─────────────────────────┘
      each cell = 1 pixel = 1 number (0-255)
      0 = black, 255 = white, in between = gray
```

Shape in code: `(height, width)` — a 2D array.

#### Color image (3D array — 3 channels)

```
              ┌─────────────┐  ← Red channel   (H x W)
             ┌┴────────────┐│
            ┌┴────────────┐││ ← Green channel
       ┌────┴─┐           │││
       │ B  G  R│ per pixel = 3 stacked values
       └───────┘
Shape: (height, width, channels) = (H, W, 3)
```

⚠️ **Critical OpenCV quirk**: OpenCV stores color images as **BGR**, not RGB (historical reason, 1990s camera vendor default). Every other library (matplotlib, PIL) expects RGB — mixing them up is the #1 beginner bug (colors look swapped, blue looks orange).

#### Data type matters

```
dtype = uint8  →  values 0–255, 1 byte/pixel
                  (standard for images: memory-efficient)

If you do math (e.g. add two images) without
converting dtype, values can "wrap around":
   250 + 20 = 270  →  wraps to 14 (overflow!)
   NOT 255 (which is what you'd expect/want)
```

This overflow issue is why OpenCV gives you safe arithmetic functions instead of raw `+` (we'll hit this in 1.4).

#### Real-world anchor: inspecting a scanned document/receipt

Before any OCR pipeline  the first debugging step is always: _what does this image actually look like as data?_

python

```python
import cv2

# Load the image. cv2.imread returns a NumPy array in BGR order.
# If the file doesn't exist or can't be read, this returns None (not an error!)
img = cv2.imread("receipt.jpg")

# Always guard against a bad load — a silent None will crash later
# with a confusing error far from the real cause.
if img is None:
    raise FileNotFoundError("Could not load receipt.jpg — check the path")

# .shape tells you (height, width, channels).
# For a color image this is a 3-tuple; grayscale would be a 2-tuple.
print("Shape:", img.shape)          # e.g. (1200, 800, 3)

# .dtype tells you the numeric type of each pixel value.
# Should be uint8 for a normal loaded image.
print("Dtype:", img.dtype)          # uint8

# Access a single pixel at row=100, col=200.
# Returns a NumPy array [B, G, R] — note the OpenCV channel order.
pixel = img[100, 200]
print("Pixel BGR:", pixel)          # e.g. [230 225 210] (light background)

# Load the SAME file directly as grayscale using a flag.
# Useful because most CV preprocessing (thresholding, edge detection)
# works on single-channel images, not color.
gray = cv2.imread("receipt.jpg", cv2.IMREAD_GRAYSCALE)
print("Gray shape:", gray.shape)    # (1200, 800) — no channel dimension
```

**Why this matters for real apps**: the very first thing you check when a CV pipeline misbehaves (wrong colors, crash, weird output) is `shape` and `dtype`. Almost every bug in Stage 1–2 traces back to a mismatch here (wrong channel order, wrong dtype, or an image that failed to load).