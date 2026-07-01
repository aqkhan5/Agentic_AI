# Basic Tracing Demo

This project demonstrates how to set up and inspect trace logs for AI agent execution using the **OpenAI Agents SDK**.

## Overview

Tracing allows developers to inspect agent runs, showing step-by-step reasoning, tool execution, and LLM completions. This is essential for debugging and profiling agent behaviors, especially when dealing with complex multi-turn interactions and tool calls.

## Key Features

1. **Agent Setup**: Configures a basic `WeatherAgent` with a simple custom weather tool.
2. **Tool-Enabled Run**: Traces a single run asking for weather details in a specific location (e.g., Karachi).
3. **Execution Tracing**: Shows how internal instrumentation captures LLM calls and tool calls.

## Files

- [main.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/07_basic_tracing/main.py): Registers the weather tool and executes the agent synchronously, printing the execution result.

## Requirements

Ensure you have installed the required dependencies:

```bash
pip install agents python-dotenv
```

Configure your `.env` file with:

```env
GEMINI_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_api_key  # Optional, but may be used by the SDK tracing middleware
```

## Running the Code

Execute the script using:

```bash
python main.py
```
