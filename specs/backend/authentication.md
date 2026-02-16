# Backend Authentication System Specification

## Overview

This document specifies the authentication system for the Phase II Hackathon Todo Application backend. The system will handle user registration, login, JWT token generation and verification, and secure task management with proper user isolation.

## Architecture

The backend will be built using FastAPI with SQLModel ORM, integrated with Neon Serverless PostgreSQL for data storage. The authentication system will handle user registration and login, generating JWT tokens that are verified for all protected endpoints.

## Components

### Core Components
- **Authentication Service**: Handles user registration, login, and JWT token generation
- **Security Module**: Manages JWT creation and verification using python-jose
- **Password Hashing**: Uses bcrypt for secure password storage
- **Database Layer**: SQLModel models for users and tasks with Neon PostgreSQL

### API Endpoints
- **Auth Endpoints** (`/api/auth`):
  - `POST /signup` - Register new user
  - `POST /login` - Authenticate user and return JWT
  - `GET /me` - Get current user info
  - `POST /logout` - Logout user (optional for stateless JWT)

- **Task Endpoints** (`/api/tasks`, require JWT):
  - `GET /` - Get user's tasks
  - `POST /` - Create new task
  - `PUT /{task_id}` - Update task
  - `PATCH /{task_id}/toggle` - Toggle task completion
  - `DELETE /{task_id}` - Delete task

## Security Measures

- Passwords are hashed using bcrypt before storage
- JWT tokens are signed with a secure secret key
- All protected endpoints validate JWT tokens
- User isolation is enforced by filtering tasks by user ID extracted from JWT
- No user ID is accepted from client requests; always extracted from JWT
- Invalid tokens return HTTP 401 Unauthorized

## Data Models

### User Model
- id: UUID (primary key)
- email: String (unique, indexed)
- hashed_password: String
- created_at: DateTime (auto-generated)

### Task Model
- id: UUID (primary key)
- title: String
- description: String (optional)
- completed: Boolean
- user_id: UUID (foreign key to User.id, indexed)
- created_at: DateTime (auto-generated)
- updated_at: DateTime (auto-generated)

## Response Format

All API responses follow a consistent structure:

Success:
```
{
  "success": true,
  "data": { ... }
}
```

Error:
```
{
  "success": false,
  "error": "error message"
}
```

## Integration Points

The backend will integrate with the existing frontend by providing:
- Authentication endpoints for signup/login
- Secure task management endpoints
- Consistent API response format
- Proper CORS configuration for frontend domain