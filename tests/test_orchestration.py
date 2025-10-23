import unittest
from orchestrator.actions import execute_action

class TestOrchestrator(unittest.TestCase):
    def test_execute_action_restart(self):
        execute_action("RESTART")  # just ensure no exceptions

    def test_execute_action_no_action(self):
        execute_action("NO_ACTION")  # just ensure no exceptions

    def test_execute_action_unknown(self):
        execute_action("UNKNOWN")  # just ensure no exceptions

if __name__ == "__main__":
    unittest.main()
