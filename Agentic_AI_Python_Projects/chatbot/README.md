# Chainlit Web Chatbot Demo

This project demonstrates how to build a web-based AI assistant interface using **Chainlit** and the **OpenAI Agents SDK**.

## Overview

While console loops are good for testing, real-world applications require interactive user interfaces. This project shows how to easily bridge your AI agents with a beautiful, real-time web UI using Chainlit, managing state and conversation history smoothly.

## Key Features

1. **Chainlit Web UI Integration**: Integrates the Agents SDK with a responsive web chat interface.
2. **Session State Management**: Uses Chainlit's `user_session` to store the active `chat_history`, the `Agent` configuration, and the `RunConfig`.
3. **Non-Blocking Execution**: Wraps the synchronous `Runner.run_sync` calls in `cl.make_async` to keep Chainlit's async event loop responsive.
4. **UX Enhancements**: Displays a dynamic "Thinking..." status message while waiting for the LLM response, updating it once the output is available.

## Files

- [main.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/chatbot/main.py): Contains the primary Chainlit event listeners (`@cl.on_chat_start` and `@cl.on_message`) and the agent runner logic.

## Requirements

Ensure you have installed the required dependencies:

```bash
pip install agents python-dotenv chainlit
```

Configure your `.env` file with:

```env
GEMINI_API_KEY=your_gemini_api_key
```

## Running the Code

Launch the Chainlit web server using:

```bash
chainlit run main.py -w
```

This will automatically open the chatbot UI in your default web browser (typically at `http://localhost:8000`).
