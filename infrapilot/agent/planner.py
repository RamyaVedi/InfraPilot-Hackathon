class Planner:
    def decide(self, health_report: dict):
        pods = health_report["pods"]

        # If no pods are running, restart deployment
        if pods["running"] == 0:
            return {
                "action": "restart_pods",
                "reason": "No pods running"
            }

        if health_report["healthy"]:
            return {
                "action": "noop",
                "reason": "Cluster is healthy"
            }

        if pods["crashloop"] > 0:
            return {
                "action": "restart_pods",
                "reason": "CrashLoopBackOff detected"
            }

        if pods["pending"] > 0:
            return {
                "action": "check_resources",
                "reason": "Pods are pending scheduling"
            }

        return {
            "action": "unknown",
            "reason": "Unrecognized cluster state"
        }

    # # from agent.planner import Planner

# p = Planner()

# fake_health = {
    # "healthy": False,
    # "pods": {
        # "total": 2,
        # "running": 1,
        # "crashloop": 1,
        # "pending": 0
    # }
# }

# # p.decide(fake_health)