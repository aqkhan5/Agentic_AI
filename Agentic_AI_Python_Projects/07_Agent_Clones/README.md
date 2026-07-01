# Agent Clones Demo

This project demonstrates how to clone AI agents using the **OpenAI Agents SDK** and provides educational examples showing the difference between shallow copying (using `dataclasses.replace`), deep copying (using Python's `copy.deepcopy`), and custom clone methods.

## Overview

In multi-agent systems, you often need to create new agents that inherit settings, tools, or models from an existing agent, but with some modifications (e.g., customized instructions or different model settings like temperature). The Agents SDK supports agent cloning to facilitate this.

## Key Features

1. **SDK Agent Cloning**: Demonstrates how to use `base_agent.clone(...)` to spawn a new agent with overridden configurations such as `name`, `model_settings` (temperature, max tokens), etc.
2. **Tavily Search Integration**: Registers a custom search tool using the Tavily search client to answer general knowledge questions.
3. **Dataclass Cloning & Mutability Analysis**:
   - Illustrates shallow copy behavior with `dataclasses.replace` where nested mutable objects (like lists of tools) are shared.
   - Shows how `copy.deepcopy` resolves mutable state sharing by duplicating lists.
   - Implements a custom `.clone()` method on a dataclass to demonstrate clean cloning with manual copies of mutable collections.

## Files

- [main.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/07_Agent_Clones/main.py): Contains the primary implementation for agent cloning and the copying comparison examples.

## Requirements

Ensure you have installed the core dependencies:

```bash
pip install agents python-dotenv tavily-python
```

Configure your `.env` file with:

```env
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Running the Code

Execute the script using:

```bash
python main.py
```
