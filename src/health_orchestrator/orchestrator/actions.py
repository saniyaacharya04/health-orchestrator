def execute_action(action):
    if action == "RESTART":
        print("[Orchestrator] Restarting service...")
    elif action == "NO_ACTION":
        print("[Orchestrator] No action needed.")
    else:
        print(f"[Orchestrator] Unknown action: {action}")
