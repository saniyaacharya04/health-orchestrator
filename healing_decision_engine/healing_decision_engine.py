# healing_decision_engine/healing_decision_engine.py

import joblib
import os
import numpy as np

model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(model_path)

def predict_service_health(service_metrics):
    try:
        features = [
            service_metrics.get("cpu", 0),
            service_metrics.get("memory", 0),
            service_metrics.get("error_rate", 0),
        ]
        prediction = model.predict([features])[0]
        return "RESTART" if prediction == 1 else "NO_ACTION"
    except Exception as e:
        print(f"[ML ERROR] {e}")
        return "NO_ACTION"

def recommend_healing_action(failures):
    actions = {}
    for service_id, metrics in failures.items():
        action = predict_service_health(metrics)
        actions[service_id] = action
    return actions
