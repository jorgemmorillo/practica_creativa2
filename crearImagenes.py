import subprocess
import sys

# Lista de imágenes a construir: (ruta_build, nombre_imagen)
IMAGES = [
    ("./bookinfo/src/details", "cdps-details:g27"),
    ("./bookinfo/src/ratings", "cdps-ratings:g27"),
    ("./bookinfo/src/reviews", "cdps-reviews:g27"),
    ("./bookinfo/src/productpage", "cdps-productpage:g27"),
]

def build_image(path, image_name):
    result = subprocess.run(
        ["docker", "build", "-t", image_name, path],
        stdout=sys.stdout,
        stderr=sys.stderr
    )

    if result.returncode != 0:
        sys.exit(1)

def main():
    for path, image in IMAGES:
        build_image(path, image)

if __name__ == "__main__":
    main()
