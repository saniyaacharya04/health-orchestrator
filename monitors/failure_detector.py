def detect_failure(metrics, cpu_threshold, memory_threshold, error_threshold):
    if (metrics["cpu"] > cpu_threshold or
        metrics["memory"] > memory_threshold or
        metrics["error_rate"] > error_threshold):
        return True
    return False
