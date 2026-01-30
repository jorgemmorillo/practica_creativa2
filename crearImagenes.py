import subprocess
import sys

DOCKERHUB_USER = "jormorno"
TAG = "g27"

IMAGES = [
    ("./bookinfo/src/details", f"{DOCKERHUB_USER}/details:{TAG}"),
    ("./bookinfo/src/ratings", f"{DOCKERHUB_USER}/ratings:{TAG}"),
    ("./bookinfo/src/reviews/reviews-v1", f"{DOCKERHUB_USER}/reviews-v1:{TAG}"),
    ("./bookinfo/src/reviews/reviews-v2", f"{DOCKERHUB_USER}/reviews-v2:{TAG}"),
    ("./bookinfo/src/reviews/reviews-v3", f"{DOCKERHUB_USER}/reviews-v3:{TAG}"),
    ("./bookinfo/src/productpage", f"{DOCKERHUB_USER}/productpage:{TAG}"),
]

def run(cmd):
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        sys.exit(1)

def main():
    for path, image in IMAGES:
        run(f"docker build -t {image} {path}")
        run(f"docker push {image}")

if __name__ == "__main__":
    main()
