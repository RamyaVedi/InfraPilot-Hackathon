from kubernetes import client, config

class K8sClient:
    def __init__(self):
        config.load_kube_config()
        self.v1 = client.CoreV1Api()
        self.apps = client.AppsV1Api()

    def list_pods(self, namespace="infrapilot-demo"):
        pods = self.v1.list_namespaced_pod(namespace)
        return [(pod.metadata.name, pod.status.phase) for pod in pods.items]

    def get_pod_logs(self, name, namespace="infrapilot-demo"):
        return self.v1.read_namespaced_pod_log(name=name, namespace=namespace)

    def delete_pod(self, name, namespace="infrapilot-demo"):
        return self.v1.delete_namespaced_pod(name=name, namespace=namespace)

    def scale_deployment(self, deployment, replicas, namespace="infrapilot-demo"):
        body = {"spec": {"replicas": replicas}}
        return self.apps.patch_namespaced_deployment(
            name=deployment,
            namespace=namespace,
            body=body
        )

