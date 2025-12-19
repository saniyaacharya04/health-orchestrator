import os
import joblib
import numpy as np


def predict_action(metrics: dict, model_path: str | None = None) -> str:
    """
    Predicts the healing action based on system metrics.

    Falls back to rule-based logic if ML model is unavailable.
    """

    cpu = metrics.get("cpu", 0)
    memory = metrics.get("memory", 0)
    disk = metrics.get("disk", 0)

    # Rule-based fallback (always safe)
    if cpu > 85 or memory > 85 or disk > 80:
        return "RESTART"

    # Optional ML-based path
    if model_path and os.path.exists(model_path):
        try:
            model = joblib.load(model_path)
            features = np.array([[cpu, memory, disk]])
            prediction = model.predict(features)[0]
            return "RESTART" if prediction == 1 else "NO_ACTION"
        except Exception:
            return "NO_ACTION"

    return "NO_ACTION"
