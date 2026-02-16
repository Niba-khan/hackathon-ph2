# Backend Architecture Specification: Secure Task Management with JWT Authentication

## Overview

This document specifies the architecture for a secure, production-ready backend for the Phase II Hackathon Todo Application. The system implements JWT-based authentication with the backend acting as the Authentication Authority, removing dependency on external authentication services. The backend uses FastAPI with SQLModel ORM to provide JWT-verified CRUD operations for tasks with strict user isolation. The backend integrates with Neon Serverless PostgreSQL for data persistence and is fully compatible with the existing Next.js frontend.

## Architecture Components

### 1. Application Layer
- **Framework**: FastAPI for high-performance async API development
- **Main Entry Point**: `/apps/api/main.py` handles app initialization, CORS configuration, and middleware setup
- **Configuration**: `/apps/api/core/config.py` manages environment variables and application settings

### 2. Security Layer
- **Authentication**: JWT token generation and verification using HS256 algorithm
- **Password Hashing**: bcrypt for secure password storage
- **Token Handling**: Generate tokens on signup/login, verify on protected routes
- **Location**: `/apps/api/core/security.py` contains JWT creation and verification logic

### 3. Database Layer
- **ORM**: SQLModel for async database operations
- **Connection**: Neon Serverless PostgreSQL with connection pooling
- **Management**: `/apps/api/db/session.py` handles async engine and session management
- **Models**: `/apps/api/db/models.py` defines SQLModel classes (User, Task)

### 4. API Layer
- **Dependencies**: `/apps/api/api/deps.py` implements dependency injection (get_current_user)
- **Routes**: `/apps/api/api/routes/` contains API route definitions
  - `/apps/api/api/routes/auth.py` for authentication endpoints
  - `/apps/api/api/routes/tasks.py` for task endpoints
- **Validation**: All endpoints require JWT authentication and enforce user isolation

### 5. Service Layer
- **Business Logic**: `/apps/api/services/` implements core functionality
  - `/apps/api/services/auth_service.py` for authentication operations
  - `/apps/api/services/task_service.py` for task operations
- **User Isolation**: All functions accept user_id and filter by user_id

### 6. Schema Layer
- **Validation**: `/apps/api/schemas/` defines Pydantic schemas
  - `/apps/api/schemas/user.py` for user-related schemas
  - `/apps/api/schemas/task.py` for task-related schemas
- **Serialization**: Proper data validation and serialization

## Technology Stack

- **Backend Framework**: FastAPI
- **Database**: Neon Serverless PostgreSQL
- **ORM**: SQLModel (async)
- **Authentication**: JWT with HS256 algorithm
- **Password Hashing**: bcrypt
- **Environment Management**: python-dotenv

## Security Considerations

- JWT tokens are generated and verified using JWT_SECRET_KEY
- All queries filter by authenticated user_id extracted from JWT
- Passwords are hashed using bcrypt before storage
- Multi-user isolation enforced at query level
- Automatic created_at and updated_at timestamps
- Proper error responses without exposing internal details

## Integration Points

- Compatible with Next.js frontend API client
- CORS configured for http://localhost:3000
- Consistent JSON response format with success/error structure
- JWT tokens issued by backend, consumed by frontend