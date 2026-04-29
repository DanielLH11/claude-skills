#!/usr/bin/env python3
"""
remove_watermark.py - Remove visible and invisible watermarks from images.

Dependencies:
    pip install opencv-python Pillow piexif numpy

Usage examples:
    # Strip metadata from a single image
    python remove_watermark.py --mode metadata photo.jpg -o photo_clean.jpg

    # Remove visible watermark (interactive region selector opens)
    python remove_watermark.py --mode visible photo.jpg -o photo_clean.jpg

    # Remove visible watermark at known coordinates
    python remove_watermark.py --mode visible photo.jpg -o clean.jpg --region 10,890,400,950

    # Batch: strip metadata from all images in a folder
    python remove_watermark.py --mode metadata ./input/ -o ./output/

    # Both: strip metadata + remove visible watermark + add noise for LSB steganography
    python remove_watermark.py --mode both photo.jpg -o clean.jpg --region 10,890,400,950 --noise
"""

import argparse
import os
import sys
import tempfile
from pathlib import Path

SUPPORTED_FORMATS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff", ".tif"}


def check_dependencies():
    missing = []
    try:
        import cv2  # noqa: F401
    except ImportError:
        missing.append("opencv-python")
    try:
        from PIL import Image  # noqa: F401
    except ImportError:
        missing.append("Pillow")
    try:
        import piexif  # noqa: F401
    except ImportError:
        missing.append("piexif")
    try:
        import numpy  # noqa: F401
    except ImportError:
        missing.append("numpy")
    if missing:
        print(f"Missing dependencies. Install with:\n  pip install {' '.join(missing)}")
        sys.exit(1)


# ---------------------------------------------------------------------------
# Visible watermark removal via inpainting
# ---------------------------------------------------------------------------

def remove_visible_watermark(input_path: Path, output_path: Path, region=None, radius=3, method="telea") -> bool:
    """
    Reconstruct the watermark region using inpainting.

    region: (x1, y1, x2, y2) or None for interactive selection.
    radius: inpainting neighbourhood radius.
    method: 'telea' (fast) or 'ns' (better on textured backgrounds).
    """
    import cv2
    import numpy as np

    img = cv2.imread(str(input_path))
    if img is None:
        raise ValueError(f"Cannot read image: {input_path}")

    if region is None:
        window_title = f"Select watermark — {input_path.name}  (ENTER or SPACE to confirm)"
        roi = cv2.selectROI(window_title, img, fromCenter=False, showCrosshair=True)
        cv2.destroyAllWindows()
        if roi == (0, 0, 0, 0):
            print(f"  Skipped (no region selected): {input_path.name}")
            return False
        x, y, w, h = roi
        region = (x, y, x + w, y + h)

    x1, y1, x2, y2 = region
    mask = np.zeros(img.shape[:2], dtype=np.uint8)
    mask[y1:y2, x1:x2] = 255

    flag = cv2.INPAINT_TELEA if method == "telea" else cv2.INPAINT_NS
    result = cv2.inpaint(img, mask, radius, flag)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(output_path), result)
    return True


# ---------------------------------------------------------------------------
# Invisible / metadata watermark removal
# ---------------------------------------------------------------------------

def remove_metadata_watermark(input_path: Path, output_path: Path, add_noise=False, noise_level=1) -> bool:
    """
    Strip EXIF, IPTC, XMP, C2PA, and PNG text chunks by re-saving cleanly.
    Optionally add per-pixel noise to disrupt LSB steganographic watermarks.
    """
    from PIL import Image
    import piexif

    img = Image.open(str(input_path))

    # Normalise mode for clean save
    out_suffix = output_path.suffix.lower()
    if out_suffix == ".png":
        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGBA" if "A" in img.getbands() else "RGB")
    else:
        if img.mode != "RGB":
            img = img.convert("RGB")

    # Add noise to disrupt LSB steganography
    if add_noise:
        import numpy as np
        arr = np.array(img, dtype=np.int16)
        rng = np.random.default_rng()
        noise = rng.integers(-noise_level, noise_level + 1, size=arr.shape, dtype=np.int16)
        arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
        img = Image.fromarray(arr)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    if out_suffix in (".jpg", ".jpeg"):
        try:
            empty_exif = piexif.dump({"0th": {}, "Exif": {}, "GPS": {}, "1st": {}})
        except Exception:
            empty_exif = b""
        img.save(str(output_path), quality=95, optimize=True, exif=empty_exif)
    elif out_suffix == ".png":
        # Do NOT pass info= so PIL drops all text/metadata chunks
        img.save(str(output_path))
    elif out_suffix == ".webp":
        img.save(str(output_path), quality=95, exif=b"")
    else:
        img.save(str(output_path))

    return True


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

def process_image(
    input_path: Path,
    output_path: Path,
    mode: str,
    region=None,
    radius=3,
    method="telea",
    add_noise=False,
    noise_level=1,
) -> bool:
    print(f"  {input_path.name}  ->  {output_path.name}")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if mode == "visible":
        return remove_visible_watermark(input_path, output_path, region, radius, method)

    if mode == "metadata":
        return remove_metadata_watermark(input_path, output_path, add_noise, noise_level)

    # mode == "both": strip metadata first, then inpaint
    with tempfile.NamedTemporaryFile(suffix=input_path.suffix, delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        remove_metadata_watermark(input_path, tmp_path, add_noise, noise_level)
        return remove_visible_watermark(tmp_path, output_path, region, radius, method)
    finally:
        tmp_path.unlink(missing_ok=True)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Remove visible and/or invisible watermarks from images.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("input", help="Input image file or directory")
    parser.add_argument("-o", "--output", required=True, help="Output file or directory")
    parser.add_argument(
        "--mode",
        choices=["visible", "metadata", "both"],
        default="metadata",
        help="visible = inpainting, metadata = strip EXIF/C2PA/XMP, both = metadata then inpainting",
    )
    parser.add_argument(
        "--region",
        help="Watermark bounding box as x1,y1,x2,y2. Omit to open interactive selector (visible/both modes).",
    )
    parser.add_argument("--radius", type=int, default=3, help="Inpainting radius (default: 3)")
    parser.add_argument(
        "--method",
        choices=["telea", "ns"],
        default="telea",
        help="Inpainting algorithm: telea (fast, default) or ns (textured backgrounds)",
    )
    parser.add_argument(
        "--noise",
        action="store_true",
        help="Add subtle pixel noise to disrupt LSB steganographic watermarks (metadata/both modes)",
    )
    parser.add_argument(
        "--noise-level",
        type=int,
        default=1,
        metavar="N",
        help="Noise intensity 1–5 (default: 1). Use 2–3 for stronger steganography disruption.",
    )

    args = parser.parse_args()
    check_dependencies()

    # Parse region
    region = None
    if args.region:
        try:
            parts = list(map(int, args.region.split(",")))
            assert len(parts) == 4, "region must have exactly 4 values"
            region = tuple(parts)
        except Exception:
            parser.error("--region must be four comma-separated integers: x1,y1,x2,y2")

    input_path = Path(args.input)
    output_path = Path(args.output)

    if input_path.is_file():
        # Single-image mode
        dest = output_path if not output_path.is_dir() else output_path / input_path.name
        success = process_image(
            input_path, dest, args.mode, region, args.radius,
            args.method, args.noise, args.noise_level,
        )
        if success:
            print(f"Done: {dest}")

    elif input_path.is_dir():
        # Batch mode
        images = sorted(f for f in input_path.iterdir() if f.suffix.lower() in SUPPORTED_FORMATS)
        if not images:
            print(f"No supported images found in: {input_path}")
            sys.exit(1)

        output_path.mkdir(parents=True, exist_ok=True)
        print(f"Processing {len(images)} image(s) from {input_path} -> {output_path}")

        ok = 0
        for img_file in images:
            dest = output_path / img_file.name
            try:
                if process_image(
                    img_file, dest, args.mode, region, args.radius,
                    args.method, args.noise, args.noise_level,
                ):
                    ok += 1
            except Exception as exc:
                print(f"  ERROR {img_file.name}: {exc}")

        print(f"\nDone: {ok}/{len(images)} images -> {output_path}")

    else:
        parser.error(f"Input '{input_path}' is not a valid file or directory")


if __name__ == "__main__":
    main()
