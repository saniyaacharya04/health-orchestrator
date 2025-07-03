# main_orchestrator.py
from health_monitor import collect_metrics
from failure_detection import detect_failures, fetch_metrics
from healing_decision_engine import recommend_healing_action
from orchestration import execute_action

def main():
    # Collect metrics
    metrics = fetch_metrics()
    
    # Detect failures
    failures = detect_failures(metrics)
    
    # Recommend healing actions
    actions = recommend_healing_action(failures)
    
    # Execute actions
    for service_id, action in actions.items():
        execute_action(action, f"my_microservice_{service_id}")

if __name__ == "__main__":
    main()
