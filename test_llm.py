# test_llm.py
from llm_integration import LLMIntegration

llm = LLMIntegration("config/llm_config.yaml")
response = llm.query_llm("Hello, how are you?")
print(response)