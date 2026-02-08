
import sys
import os
from unittest.mock import MagicMock

# Mock openai BEFORE importing ace_framework.core.agent
mock_openai = MagicMock()
sys.modules["openai"] = mock_openai

# Add current directory to sys.path
sys.path.append(os.getcwd())

from ace_framework.core.agent import AceAgent

def test_placeholder_replacement():
    # Create a temporary template file
    template_path = "test_template.md"
    with open(template_path, "w") as f:
        f.write("Hello {{name}}, welcome to {{place}}! {{missing}} stays. Double {{name}}.")

    try:
        agent = AceAgent("TestRole", template_path)
        # Mock _mock_response to return the prompt it receives so we can inspect it
        agent._mock_response = MagicMock(side_effect=lambda x: x)
        agent.client = None # Force mock response

        inputs = {
            "name": "Jules",
            "place": "the Sandbox",
            "unused": "should not appear"
        }

        result = agent.run(inputs)

        expected = "Hello Jules, welcome to the Sandbox! {{missing}} stays. Double Jules."
        assert result == expected, f"Expected '{expected}', but got '{result}'"
        print("Functional test passed!")
    finally:
        if os.path.exists(template_path):
            os.remove(template_path)

if __name__ == "__main__":
    test_placeholder_replacement()
