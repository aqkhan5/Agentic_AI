# Session Context Engineering Demo

This project demonstrates advanced session management and custom context management strategies using the **OpenAI Agents SDK**.

## Overview

In complex multi-turn AI interactions, managing the conversation context window is critical. As the conversation history grows, it consumes more tokens, increases costs, increases LLM response latency, and can eventually exceed the model's context limit. 

This folder shows two primary ways to engineer your agent's session memory:
1. **SQL Database Persistency via SQLAlchemy**: Storing the conversation history in an external relational database (e.g. PostgreSQL) instead of in-memory lists.
2. **Context Window Trimming (Sliding Window)**: Implementing custom session classes that inherit from `SessionABC` to programmatically prune old conversational context (e.g. keeping only the last $N$ turns of user-assistant interactions).

## Key Features

### 1. Persistent SQLAlchemy Session
- **SQLAlchemy Persistency** ([main.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/session_context_engineering/main.py)): Uses `SQLAlchemySession` linked to a Neon Postgres DB engine to save conversation history. The agent automatically retrieves past message logs when queried with the same session token.

### 2. Custom Context Pruning (Sliding Window)
- **Sliding Turn Trimming** ([trimming.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/session_context_engineering/trimming.py)): Implements a custom `TrimmingSession` class which inherits from `SessionABC`. It dynamically maintains a sliding history, preserving only the last `max_turns` (e.g., 3 turns) of user messages and their corresponding agent responses/tool calls.
- **Turn Isolation Helper**: Automatically parses dictionary-based structure inputs and identifies which blocks correspond to user turns vs. assistant or tool responses.

## Files

- [main.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/session_context_engineering/main.py): Persisting memory with Postgres DB & `SQLAlchemySession`.
- [trimming.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/session_context_engineering/trimming.py): Programmatic context window trimming via a custom `SessionABC` class.

## Requirements

Ensure you have installed the required dependencies:

```bash
pip install agents python-dotenv sqlalchemy psycopg2-binary asyncpg
```

Configure your `.env` file with:

```env
GEMINI_API_KEY=your_gemini_api_key
```

## Running the Code

Run the Neon Postgres persistent session example:

```bash
python main.py
```

Run the context pruning (Trimming) simulation:

```bash
python trimming.py
```
