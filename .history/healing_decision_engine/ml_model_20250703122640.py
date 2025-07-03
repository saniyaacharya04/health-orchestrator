# healing_decision_engine/ml_model.py
def predict_service_health(metrics):
    # Example dummy logic – replace with real model
    if metrics.get("cpu_usage", 0) > 80:
        return "unhealthy"
    return "healthy"
