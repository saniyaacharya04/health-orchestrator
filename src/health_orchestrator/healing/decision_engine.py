# healing/decision_engine.py
import os
import joblib

# Define the expected feature order for your model
feature_order = ["cpu", "memory", "disk"]  # keep all features the model expects

def predict_action(metrics: dict, model_path: str = "healing/model.pkl") -> str:
    """
    Predicts the healing action based on system metrics.

    Args:
        metrics (dict): Metrics dictionary, e.g. {"cpu": 0.5, "memory": 0.3, "disk": 0.1}
        model_path (str): Path to the saved sklearn model

    Returns:
        str: "RESTART" or "NO_ACTION"
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path}")

    # Load the trained model using joblib
    model = joblib.load(model_path)

    # Convert metrics to feature vector
    # If a metric is missing, use 0.0 as default
    feature_vector = [float(metrics.get(key, 0.0)) for key in feature_order]

    # Predict: model should return 0 or 1
    prediction = model.predict([feature_vector])[0]

    # Map numeric prediction to action
    action_map = {0: "NO_ACTION", 1: "RESTART"}
    return action_map.get(prediction, "NO_ACTION")
