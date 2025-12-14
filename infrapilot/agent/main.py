print("🚀 InfraPilot starting...")

from agent.observer import Observer
from agent.planner import Planner
from agent.executor import Executor
import time

NAMESPACE = "infrapilot-demo"
DEPLOYMENT = "nginx-deployment"

def run():
    observer = Observer(namespace=NAMESPACE)
    planner = Planner()
    executor = Executor()

    print("🔍 Observing cluster state...")
    health = observer.cluster_health()
    print("Health report:", health)

    print("🧠 Planning action...")
    plan = planner.decide(health)
    print("Plan:", plan)

    if plan["action"] == "restart_pods":
        print("⚙️ Executing remediation...")
        result = executor.restart_deployment(DEPLOYMENT, NAMESPACE)
        print(result)

        time.sleep(10)
        print("🔁 Verifying recovery...")
        print(observer.cluster_health())
    else:
        print("✅ No action required")

if __name__ == "__main__":
    run()
