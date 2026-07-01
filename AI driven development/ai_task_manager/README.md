# AI Task Manager 🚀

An AI-native task management system that helps users manage tasks, reminders, and appointment-style workflows through natural conversation.

This project is built on the principles of **agentic orchestration**, where specialized AI agents coordinate through strict boundaries to deliver a reliable, modular user experience.

---

## 🏗️ Architecture & Boundaries

The system is divided into clear operational domains:

1.  **Tasks Manager Agent:** The primary user-facing orchestrator. Owns intent parsing, clarification, routing, and final user confirmation.
2.  **Tasks MCP Server (`tasks_mcp`):** The exclusive backend service for all task mutations. Agents do not mutate the database directly; they communicate via the Model Context Protocol (MCP).
3.  **Appointment Booking Agent:** A specialized agent routed to for booking workflows. It handles scheduling but **never** mutates tasks directly.
4.  **Notifications API:** A standalone service triggered only after valid task mutations succeed.

---

## 📁 Project Structure

```
ai_task_manager/
├── services/
│   └── tasks_mcp/
│       ├── src/
│       │   ├── __init__.py
│       │   ├── models.py         # Task schemas and validators (Pydantic)
│       │   ├── storage.py        # In-memory database with asyncio locks
│       │   └── server.py         # FastMCP Server defining the tool schemas
│       └── tests/
│           ├── __init__.py
│           └── test_intents.py   # Asynchronous tests for intents and storage
├── specs/
│   ├── implementation.md         # Detailed API and testing specs
│   ├── mcp-server-architecture.md # Architectural guidelines
│   └── tasks-tool-definitions.md # Definitions for MCP tools
├── AGENTS.md                     # Academic tone and constitution
├── GEMINI.md                     # Gemini-specific guidelines
├── main.py                       # Main CLI entry point
├── pyproject.toml                # Project configurations & dependency manifest
├── uv.lock                       # uv lockfile
└── README.md                     # Project documentation (this file)
```

---

## 🛠️ Tech Stack & Defaults

- **Language:** Python 3.12+ (Backend/Agents), TypeScript (Frontend)
- **Package Manager:** `uv` (Exclusive tool for dependency resolution and environments)
- **AI Framework:** OpenAI Agents SDK / Claude Code
- **Protocol:** Model Context Protocol (MCP) (via `FastMCP`)
- **Testing:** `pytest` and `pytest-asyncio` for async database & mutation verification
- **Infrastructure:** Kubernetes-first (Containers via `ghcr.io`, stateless design)

---

## 📜 The Constitution

Every design and implementation decision in this repository is governed by our project constitution. 

👉 **[Read AGENTS.md](./AGENTS.md)** before contributing. 

Key principles include:
- **Test-First Default:** Write failing tests covering expected behavior before implementing.
- **Docs-First Development:** Verify SDK/Framework behavior against official docs. Outdated assumptions are bugs.
- **Kubernetes From The Start:** All services must be stateless, configurable via environment variables, and equipped with health probes.
- **Always Verify:** Plausible output is not verified output. Prove it works empirically.

---

## 🚀 Getting Started

This project is managed with the modern and extremely fast Python package manager `uv`.

### 1. Installation
Initialize the virtual environment and sync dependencies:
```bash
# Navigate to the project directory
cd ai_task_manager

# Sync python environment
uv sync
```

### 2. Running the Tasks MCP Server
The backend service uses `FastMCP` from the `mcp.server.fastmcp` module. It can be started in http/SSE streamable mode:
```bash
uv run python services/tasks_mcp/src/server.py
```

To run it as an MCP service for your AI client (like Claude Code or cursor):
```bash
# Add the server using the CLI (example for Claude Code)
claude mcp add --transport stdio tasks-mcp -- uv run python services/tasks_mcp/src/server.py
```

### 3. Exposed MCP Tools

The `tasks_mcp` server exposes the following tools to AI agents:

- **`tasks_capture`**: Capture a new task and optional schedule.
- **`tasks_review`**: Retrieve a high-signal list of tasks matching a query (e.g. `'today'`, `'overdue'`).
- **`tasks_modify`**: Update details, due times, or reschedule a task by UUID.
- **`tasks_resolve`**: Complete or skip a task by UUID.
- **`tasks_remove`**: Destructive operation to permanently delete a task (requires confirmation).

---

## 🧪 Testing

The testing suite utilizes `pytest` and `pytest-asyncio` for testing async databases and storage mutations.

To run the tests:
```bash
uv run pytest
```

---
**Maintained by:** [AbdulQadeerKhan555](https://github.com/AbdulQadeerKhan555)
