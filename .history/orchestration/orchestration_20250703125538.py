# orchestration.py

import os
import subprocess

# Enable mock mode for safe testing (set MOCK_MODE=true in env)
MOCK_MODE = os.getenv("MOCK_MODE", "false").lower() == "true"

def execute_action(action, service_name):
    """
    Execute orchestration actions like 'restart' on Kubernetes deployments.
    """
    if action == "restart":
        if MOCK_MODE:
            print(f"[MOCK] Would restart: deployment/{service_name}")
            return
        
        try:
            result = subprocess.run(
                ["kubectl", "rollout", "restart", f"deployment/{service_name}"],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            print(f"[✓] Restarted {service_name}:\n{result.stdout}")
        except subprocess.CalledProcessError as e:
            print(f"[✗] Failed to restart {service_name}:\n{e.stderr}")
        except FileNotFoundError:
            print(f"[✗] 'kubectl' command not found. Is it installed and in PATH?")

    else:
        print(f"[!] Unknown action '{action}' for {service_name}")

def get_actions():
    """
    This simulates actions to take for services.
    In real scenarios, this would come from a health analyzer or ML prediction engine.
    """
    # Example: Restart service 1 and 3
    return {
        1: "restart",
        3: "restart"
    }

if __name__ == "__main__":
    print("🔧 Starting Orchestration Engine...")
    actions = get_actions()
    
    for service_id, action in actions.items():
        service_name = f"my_microservice_{service_id}"
        print(f"→ Executing '{action}' on {service_name}")
        execute_action(action, service_name)
 