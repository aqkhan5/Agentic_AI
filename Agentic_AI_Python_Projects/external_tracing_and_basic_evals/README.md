# External Tracing with Langfuse: Learning Observability

Learn the core concepts of agent observability through simple, hands-on Python scripts. This project demonstrates how to set up, track, and group traces for AI agents using **Langfuse** and the **OpenAI Agents SDK**.

## 🎯 What This Project Teaches

- **Observability Setup**: Configuring OpenTelemetry-based auto-instrumentation using `openinference-instrumentation-openai-agents`.
- **Tool Tracing**: Visualizing custom tool invocations and inputs/outputs in a trace span.
- **Multi-Agent Tracing**: Observing conversation routing (triage agents handing off to specialized agents).
- **Trace Grouping**: Grouping multiple independent agent runs into a single logical workflow using `with trace(...)`.
- **Custom Metadata**: Adding attributes (user IDs, session IDs, custom metadata tags, and versioning) to trace logs via Langfuse's `@observe()` decorator.

## 📦 Prerequisites

- **Python 3.10+**
- **Gemini API key**: Get one from [Google AI Studio](https://aistudio.google.com/)
- **Langfuse Account**: Create a free account at [cloud.langfuse.com](https://cloud.langfuse.com) and retrieve your public/secret credentials.

## 🚀 Quick Setup

### 1. Install Dependencies

Ensure you have all dependencies synced:

```bash
pip install agents python-dotenv langfuse openinference-instrumentation-openai-agents opentelemetry-sdk opentelemetry-api
```

### 2. Configure Environment

Create a `.env` file in this folder:

```env
GEMINI_API_KEY=your-gemini-key-here
LANGFUSE_PUBLIC_KEY=pk-lf-your-public-key
LANGFUSE_SECRET_KEY=sk-lf-your-secret-key
LANGFUSE_HOST=https://cloud.langfuse.com  # Default host
```

## 📖 Step-by-Step Learning Path

Run these scripts in order to trace your agent's activity step-by-step:

### Step 1: Basic Tracing 🌟
**File**: [01_basic_trace.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/external_tracing_and_basic_evals/01_basic_trace.py)  
Demonstrates setting up `OpenAIAgentsInstrumentor` to capture agent executions and logging basic LLM inputs and outputs to the Langfuse backend.
```bash
python 01_basic_trace.py
```

### Step 2: Weather Agent Tool Tracing weather 🔧
**File**: [02_tool_trace.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/external_tracing_and_basic_evals/02_tool_trace.py)  
Showcases weather tool registration and logs detailed function invocation spans showing parameters and execution results.
```bash
python 02_tool_trace.py
```

### Step 3: Multi-Agent Handoff Tracing 🤝
**File**: [03_multi_agent_handsoff_trace.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/external_tracing_and_basic_evals/03_multi_agent_handsoff_trace.py)  
Demonstrates tracing a triage agent handing off control to language-specific specialized agents (Spanish vs. English).
```bash
python 03_multi_agent_handsoff_trace.py
```

### Step 4: Grouping Runs under workflows 📂
**File**: [04_grouping_agent_runs_trace.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/external_tracing_and_basic_evals/04_grouping_agent_runs_trace.py)  
Shows how to use `with trace("workflow_name"):` context managers to cluster consecutive agent operations (joke generator and joke rater) under a single parent trace session.
```bash
python 04_grouping_agent_runs_trace.py
```

### Step 5: Enriched Custom Metadata 🏷️
**File**: [05_custom_metadata.py](file:///mnt/FA68E41D68E3D683/Agentic%20_AI/Agentic_AI_Python_Projects/external_tracing_and_basic_evals/05_custom_metadata.py)  
Illustrates enrichment of traces with user IDs, session IDs, tags, version identifiers, and arbitrary metadata objects using Langfuse's `@observe` decorator and `langfuse.update_current_trace(...)`.
```bash
python 05_custom_metadata.py
```

## 🔗 View Your Traces

After executing any of the scripts above, log in to your Langfuse dashboard to explore the visual call tree:
👉 [cloud.langfuse.com](https://cloud.langfuse.com)
