# health_monitor/health_monitor.py

import random

def collect_metrics():
    """
    Simulate collecting metrics for multiple microservices.
    Returns a dictionary of metrics for each service.
    """
    services = ["service_1", "service_2", "service_3"]
    metrics = {}

    for service in services:
        metrics[service] = {
            "cpu": random.randint(30, 95),
            "memory": random.randint(40, 90),
            "error_rate": round(random.uniform(0, 0.2), 2)
        }

    return metrics
