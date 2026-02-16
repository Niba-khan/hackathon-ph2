# Tasks: Secure Task Management Backend (Resource Server)

**Feature**: Secure Task Management Backend
**Date**: Wednesday, February 11, 2026

## Implementation Strategy

This document outlines the implementation tasks for the secure task management backend that acts as a resource server. The approach follows an MVP-first methodology with incremental delivery of user stories. Each user story is designed to be independently testable and deliverable.

**MVP Scope**: User Story 1 (Secure Task Management) with JWT token verification and CRUD operations.

## Phase 1: Setup

### Project Initialization
- [X] T001 Create project structure under /apps/api/
- [X] T002 [P] Create requirements.txt with dependencies (FastAPI, SQLModel, python-jose, python-multipart, asyncpg)
- [X] T003 [P] Create .env file template with environment variables
- [X] T004 Create main.py with basic FastAPI app initialization
- [X] T005 [P] Create core/ directory structure
- [X] T006 [P] Create db/ directory structure
- [X] T007 [P] Create api/ directory structure
- [X] T008 [P] Create schemas/ directory structure
- [X] T009 [P] Create services/ directory structure

## Phase 2: Foundational Components

### Configuration and Security Setup
- [X] T010 Implement config.py to manage environment variables
- [X] T011 Implement security.py with JWT verification utilities (verification only, no generation)
- [X] T012 [P] Implement database session management in db/session.py
- [X] T013 Implement CORS middleware in main.py to allow http://localhost:3000

## Phase 3: User Story 1 - Secure Task Management (Priority: P1)

### Story Goal
As an authenticated user, I want to securely create, view, update, and delete my own tasks without accessing others' data, so that I can manage my personal to-do list with confidence that my data is private and secure.

### Independent Test Criteria
Can be fully tested by obtaining a JWT token from the frontend, creating tasks, performing CRUD operations on those tasks, and verifying that the user cannot access other users' tasks.

### Implementation Tasks

#### Data Layer
- [X] T014 [US1] Create Task model in db/models.py with proper fields and constraints
- [X] T015 [US1] Add indexes for user_id and completed fields in Task model

#### Schemas
- [X] T016 [US1] Create TaskCreate schema in schemas/task.py
- [X] T017 [US1] Create TaskUpdate schema in schemas/task.py
- [X] T018 [US1] Create TaskResponse schema in schemas/task.py

#### Service Layer
- [X] T019 [US1] Implement create_task function in services/task_service.py
- [X] T020 [US1] Implement get_user_tasks function in services/task_service.py
- [X] T021 [US1] Implement update_task function in services/task_service.py
- [X] T022 [US1] Implement delete_task function in services/task_service.py

#### API Routes
- [X] T023 [US1] Create dependency injection module in api/deps.py with get_current_user
- [X] T024 [US1] Implement GET /api/tasks endpoint in api/routes/tasks.py
- [X] T025 [US1] Implement POST /api/tasks endpoint in api/routes/tasks.py
- [X] T026 [US1] Implement PUT /api/tasks/{task_id} endpoint in api/routes/tasks.py
- [X] T027 [US1] Implement DELETE /api/tasks/{task_id} endpoint in api/routes/tasks.py

#### Acceptance Scenario Implementation
- [X] T028 [US1] Ensure task creation associates task with authenticated user's ID from JWT
- [X] T029 [US1] Ensure task retrieval filters by authenticated user's ID from JWT
- [X] T030 [US1] Ensure task updates verify ownership via JWT user ID
- [X] T031 [US1] Ensure task deletion verifies ownership via JWT user ID

## Phase 4: User Story 2 - JWT-Based Authentication (Priority: P2)

### Story Goal
As a user, I want to authenticate using JWT tokens issued by Better Auth, so that I can securely access the task management system without repeatedly entering credentials.

### Independent Test Criteria
Can be tested by attempting to access protected endpoints with valid JWT, invalid JWT, expired JWT, and no token, verifying appropriate responses.

### Implementation Tasks

#### Enhanced Security
- [X] T032 [US2] Enhance JWT token verification in core/security.py with expiration validation
- [X] T033 [US2] Implement proper error handling for invalid/expired tokens
- [X] T034 [US2] Ensure all API endpoints require JWT authentication from Better Auth

#### Acceptance Scenario Implementation
- [X] T035 [US2] Verify valid JWT tokens from Better Auth allow access to protected endpoints
- [X] T036 [US2] Verify invalid/expired JWT tokens return HTTP 401
- [X] T037 [US2] Verify missing JWT tokens return HTTP 401

## Phase 5: User Story 3 - Task Filtering and Sorting (Priority: P3)

### Story Goal
As a user with many tasks, I want to filter and sort my tasks by status and other criteria, so that I can efficiently manage my workload.

### Independent Test Criteria
Can be tested by creating multiple tasks with different statuses and properties, then requesting filtered and sorted views.

### Implementation Tasks

#### Enhanced Service Layer
- [X] T038 [US3] Enhance get_user_tasks function with filtering capabilities (status: all/pending/completed)
- [X] T039 [US3] Enhance get_user_tasks function with sorting capabilities (created/title/due_date)

#### Enhanced API Routes
- [X] T040 [US3] Update GET /api/tasks endpoint to support query parameters for filtering and sorting

#### Acceptance Scenario Implementation
- [X] T041 [US3] Verify filtering by status returns only tasks with that status
- [X] T042 [US3] Verify sorting by creation date returns tasks in chronological order

## Phase 6: Toggle Task Endpoint

### Implementation Tasks
- [X] T043 [P] Implement PATCH /api/tasks/{task_id}/toggle endpoint in api/routes/tasks.py
- [X] T044 [P] Implement toggle_task function in services/task_service.py
- [X] T045 [P] Ensure toggle endpoint verifies ownership via JWT user ID before updating

## Phase 7: Error Handling and Edge Cases

### Implementation Tasks
- [X] T046 Implement global exception handler for HTTPException
- [X] T047 Implement global exception handler for ValidationError
- [X] T048 Implement global exception handler for JWT errors
- [X] T049 Implement global exception handler for Database errors
- [X] T050 Ensure consistent JSON error response format
- [X] T051 Handle malformed JWT tokens appropriately
- [X] T052 Handle database connection failures gracefully
- [X] T053 Ensure 404 responses when accessing another user's resources
- [X] T054 Ensure no authentication endpoints (signup, signin, logout) are created

## Phase 8: Polish & Cross-Cutting Concerns

### Implementation Tasks
- [X] T055 Add automatic created_at and updated_at timestamp management
- [X] T056 Validate task title length (1-200 characters) in schemas
- [X] T057 Ensure all responses follow the success/error structure format
- [X] T058 Add proper logging for debugging and monitoring
- [X] T059 Update main.py with proper middleware and startup/shutdown events
- [X] T060 Write comprehensive README with setup instructions
- [X] T061 Perform security review to ensure no user can access another's data
- [X] T062 Confirm no password handling or JWT generation logic exists in backend

## Dependencies

### User Story Completion Order
1. User Story 2 (JWT Authentication) must be partially complete before User Story 1 (Secure Task Management) can begin
2. User Story 1 (Secure Task Management) must be complete before User Story 3 (Filtering and Sorting) can begin

### Blocking Dependencies
- T010-T013 must complete before any user story implementation begins
- T014-T018 must complete before API routes can be implemented
- T019-T022 must complete before API routes can be fully functional

## Parallel Execution Examples Per Story

### User Story 1 Parallel Tasks
- T014 (Task model) and T016-T018 (schemas) can run in parallel
- T019-T022 (service functions) can run in parallel after schemas are complete
- T024-T027 (API routes) can run in parallel after services are complete

### User Story 2 Parallel Tasks
- T032 (enhanced JWT verification) and T033 (error handling) can run in parallel
- T035-T037 (acceptance scenarios) can run in parallel after implementation

### User Story 3 Parallel Tasks
- T038 (filtering) and T039 (sorting) can run in parallel
- T040 (endpoint update) can run after T038-T039
- T041-T042 (acceptance scenarios) can run after implementation