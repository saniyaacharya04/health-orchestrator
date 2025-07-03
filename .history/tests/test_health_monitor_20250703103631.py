import unittest
from health_monitor.health_monitor import collect_metrics  # Adjust import based on your implementation

class TestHealthMonitor(unittest.TestCase):
    def test_collect_metrics(self):
        # This is a placeholder test. You would need to mock the Prometheus server.
        metrics = collect_metrics()  # Assuming this function returns metrics for testing
        self.assertIsNotNone(metrics)
        self.assertGreaterEqual(metrics, 0)  # Assuming health value is between 0 and 1

if __name__ == '__main__':
    unittest.main()
