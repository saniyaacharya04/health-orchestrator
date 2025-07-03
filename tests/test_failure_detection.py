import unittest
from failure_detection.failure_detection import detect_failures

class TestFailureDetection(unittest.TestCase):
    def test_detect_failures(self):
        metrics = [0.9, 0.2, 0.5, 0.1, 0.8]  # Example metrics
        failures = detect_failures(metrics)
        self.assertIn(1, failures)  # Index 1 should be detected as a failure
        self.assertIn(3, failures)  # Index 3 should also be detected as a failure

if __name__ == '__main__':
    unittest.main()
