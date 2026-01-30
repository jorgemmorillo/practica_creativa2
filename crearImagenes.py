import subprocess
import sys

# CONFIGURACIÓN
PROJECT_ID = "pcreativa2-485818"
GCR_HOST = f"gcr.io/{PROJECT_ID}"
TAG = "g27"

# Lista de imágenes a construir: (ruta_build, nombre_imagen_en_gcr)
IMAGES = [
    ("./bookinfo/src/details", f"{GCR_HOST}/details:{TAG}"),
    ("./bookinfo/src/ratings", f"{GCR_HOST}/ratings:{TAG}"),
    ("./bookinfo/src/reviews/reviews-v1", f"{GCR_HOST}/reviews-v1:{TAG}"),
    ("./bookinfo/src/reviews/reviews-v2", f"{GCR_HOST}/reviews-v2:{TAG}"),
    ("./bookinfo/src/reviews/reviews-v3", f"{GCR_HOST}/reviews-v3:{TAG}"),
    ("./bookinfo/src/productpage", f"{GCR_HOST}/productpage:{TAG}"),
]

def run(cmd):
    result = subprocess.run(cmd, stdout=sys.stdout, stderr=sys.stderr)
    if result.returncode != 0:
        sys.exit(result.returncode)

def build_and_push_image(path, image_name):
    run(["docker", "build", "-t", image_name, path])
    run(["docker", "push", image_name])

def main():
    for path, image in IMAGES:
        build_and_push_image(path, image)

    print("\n Todas las imágenes han sido subidas correctamente a GCR")

if __name__ == "__main__":
    main()
