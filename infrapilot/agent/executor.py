from kubernetes import client, config

class Executor:
    def __init__(self):
        # Load kubeconfig from ~/.kube/config
        config.load_kube_config()
        self.apps = client.AppsV1Api()

    def restart_deployment(self, name: str, namespace: str):
        # Restart by patching pod template annotation
        body = {
            "spec": {
                "replicas":2,
                "template": {
                    "metadata": {
                        "annotations": {
                            "infrapilot/restartedAt": "now"
                        }
                    }
                }
            }
        }

        self.apps.patch_namespaced_deployment(
            name=name,
            namespace=namespace,
            body=body
        )

        return f"Deployment '{name}' restarted"

# from agent.executor import Executor

# e = Executor()
# # e.restart_deployment("nginx-deployment", "infrapilot-demo")
