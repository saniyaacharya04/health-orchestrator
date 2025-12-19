import random

def generate_metrics():
    return {
        "cpu": random.randint(10, 100),
        "memory": random.randint(10, 100),
        "error_rate": random.randint(0, 10)
    }
