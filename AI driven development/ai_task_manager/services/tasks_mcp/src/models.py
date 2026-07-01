from datetime import datetime, UTC
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, field_validator
import uuid

class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class Task(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str = "mock_user_123"
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.TODO
    due_at: Optional[datetime] = None
    remind_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    @field_validator("due_at", "remind_at", mode="before")
    @classmethod
    def validate_utc(cls, v):
        if isinstance(v, str):
            try:
                dt = datetime.fromisoformat(v.replace("Z", "+00:00"))
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=UTC)
                return dt
            except ValueError:
                return v
        return v
