#### The three core I/O operations

```
┌─────────────┐    imread()     ┌─────────────┐    imwrite()    ┌─────────────┐
│  disk file  │ ──────────────→ │ NumPy array │ ──────────────→ │  disk file  │
│ (.jpg/.png) │                 │  (in RAM)   │                 │  (.jpg/.png)│
└─────────────┘                 └─────────────┘                 └─────────────┘
                                       │
                                imshow() → pops up a GUI window
```

`imread` decodes the file into a NumPy array (you saw this in 1.1). `imwrite` re-encodes it back to a file — the format is decided by the extension you pass (`.jpg`, `.png`, etc.), not by anything in the array itself.



#### Video — same idea, but frame-by-frame

```
VideoCapture object
     │
     ├─ .read() → (success: bool, frame: NumPy array)  ← called in a loop
     │             one call = one frame, same shape/dtype rules as an image
     │
     └─ works identically for: a video FILE, or a live camera index
```

A video is just a _sequence_ of images — everything you learned in 1.1/1.2 applies to each frame individually.

#### Real-world anchor: batch-processing a folder of scanned receipts (your actual workflow — no live camera)

python

```python
import cv2
import os

input_dir = "receipts_raw"
output_dir = "receipts_processed"
os.makedirs(output_dir, exist_ok=True)

# Loop over every file in the input folder — this is the realistic
# pattern for a freelance gig: "process these 50 scanned receipts"
for filename in os.listdir(input_dir):
    path = os.path.join(input_dir, filename)

    # imread: decode file -> NumPy array. Returns None on failure
    # (e.g. non-image file in the folder, corrupted file).
    img = cv2.imread(path)
    if img is None:
        print(f"Skipping unreadable file: {filename}")
        continue  # don't crash the whole batch over one bad file

    # A tiny "processing step" placeholder — convert to grayscale.
    # In a real pipeline this is where Stage 2 operations would go
    # (denoise, threshold, deskew, etc.)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # imwrite: encode array -> file, format chosen by the extension.
    # We save to a DIFFERENT folder so we never overwrite raw input.
    out_path = os.path.join(output_dir, filename)
    cv2.imwrite(out_path, gray)

print("Batch done. Check receipts_processed/ to inspect results.")
```

python

```python
import cv2

# Same idea for video: open a file (or camera index like 0 for a live cam,
# not usable in your WSL2 setup without an external USB webcam).
cap = cv2.VideoCapture("input_video.mp4")

if not cap.isOpened():
    raise IOError("Could not open video file")

frame_count = 0
while True:
    # .read() grabs the next frame. 'ret' is False when the video ends
    # (or a camera disconnects) — this is your loop's exit condition.
    ret, frame = cap.read()
    if not ret:
        break

    # Save every 30th frame as a still image — a common real pattern:
    # extracting sample frames from a video for later analysis/training data.
    if frame_count % 30 == 0:
        cv2.imwrite(f"frame_{frame_count}.jpg", frame)

    frame_count += 1

# Always release the capture — frees the file handle / camera device.
cap.release()
```

**Why this matters for real apps**: production CV pipelines (a server processing uploaded images, a batch tool, a cron job) almost never use `imshow` — they read from disk/network, process, and write results or push to a database. What you're already doing (static images, no live display) is actually the _production-realistic_ pattern, not a workaround.