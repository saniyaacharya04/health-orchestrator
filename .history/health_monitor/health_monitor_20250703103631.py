# health_monitor.py
from prometheus_client import start_http_server, Gauge
import random
import time

# Create a metric to track service health
service_health = Gauge('service_health', 'Health of the microservice', ['service_name'])

def collect_metrics():
    while True:
        # Simulate health metrics
        service_name = "my_microservice"
        health_value = random.uniform(0, 1)  # Simulate health value between 0 and 1
        service_health.labels(service_name).set(health_value)
        time.sleep(5)  # Collect metrics every 5 seconds

if __name__ == "__main__":
    start_http_server(8000)  # Start Prometheus metrics server
    collect_metrics()
