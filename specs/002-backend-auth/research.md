# Research: Backend Authentication Implementation

**Feature**: Backend Authentication System
**Date**: Wednesday, February 11, 2026

## Research Summary

This document consolidates research findings for implementing the backend authentication system for the Phase II Hackathon Todo Application. The research addresses all unknowns identified in the technical context and provides the foundation for the implementation plan.

## Decision: JWT Token Generation and Verification Implementation
**Rationale**: Need to properly generate and verify JWT tokens with expiration and user information for secure authentication.

**Implementation Approach**:
- Use the `python-jose` library with `cryptography` extra for JWT operations
- Generate tokens with HS256 algorithm using a secure secret key
- Include claims: `sub` (user_id), `email`, `exp` (expiration), `iat` (issued at)
- Set token expiration to 60 minutes (configurable)
- Verify tokens by decoding with the same secret key and checking expiration

**Code Pattern**:
```python
from datetime import datetime, timedelta
from jose import jwt
from core.config import settings

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)  # Default 60 minutes
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
```

## Decision: Password Hashing with bcrypt
**Rationale**: Need to securely hash passwords before storing in the database to protect user credentials.

**Implementation Approach**:
- Use the `passlib` library with `bcrypt` scheme for password hashing
- Implement hash_password() and verify_password() functions
- Use automatic salt generation (built into bcrypt)
- Store only the hashed password in the database, never plain text

**Code Pattern**:
```python
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)
```

## Decision: SQLModel Async Setup
**Rationale**: Need to implement async database operations using SQLModel for optimal performance in a web application.

**Implementation Approach**:
- Use SQLModel with async SQLAlchemy engine
- Implement async_sessionmaker for database sessions
- Create a dependency to provide database sessions to endpoints
- Ensure proper connection pooling for Neon Serverless PostgreSQL

**Code Pattern**:
```python
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.pool import QueuePool
from core.config import settings

DATABASE_URL = settings.database_url
engine = create_async_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=5,
    max_overflow=10,
    pool_pre_ping=True,
    pool_recycle=300,
)

async_session = async_sessionmaker(engine, class_=AsyncSession)

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
```

## Decision: FastAPI Security Dependencies
**Rationale**: Need to implement security dependencies to protect all endpoints and ensure proper authentication flow.

**Implementation Approach**:
- Create a dependency function that verifies JWT and extracts user_id
- Apply this dependency to all protected endpoints
- Use FastAPI's Depends for dependency injection
- Return HTTP 401 for unauthorized requests
- Never trust user_id from request body, always extract from JWT

**Code Pattern**:
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from core.security import verify_token

security = HTTPBearer()

async def get_current_user(token: str = Depends(security)):
    user_id = verify_token(token.credentials)
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user_id
```

## Additional Research Findings

### Neon Serverless PostgreSQL Best Practices
- Use connection pooling to optimize for serverless environments
- Handle connection timeouts gracefully
- Implement retry logic for transient connection failures
- Monitor connection limits and optimize accordingly

### FastAPI Error Handling
- Use FastAPI's exception handlers for consistent error responses
- Implement custom exception handlers for specific error types
- Return consistent JSON error format as specified in the feature requirements
- Never expose internal stack traces to clients

### Security Considerations
- Never trust user_id from request body or URL parameters
- Always extract user_id from verified JWT token only
- Implement proper input validation for all request parameters
- Use HTTPS in production to protect JWT tokens in transit
- Log authentication failures for security monitoring

### Better Auth Integration
- Better Auth handles user registration, login, and session management
- The backend only needs to verify the JWT tokens provided by Better Auth
- No need to implement user management endpoints in the backend
- Follow Better Auth's documentation for JWT payload structure