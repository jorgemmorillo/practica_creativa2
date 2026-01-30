import subprocess
import sys

DOCKERHUB_USER = "jorgemoreno1"
TAG = "g27"

IMAGES = [
    ("./bookinfo/src/details", f"{DOCKERHUB_USER}/details:{TAG}"),
    ("./bookinfo/src/ratings", f"{DOCKERHUB_USER}/ratings:{TAG}"),
    ("./bookinfo/src/reviews", f"{DOCKERHUB_USER}/reviews:{TAG}"),
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
