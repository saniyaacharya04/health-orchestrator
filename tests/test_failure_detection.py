import unittest
from monitors.failure_detector import detect_failure

class TestFailureDetector(unittest.TestCase):
    def test_detect_failure_true(self):
        metrics = {"cpu": 90, "memory": 90, "error_rate": 10}
        self.assertTrue(detect_failure(metrics, 80, 80, 5))

    def test_detect_failure_false(self):
        metrics = {"cpu": 50, "memory": 50, "error_rate": 0}
        self.assertFalse(detect_failure(metrics, 80, 80, 5))

if __name__ == "__main__":
    unittest.main()
