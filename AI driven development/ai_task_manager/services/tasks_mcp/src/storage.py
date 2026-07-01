import asyncio
from datetime import datetime, UTC
from typing import Optional, List
from services.tasks_mcp.src.models import Task, TaskStatus

class StorageManager:
    def __init__(self):
        self.tasks_db: dict[str, Task] = {}
        self.lock = asyncio.Lock()

    async def capture(
        self, 
        title: str, 
        description: Optional[str] = None, 
        remind_at: Optional[str] = None, 
        user_id: str = "mock_user_123"
    ) -> Task:
        async with self.lock:
            task = Task(
                title=title,
                description=description,
                remind_at=remind_at,
                user_id=user_id
            )
            self.tasks_db[task.id] = task
            # TODO: Trigger notification service if remind_at is set
            return task

    async def get_by_id(self, task_id: str) -> Optional[Task]:
        return self.tasks_db.get(task_id)

    async def review(self, query: str = "today", user_id: str = "mock_user_123") -> List[Task]:
        now = datetime.now(UTC)
        filtered_tasks = [
            t for t in self.tasks_db.values() 
            if t.user_id == user_id and t.status != TaskStatus.COMPLETED
        ]

        if query == "today":
            filtered_tasks = [
                t for t in filtered_tasks
                if (t.due_at and t.due_at.date() == now.date()) or 
                   (t.remind_at and t.remind_at.date() == now.date())
            ]
        elif query == "overdue":
            filtered_tasks = [
                t for t in filtered_tasks
                if t.due_at and t.due_at < now
            ]
        
        # Sort by due_at or remind_at or created_at
        filtered_tasks.sort(key=lambda x: x.due_at or x.remind_at or x.created_at)
        return filtered_tasks

    async def modify(self, task_id: str, **kwargs) -> Optional[Task]:
        async with self.lock:
            if task_id not in self.tasks_db:
                return None
            
            task = self.tasks_db[task_id]
            for key, value in kwargs.items():
                if hasattr(task, key) and value is not None:
                    setattr(task, key, value)
            
            task.updated_at = datetime.now(UTC)
            # TODO: Handle notification rescheduling if remind_at changed
            return task

    async def resolve(self, task_id: str, resolution: str = "completed") -> Optional[Task]:
        async with self.lock:
            if task_id not in self.tasks_db:
                return None
            
            task = self.tasks_db[task_id]
            if resolution == "completed":
                task.status = TaskStatus.COMPLETED
            elif resolution == "skipped":
                # For now, we'll just treat skipped as completed or add a SKIPPED status
                task.status = TaskStatus.COMPLETED 
            
            task.updated_at = datetime.now(UTC)
            # TODO: Cancel notifications
            return task

    async def remove(self, task_id: str) -> bool:
        async with self.lock:
            if task_id in self.tasks_db:
                del self.tasks_db[task_id]
                # TODO: Cancel notifications
                return True
            return False
