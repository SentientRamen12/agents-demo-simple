"""
Simple Configuration for Anthropic Agent

Basic configuration management focused on Anthropic Claude integration.

Learning Week 1 Focus Areas:
- Environment variable management
- API key handling
- Basic configuration patterns
"""

import os
from typing import Optional
from dotenv import load_dotenv


class Config:
    """
    Simple configuration for Anthropic Claude agent
    """
    
    def __init__(self):
        """Initialize configuration"""
        load_dotenv()
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        self.google_api_key = os.getenv("GOOGLE_API_KEY")
        self.llm_provider = os.getenv("LLM_PROVIDER", "gemini")
        self.model = os.getenv("MODEL", "gemini-1.5-pro")
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))
        self.max_tokens = int(os.getenv("MAX_TOKENS", "4000"))
        pass
    
    def validate(self) -> bool:
        """
        Validate configuration
        
        Returns:
            True if configuration is valid
        """
        if self.llm_provider == "anthropic":
            return self.anthropic_api_key is not None
        elif self.llm_provider == "gemini":
            return self.google_api_key is not None
        else:
            raise ValueError(f"Invalid LLM provider: {self.llm_provider}")
        
        return False
    
    def get_api_key(self) -> Optional[str]:
        """
        Get Anthropic API key
        
        Returns:
            API key if available
        """
        if self.llm_provider == "anthropic":
            return self.anthropic_api_key
        elif self.llm_provider == "gemini":
            return self.google_api_key
        else:
            raise ValueError(f"Invalid LLM provider: {self.llm_provider}")
        return None


def load_config() -> Config:
    """
    Load configuration from environment
    
    Returns:
        Config instance
    """
    config = Config()
    if not config.validate():
        raise ValueError("ANTHROPIC_API_KEY environment variable is required")
    return config
