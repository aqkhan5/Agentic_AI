# Streaming Response Agent Demo

This project demonstrates how to run an agent asynchronously and stream its execution events in real-time using the **OpenAI Agents SDK**.

## Overview

Streaming is crucial for building interactive, low-latency AI applications. Instead of waiting for the agent to finish its execution and output the entire response, streaming allows you to process and display parts of the response (deltas), tool executions, and step-by-step progress as they happen.

## Key Features

1. **Stream Runner**: Uses `Runner.run_streamed` to initiate a streamed execution of the agent.
2. **Event Consumption**: Iterates over events asynchronously using `async for event in output.stream_events()`.
3. **Custom User Context**: Passes a custom typed `UserContext` dataclass to the agent runtime, showing how context-aware agents can access user parameters inside both dynamic instructions and custom tools (`RunContextWrapper`).
4. **Tool Execution in Stream**: Demonstrates how tool execution (e.g., an async `search` tool with simulated delay) is reported as part of the stream event lifecycle.

## Files

- [main.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/6_streaming/main.py): Registers the streaming execution loop, custom context, and streaming runner.

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
