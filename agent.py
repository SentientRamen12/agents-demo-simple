"""
LangGraph Agent using Anthropic Claude & Google Gemini

A LangGraph-based agent implementation supporting multiple LLM providers.
Uses LangGraph's create_react_agent for efficient agent workflows.

Learning Week 1 Focus Areas:
- LangGraph agent patterns
- Multi-provider LLM integration (Anthropic Claude & Google Gemini)
- Tool calling with LangGraph
- ReAct (Reason + Act) agent workflow
"""

from typing import Optional, List

from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage

from tools import get_tools
from config import load_config


class Agent:
    """
    LangGraph Agent supporting Anthropic Claude & Google Gemini
    
    Uses LangGraph's create_react_agent for efficient tool-calling workflows.
    """
    
    def __init__(self, llm_provider: Optional[str] = None, api_key: Optional[str] = None, model: Optional[str] = None):
        """
        Initialize the LangGraph agent with chosen LLM provider
        
        Args:
            llm_provider: LLM provider ("anthropic" or "gemini", uses LLM_PROVIDER env var if not provided)
            api_key: API key for the chosen provider (uses appropriate env var if not provided)
            model: Model name (uses provider default if not provided)
        """
        # Message history for conversation context
        self.messages: List[BaseMessage] = []
        
        # System prompt for agent behavior
        self.system_prompt = self._create_system_prompt()
        
        # TODO: Get LLM provider from config (anthropic or gemini)
        # TODO: Initialize appropriate LLM provider based on choice
        # TODO: Get tools from tools.py  
        # TODO: Create LangGraph ReAct agent
        pass
    
    async def send_message(self, message: str) -> str:
        """
        Send a message to the LangGraph agent and get response
        
        Args:
            message: User message
            
        Returns:
            Agent response
        """
        # TODO: Add user message to self.messages
        # TODO: Invoke LangGraph agent with message history
        # TODO: Add agent response to self.messages
        # TODO: Return response content
        return f"Agent would respond to: '{message}' (not implemented yet)"
    
    def _create_system_prompt(self) -> str:
        """
        Create system prompt that defines agent behavior and personality
        
        Returns:
            System prompt string
        """
        # TODO: Create system prompt with agent role and tool descriptions
        # TODO: Include available tools (calculator, time, web search)
        return "You are a helpful AI assistant. (System prompt not implemented yet)"
    
    def get_available_tools(self) -> list:
        """
        Get list of available tools
        
        Returns:
            List of tool names
        """
        # TODO: Return list of tool names from self.tools
        return []
    
    def get_conversation_history(self) -> List[BaseMessage]:
        """
        Get the current conversation history
        
        Returns:
            List of messages in the conversation
        """
        return self.messages.copy()
    
    def clear_conversation(self) -> None:
        """
        Clear the conversation history
        """
        self.messages.clear()


async def initialize_agent() -> Agent:
    """
    Initialize a LangGraph agent instance
    
    Returns:
        Ready-to-use Agent instance
    """
    # TODO: Load config and create agent with LLM provider choice
    return Agent()
