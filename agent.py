"""
LangGraph Agent using Anthropic Claude

A LangGraph-based agent implementation using Anthropic Claude with tool support.
Uses LangGraph's create_react_agent for efficient agent workflows.

Learning Week 1 Focus Areas:
- LangGraph agent patterns
- Anthropic Claude integration via LangChain
- Tool calling with LangGraph
- ReAct (Reason + Act) agent workflow
"""

from typing import Optional, List

from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage

from tools import get_tools
from config import load_config


class Agent:
    """
    LangGraph Agent using Anthropic Claude
    
    Uses LangGraph's create_react_agent for efficient tool-calling workflows.
    """
    
    def __init__(self, api_key: Optional[str] = None, model: str = "claude-3-5-sonnet-20241022"):
        """
        Initialize the LangGraph agent with Anthropic Claude
        
        Args:
            api_key: Anthropic API key (will use ANTHROPIC_API_KEY env var if not provided)
            model: Claude model to use (default: claude-3-5-sonnet-20241022)
        """
        # Message history for conversation context
        self.messages: List[BaseMessage] = []
        
        # System prompt for agent behavior
        self.system_prompt = self._create_system_prompt()
        
        # TODO: Initialize Claude model with config
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
    # TODO: Load config and create agent with API key
    return Agent()
