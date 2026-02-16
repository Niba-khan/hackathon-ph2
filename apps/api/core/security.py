from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from core.config import settings
from datetime import datetime, timedelta
from typing import Optional
import os

# Initialize the security scheme
security = HTTPBearer()

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Create a new access token with the provided data.
    
    Args:
        data: Data to encode in the token (typically user info)
        expires_delta: Optional timedelta for token expiration (defaults to settings value)
        
    Returns:
        str: Encoded JWT token
    """
    to_encode = data.copy()
    
    # Set token expiration
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    
    to_encode.update({"exp": expire})
    
    # Encode the JWT token using the secret key
    encoded_jwt = jwt.encode(to_encode, settings.better_auth_secret, algorithm="HS256")
    return encoded_jwt

def verify_token(token: str):
    """
    Verify the JWT token and return the user ID.
    
    Args:
        token: The JWT token to verify
        
    Returns:
        str: The user ID extracted from the token
        
    Raises:
        HTTPException: If the token is invalid, expired, or missing
    """
    try:
        # Decode the JWT token using the secret key
        payload = jwt.decode(token, settings.better_auth_secret, algorithms=["HS256"])
        
        # Extract the user ID from the token payload
        user_id: str = payload.get("sub")  # Using "sub" as per JWT standard
        
        # Check if token has expired (redundant since jwt.decode handles this, but keeping for clarity)
        exp = payload.get("exp")
        if exp and datetime.fromtimestamp(exp) < datetime.utcnow():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired"
            )
        
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials - no user ID in token"
            )
            
        return user_id
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials - invalid token"
        )

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Get the current user from the JWT token in the Authorization header.
    
    Args:
        credentials: The HTTP authorization credentials from the request header
        
    Returns:
        str: The user ID extracted from the JWT token
        
    Raises:
        HTTPException: If the token is invalid, expired, or missing
    """
    token = credentials.credentials
    
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated - no token provided"
        )
    
    user_id = verify_token(token)
    return user_id