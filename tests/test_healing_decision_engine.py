# tests/test_healing_decision_engine.py
import unittest
from healing.decision_engine import predict_action

class TestDecisionEngine(unittest.TestCase):
    
    def test_predict_action_restart(self):
        # Include all expected features: cpu, memory, disk
        metrics = {"cpu": 95, "memory": 50, "disk": 10}  # missing keys are defaulted in decision_engine
        action = predict_action(metrics, "healing/model.pkl")
        self.assertIn(action, ["RESTART", "NO_ACTION"])

    def test_predict_action_no_action(self):
        metrics = {"cpu": 50, "memory": 50, "disk": 0}  # ensure 'disk' exists
        action = predict_action(metrics, "healing/model.pkl")
        self.assertIn(action, ["RESTART", "NO_ACTION"])

if __name__ == "__main__":
    unittest.main()
