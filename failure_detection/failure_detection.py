# failure_detection/failure_detection.py

def fetch_metrics():
    """
    Simulate fetching metrics from services.
    This function should return a dictionary where keys are service IDs
    and values are dictionaries of metrics.
    """
    return {
        "service_1": {"cpu": 85, "memory": 70, "error_rate": 0.05},
        "service_2": {"cpu": 45, "memory": 55, "error_rate": 0.15},
        "service_3": {"cpu": 90, "memory": 80, "error_rate": 0.01}
    }

def detect_failures(metrics):
    """
    Analyze metrics and return a dictionary of services that are unhealthy.
    Each key is a service ID and each value is its metrics.
    """
    failures = {}
    for service_id, service_metrics in metrics.items():
        cpu = service_metrics.get("cpu", 0)
        error_rate = service_metrics.get("error_rate", 0)

        if cpu > 80 or error_rate > 0.1:
            failures[service_id] = service_metrics

    return failures
