# InfraPilot — Autonomous DevOps SRE Agent

🚀 **Project:** InfraPilot  
**Hackathon:** WeMakeDevs - AI Agents Assemble  
**Author:** Ramya Vedi  
**GitHub:** [https://github.com/RamyaVedi/InfraPilot-Hackathon](https://github.com/RamyaVedi/InfraPilot-Hackathon)

---

## **Project Description**

InfraPilot is an autonomous DevOps/Site Reliability Engineering (SRE) agent that observes, plans, and executes remediation actions on a Kubernetes cluster. It detects cluster issues, decides the best action, and restores health without human intervention.

Key features:

- Observes the Kubernetes cluster state and pod health  
- Plans actions based on cluster health (e.g., restart deployments, scale replicas)  
- Executes remediation automatically  
- Verifies cluster recovery  

InfraPilot demonstrates a complete **“Break → Detect → Fix → Verify”** workflow and can be extended with AI/LLM integration (e.g., Together.ai) for intelligent planning.

---

## **Architecture / Demo Flow**

🚀 Start Demo
│
🔹 Healthy Cluster (2 pods running)
│
⚠️ Break Deployment (scale replicas = 0)
│
🔍 InfraPilot Observes Cluster
│
🧠 Planner Decides: restart_pods
│
⚙️ Executor Restarts Deployment (replicas = 2)
│
✅ Verify Recovery (pods running)
│
🏁 Demo Complete


## **Installation & Setup**

1. **Clone the repository**

```bash
git clone https://github.com/RamyaVedi/InfraPilot-Hackathon.git
cd InfraPilot-Hackathon/infrapilot

2.Create a virtual environment

python3 -m venv venv
source venv/bin/activate

3.Install dependencies

pip install -r requirements.txt

4.Start k3d Kubernetes cluster (if not already running)
k3d cluster create infrapilot
kubectl get nodes

5.Deploy sample Nginx application
kubectl create namespace infrapilot-demo
kubectl apply -f https://k8s.io/examples/application/deployment.yaml -n infrapilot-demo


Run InfraPilot

python3 main.py

Demo Steps
1.Healthy cluster
-->InfraPilot observes 2 running pods → no action needed:

Plan: {'action': 'noop', 'reason': 'Cluster is healthy'}
✅ No action required

2.Break cluster
kubectl scale deployment nginx-deployment -n infrapilot-demo --replicas=0
-->InfraPilot detects 0 running pods → plans to restart deployment:

Plan: {'action': 'restart_pods', 'reason': 'No pods running'}
⚙️ Executing remediation...
Deployment 'nginx-deployment' restarted
🔁 Verifying recovery...
{'healthy': True, 'pods': {'total': 2, 'running': 2, 'crashloop': 0, 'pending': 0}}

3.Verify recovery

kubectl get pods -n infrapilot-demo
-->Should see 2 pods running, InfraPilot restored cluster automatically.

**Project Structure**
infrapilot/
├── main.py
├── agent/
│   ├── __init__.py
│   ├── kubernetes_client.py
│   ├── executor.py
│   ├── planner.py
│   ├── observer.py
│   └── monitor.py
├── requirements.txt
└── README.md


**Notes**

Designed for hackathon demo; can be extended with LLM-driven planning using Together.ai

Fully autonomous Observe → Plan → Execute → Verify loop

Works with k3d Kubernetes cluster for testing
