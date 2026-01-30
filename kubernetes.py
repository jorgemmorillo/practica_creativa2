import subprocess

def run(cmd):
    print(f"▶ {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def main():
    run("kubectl apply -f bookinfo/platform/kube/namespace.yaml")
    run("kubectl apply -f bookinfo/platform/kube/ratings.yaml")
    run("kubectl apply -f bookinfo/platform/kube/reviews-svc.yaml")
    run("kubectl apply -f bookinfo/platform/kube/reviews-v1-deployment.yaml")
    run("kubectl apply -f bookinfo/platform/kube/reviews-v2-deployment.yaml")
    run("kubectl apply -f bookinfo/platform/kube/reviews-v3-deployment.yaml")
    run("kubectl apply -f bookinfo/platform/kube/details.yaml")
    run("kubectl apply -f bookinfo/platform/kube/productpage.yaml")
    run("kubectl get all -n cdps-27")

if __name__ == "__main__":
    main()

