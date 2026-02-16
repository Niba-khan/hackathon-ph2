# Research: Secure Task Management Backend (Updated for Frontend Auth)

**Feature**: Secure Task Management Backend
**Date**: Wednesday, February 11, 2026

## Research Summary

This document consolidates research findings for implementing the updated secure task management backend that acts as a resource server, verifying JWT tokens issued by Better Auth on the frontend. The research addresses all unknowns identified in the technical context and provides the foundation for the implementation plan.

## Decision: JWT Token Verification Implementation (Resource Server Pattern)
**Rationale**: Need to properly decode and verify JWT tokens issued by Better Auth without generating tokens ourselves. The backend should only verify tokens that come from the frontend, following the resource server pattern.

**Implementation Approach**:
- Use the `python-jose` library to decode and verify JWT tokens
- Extract the user_id from the token payload
- Verify the token signature using BETTER_AUTH_SECRET
- Validate token expiration
- Raise HTTP 401 if token is invalid, expired, or missing
- DO NOT implement token generation logic

**Code Pattern**:
```python
from jose import JWTError, jwt
from fastapi import HTTPException, status
from datetime import datetime

SECRET_KEY = os.getenv("BETTER_AUTH_SECRET")
ALGORITHM = "HS256"

def verify_jwt_token(token: str):
    """
    Verify the JWT token issued by Better Auth and return the user ID.
    This function only verifies tokens - it does not generate them.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("userId")  # Adjust based on Better Auth's payload structure
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )
        return user_id
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials"
        )
```

## Decision: Resource Server Architecture
**Rationale**: The backend should follow the resource server pattern, where it only verifies tokens issued by an external authentication provider (Better Auth) rather than handling authentication itself.

**Implementation Approach**:
- Remove all authentication endpoints (signup, signin, logout)
- Remove all password handling logic
- Only verify JWT tokens from the Authorization header
- Extract user identity from verified tokens
- Focus solely on protecting resources (tasks) based on verified identity

## Decision: Better Auth Integration (Verification Only)
**Rationale**: Need to integrate with Better Auth's JWT tokens for verification while ensuring no duplication of authentication logic.

**Implementation Approach**:
- Extract JWT from Authorization header (format: "Bearer <token>")
- Verify token using BETTER_AUTH_SECRET
- Extract user identity from token payload
- Follow Better Auth's JWT structure for user identification
- DO NOT implement any authentication logic that duplicates frontend functionality

**Expected Token Payload Structure** (based on Better Auth documentation):
```json
{
  "userId": "user-id-string",
  "exp": 1234567890,
  "iat": 1234567890
}
```

## Decision: Security Dependencies (Verification Focus)
**Rationale**: Need to implement security dependencies that only verify JWT and extract user identity, without handling authentication flows.

**Implementation Approach**:
- Create a dependency function that verifies JWT and extracts user_id
- Apply this dependency to all protected endpoints
- Use FastAPI's Depends for dependency injection
- Return HTTP 401 for unauthorized requests
- DO NOT implement authentication dependencies

**Code Pattern**:
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer

security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Get the current user from the JWT token in the Authorization header.
    This function only verifies tokens issued by Better Auth.
    """
    token = credentials.credentials
    
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )
    
    user_id = verify_jwt_token(token)
    return user_id
```

## Additional Research Findings

### Resource Server Best Practices
- Keep the backend focused solely on resource protection
- Don't duplicate authentication logic from the frontend
- Validate tokens without storing session state
- Implement proper error responses for invalid tokens

### Security Considerations for Resource Servers
- Never trust user_id from request body or URL parameters
- Always extract user_id from verified JWT token only
- Implement proper input validation for all request parameters
- Use HTTPS in production to protect JWT tokens in transit
- Log authentication failures for security monitoring

### Better Auth Specific Integration
- Better Auth handles user registration, login, and session management
- The backend only needs to verify the JWT tokens provided by Better Auth
- No need to implement user management endpoints in the backend
- Follow Better Auth's documentation for JWT payload structure