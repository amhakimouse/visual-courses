#### The overflow problem (from 1.1), solved properly

```
NumPy raw add (WRONG for images):          OpenCV safe add (cv2.add):
   250 + 20 = 270                             250 + 20 = 270
   uint8 wraps: 270 - 256 = 14                clipped (saturated) at 255
   → pixel gets DARKER when adding light!     → pixel correctly maxes out at white

   "wrap-around"                              "saturation"
   ░░░░░░░░████░░░░  (wrong, dark band)       ████████████████  (correct, clipped)
```

```
gray_img  +  20   →  np.add:  wraps past 255, weird dark artifacts
                  →  cv2.add: clips at 255, looks like a real brightness boost
```

Rule of thumb: **any time you do pixel math, use `cv2.*` functions, never raw `+`/`-` on the arrays**, unless you've deliberately cast to a wider dtype yourself.

#### Weighted blending — two images merged smoothly

```
result = α * imgA + β * imgB + γ

α=1.0, β=0.0  →  100% image A
α=0.0, β=1.0  →  100% image B
α=0.5, β=0.5  →  50/50 transparent blend  (like a watermark or fade)

┌────────┐        ┌────────┐        ┌─────────────┐
│ Image A│  0.7 ×  │ Image B│  0.3 × │   blended   │
│(photo) │   +     │(logo)  │   =    │(watermarked)│
└────────┘         └────────┘        └─────────────┘
```

This is exactly how a semi-transparent watermark/logo overlay works.

#### Masking — combining images where only PART should show

```
Image A        Mask (binary)       Result
┌────────┐     ┌────────┐         ┌────────┐
│████████│  &   │░░████░░│    =    │░░AAAA░░│
│████████│      │░░████░░│         │░░AAAA░░│
└────────┘      └────────┘         └────────┘
                (255=keep,          only the masked
                 0=drop)            region survives
```

This is the same `bitwise_and` + mask pattern from 1.2 (green-screen removal) — masking is a general tool, not just for color.

#### Real-world anchor: watermarking product photos + a "sticker overlay" feature 

python

```python
import cv2

# Both images must be the SAME size for arithmetic ops to work directly.
photo = cv2.imread("product_photo.jpg")
photo = cv2.resize(photo, (800, 800))

logo = cv2.imread("watermark_logo.png")
logo = cv2.resize(logo, (800, 800))  # match dimensions exactly

# cv2.addWeighted computes: result = photo*alpha + logo*beta + gamma
# It handles the uint8 saturation correctly (no wrap-around from 1.1's issue).
watermarked = cv2.addWeighted(photo, 0.85, logo, 0.15, 0)
# 0.85 photo + 0.15 logo → logo appears as a faint, semi-transparent overlay

cv2.imwrite("product_watermarked.jpg", watermarked)
```

python

```python
import cv2
import numpy as np

# Overlaying a non-rectangular sticker/icon onto a photo at an exact spot,
# WITHOUT the sticker's own background square covering the photo underneath.
base = cv2.imread("photo.jpg")
sticker = cv2.imread("sticker.png")  # assume sticker has a black background
h, w = sticker.shape[:2]

# Grab the region of 'base' where the sticker will go — same size as sticker.
x, y = 50, 50  # top-left corner placement
roi = base[y:y+h, x:x+w]

# Build a mask from the sticker: anywhere it's "black background" -> 0,
# anywhere it's actual sticker content -> 255.
gray_sticker = cv2.cvtColor(sticker, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(gray_sticker, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Black out the sticker's footprint in the base ROI, keeping surroundings.
base_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Keep only the sticker's actual content (drop its black background).
sticker_fg = cv2.bitwise_and(sticker, sticker, mask=mask)

# Add the two: background-with-hole + sticker-content = seamless overlay.
combined = cv2.add(base_bg, sticker_fg)  # cv2.add = safe, saturated addition

# Paste the combined region back into the full photo.
base[y:y+h, x:x+w] = combined
cv2.imwrite("photo_with_sticker.jpg", base)
```

**Why this matters for real apps**: this exact mask+`bitwise_and`+`cv2.add` pattern is how you composite _any_ non-rectangular overlay onto a background (logos, stickers, UI elements, AR-style effects) without ugly rectangular boxes — it's a building block you'll reuse constantly, including later for green-screen work and object cutouts.

---
