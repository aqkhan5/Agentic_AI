# Basic Agent Handoffs Demo

This project demonstrates the **Agent Handoff** pattern using the **OpenAI Agents SDK**.

## Overview

Unlike the "Agent as a Tool" pattern where the orchestrator stays in charge, the **Agent Handoff** pattern completely transfers ownership of the conversation from one agent to another. Once a handoff is triggered, the target agent (specialist) takes full control and interacts directly with the user. This is particularly useful for routing tasks (e.g., triage bots directing users to specific support desks).

## Key Features

1. **Conversation Handoff**: Demonstrates how to use `handoffs=[agent_a, handoff(agent_b)]` in the `Agent` configuration to define target agents for routing.
2. **Multi-Turn Conversation Tracking**:
   - Shows how the routing/triage agent determines the appropriate specialist based on user input.
   - Demonstrates how to retrieve the active specialist from the runner execution result (`r1.last_agent`).
   - Demonstrates how to maintain conversation context over multiple turns using `result.to_input_list()`.

## Files

- [hello.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/08_basic_handsoff/hello.py): Standard triage router example handing off to `Billing Agent` or `Refunds Agent`.
- [main.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/08_basic_handsoff/main.py): A multi-turn coach router that hands off to either a `Fitness Coach` or `Study Coach`, continuing the chat with the chosen specialist.

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

To run the triage support example:

```bash
python hello.py
```

To run the multi-turn coach routing example:

```bash
python main.py
```
