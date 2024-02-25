import unittest
from src.workflow_patterns import Workflow


class TestWorkflow(unittest.TestCase):
    def test_workflow(self):
        workflow = Workflow()
        self.assertIsInstance(workflow, Workflow)


if __name__ == '__main__':
    unittest.main()
