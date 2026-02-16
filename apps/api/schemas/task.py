from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import uuid

class TaskBase(BaseModel):
    """
    Base schema for task with common fields.
    """
    title: str = Field(..., min_length=1, max_length=200, description="Task title (1-200 characters)")
    description: Optional[str] = Field(default=None, description="Optional task description")

class TaskCreate(TaskBase):
    """
    Schema for creating a new task.
    """
    pass  # Inherits from TaskBase

class TaskUpdate(BaseModel):
    """
    Schema for updating an existing task.
    """
    title: Optional[str] = Field(default=None, min_length=1, max_length=200, description="Task title (1-200 characters)")
    description: Optional[str] = Field(default=None, description="Optional task description")
    completed: Optional[bool] = Field(default=None, description="Task completion status")

class TaskResponse(TaskBase):
    """
    Schema for returning task data to the client.
    """
    id: uuid.UUID
    completed: bool
    user_id: str
    created_at: datetime
    updated_at: datetime