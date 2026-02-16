from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime
import uuid

class UserBase(BaseModel):
    """
    Base schema for user with common fields.
    """
    email: EmailStr

class UserCreate(UserBase):
    """
    Schema for creating a new user.
    """
    password: str = Field(..., min_length=8, description="Password must be at least 8 characters with complexity")

class UserLogin(BaseModel):
    """
    Schema for user login.
    """
    email: EmailStr
    password: str

class UserResponse(UserBase):
    """
    Schema for returning user data to the client.
    """
    id: uuid.UUID
    created_at: datetime
    
    class Config:
        from_attributes = True