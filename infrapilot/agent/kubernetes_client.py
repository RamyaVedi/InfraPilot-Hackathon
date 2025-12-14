from kubernetes import client, config

class K8sClient:
    def __init__(self):
        config.load_kube_config()  # loads your k3d kubeconfig
        self.v1 = client.CoreV1Api()
        self.apps = client.AppsV1Api()

    def list_pods(self, namespace):
        return self.v1.list_namespaced_pod(namespace=namespace)

    def restart_deployment(self, name, namespace):
        body = {
            "spec": {
                "template": {
                    "metadata": {
                        "annotations": {"kubectl.kubernetes.io/restartedAt": str(client.V1Time.now())}
                    }
                }
            }
        }
        return self.apps.patch_namespaced_deployment(name, namespace, body)

