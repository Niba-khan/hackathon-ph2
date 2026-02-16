# Implementation Plan: Secure Task Management Backend (Updated for Frontend Auth)

**Branch**: `001-backend-jwt-tasks` | **Date**: Wednesday, February 11, 2026 | **Spec**: [/specs/features/backend-tasks.md](../specs/features/backend-tasks.md)
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Updated implementation plan for the secure, production-ready backend for the Phase II Hackathon Todo Application. The system now acts solely as a resource server that verifies JWT tokens issued by Better Auth on the frontend, rather than handling authentication itself. The backend uses FastAPI with SQLModel ORM to provide JWT-verified CRUD operations for tasks with strict user isolation. The backend integrates with Neon Serverless PostgreSQL for data persistence and is fully compatible with the existing Next.js frontend using Better Auth for JWT token issuance.

## Technical Context

**Language/Version**: Python 3.11+, TypeScript 5.3+
**Primary Dependencies**: FastAPI, SQLModel, PyJWT, python-jose, Neon PostgreSQL driver
**Storage**: Neon Serverless PostgreSQL
**Testing**: pytest, integration tests
**Target Platform**: Web application (backend API)
**Project Type**: Monorepo with clear separation of frontend, backend, and database layers
**Performance Goals**: Multi-user support with secure authentication and authorization
**Constraints**: JWT-based authentication (verification only, not generation), user task isolation, secure API endpoints
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
    │   └── security.py  # JWT verification and authentication (verification only)
    ├── db/              # Database models and session management
    │   ├── session.py   # Database session management
    │   └── models.py    # SQLModel database models
    ├── api/             # API route handlers and dependencies
    │   ├── deps.py      # Dependency injection (get_current_user)
    │   └── routes/      # API route definitions
    │       └── tasks.py # Task CRUD endpoints (NO auth endpoints)
    ├── schemas/         # Pydantic schemas for request/response validation
    │   └── task.py      # TaskCreate, TaskUpdate, TaskResponse schemas
    └── services/        # Business logic layer
        └── task_service.py # Task CRUD operations
```

**Structure Decision**: Following the constitution's requirement for monorepo structure with clear separation of frontend, backend, and database layers. The backend uses FastAPI with SQLModel ORM, and Neon Serverless PostgreSQL serves as the database. The backend acts as a resource server that only verifies JWT tokens issued by the frontend.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |

## Phase 0: Research & Unknown Resolution

### Research Tasks Identified:
1. **JWT Token Verification**: Research how to properly decode and verify JWT tokens issued by Better Auth (verification only, no generation)
2. **Resource Server Architecture**: Research best practices for implementing a backend that only verifies tokens issued by frontend
3. **Better Auth Integration**: Research how to integrate with Better Auth's JWT tokens without duplicating auth logic
4. **Security Dependencies**: Research best practices for implementing security dependencies that only verify tokens

### Expected Outcomes:
- JWT verification implementation details (no generation)
- Resource server architecture approach
- Security best practices for token verification only
- Dependency injection patterns for authentication

## Phase 1: Design & Contracts

### Data Model (data-model.md)
- Task entity with fields: id (UUID), title (string, 1-200 chars), description (optional string), completed (boolean), user_id (string), created_at (timestamp), updated_at (timestamp)
- Indexes on user_id and completed fields
- Validation rules for title length (1-200 chars)
- Automatic timestamp management
- NO user password storage (frontend handles auth)

### API Contracts (contracts/)
- OpenAPI specification for all task endpoints:
  - GET /api/tasks (with query params for status and sort)
  - POST /api/tasks (with validation for title length)
  - PUT /api/tasks/{task_id} (with ownership verification)
  - PATCH /api/tasks/{task_id}/toggle (with ownership verification)
  - DELETE /api/tasks/{task_id} (with ownership verification)
- NO authentication endpoints (signup, signin, logout)
- Request/response schemas for all endpoints
- Error response formats

### Quickstart Guide (quickstart.md)
- Setup instructions for environment variables
- Database migration steps
- Running the backend service
- Testing the endpoints with JWT tokens from frontend

## Phase 2: Implementation Plan

### Phase A – Project Setup
- Create the project structure under /apps/api/
- Set up requirements.txt with necessary dependencies
- Configure environment variables (DATABASE_URL, BETTER_AUTH_SECRET, BETTER_AUTH_URL)
- NO authentication endpoint setup

### Phase B – Database & ORM Setup
- Implement async SQLModel engine using DATABASE_URL
- Create async_sessionmaker
- Define Task model with proper fields and constraints
- Add indexes for user_id and completed fields
- Create get_session() dependency
- NO User model with password storage

### Phase C – JWT Verification & Security (Resource Server)
- Implement get_current_user() dependency
- Create JWT verification utility functions (verification only, no generation)
- Validate JWT signature using BETTER_AUTH_SECRET
- Extract user_id from JWT payload
- Raise HTTP 401 on invalid/missing token
- NO signup/login/logout endpoints

### Phase D – Task CRUD Implementation
- Create Pydantic schemas (TaskCreate, TaskUpdate, TaskResponse)
- Implement task_service.py with all required functions
- Create API routes for all task operations (NO auth routes)
- Connect routes with authentication dependencies

### Phase E – Service Layer Development
- Implement all service functions with proper error handling
- Ensure all operations filter by user_id
- Add proper exception handling for not-found cases
- Connect service layer with database models

### Phase F – API Routes & Dependency Injection
- Implement all task endpoints with proper authentication
- Add query parameter support for filtering and sorting
- Ensure proper response formatting
- Add request validation using Pydantic schemas
- NO authentication endpoints

### Phase G – Frontend Integration & Testing
- Test all endpoints with valid JWT tokens from Better Auth
- Verify multi-user isolation
- Ensure response format matches frontend expectations
- Test CORS configuration

### Phase H – Error Handling & Edge Cases
- Implement global exception handlers
- Ensure proper HTTP status codes
- Hide internal stack traces
- Handle database connection errors gracefully

### Phase I – Final Review & Optimization
- Performance testing
- Security review
- Code optimization
- Documentation completion

## Section 1: Authentication Architecture Decision

### Final Architecture:

#### Frontend:
- Handles signup/login/logout via Better Auth
- Receives JWT from Better Auth
- Sends Authorization: Bearer <token> to backend

#### Backend (Resource Server):
- Does NOT generate JWT tokens
- Does NOT store passwords
- Does NOT implement signup/signin/logout endpoints
- Only verifies JWT signature using BETTER_AUTH_SECRET
- Extracts user_id from token payload
- Protects task endpoints based on verified user_id

## Section 2: Remove Auth Endpoints Plan

### Implementation Steps:
1. **Remove Authentication Routes**:
   - Remove /signup endpoint
   - Remove /signin endpoint
   - Remove /logout endpoint
   - Remove any user registration/login logic

2. **Remove Password Handling Logic**:
   - Remove password hashing utilities
   - Remove password validation logic
   - Remove any password-related dependencies

3. **Update User Model (if exists)**:
   - Remove password field from User model
   - Keep only user metadata if required for relations
   - Ensure no password storage occurs

4. **Keep User Identification**:
   - Keep user_id extraction from JWT token
   - Maintain user isolation based on JWT user_id

## Section 3: JWT Verification Plan

### Implementation:
- Implement get_current_user() dependency that verifies JWT
- Decode JWT using BETTER_AUTH_SECRET for verification only
- Validate token expiration
- Extract user_id from token payload
- Raise HTTP 401 if token is invalid

### Security Measures:
- No endpoint accepts user_id from request body
- All queries filter by JWT user_id only
- No token generation logic in backend
- Strict verification of externally issued tokens

## Section 4: Database Adjustment Plan

### Tasks Table Contains:
- user_id (string, indexed) - extracted from JWT, not from request

### User Table (Optional):
- If used, contains only user metadata
- NO password storage
- Only for relational purposes if needed

## Section 5: API Route Structure

### Final Backend Routes:

/api/tasks
- GET (protected)
- POST (protected)
- PUT (protected)
- PATCH /toggle (protected)
- DELETE (protected)

### All Routes:
- Require get_current_user dependency for JWT verification
- Enforce ownership filtering by JWT user_id
- NO authentication routes

## Section 6: Frontend Integration Confirmation

### Verification:
- Backend accepts JWT from Better Auth frontend
- CORS allows http://localhost:3000
- Response format matches frontend API client expectations
- 401 returned for missing/invalid tokens

## Section 7: Security Hardening

### Ensured:
- No password handling logic exists in backend
- No JWT generation logic exists in backend
- Only signature verification from external issuer
- No sensitive error information leaked
- Proper exception handling for all scenarios

## Section 8: Final Clean Architecture Summary

### Architecture Description:
- **Frontend as Authentication Provider**: Handles all user authentication via Better Auth
- **Backend as Resource Server**: Only verifies externally issued JWT tokens
- **JWT as Identity Bridge**: Token issued by frontend auth system, verified by backend
- **Strict User Isolation Enforcement**: All data access filtered by verified user_id from JWT