import random
from health_orchestrator.core.logging import get_logger

logger = get_logger(__name__)


def generate_metrics():
    metrics = {
        "cpu": random.randint(10, 100),
        "memory": random.randint(10, 100),
        "error_rate": random.randint(0, 10),
    }
    logger.info(f"Generated system metrics: {metrics}")
    return metrics
