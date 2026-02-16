# Feature Specification: Secure Task Management Backend

**Feature Branch**: `001-backend-jwt-tasks`
**Created**: Wednesday, February 11, 2026
**Status**: Draft
**Input**: User description: "Create a complete backend specification for Phase II of the Hackathon Todo Application. Reference: - Follow constitution.md strictly. - Ensure full integration with existing frontend. - Follow monorepo structure. - Use /specs/backend and /specs/features conventions. Objective: Design a secure, production-ready backend with database integration that supports: - Token-based authentication - Multi-user task isolation - CRUD operations for tasks - Full compatibility with the frontend API client Environment Variables: - DATABASE_URL - BETTER_AUTH_SECRET - BETTER_AUTH_URL ------------------------------------------------------- SECTION 1: BACKEND GOALS ------------------------------------------------------- The backend must: - Verify authentication tokens - Extract user identity from tokens only - Reject invalid, expired, or missing tokens with HTTP 401 - Enforce per-user task isolation - Return proper HTTP status codes - Use JSON responses with success/error structure - Be fully compatible with frontend API client ------------------------------------------------------- SECTION 2: PROJECT STRUCTURE ------------------------------------------------------- Define folder structure: /apps/api/ ├── main.py ├── core/ │ ├── config.py # Environment variables and settings │ └── security.py # Token verification and authentication integration ├── db/ │ ├── session.py # Database session management │ └── models.py # Data models (User, Task) ├── api/ │ ├── deps.py # Dependencies (get_current_user) │ └── routes/ │ └── tasks.py # CRUD endpoints ├── schemas/ │ └── task.py # Request/response schemas (TaskCreate, TaskUpdate, TaskResponse) └── services/ └── task_service.py # Business logic for tasks Responsibilities: - main.py → App initialization, CORS, middleware - config.py → Read .env - security.py → Token validation - session.py → Database session - models.py → Database tables - deps.py → Dependency injection - routes/tasks.py → API endpoints - task_service.py → CRUD logic - schemas/task.py → Request/response validation ------------------------------------------------------- SECTION 3: DATABASE SPECIFICATION ------------------------------------------------------- Database: Serverless PostgreSQL Tasks table: - id: UUID, primary key - title: string, required - description: string, optional - completed: boolean, default false - user_id: string, indexed, foreign key to users - created_at: timestamp - updated_at: timestamp Indexes: - tasks.user_id - tasks.completed Requirements: - All queries filter by authenticated user_id - Automatic created_at and updated_at - Multi-user isolation enforced at query level ------------------------------------------------------- SECTION 4: AUTHENTICATION SPECIFICATION ------------------------------------------------------- - Extract Authorization: Bearer <token> - Verify token signature - Validate token expiration - Extract user_id - Reject invalid/missing tokens with HTTP 401 Dependency: get_current_user() - Decode token - Return user_id - Raise HTTPException 401 if invalid Rules: - Never trust user_id from request body - Always extract user_id from token - Never expose another user's data ------------------------------------------------------- SECTION 5: API ENDPOINTS SPECIFICATION ------------------------------------------------------- Base path: /api/tasks Endpoints: 1. GET /api/tasks - Return all tasks for authenticated user - Support query params: status (all/pending/completed), sort (created/title/due_date) 2. POST /api/tasks - Create a task for authenticated user - Validate title length (1–200), optional description 3. PUT /api/tasks/{task_id} - Update task title/description - Verify ownership 4. PATCH /api/tasks/{task_id}/toggle - Toggle task completion - Verify ownership 5. DELETE /api/tasks/{task_id} - Delete task - Verify ownership All endpoints: - Require authentication token - Return 404 if task not owned by user - Return 401 if unauthorized ------------------------------------------------------- SECTION 6: SCHEMA SPECIFICATION ------------------------------------------------------- Request/response schemas: - TaskCreate - TaskUpdate - TaskResponse Requirements: - Hide internal fields if necessary - Serialize UUID properly - Include created_at and updated_at ------------------------------------------------------- SECTION 7: SERVICE LAYER SPECIFICATION ------------------------------------------------------- task_service.py: - create_task(user_id, data) - get_user_tasks(user_id) - update_task(user_id, task_id, data) - toggle_task(user_id, task_id) - delete_task(user_id, task_id) Requirements: - All functions accept user_id - Filter by user_id - Raise exception if task not found ------------------------------------------------------- SECTION 8: DATABASE SESSION MANAGEMENT ------------------------------------------------------- - Database engine with connection pooling - Session management - Dependency get_session() - Proper cleanup after request ------------------------------------------------------- SECTION 9: FRONTEND INTEGRATION REQUIREMENTS ------------------------------------------------------- - CORS allowed for http://localhost:3000 - JSON responses only - Proper status codes - Consistent response format Success: { \"success\": true, \"data\": ... } Error: { \"success\": false, \"error\": \"message\" } ------------------------------------------------------- SECTION 10: ERROR HANDLING STRATEGY ------------------------------------------------------- Global exception handlers for: - HTTPException - Validation errors - Authentication errors - Database errors No internal stack traces exposed to frontend. ------------------------------------------------------- SECTION 11: TESTING REQUIREMENTS ------------------------------------------------------- Integration tests must verify: - No token → 401 - Invalid token → 401 - Expired token → 401 - User A cannot access User B tasks - CRUD operations work correctly - Task persists in database ------------------------------------------------------- SECTION 12: OUTPUT FILES ------------------------------------------------------- Generate specification files under: /specs/backend/architecture.md /specs/backend/database.md /specs/backend/authentication.md /specs/backend/api.md /specs/features/backend-tasks.md The backend must be secure, production-ready, and fully integrated with the frontend."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Secure Task Management (Priority: P1)

As an authenticated user, I want to securely create, view, update, and delete my own tasks without accessing others' data, so that I can manage my personal to-do list with confidence that my data is private and secure.

**Why this priority**: This is the core functionality of the application - users need to be able to manage their tasks securely with proper isolation from other users.

**Independent Test**: Can be fully tested by registering a user, creating tasks, performing CRUD operations on those tasks, and verifying that the user cannot access other users' tasks.

**Acceptance Scenarios**:

1. **Given** a registered user with valid JWT token, **When** the user creates a new task, **Then** the task is saved to the database with the user's ID and is accessible only to that user
2. **Given** a user with multiple tasks, **When** the user requests their tasks, **Then** only tasks belonging to that user are returned
3. **Given** a user with a task, **When** the user updates the task, **Then** only that user's task is modified
4. **Given** a user with a task, **When** the user deletes the task, **Then** only that user's task is removed from the database

---

### User Story 2 - JWT-Based Authentication (Priority: P2)

As a user, I want to authenticate using JWT tokens issued by Better Auth, so that I can securely access the task management system without repeatedly entering credentials.

**Why this priority**: Authentication is foundational to the security of the entire system - without proper authentication, task isolation cannot be guaranteed.

**Independent Test**: Can be tested by attempting to access protected endpoints with valid JWT, invalid JWT, expired JWT, and no token, verifying appropriate responses.

**Acceptance Scenarios**:

1. **Given** a valid JWT token from Better Auth, **When** the user accesses protected endpoints, **Then** the request is processed successfully
2. **Given** an invalid or expired JWT token, **When** the user accesses protected endpoints, **Then** an HTTP 401 Unauthorized response is returned
3. **Given** no JWT token, **When** the user accesses protected endpoints, **Then** an HTTP 401 Unauthorized response is returned

---

### User Story 3 - Task Filtering and Sorting (Priority: P3)

As a user with many tasks, I want to filter and sort my tasks by status and other criteria, so that I can efficiently manage my workload.

**Why this priority**: This enhances usability for users with many tasks, making the application more practical for daily use.

**Independent Test**: Can be tested by creating multiple tasks with different statuses and properties, then requesting filtered and sorted views.

**Acceptance Scenarios**:

1. **Given** a user with mixed completed and pending tasks, **When** the user requests tasks with status=pending, **Then** only pending tasks are returned
2. **Given** a user with multiple tasks, **When** the user requests tasks sorted by creation date, **Then** tasks are returned in chronological order

---

### Edge Cases

- What happens when a user tries to access a task that doesn't exist?
- How does the system handle malformed JWT tokens?
- What occurs when the database connection fails during a request?
- How does the system behave when a user tries to access another user's task ID?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST support multiple authenticated users with strict task isolation
- **FR-002**: System MUST implement JWT-based authentication with proper token verification using BETTER_AUTH_SECRET
- **FR-003**: Users MUST be able to securely create, read, update, and delete their own tasks
- **FR-004**: System MUST persist data in Neon Serverless PostgreSQL with proper indexing
- **FR-005**: System MUST validate JWT signatures independently on all protected endpoints
- **FR-006**: System MUST filter all task operations by authenticated user ID extracted from JWT
- **FR-007**: System MUST return HTTP 401 for unauthorized access attempts
- **FR-008**: System MUST return HTTP 404 when attempting to access another user's resources
- **FR-009**: System MUST support filtering and sorting of tasks by status and other criteria
- **FR-010**: System MUST validate task titles to be between 1 and 200 characters
- **FR-011**: System MUST automatically set created_at and updated_at timestamps for tasks
- **FR-012**: System MUST return consistent JSON responses with success/error structure
- **FR-013**: System MUST allow toggling of task completion status via dedicated endpoint
- **FR-014**: System MUST implement proper CORS policy allowing http://localhost:3000

### Key Entities *(include if feature involves data)*

- **User**: Represents an authenticated user with unique identifier from JWT token
- **Task**: Represents a todo item associated with a specific user, with title, description, completion status, and timestamps

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can authenticate using JWT tokens and access the system securely
- **SC-002**: Users can perform CRUD operations on their own tasks without accessing others' data
- **SC-003**: System properly validates JWT tokens and enforces user isolation with 99.9% accuracy
- **SC-004**: All API endpoints require proper authentication and return appropriate error codes (401, 404)
- **SC-005**: Task creation, retrieval, update, and deletion operations complete within 1 second 95% of the time
- **SC-006**: System handles at least 100 concurrent users without performance degradation
- **SC-007**: Frontend application can successfully integrate with all backend API endpoints
- **SC-008**: All data persists correctly in Neon PostgreSQL database with proper indexing