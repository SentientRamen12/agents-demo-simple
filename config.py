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
        self.model = os.getenv("ANTHROPIC_MODEL", "claude-3-5-sonnet-20241022")
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))
        self.max_tokens = int(os.getenv("MAX_TOKENS", "4000"))
        pass
    
    def validate(self) -> bool:
        """
        Validate configuration
        
        Returns:
            True if configuration is valid
        """
        return self.anthropic_api_key is not None
    
    def get_anthropic_api_key(self) -> Optional[str]:
        """
        Get Anthropic API key
        
        Returns:
            API key if available
        """
        return self.anthropic_api_key


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
