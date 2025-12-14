from agent.kubernetes_client import K8sClient

class Observer:
    def __init__(self, namespace="default"):
        self.namespace = namespace
        self.k8s = K8sClient()

    def cluster_health(self):
        pods = self.k8s.list_pods(self.namespace)
        total = len(pods)
        running = sum(1 for p in pods if p[1] == "Running")
        crashloop = sum(1 for p in pods if "CrashLoopBackOff" in p[1])
        pending = sum(1 for p in pods if p[1] == "Pending")

        return {
            "healthy": total == running,
            "pods": {
                "total": total,
                "running": running,
                "crashloop": crashloop,
                "pending": pending
            }
        }
