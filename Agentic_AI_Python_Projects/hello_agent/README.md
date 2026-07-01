# Hello Agent

A simple AI agent built with the **OpenAI Agents SDK** that demonstrates basic agent functionality using Google's Gemini API.

## Overview

This project creates a basic math agent that can solve mathematical problems using the Gemini 2.5 Flash model. It demonstrates the fundamental concepts of creating and running an AI agent.

## Features

- Basic agent setup with Gemini API integration
- Simple math problem-solving capabilities
- Synchronous agent execution
- Environment variable configuration

## Prerequisites

- Python 3.8+
- Gemini API key from Google AI Studio

## Installation

1. Clone the repository
2. Install dependencies:
```bash
pip install agents python-dotenv
```

3. Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

## Usage

Run the agent:
```bash
python main.py
```

The agent will solve the question: "What is the square root of 16?"

## How It Works

1. Loads environment variables from `.env` file
2. Initializes an OpenAI-compatible client with Gemini API
3. Creates a math agent with specific instructions
4. Runs the agent synchronously with a math query
5. Prints the agent's response

## Project Structure

```
hello_agent/
├── main.py          # Main agent implementation
├── .env             # Environment variables (not tracked)
└── README.md        # This file
```

## Example Output

```
AGENT RESPONSE: The square root of 16 is 4.
```

## License

MIT
