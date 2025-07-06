# llm_integration.py
from openai import OpenAI  # Updated import
from typing import Optional, Dict, Any
import os
import time
import yaml

class LLMIntegration:
    def __init__(self, config_path: str = "config/llm_config.yaml"):
        """
        Initialize the LLM integration with configuration
        
        Args:
            config_path: Path to YAML configuration file
        """
        self.config = self._load_config(config_path)
        self._setup_llm()
        
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            if config is None:
                raise ValueError(f"Config file '{config_path}' is empty or invalid!")
            return config
    
    def _setup_llm(self):
        """Setup the LLM based on configuration"""
        if self.config['llm_provider'] == 'openai':
            api_key = os.getenv("OPENAI_API_KEY", self.config.get('api_key', ''))
            if not api_key:
                raise ValueError("OpenAI API key not found in environment or config")
            self.client = OpenAI(api_key=api_key)  # New client initialization
            
        elif self.config['llm_provider'] == 'llama':
            # Setup for LLaMA would go here
            self._setup_llama()
        else:
            raise ValueError(f"Unsupported LLM provider: {self.config['llm_provider']}")
    
    def _setup_llama(self):
        """Initialize LLaMA model"""
        try:
            from llama_cpp import Llama
        except ImportError:
            raise ImportError("llama-cpp-python not installed. Install with: pip install llama-cpp-python")
        
        model_path = self.config.get('model_path', 'models/llama-2-7b-chat.ggmlv3.q4_0.bin')
        self._llama = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_threads=4
        )
    
    def query_llm(
        self,
        prompt: str,
        max_tokens: int = 2048,
        temperature: float = 0.7,
        retries: int = 3,
        retry_delay: int = 5
    ) -> str:
        """
        Send prompt to LLM and return response
        
        Args:
            prompt: The input prompt for the LLM
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            retries: Number of retry attempts on failure
            retry_delay: Delay between retries in seconds
            
        Returns:
            Generated response from LLM
        """
        last_error = None
        
        for attempt in range(retries):
            try:
                if self.config['llm_provider'] == 'openai':
                    response = self.client.chat.completions.create(  # Updated API call
                        model=self.config.get('model', 'gpt-4'),
                        messages=[{"role": "user", "content": prompt}],
                        max_tokens=max_tokens,
                        temperature=temperature,
                    )
                    return response.choices[0].message.content
                
                elif self.config['llm_provider'] == 'llama':
                    return self._query_local_llama(prompt, max_tokens, temperature)
                    
            except Exception as e:
                last_error = e
                print(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt < retries - 1:
                    time.sleep(retry_delay)
        
        raise Exception(f"All retries failed. Last error: {str(last_error)}")
    
    def _query_local_llama(
        self,
        prompt: str,
        max_tokens: int,
        temperature: float
    ) -> str:
        """
        Query a locally hosted LLaMA model
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            
        Returns:
            Generated response
        """
        if not hasattr(self, '_llama'):
            self._setup_llama()
        
        response = self._llama(
            prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            stop=["\n\n"],
            echo=False
        )
        
        return response['choices'][0]['text']