import os
import subprocess
from pathlib import Path


def png_to_icns(png_path):
    png_path = Path(png_path).resolve()
    if not png_path.exists():
        raise FileNotFoundError(f"File not found: {png_path}")

    iconset_name = png_path.stem + ".iconset"
    iconset_path = png_path.parent / iconset_name
    icns_path = png_path.with_suffix(".icns")

    os.makedirs(iconset_path, exist_ok=True)

    sizes = [
        (16, 1), (16, 2),
        (32, 1), (32, 2),
        (128, 1), (128, 2),
        (256, 1), (256, 2),
        (512, 1), (512, 2),
    ]

    for size, scale in sizes:
        out_name = f"icon_{size}x{size}"
        if scale == 2:
            out_name += "@2x"
        out_name += ".png"

        output_path = iconset_path / out_name
        width = height = size * scale

        if size == 512 and scale == 2:
            # for 1024x1024, just copy the original png directly
            subprocess.run(["cp", str(png_path), str(output_path)])
        else:
            subprocess.run([
                "sips", "-z", str(height), str(width),
                str(png_path), "--out", str(output_path)
            ])

    subprocess.run(["iconutil", "-c", "icns", str(iconset_path)])

if __name__ == "__main__":
    png_to_icns("JMTS.png")