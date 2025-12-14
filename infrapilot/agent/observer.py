from agent.kubernetes_client import K8sClient

class Observer:
    def __init__(self, namespace):
        self.k8s = K8sClient()
        self.namespace = namespace

    def cluster_health(self):
        try:
            pods = self.k8s.list_pods(self.namespace)  # ✅ CALL the function
            total = len(pods.items)
            running = sum(1 for p in pods.items if p.status.phase == "Running")
            crashloop = sum(1 for p in pods.items if p.status.phase == "CrashLoopBackOff")
            pending = sum(1 for p in pods.items if p.status.phase == "Pending")

            return {
                "healthy": running > 0,
                "pods": {
                    "total": total,
                    "running": running,
                    "crashloop": crashloop,
                    "pending": pending,
                },
            }
        except Exception as e:
            print(f"Exception when listing pods: {e}")
            return {
                "healthy": False,
                "pods": {"total": 0, "running": 0, "crashloop": 0, "pending": 0},
            }

