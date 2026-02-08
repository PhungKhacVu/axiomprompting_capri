
import time
import re
import os
import sys

# Add the current directory to sys.path to import ace_framework
sys.path.append(os.getcwd())

from unittest.mock import MagicMock

# Mock openai BEFORE importing ace_framework.core.agent
mock_openai = MagicMock()
sys.modules["openai"] = mock_openai

from ace_framework.core.agent import AceAgent

class BenchmarkAgent(AceAgent):
    def __init__(self, template_content):
        self.role_name = "BenchmarkRole"
        self.template_path = "mock_path"
        self.template_content = template_content
        self.api_key = None
        self.client = None

    def _load_template(self):
        return self.template_content

def original_replace(template_content, inputs):
    prompt = template_content
    for key, value in inputs.items():
        prompt = prompt.replace(f"{{{{{key}}}}}", str(value))
    return prompt

_PLACEHOLDER_PATTERN = re.compile(r"\{\{(.*?)\}\}", re.DOTALL)
def optimized_replace(template_content, inputs):
    # This is what is implemented
    return _PLACEHOLDER_PATTERN.sub(lambda m: str(inputs.get(m.group(1), m.group(0))), template_content)

def run_benchmark():
    # Scenario 1: Large template, many inputs, many matches
    num_inputs = 1000
    template_content = " ".join([f"Word {i} {{{{key_{i}}}}}" for i in range(num_inputs)])
    inputs = {f"key_{i}": f"value_{i}" for i in range(num_inputs)}

    print(f"--- Scenario 1: {num_inputs} inputs, all present in template ---")

    start = time.perf_counter()
    for _ in range(100):
        original_replace(template_content, inputs)
    end = time.perf_counter()
    original_time = end - start
    print(f"Original: {original_time:.4f}s")

    start = time.perf_counter()
    for _ in range(100):
        optimized_replace(template_content, inputs)
    end = time.perf_counter()
    optimized_time = end - start
    print(f"Optimized: {optimized_time:.4f}s")
    print(f"Improvement: {(original_time - optimized_time) / original_time * 100:.2f}%")

    # Scenario 2: Large template, many inputs, few matches
    inputs_large = {f"unused_{i}": f"val_{i}" for i in range(1000)}
    inputs_large.update({"key_0": "val_0"})
    template_simple = "Hello {{key_0}}!"

    print(f"\n--- Scenario 2: 1000 inputs, only 1 present in template ---")

    start = time.perf_counter()
    for _ in range(100):
        original_replace(template_simple, inputs_large)
    end = time.perf_counter()
    original_time = end - start
    print(f"Original: {original_time:.4f}s")

    start = time.perf_counter()
    for _ in range(100):
        optimized_replace(template_simple, inputs_large)
    end = time.perf_counter()
    optimized_time = end - start
    print(f"Optimized: {optimized_time:.4f}s")
    print(f"Improvement: {(original_time - optimized_time) / original_time * 100:.2f}%")

if __name__ == "__main__":
    run_benchmark()
