# Agent as a Tool Demo

This project demonstrates the **"Agents as a Tool"** pattern using the **OpenAI Agents SDK**.

## Overview

"Agent as a tool" means you let one agent call another agent like a function—without giving away control of the conversation. It is perfect when you want a main agent (orchestrator) 🧑‍💼 to stay in charge of the primary conversation flow, while specialist agents do small, focused jobs (e.g., translate text, extract dates, summarize, or search databases) and return their results back to the orchestrator.

## Key Features

1. **Sub-Agent Tools**: Converts specialized agents (`spanish_agent`, `french_agent`) into tools using the `.as_tool(tool_name, tool_description)` method.
2. **Orchestrator Agent**: Manages the main user request and selectively invokes the sub-agent tools based on the user's prompt (e.g., translating a message to Spanish or French).
3. **Async Runner Execution**: Runs the orchestration workflow asynchronously using `Runner.run`.

## Files

- [main.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/08_agentAs_tool/main.py): Contains the definition of the orchestrator, translation agents, and execution loop.

## Requirements

Ensure you have installed the required dependencies:

```bash
pip install agents python-dotenv
```

Configure your `.env` file with:

```env
GEMINI_API_KEY=your_gemini_api_key
```

## Running the Code

Execute the script using:

```bash
python main.py
```
