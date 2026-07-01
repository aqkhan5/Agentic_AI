# Agent Memory Demo

This project demonstrates different memory patterns for AI agents using the **OpenAI Agents SDK** and the **Mem0** semantic memory service.

## Overview

For an AI agent to build context in multi-turn conversations, it needs a way to retain past interactions. This repository illustrates:
1. **Session-based SQLite memory** built into the Agents SDK (for local, structured short-to-medium-term storage).
2. **Semantic long-term memory** powered by `mem0` (for personalized memory that persists across sessions and projects).

## Key Features

### 1. SDK-native SQLite Session Memory
- **In-Memory/Temporary Session** ([main.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/agent_memory/main.py)): Uses `SQLiteSession(session_id)` to manage memory in a temporary session during the application run.
- **Persistent Session** ([main_2.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/agent_memory/main_2.py)): Saves conversation history locally to a `.db` file (e.g. `conversation.db`). The history persists even after closing and restarting the script.
- **Direct Session Manipulation** ([memory_operation.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/agent_memory/memory_operation.py)): Programmatic manipulation of session history, including:
  - Inserting raw conversation turns (`await session.add_items(...)`)
  - Retrieval (`await session.get_items()`)
  - Deleting the last turn (`await session.pop_item()`)
  - Wiping session memory (`await session.clear_session()`)

### 2. Semantic/Long-Term Memory with Mem0
- **Semantic Memory Integration** ([main_3.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/agent_memory/main_3.py)): Integrates Mem0's `MemoryClient` to:
  - Search semantic history based on user preferences.
  - Dynamically inject past memories into system prompts (`dynamic_instructions_generator`).
  - Provide tools allowing the agent to explicitly `search_user_memory` and `save_user_memory` during execution.

## Files

- [main.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/agent_memory/main.py): Temporary SQLite memory loop.
- [main_2.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/agent_memory/main_2.py): Persistent SQLite memory loop (`conversation.db`).
- [main_3.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/agent_memory/main_3.py): Semantic memory using Mem0.
- [memory_operation.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/agent_memory/memory_operation.py): Direct manual SQLite session CRUD operations.

## Requirements

Install SDK and Mem0 dependencies:

```bash
pip install agents python-dotenv mem0ai
```

Configure your `.env` file with:

```env
GEMINI_API_KEY=your_gemini_api_key
MEM0_API_KEY=your_mem0_api_key  # Optional if running mem0 local/mock
```

## Running the Code

Run any of the memory examples:

```bash
python main.py
python main_2.py
python main_3.py
python memory_operation.py
```
