import unittest
from healing_decision_engine.healing_decision_engine import recommend_healing_action

class TestHealingDecisionEngine(unittest.TestCase):
    def test_recommend_healing_action(self):
        failures = [1, 3]  # Example detected failures
        actions = recommend_healing_action(failures)
        self.assertEqual(actions[1], "restart")  # Check if action for service 1 is restart
        self.assertEqual(actions[3], "restart")  # Check if action for service 3 is restart

if __name__ == '__main__':
    unittest.main()
