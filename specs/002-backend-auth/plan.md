# Implementation Plan: Backend Authentication System

**Branch**: `002-backend-auth` | **Date**: Wednesday, February 11, 2026 | **Spec**: [../specs/features/backend-auth.md](../specs/features/backend-auth.md)
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a complete backend authentication system for the Phase II Hackathon Todo Application. The system will handle user registration, login, JWT token generation and verification, and secure task management with strict user isolation. The backend uses FastAPI with SQLModel ORM to provide a complete authentication and task management solution with Neon Serverless PostgreSQL for data persistence. The system is fully compatible with the existing frontend and follows all security requirements from the constitution.

## Technical Context

**Language/Version**: Python 3.11+, TypeScript 5.3+
**Primary Dependencies**: FastAPI, SQLModel, PyJWT, python-jose, bcrypt, passlib, python-multipart, uvicorn, httpx, python-dotenv, alembic
**Storage**: Neon Serverless PostgreSQL
**Testing**: pytest, integration tests
**Target Platform**: Web application (backend API)
**Project Type**: Monorepo with clear separation of frontend, backend, and database layers
**Performance Goals**: Multi-user support with secure authentication and authorization
**Constraints**: JWT-based authentication, user task isolation, secure API endpoints
**Scale/Scope**: Multi-user todo application with secure data isolation

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- Multi-User Security: All endpoints must validate JWT signatures and enforce user isolation ✓
- Full-Stack Architecture: Clear separation of frontend (Next.js), backend (FastAPI), and database (Neon PostgreSQL) ✓
- Database Integrity: Proper indexing and foreign key relationships in PostgreSQL ✓
- Spec-Driven Development: All implementation follows specifications in /specs directory ✓
- Agent Governance: Specialized agents with defined responsibilities ✓
- API Security Compliance: All endpoints under /api/ require Authorization header with JWT ✓

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
# Monorepo structure for full-stack web application
apps/
└── api/                 # FastAPI application
    ├── main.py          # Application entry point
    ├── core/            # Configuration and security
    │   ├── config.py    # Environment variables and settings
    │   ├── security.py  # JWT creation & verification
    │   └── hashing.py   # bcrypt password hashing
    ├── db/              # Database models and session management
    │   ├── session.py   # Database session management
    │   └── models.py    # SQLModel database models (User, Task)
    ├── api/             # API route handlers and dependencies
    │   ├── deps.py      # Dependency injection (get_current_user)
    │   └── routes/      # API route definitions
    │       ├── auth.py  # Authentication endpoints (signup/login/logout)
    │       └── tasks.py # Task endpoints (CRUD operations)
    ├── schemas/         # Pydantic schemas for request/response validation
    │   ├── user.py      # User-related schemas (UserCreate, UserLogin, UserResponse)
    │   └── task.py      # Task-related schemas (TaskCreate, TaskUpdate, TaskResponse)
    └── services/        # Business logic layer
        ├── auth_service.py  # Authentication business logic
        └── task_service.py  # Task business logic
```

**Structure Decision**: Following the constitution's requirement for monorepo structure with clear separation of frontend, backend, and database layers. The backend uses FastAPI with SQLModel ORM, and Neon Serverless PostgreSQL serves as the database. The backend handles both authentication (signup, login, JWT generation) and task management with proper user isolation.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |

## Phase 0: Research & Unknown Resolution

### Research Tasks Identified:
1. **JWT Token Generation**: Research how to properly generate JWT tokens with expiration and user information
2. **Password Hashing Best Practices**: Research bcrypt implementation with proper salt generation
3. **SQLModel Async Setup**: Research best practices for async SQLModel engine and session management
4. **FastAPI Security Dependencies**: Research best practices for implementing security dependencies with JWT

### Expected Outcomes:
- JWT generation and verification implementation details
- Password hashing with bcrypt implementation
- Async database session management approach
- Security dependency injection patterns

## Phase 1: Design & Contracts

### Data Model (data-model.md)
- User entity with fields: id (UUID), email (unique, indexed), hashed_password, created_at
- Task entity with fields: id (UUID), title (string, 1-200 chars), description (optional), completed (boolean), user_id (foreign key, indexed), created_at, updated_at
- Indexes on email (users), user_id and completed (tasks)
- Validation rules for title length (1-200 chars) and email format

### API Contracts (contracts/)
- OpenAPI specification for auth endpoints:
  - POST /api/auth/signup (with email/password validation)
  - POST /api/auth/login (with credential validation)
  - GET /api/auth/me (with JWT verification)
  - POST /api/auth/logout (optional stateless endpoint)
- OpenAPI specification for task endpoints:
  - GET /api/tasks (with query params for status and sort)
  - POST /api/tasks (with validation for title length)
  - PUT /api/tasks/{task_id} (with ownership verification)
  - PATCH /api/tasks/{task_id}/toggle (with ownership verification)
  - DELETE /api/tasks/{task_id} (with ownership verification)
- Request/response schemas for all endpoints
- Error response formats

### Quickstart Guide (quickstart.md)
- Setup instructions for environment variables
- Database migration steps
- Running the backend service
- Testing the authentication and task endpoints

## Phase 2: Implementation Plan

### Phase 1 – Project Initialization
- **Goal**: Set up the project structure and dependencies
- **Files to create/update**: requirements.txt, .env, main.py, directory structure
- **Dependencies**: None
- **Completion criteria**: Project structure in place with dependencies installed

### Phase 2 – Database & Models Setup
- **Goal**: Implement database models and session management
- **Files to create/update**: db/models.py, db/session.py
- **Dependencies**: Project initialization complete
- **Completion criteria**: User and Task models defined with proper relationships and indexes

### Phase 3 – Password Hashing & Security Core
- **Goal**: Implement secure password hashing and JWT infrastructure
- **Files to create/update**: core/hashing.py, core/security.py
- **Dependencies**: Project initialization complete
- **Completion criteria**: Password hashing functions and JWT creation/verification available

### Phase 4 – JWT Token Infrastructure
- **Goal**: Complete JWT token generation and verification system
- **Files to create/update**: core/security.py, core/config.py
- **Dependencies**: Password hashing implemented
- **Completion criteria**: JWT tokens can be generated with proper claims and verified with expiration check

### Phase 5 – Authentication Services
- **Goal**: Implement authentication business logic
- **Files to create/update**: services/auth_service.py
- **Dependencies**: Database models and security core complete
- **Completion criteria**: User registration, login, and authentication functions working

### Phase 6 – Authentication Routes
- **Goal**: Implement authentication API endpoints
- **Files to create/update**: api/routes/auth.py
- **Dependencies**: Authentication services complete
- **Completion criteria**: All auth endpoints (signup, login, me, logout) working with proper validation

### Phase 7 – Task Service Layer
- **Goal**: Implement task business logic with user isolation
- **Files to create/update**: services/task_service.py
- **Dependencies**: Database models and security core complete
- **Completion criteria**: All task CRUD operations with proper user filtering

### Phase 8 – Protected Task Routes
- **Goal**: Implement task API endpoints with authentication
- **Files to create/update**: api/routes/tasks.py, api/deps.py
- **Dependencies**: Task services and authentication routes complete
- **Completion criteria**: All task endpoints protected with JWT authentication and user isolation

### Phase 9 – Frontend Integration
- **Goal**: Ensure compatibility with frontend and complete integration
- **Files to create/update**: main.py (CORS), schemas/user.py, schemas/task.py
- **Dependencies**: All endpoints implemented
- **Completion criteria**: Frontend can successfully register, login, and perform task operations

### Phase 10 – Error Handling & Security Hardening
- **Goal**: Implement comprehensive error handling and security measures
- **Files to create/update**: main.py (exception handlers), core/security.py (validation), services/*.py (validation)
- **Dependencies**: All endpoints implemented
- **Completion criteria**: Proper error responses, no sensitive data exposure, security validation in place

### Phase 11 – Testing & Final Validation
- **Goal**: Validate complete functionality and security
- **Files to create/update**: README.md, test files if needed
- **Dependencies**: All previous phases complete
- **Completion criteria**: All functionality working as specified, security measures validated, documentation complete