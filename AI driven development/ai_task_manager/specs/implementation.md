# Implementation Overview: Tasks MCP Server

This document provides a comprehensive explanation of the current implementation of the Tasks MCP Server, detailing the architecture, components, and tool logic.

---

## 1. System Architecture

The Tasks MCP Server is designed as a modular, stateless service using the Model Context Protocol (MCP).

### Transport Layer
- **Protocol:** Streamable HTTP.
- **Framework:** `FastMCP` (Python).
- **Rationale:** Enables remote access, horizontal scaling, and compatibility with cloud environments like Kubernetes by avoiding the local-only constraints of `stdio`.

### Storage Layer
- **Type:** In-memory (Python dictionary).
- **Thread Safety:** Managed via `asyncio.Lock` to ensure atomic updates during task mutations.
- **Location:** `services/tasks_mcp/src/storage.py` (`StorageManager` class).

---

## 2. Core Components

### Data Model (`models.py`)
Uses **Pydantic v2** for robust validation and serialization.
- **Task Schema:** Includes `id` (UUID), `user_id` (defaults to `mock_user_123`), `title`, `description`, `status` (todo, in_progress, completed), `due_at`, `remind_at`, `created_at`, and `updated_at`.
- **Validation:** Automatic ISO 8601 string parsing for datetime fields with UTC enforcement.

### Storage Manager (`storage.py`)
Acts as the internal "database" engine.
- Implements CRUD logic for tasks.
- Handles filtering for the `tasks_review` intent (e.g., "today", "overdue").
- Ensures consistent `updated_at` timestamps on modification.

### MCP Server (`server.py`)
The entry point that exposes the business logic to AI agents.
- Defines **Input Schemas** for every tool using Pydantic models with `extra='forbid'` for strictness.
- Maps MCP tool calls to `StorageManager` methods.

---

## 3. The 5-Intent Tool Model

We implement five specialized tools that map to common human task management workflows:

1.  **`tasks_capture`**: Creates a new task.
    - *Default:* Sets owner to `mock_user_123` if not specified.
    - *Future:* Will trigger the Notification Service if a reminder time is provided.

2.  **`tasks_review`**: Returns a filtered list of tasks.
    - *Queries:* `today` (tasks due/reminding today), `overdue` (uncompleted tasks with past due dates), or `all`.

3.  **`tasks_modify`**: Patches existing task fields (title, description, dates).
    - *Logic:* Only updates provided fields; leaves others unchanged.

4.  **`tasks_resolve`**: Marks a task as `completed` or `skipped`.
    - *Logic:* Essential for stopping recurring alerts or clearing lists without deletion.

5.  **`tasks_remove`**: Permanently deletes a task.
    - *Annotation:* Marked with `destructiveHint: true` to ensure AI agents request user confirmation.

---

## 4. Current State & Verification

- **Tests:** Unit tests in `tests/test_intents.py` verify the `capture` and `review` logic.
- **Package Structure:** Fully configured with `__init__.py` files for proper Python module resolution.
- **Execution:** The server can be started via:
  ```bash
  PYTHONPATH=. uv run python services/tasks_mcp/src/server.py
  ```
