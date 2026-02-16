from fastapi import APIRouter, Depends, HTTPException, status
from datetime import timedelta
from core.security import create_access_token
from core.config import settings
from schemas.user import UserCreate, UserLogin
from services.auth_service import register_user, authenticate_user
from api.deps import get_current_user_dependency
from core.security import get_current_user

router = APIRouter()

@router.post("/auth/signup")
async def signup(user_data: UserCreate):
    """
    Register a new user and return JWT token.
    """
    try:
        # Create the user in the database
        user = await register_user(user_data)
        
        # Generate JWT access token
        access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
        access_token = create_access_token(
            data={"sub": str(user.id), "email": user.email},
            expires_delta=access_token_expires
        )
        
        # Return token to client
        return {
            "success": True,
            "data": {
                "access_token": access_token,
                "token_type": "bearer"
            }
        }
    except HTTPException:
        # Re-raise HTTP exceptions (like 409) as-is
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating user: {str(e)}"
        )

@router.post("/auth/login")
async def login(user_data: UserLogin):
    """
    Authenticate user and return JWT token.
    """
    try:
        # Verify user credentials
        user = await authenticate_user(user_data.email, user_data.password)
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password"
            )
        
        # Generate JWT access token
        access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
        access_token = create_access_token(
            data={"sub": str(user.id), "email": user.email},
            expires_delta=access_token_expires
        )
        
        # Return token to client
        return {
            "success": True,
            "data": {
                "access_token": access_token,
                "token_type": "bearer"
            }
        }
    except HTTPException:
        # Re-raise HTTP exceptions (like 401) as-is
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error during authentication: {str(e)}"
        )

@router.get("/auth/me")
async def get_user_profile(current_user_id: str = Depends(get_current_user_dependency)):
    """
    Get authenticated user information.
    """
    # For now, just return a success response with user ID
    # In a real implementation, we would fetch user details from the database
    return {
        "success": True,
        "data": {
            "user_id": current_user_id
        }
    }

@router.post("/auth/logout")
async def logout():
    """
    Logout endpoint (stateless JWT - no server-side action needed).
    """
    return {
        "success": True,
        "data": None
    }