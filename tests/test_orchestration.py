import unittest
from unittest.mock import patch
from orchestration.orchestration import execute_action

class TestOrchestration(unittest.TestCase):
    @patch('subprocess.run')
    def test_execute_action_restart(self, mock_run):
        execute_action("restart", "my_microservice_1")
        mock_run.assert_called_once_with(["kubectl", "rollout", "restart", "deployment/my_microservice_1"])

if __name__ == '__main__':
    unittest.main()
