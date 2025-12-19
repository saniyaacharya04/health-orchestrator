import os
import joblib
import numpy as np
from health_orchestrator.core.logging import get_logger

logger = get_logger(__name__)


def predict_action(metrics: dict, model_path: str | None = None) -> str:
    cpu = metrics.get("cpu", 0)
    memory = metrics.get("memory", 0)
    disk = metrics.get("disk", 0)

    logger.info(f"Evaluating healing decision for metrics={metrics}")

    if cpu > 85 or memory > 85 or disk > 80:
        logger.warning("Rule-based trigger: RESTART")
        return "RESTART"

    if model_path and os.path.exists(model_path):
        try:
            model = joblib.load(model_path)
            features = np.array([[cpu, memory, disk]])
            prediction = model.predict(features)[0]
            action = "RESTART" if prediction == 1 else "NO_ACTION"
            logger.info(f"ML decision result={action}")
            return action
        except Exception as e:
            logger.error("ML inference failed, falling back", exc_info=e)

    logger.info("No action required")
    return "NO_ACTION"
