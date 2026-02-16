from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class UserBase(SQLModel):
    """
    Base model for user with common fields.
    """
    email: str = Field(unique=True, index=True)

class User(UserBase, table=True):
    """
    User model for authentication.
    """
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class TaskBase(SQLModel):
    """
    Base model for task with common fields.
    """
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None)
    completed: bool = Field(default=False)
    user_id: str = Field(index=True)  # Index for efficient user-based queries

class Task(TaskBase, table=True):
    """
    Task model representing a todo item associated with a specific user.
    """
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class UserCreate(SQLModel):
    """
    Schema for creating a new user.
    """
    email: str
    password: str

class UserLogin(SQLModel):
    """
    Schema for user login.
    """
    email: str
    password: str

class UserResponse(SQLModel):
    """
    Schema for returning user data to the client.
    """
    id: uuid.UUID
    email: str
    created_at: datetime

class TaskCreate(TaskBase):
    """
    Schema for creating a new task.
    """
    title: str = Field(min_length=1, max_length=200)
    description: Optional[str] = Field(default=None)

class TaskUpdate(SQLModel):
    """
    Schema for updating an existing task.
    """
    title: Optional[str] = Field(default=None, min_length=1, max_length=200)
    description: Optional[str] = Field(default=None)
    completed: Optional[bool] = Field(default=None)

class TaskResponse(TaskBase):
    """
    Schema for returning task data to the client.
    """
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime