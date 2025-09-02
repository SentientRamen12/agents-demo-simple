"""
Simple LLM Agent Driver

A minimal command-line interface for interacting with the LLM agent.
Just initialize the agent, chat in a loop, and exit when user says stop.

Learning Week 1 Focus Areas:
- Basic agent initialization
- Simple chat loop interaction
- Clean exit handling
"""

import asyncio
from agent import initialize_agent


async def main():
    """
    Simple main function that:
    1. Initializes the agent
    2. Runs a chat loop
    3. Exits when user says stop/exit
    """
    print("🤖 Initializing LLM Agent...")
    
    agent = await initialize_agent()
    print("✅ Agent ready! Type 'stop' or 'exit' to quit.\n")
    
    print("⚠️  Agent not implemented yet. This is just the structure.")
    # print("✅ Ready for implementation! Type 'stop' or 'exit' to quit.\n")
    
    # Simple chat loop
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Check for exit conditions
            if user_input.lower() in ['stop', 'exit', 'quit', 'bye']:
                print("👋 Goodbye!")
                break
            
            # Skip empty inputs
            if not user_input:
                continue
            
            response = await agent.send_message(user_input)
            print(f"Agent: {response}\n")
            
            # Placeholder response for now
            print(f"Agent: I received your message: '{user_input}' (not implemented yet)\n")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    """
    Run the simple agent chat interface
    """
    asyncio.run(main())
