def predict_service_health(metrics):
    """
    Predict service health based on CPU usage, memory usage, and error rate.

    Args:
        metrics (dict): {
            "cpu_usage": float (percentage, 0-100),
            "memory_usage": float (percentage, 0-100),
            "error_rate": float (percentage, 0-100)
        }

    Returns:
        str: "healthy" or "unhealthy"
    """

    cpu = metrics.get("cpu_usage", 0)
    memory = metrics.get("memory_usage", 0)
    error_rate = metrics.get("error_rate", 0)

    # Thresholds (example)
    CPU_THRESHOLD = 75
    MEMORY_THRESHOLD = 80
    ERROR_RATE_THRESHOLD = 5

    if cpu > CPU_THRESHOLD:
        return "unhealthy"
    if memory > MEMORY_THRESHOLD:
        return "unhealthy"
    if error_rate > ERROR_RATE_THRESHOLD:
        return "unhealthy"
    
    return "healthy"
