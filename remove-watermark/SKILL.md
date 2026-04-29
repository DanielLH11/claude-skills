---
name: remove-watermark
description: Remove watermarks from images — both visible (text/logo overlays, AI branding, stock photo overlays) and invisible (EXIF, C2PA Content Credentials, LSB steganography). Supports single images and batch directories. Use when the user wants to remove watermarks, clean image metadata, strip AI image branding (DALL-E, Midjourney, Firefly), remove stock photo overlays, erase C2PA content credentials, or strip steganographic watermarks. Requires Python with opencv-python, Pillow, piexif, and numpy.
argument-hint: "<image-or-folder> --mode <visible|metadata|both>"
user-invocable: true
---

# Remove Watermark

## Quick start

Install dependencies (once):
```bash
pip install opencv-python Pillow piexif numpy
```

Strip metadata from a single image:
```bash
python scripts/remove_watermark.py --mode metadata photo.jpg -o photo_clean.jpg
```

Remove a visible watermark (opens interactive region selector):
```bash
python scripts/remove_watermark.py --mode visible photo.jpg -o photo_clean.jpg
```

## Workflows

### Visible watermark (text/logo overlay)

- [ ] Identify the watermark region (corner text, center overlay, recurring logo)
- [ ] Choose: interactive selection (omit `--region`) or exact coordinates (`--region x1,y1,x2,y2`)
- [ ] Run with `--mode visible`
- [ ] If result looks blurry over textured areas, retry with `--method ns`
- [ ] For large watermarks, increase `--radius` (e.g. `--radius 7`)

### Invisible / metadata watermark (EXIF, C2PA, steganography)

- [ ] Run with `--mode metadata` — strips all EXIF, IPTC, XMP, and C2PA chunks
- [ ] Add `--noise` if the image may contain LSB steganographic watermarks
- [ ] Verify result: `exiftool output.jpg` — no metadata fields should remain

### Batch processing

- [ ] Point input at a directory, `-o` at a destination directory
- [ ] All `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`, `.tiff` files are processed
- [ ] For visible batch with a shared region, pass `--region x1,y1,x2,y2` upfront
- [ ] Without `--region`, an interactive selector opens per image

### Both visible + metadata

```bash
python scripts/remove_watermark.py --mode both photo.jpg -o clean.jpg --noise
```

Strips metadata first, then applies inpainting for visible removal.

## Choosing the right mode

| Situation | Mode |
|---|---|
| AI-generated image with corner/edge text | `visible` |
| Stock photo semi-transparent overlay | `visible` |
| C2PA / Content Credentials embedded in AI image | `metadata` |
| EXIF GPS, author, or software tool metadata | `metadata` |
| Suspected LSB steganographic watermark | `metadata --noise` |
| Both a visible overlay and embedded metadata | `both` |

## Key flags

| Flag | Default | Purpose |
|---|---|---|
| `--mode` | `metadata` | `visible`, `metadata`, or `both` |
| `--region x1,y1,x2,y2` | interactive | Watermark bounding box in pixels |
| `--radius N` | `3` | Inpainting fill radius (larger = smoother) |
| `--method telea\|ns` | `telea` | Algorithm: telea (fast) or ns (textured) |
| `--noise` | off | Add pixel noise to disrupt LSB steganography |
| `--noise-level N` | `1` | Noise intensity 1–5 |

See [REFERENCE.md](REFERENCE.md) for: finding watermark coordinates, LaMa inpainting for large watermarks, C2PA verification, and format notes.
