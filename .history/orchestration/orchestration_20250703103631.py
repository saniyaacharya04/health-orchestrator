# orchestration.py
import subprocess

def execute_action(action, service_name):
    if action == "restart":
        # Example command to restart a service in Kubernetes
        subprocess.run(["kubectl", "rollout", "restart", f"deployment/{service_name}"])

if __name__ == "__main__":
    actions = {1: "restart", 3: "restart"}  # Example actions
    for service_id, action in actions.items():
        execute_action(action, f"my_microservice_{service_id}")
