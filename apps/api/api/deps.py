from fastapi import Depends
from core.security import get_current_user

# This module contains dependency injection functions
# Currently, we're using the get_current_user function from core.security
# but we could add more complex dependencies here if needed

# Export the get_current_user dependency for use in routes
async def get_current_user_dependency(current_user_id: str = Depends(get_current_user)) -> str:
    """
    Dependency to get the current user ID from the JWT token.
    
    Args:
        current_user_id: The user ID extracted from the JWT token
        
    Returns:
        str: The user ID of the authenticated user
    """
    return current_user_id