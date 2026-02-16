from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import Optional
from uuid import UUID
from api.deps import get_current_user_dependency
from schemas.task import TaskCreate, TaskUpdate
from services.task_service import (
    create_task,
    get_user_tasks,
    update_task,
    toggle_task,
    delete_task
)

router = APIRouter()

@router.get("/tasks")
async def get_tasks(
    current_user_id: str = Depends(get_current_user_dependency),
    status: Optional[str] = Query(None, description="Filter tasks by status (all/pending/completed)"),
    sort: Optional[str] = Query(None, description="Sort tasks by criteria (created/title/due_date)")
):
    """
    Get all tasks for the authenticated user.
    
    Args:
        current_user_id: The ID of the authenticated user (extracted from JWT)
        status: Optional filter for task status
        sort: Optional sort parameter
        
    Returns:
        dict: A dictionary containing success status and task data
    """
    try:
        tasks = await get_user_tasks(current_user_id, status, sort)
        task_responses = [
            {
                "id": str(task.id),
                "title": task.title,
                "description": task.description,
                "completed": task.completed,
                "user_id": task.user_id,
                "created_at": task.created_at,
                "updated_at": task.updated_at
            }
            for task in tasks
        ]
        return {
            "success": True,
            "data": task_responses
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving tasks: {str(e)}"
        )

@router.post("/tasks")
async def create_new_task(
    task_data: TaskCreate,
    current_user_id: str = Depends(get_current_user_dependency)
):
    """
    Create a new task for the authenticated user.
    
    Args:
        task_data: The task data to create
        current_user_id: The ID of the authenticated user (extracted from JWT)
        
    Returns:
        dict: A dictionary containing success status and created task data
    """
    try:
        task = await create_task(current_user_id, task_data)
        task_response = {
            "id": str(task.id),
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
            "user_id": task.user_id,
            "created_at": task.created_at,
            "updated_at": task.updated_at
        }
        return {
            "success": True,
            "data": task_response
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating task: {str(e)}"
        )

@router.put("/tasks/{task_id}")
async def update_existing_task(
    task_id: UUID,
    task_data: TaskUpdate,
    current_user_id: str = Depends(get_current_user_dependency)
):
    """
    Update an existing task for the authenticated user.
    
    Args:
        task_id: The ID of the task to update
        task_data: The updated task data
        current_user_id: The ID of the authenticated user (extracted from JWT)
        
    Returns:
        dict: A dictionary containing success status and updated task data
    """
    try:
        task = await update_task(current_user_id, task_id, task_data)
        task_response = {
            "id": str(task.id),
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
            "user_id": task.user_id,
            "created_at": task.created_at,
            "updated_at": task.updated_at
        }
        return {
            "success": True,
            "data": task_response
        }
    except HTTPException:
        # Re-raise HTTP exceptions (like 404) as-is
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating task: {str(e)}"
        )

@router.patch("/tasks/{task_id}/toggle")
async def toggle_task_completion(
    task_id: UUID,
    current_user_id: str = Depends(get_current_user_dependency)
):
    """
    Toggle the completion status of a task for the authenticated user.
    
    Args:
        task_id: The ID of the task to toggle
        current_user_id: The ID of the authenticated user (extracted from JWT)
        
    Returns:
        dict: A dictionary containing success status and updated task data
    """
    try:
        task = await toggle_task(current_user_id, task_id)
        task_response = {
            "id": str(task.id),
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
            "user_id": task.user_id,
            "created_at": task.created_at,
            "updated_at": task.updated_at
        }
        return {
            "success": True,
            "data": task_response
        }
    except HTTPException:
        # Re-raise HTTP exceptions (like 404) as-is
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error toggling task: {str(e)}"
        )

@router.delete("/tasks/{task_id}")
async def delete_existing_task(
    task_id: UUID,
    current_user_id: str = Depends(get_current_user_dependency)
):
    """
    Delete a task for the authenticated user.
    
    Args:
        task_id: The ID of the task to delete
        current_user_id: The ID of the authenticated user (extracted from JWT)
        
    Returns:
        dict: A dictionary containing success status
    """
    try:
        success = await delete_task(current_user_id, task_id)
        if success:
            return {
                "success": True,
                "data": None
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Error deleting task"
            )
    except HTTPException:
        # Re-raise HTTP exceptions (like 404) as-is
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting task: {str(e)}"
        )