"""
LangChain Tools for LangGraph Agent

Tools implemented using LangChain's @tool decorator for easy integration
with LangGraph agents.

Learning Week 1 Focus Areas:
- LangChain tool patterns
- Tool registration with @tool decorator
- Function calling with LangGraph
- Tool result formatting
"""

from langchain_core.tools import tool
from datetime import datetime
import json
from typing import List


# Basic tools using LangChain @tool decorator

@tool
def calculator(expression: str) -> str:
    """
    Evaluate a mathematical expression safely.
    
    Args:
        expression: Mathematical expression to evaluate (e.g., '2 + 2', '10 * 5', 'sqrt(16)')
    
    Returns:
        Result of the calculation
    """
    # TODO: Use eval() with safe builtins or expression parser
    return f"Calculator would evaluate: {expression} (not implemented yet)"


@tool
def get_current_time() -> str:
    """
    Get the current date and time.
    
    Returns:
        Current date and time as a formatted string
    """
    # TODO: Return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return "Current time: 2024-01-15 10:30:00 (not implemented yet)"


@tool
def web_search(query: str) -> str:
    """
    Search the web for information.
    
    Args:
        query: Search query to look up
    
    Returns:
        Search results summary
    """
    # TODO: Use DuckDuckGo API or other search service
    return f"Web search for '{query}': [Search results would appear here] (not implemented yet)"


# List of all available tools for the agent
def get_tools() -> List:
    """
    Get all available tools for the LangGraph agent.
    
    Returns:
        List of LangChain tools
    """
    return [
        calculator,
        get_current_time,
        web_search,
    ]
