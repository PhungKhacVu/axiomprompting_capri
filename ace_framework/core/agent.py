import os
import re
from openai import OpenAI
from typing import Optional

# Regex for matching double curly brace placeholders: {{key}}
_PLACEHOLDER_PATTERN = re.compile(r"\{\{(.*?)\}\}", re.DOTALL)

class AceAgent:
    def __init__(self, role_name: str, template_path: str):
        self.role_name = role_name
        self.template_path = template_path
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key) if self.api_key else None
        self.template_content = self._load_template()

    def _load_template(self) -> str:
        """Loads the markdown template for this agent role."""
        if not os.path.exists(self.template_path):
            return f"Error: Template not found at {self.template_path}"
        with open(self.template_path, 'r') as f:
            return f.read()

    def run(self, inputs: dict) -> str:
        """
        Runs the agent with the given inputs.
        If NO API key is present, returns a mock response for testing.
        """
        # 1. Fill placeholders in the template using single-pass replacement
        prompt = _PLACEHOLDER_PATTERN.sub(
            lambda m: str(inputs.get(m.group(1), m.group(0))),
            self.template_content
        )

        # 2. Call LLM or Mock
        if not self.client:
            return self._mock_response(prompt)

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",  # Defaulting to a high-quality model
                messages=[
                    {"role": "system", "content": f"You are the {self.role_name} Agent."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error calling OpenAI API: {str(e)}"

    def _mock_response(self, prompt: str) -> str:
        """Generates a dummy response based on the role."""
        return f"""
[MOCK OUTPUT for {self.role_name}]
----------------------------------
(Since no OPENAI_API_KEY was found, this is a simulated response.)

Received Prompt Length: {len(prompt)} chars

Output:
Based on your request, here is the work product for {self.role_name}.
...
(Real LLM would generate code/design here)
...
"""
