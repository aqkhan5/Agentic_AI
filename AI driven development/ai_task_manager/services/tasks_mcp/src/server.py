import asyncio
from typing import Optional, List
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field, ConfigDict

from services.tasks_mcp.src.storage import StorageManager
from services.tasks_mcp.src.models import Task, TaskStatus

mcp = FastMCP("tasks_mcp")
storage = StorageManager()

# --- Input Models ---

class CaptureInput(BaseModel):
    model_config = ConfigDict(extra='forbid')
    title: str = Field(..., description="The task summary")
    description: Optional[str] = Field(None, description="Optional details")
    remind_at: Optional[str] = Field(None, description="Optional reminder time (ISO 8601)")
    user_id: str = Field("mock_user_123", description="Optional user ID")

class ReviewInput(BaseModel):
    model_config = ConfigDict(extra='forbid')
    query: str = Field("today", description="Query type: 'today', 'overdue', or 'all'")
    user_id: str = Field("mock_user_123", description="Optional user ID")

class ModifyInput(BaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str = Field(..., description="The UUID of the task to modify")
    title: Optional[str] = Field(None, description="Updated task summary")
    description: Optional[str] = Field(None, description="Updated details")
    due_at: Optional[str] = Field(None, description="Updated due time (ISO 8601)")
    remind_at: Optional[str] = Field(None, description="Updated reminder time (ISO 8601)")

class ResolveInput(BaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str = Field(..., description="The UUID of the task to resolve")
    resolution: str = Field("completed", description="Resolution type: 'completed' or 'skipped'")

class RemoveInput(BaseModel):
    model_config = ConfigDict(extra='forbid')
    id: str = Field(..., description="The UUID of the task to remove")

# --- Tools ---

@mcp.tool(name="tasks_capture")
async def tasks_capture(params: CaptureInput) -> str:
    """Capture a new task and optional schedule."""
    task = await storage.capture(
        title=params.title,
        description=params.description,
        remind_at=params.remind_at,
        user_id=params.user_id
    )
    return f"Task captured successfully: {task.title} (ID: {task.id})"

@mcp.tool(name="tasks_review")
async def tasks_review(params: ReviewInput) -> List[Task]:
    """Get a high-signal overview of tasks."""
    tasks = await storage.review(query=params.query, user_id=params.user_id)
    return tasks

@mcp.tool(name="tasks_modify")
async def tasks_modify(params: ModifyInput) -> str:
    """Update task details or reschedule."""
    task = await storage.modify(
        task_id=params.id,
        title=params.title,
        description=params.description,
        due_at=params.due_at,
        remind_at=params.remind_at
    )
    if not task:
        return f"Error: Task with ID {params.id} not found."
    return f"Task {params.id} updated successfully."

@mcp.tool(name="tasks_resolve")
async def tasks_resolve(params: ResolveInput) -> str:
    """Complete or skip a task."""
    task = await storage.resolve(task_id=params.id, resolution=params.resolution)
    if not task:
        return f"Error: Task with ID {params.id} not found."
    return f"Task {params.id} resolved as {params.resolution}."

@mcp.tool(
    name="tasks_remove",
    annotations={
        "destructiveHint": True
    }
)
async def tasks_remove(params: RemoveInput) -> str:
    """Delete a task permanently."""
    success = await storage.remove(task_id=params.id)
    if not success:
        return f"Error: Task with ID {params.id} not found."
    return f"Task {params.id} removed permanently."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
