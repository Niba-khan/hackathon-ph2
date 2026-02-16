from sqlmodel import select
from sqlalchemy.exc import IntegrityError
from db.models import User, UserCreate
from core.hashing import hash_password, verify_password
from db.session import AsyncSessionLocal
from typing import Optional
from fastapi import HTTPException, status
import uuid
from datetime import datetime

async def register_user(user_data: UserCreate) -> User:
    """
    Register a new user with secure password hashing.
    
    Args:
        user_data: The user registration data containing email and password
        
    Returns:
        User: The created user object
        
    Raises:
        HTTPException: If email is already registered or validation fails
    """
    async with AsyncSessionLocal() as session:
        # Check if user with this email already exists
        existing_user_query = select(User).where(User.email == user_data.email)
        result = await session.execute(existing_user_query)
        existing_user = result.scalar_one_or_none()
        
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )
        
        # Hash the password
        hashed_password = hash_password(user_data.password)
        
        # Create new user
        user = User(
            email=user_data.email,
            hashed_password=hashed_password,
            created_at=datetime.utcnow()
        )
        
        # Add to session and commit
        session.add(user)
        try:
            await session.commit()
            await session.refresh(user)
        except IntegrityError:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered"
            )
        
        return user

async def authenticate_user(email: str, password: str) -> Optional[User]:
    """
    Authenticate user credentials.

    Args:
        email: User's email
        password: User's password

    Returns:
        User object if credentials are valid, None otherwise
    """
    async with AsyncSessionLocal() as session:
        # Find user by email
        query = select(User).where(User.email == email)
        result = await session.execute(query)
        user = result.scalar_one_or_none()

        if not user or not verify_password(password, user.hashed_password):
            return None

        return user