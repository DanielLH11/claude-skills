# Remove Watermark — Reference

## Technique overview

### Visible watermarks: OpenCV inpainting

`cv2.inpaint()` reconstructs the masked region from surrounding pixels.

- **TELEA** (default): Fast, accurate for text watermarks and small regions
- **NS** (Navier-Stokes): Slower, better quality on textured backgrounds

**Radius guide:**

| Watermark size | `--radius` |
|---|---|
| Small text (≤30px tall) | `3` (default) |
| Medium overlay | `5–7` |
| Large logo / block | `10+` or use LaMa |

### Invisible watermarks: what gets stripped

| Type | What the script does |
|---|---|
| EXIF metadata | Replaced with empty EXIF on save |
| IPTC / XMP | Dropped on clean PIL save |
| C2PA Content Credentials | Dropped — stored as XMP or dedicated chunk; clean save removes it |
| PNG tEXt / iTXt chunks | Dropped on clean save |
| LSB steganography | Disrupted by adding ±1–5 noise to pixel values (`--noise`) |
| DCT / frequency domain | Partially disrupted by JPEG recompression at quality 95 |

### Limits

Invisible watermarks that **cannot** be fully removed by this script:

- **Perceptual/frequency watermarks** (tree-ring, WatermarkAnything, Stable Signature) — woven into the frequency domain; survive noise and recompression. These require dedicated reversal tools that know the original key.

## Finding watermark coordinates

Quick size check:
```python
from PIL import Image
img = Image.open("photo.jpg")
print(img.size)  # (width, height)
```

Use an image viewer that shows cursor pixel coordinates (IrfanView on Windows, Preview on macOS), then note the top-left and bottom-right corners of the watermark rectangle.

Or use the interactive OpenCV selector by running the script without `--region` — it shows coordinates in the window title bar on hover.

## LaMa inpainting for large watermarks

OpenCV inpainting blurs or smears on large masked areas. LaMa produces dramatically better results.

```bash
pip install simple-lama-inpainting
```

```python
from simple_lama_inpainting import SimpleLama
from PIL import Image, ImageDraw

simple_lama = SimpleLama()

image = Image.open("input.jpg").convert("RGB")
mask = Image.new("L", image.size, 0)
draw = ImageDraw.Draw(mask)
draw.rectangle([x1, y1, x2, y2], fill=255)  # white = region to fill

result = simple_lama(image, mask)
result.save("output.jpg")
```

## Verifying metadata removal

```bash
# Requires exiftool — Windows installer: https://exiftool.org
exiftool output.jpg
# Should show only basic file type info — no software, author, GPS, XMP fields

# C2PA specifically
exiftool -xmp output.jpg   # should return nothing
```

## Batch with a shared watermark region

If every image in a folder has a watermark at the same position (common for AI outputs from the same service), run on one image first to confirm the region, then batch:

```bash
# Step 1: confirm region on one image
python scripts/remove_watermark.py --mode visible sample.jpg -o test.jpg

# Step 2: batch with confirmed region
python scripts/remove_watermark.py --mode both ./raw/ -o ./clean/ --region 10,890,400,950
```

## Format notes

| Format | Behaviour |
|---|---|
| JPEG | Re-saved at quality 95; recompression also disrupts DCT watermarks |
| PNG | Losslessly re-saved; use `--noise` for LSB watermarks (lossless save alone won't disrupt them) |
| WebP | Re-saved at quality 95 |
| TIFF / BMP | Converted to RGB and saved cleanly |
