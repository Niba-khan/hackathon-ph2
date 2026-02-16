from sqlmodel import select
from sqlalchemy import and_
from sqlalchemy.exc import IntegrityError
from db.models import Task, TaskCreate, TaskUpdate
from db.session import AsyncSessionLocal
from typing import List, Optional
from fastapi import HTTPException, status
from datetime import datetime
import uuid

async def create_task(user_id: str, task_data: TaskCreate) -> Task:
    """
    Create a new task for the authenticated user.
    
    Args:
        user_id: The ID of the user creating the task (extracted from JWT)
        task_data: The task data to create
        
    Returns:
        Task: The created task object
    """
    async with AsyncSessionLocal() as session:
        # Create a new task instance with the provided data
        task = Task(
            title=task_data.title,
            description=task_data.description,
            completed=False,  # Default to not completed
            user_id=user_id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        
        # Add to session and commit
        session.add(task)
        try:
            await session.commit()
            await session.refresh(task)
        except IntegrityError:
            await session.rollback()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error creating task"
            )
        
        return task

async def get_user_tasks(
    user_id: str, 
    status_filter: Optional[str] = None, 
    sort_by: Optional[str] = None
) -> List[Task]:
    """
    Get all tasks for the authenticated user, with optional filtering and sorting.
    
    Args:
        user_id: The ID of the user whose tasks to retrieve (extracted from JWT)
        status_filter: Optional filter for task status ('all', 'pending', 'completed')
        sort_by: Optional sort parameter ('created', 'title', 'due_date')
        
    Returns:
        List[Task]: List of tasks belonging to the user
    """
    async with AsyncSessionLocal() as session:
        # Build the query to filter tasks by user_id
        query = select(Task).where(Task.user_id == user_id)
        
        # Apply status filter if provided
        if status_filter and status_filter.lower() != 'all':
            if status_filter.lower() == 'pending':
                query = query.where(Task.completed == False)
            elif status_filter.lower() == 'completed':
                query = query.where(Task.completed == True)
        
        # Apply sorting if provided
        if sort_by:
            if sort_by == 'created':
                query = query.order_by(Task.created_at.desc())
            elif sort_by == 'title':
                query = query.order_by(Task.title.asc())
        
        # Execute the query
        result = await session.execute(query)
        tasks = result.scalars().all()
        
        return tasks

async def update_task(user_id: str, task_id: uuid.UUID, task_data: TaskUpdate) -> Task:
    """
    Update an existing task for the authenticated user.
    
    Args:
        user_id: The ID of the user who owns the task (extracted from JWT)
        task_id: The ID of the task to update
        task_data: The updated task data
        
    Returns:
        Task: The updated task object
        
    Raises:
        HTTPException: If the task doesn't exist or doesn't belong to the user
    """
    async with AsyncSessionLocal() as session:
        # Find the task that belongs to the user
        query = select(Task).where(and_(Task.id == task_id, Task.user_id == user_id))
        result = await session.execute(query)
        task = result.scalar_one_or_none()
        
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found or does not belong to the authenticated user"
            )
        
        # Update the task with provided data
        if task_data.title is not None:
            task.title = task_data.title
        if task_data.description is not None:
            task.description = task_data.description
        if task_data.completed is not None:
            task.completed = task_data.completed
            
        # Update the updated_at timestamp
        task.updated_at = datetime.utcnow()
        
        # Commit the changes
        await session.commit()
        await session.refresh(task)
        
        return task

async def toggle_task(user_id: str, task_id: uuid.UUID) -> Task:
    """
    Toggle the completion status of a task for the authenticated user.
    
    Args:
        user_id: The ID of the user who owns the task (extracted from JWT)
        task_id: The ID of the task to toggle
        
    Returns:
        Task: The updated task object with toggled completion status
        
    Raises:
        HTTPException: If the task doesn't exist or doesn't belong to the user
    """
    async with AsyncSessionLocal() as session:
        # Find the task that belongs to the user
        query = select(Task).where(and_(Task.id == task_id, Task.user_id == user_id))
        result = await session.execute(query)
        task = result.scalar_one_or_none()
        
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found or does not belong to the authenticated user"
            )
        
        # Toggle the completion status
        task.completed = not task.completed
        # Update the updated_at timestamp
        task.updated_at = datetime.utcnow()
        
        # Commit the changes
        await session.commit()
        await session.refresh(task)
        
        return task

async def delete_task(user_id: str, task_id: uuid.UUID) -> bool:
    """
    Delete a task for the authenticated user.
    
    Args:
        user_id: The ID of the user who owns the task (extracted from JWT)
        task_id: The ID of the task to delete
        
    Returns:
        bool: True if the task was successfully deleted
        
    Raises:
        HTTPException: If the task doesn't exist or doesn't belong to the user
    """
    async with AsyncSessionLocal() as session:
        # Find the task that belongs to the user
        query = select(Task).where(and_(Task.id == task_id, Task.user_id == user_id))
        result = await session.execute(query)
        task = result.scalar_one_or_none()
        
        if not task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found or does not belong to the authenticated user"
            )
        
        # Delete the task
        await session.delete(task)
        await session.commit()
        
        return True