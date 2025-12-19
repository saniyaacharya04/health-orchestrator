import unittest
from health_orchestrator.monitors.health_monitor import generate_metrics

class TestHealthMonitor(unittest.TestCase):
    def test_generate_metrics(self):
        metrics = generate_metrics()
        self.assertIn("cpu", metrics)
        self.assertIn("memory", metrics)
        self.assertIn("error_rate", metrics)
        self.assertIsInstance(metrics["cpu"], int)
        self.assertIsInstance(metrics["memory"], int)
        self.assertIsInstance(metrics["error_rate"], int)

if __name__ == "__main__":
    unittest.main()
