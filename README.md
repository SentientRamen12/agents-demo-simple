# LangGraph Multi-Provider Agent Starter

Starter learner code for setting up agents with LangGraph, supporting Anthropic Claude and Google Gemini.

### Core Learning Areas

- **System Prompt**: Defining agent behavior and personality
- **LangGraph**: Agent workflows and state management
- **Multi-Provider LLMs**: Anthropic Claude & Google Gemini integration
- **Message Management**: Conversation history and context
- **Tools**: Function calling with @tool decorators

### Quick Start

1. **Install dependencies**: `pip install -r requirements.txt`
2. **Configure**: Copy `env.example` to `.env` and set `LLM_PROVIDER` and add your API key
3. **Run**: `python main.py` (when implemented)

### Implementation TODO

- [ ] System prompt design in `agent.py`
- [ ] LangGraph ReAct agent setup with provider choice
- [ ] Multi-provider LLM integration (Anthropic & Gemini)
- [ ] Message history management
- [ ] Tool implementations in `tools.py`

**API Keys:**
- Anthropic: [console.anthropic.com](https://console.anthropic.com/)
- Google: [makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)