import os
import subprocess
from llm_integration import query_llm  # Your LLM integration function

def generate_initial_tests(source_dir, test_dir):
    for dirpath, _, filenames in os.walk(source_dir):
        for filename in filenames:
            if filename.endswith('.cpp'):
            with open(os.path.join(source_dir, file), 'r') as f:
                code = f.read()
            
            with open('instructions/initial_test_gen.yaml', 'r') as f:
                instructions = f.read()
            
            prompt = f"Generate unit tests for this C++ file:\n\n{code}\n\nFollow these instructions:\n{instructions}"
            test_code = query_llm(prompt)
            
            test_file = os.path.join(test_dir, f"test_{file}")
            with open(test_file, 'w') as f:
                f.write(test_code)

if __name__ == "__main__":
    generate_initial_tests('src', 'tests')