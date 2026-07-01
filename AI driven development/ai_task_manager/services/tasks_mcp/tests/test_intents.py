import pytest
from datetime import datetime, UTC
from services.tasks_mcp.src.models import Task, TaskStatus
# We expect this import to fail or the class to be missing initially
from services.tasks_mcp.src.storage import StorageManager

@pytest.mark.asyncio
async def test_tasks_capture_intent():
    storage = StorageManager()
    title = "Buy groceries"
    remind_at = "2026-06-01T10:00:00Z"
    
    task = await storage.capture(title=title, remind_at=remind_at)
    
    assert task.title == title
    assert task.status == TaskStatus.TODO
    assert task.user_id == "mock_user_123"
    assert task.remind_at == datetime(2026, 6, 1, 10, 0, tzinfo=UTC)
    
    # Verify it's actually in the database
    stored_task = await storage.get_by_id(task.id)
    assert stored_task.id == task.id

@pytest.mark.asyncio
async def test_tasks_review_intent_today():
    storage = StorageManager()
    now = datetime.now(UTC)
    
    # Task for today
    await storage.capture(title="Task Today", remind_at=now.isoformat())
    # Task for future
    await storage.capture(title="Task Future", remind_at="2026-12-31T23:59:59Z")
    
    agenda = await storage.review(query="today")
    
    assert len(agenda) == 1
    assert agenda[0].title == "Task Today"
