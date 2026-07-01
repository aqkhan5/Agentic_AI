# Dynamic Instructions Demo

This project demonstrates how to use **Dynamic Instructions** in the **OpenAI Agents SDK** to let agents adapt their behavior at runtime.

## Overview

Typically, agent instructions (prompts) are static strings. However, the OpenAI Agents SDK allows you to supply a Python function or callable object as the agent's `instructions`. This callable is executed on every run, allowing the agent's behavior to change dynamically based on the current context, conversation history, time of day, or other external states.

## Key Features

The project includes five concrete examples of dynamic instructions:

1. **Basic Dynamic Instructions**: A simple function that returns system instructions dynamically based on the agent's name.
2. **Context-Aware Instructions**: Modifies instructions based on the number of messages exchanged in the current conversation (retrieved from `context.messages`).
3. **Time-Based Instructions**: Adapts the agent's tone (e.g., energetic vs. calm) based on the current hour of the day.
4. **Stateful Instructions**: Implements a callable class that tracks the total number of interactions and changes its prompt accordingly (e.g., starting as welcoming, then becoming more efficient over time).
5. **Context & Agent Explorer**: Inspects attributes from the `RunContextWrapper` and `Agent` objects to dynamically generate system instructions detailing the agent's capabilities (name, tools, etc.) and current conversation status.

## Files

- [main.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/5_dynamic_instruction/main.py): Contains all five examples in a runnable tutorial format.

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
