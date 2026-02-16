---
id: 001
title: "Backend JWT Authentication and Task Management Spec"
stage: spec
date_iso: "2026-02-11"
surface: "agent"
model: "OpenAI GPT-4"
feature: "backend-jwt-tasks"
branch: "001-backend-jwt-tasks"
user: "user"
command: "/sp.specify"
labels: ["specification", "backend", "authentication", "task-management"]
links:
  spec: "/specs/features/backend-tasks.md"
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - /specs/features/backend-tasks.md
  - /specs/backend/architecture.md
  - /specs/backend/database.md
  - /specs/backend/authentication.md
  - /specs/backend/api.md
  - /specs/features/checklists/requirements.md
tests_yaml: []
outcome: "Successfully created comprehensive backend specification for JWT authentication and task management with all required components"
evaluation: "All specification documents completed and validated with technology-agnostic approach"
---

# Prompt History Record: Backend JWT Authentication and Task Management Spec

## Original User Prompt

Create a complete backend specification for Phase II of the Hackathon Todo Application. Reference: - Follow constitution.md strictly. - Ensure full integration with existing frontend. - Follow monorepo structure. - Use /specs/backend and /specs/features conventions. Objective: Design a secure, production-ready FastAPI backend with Neon PostgreSQL integration that supports: - JWT authentication via Better Auth - Multi-user task isolation - CRUD operations for tasks - Full compatibility with the Next.js frontend API client Environment Variables: - DATABASE_URL = 'postgresql://neondb_owner:npg_ALn8w2VXuimk@ep-bold-thunder-ais27zzv-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require' - BETTER_AUTH_SECRET = 'lT0xTkTtucbCzseAXORUchH333AsAHrM' - BETTER_AUTH_URL = 'http://localhost:3000' ------------------------------------------------------- SECTION 1: BACKEND GOALS ------------------------------------------------------- The backend must: - Use FastAPI and SQLModel (async) - Verify JWT tokens issued by Better Auth - Extract user identity from JWT only - Reject invalid, expired, or missing tokens with HTTP 401 - Enforce per-user task isolation - Return proper HTTP status codes - Use JSON responses with success/error structure - Be fully compatible with frontend API client ------------------------------------------------------- SECTION 2: PROJECT STRUCTURE ------------------------------------------------------- Define folder structure: /apps/api/ ├── main.py ├── core/ │ ├── config.py # Environment variables and settings │ └── security.py # JWT verification, Better Auth integration ├── db/ │ ├── session.py # Async engine and session management │ └── models.py # SQLModel classes (User, Task) ├── api/ │ ├── deps.py # Dependencies (get_current_user) │ └── routes/ │ └── tasks.py # CRUD endpoints ├── schemas/ │ └── task.py # Pydantic schemas (TaskCreate, TaskUpdate, TaskResponse) └── services/ └── task_service.py # Business logic for tasks Responsibilities: - main.py → App initialization, CORS, middleware - config.py → Read .env - security.py → JWT validation - session.py → Async session - models.py → Database tables - deps.py → Dependency injection - routes/tasks.py → API endpoints - task_service.py → CRUD logic - schemas/task.py → Request/response validation ------------------------------------------------------- SECTION 3: DATABASE SPECIFICATION ------------------------------------------------------- Database: Neon Serverless PostgreSQL Tasks table: - id: UUID, primary key - title: string, required - description: string, optional - completed: boolean, default false - user_id: string, indexed, foreign key to users - created_at: timestamp - updated_at: timestamp Indexes: - tasks.user_id - tasks.completed Requirements: - All queries filter by authenticated user_id - Automatic created_at and updated_at - Multi-user isolation enforced at query level ------------------------------------------------------- SECTION 4: JWT AUTHENTICATION SPECIFICATION ------------------------------------------------------- - Extract Authorization: Bearer <token> - Verify signature using BETTER_AUTH_SECRET - Validate expiration - Extract user_id - Reject invalid/missing tokens with HTTP 401 Dependency: get_current_user() - Decode token - Return user_id - Raise HTTPException 401 if invalid Rules: - Never trust user_id from request body - Always extract user_id from JWT - Never expose another user's data ------------------------------------------------------- SECTION 5: API ENDPOINTS SPECIFICATION ------------------------------------------------------- Base path: /api/tasks Endpoints: 1. GET /api/tasks - Return all tasks for authenticated user - Support query params: status (all/pending/completed), sort (created/title/due_date) 2. POST /api/tasks - Create a task for authenticated user - Validate title length (1–200), optional description 3. PUT /api/tasks/{task_id} - Update task title/description - Verify ownership 4. PATCH /api/tasks/{task_id}/toggle - Toggle task completion - Verify ownership 5. DELETE /api/tasks/{task_id} - Delete task - Verify ownership All endpoints: - Require JWT - Return 404 if task not owned by user - Return 401 if unauthorized ------------------------------------------------------- SECTION 6: SCHEMA SPECIFICATION ------------------------------------------------------- Pydantic Schemas: - TaskCreate - TaskUpdate - TaskResponse Requirements: - Hide internal fields if necessary - Serialize UUID properly - Include created_at and updated_at ------------------------------------------------------- SECTION 7: SERVICE LAYER SPECIFICATION ------------------------------------------------------- task_service.py: - create_task(user_id, data) - get_user_tasks(user_id) - update_task(user_id, task_id, data) - toggle_task(user_id, task_id) - delete_task(user_id, task_id) Requirements: - All functions accept user_id - Filter by user_id - Raise exception if task not found ------------------------------------------------------- SECTION 8: DATABASE SESSION MANAGEMENT ------------------------------------------------------- - Use async SQLModel engine - async_sessionmaker - Dependency get_session() - Connection pooling with Neon - Proper cleanup after request ------------------------------------------------------- SECTION 9: FRONTEND INTEGRATION REQUIREMENTS ------------------------------------------------------- - CORS allowed for http://localhost:3000 - JSON responses only - Proper status codes - Consistent response format Success: { "success": true, "data": ... } Error: { "success": false, "error": "message" } ------------------------------------------------------- SECTION 10: ERROR HANDLING STRATEGY ------------------------------------------------------- Global exception handlers for: - HTTPException - ValidationError - JWT errors - Database errors No internal stack traces exposed to frontend. ------------------------------------------------------- SECTION 11: TESTING REQUIREMENTS ------------------------------------------------------- Integration tests must verify: - No token → 401 - Invalid token → 401 - Expired token → 401 - User A cannot access User B tasks - CRUD operations work correctly - Task persists in Neon database ------------------------------------------------------- SECTION 12: OUTPUT FILES ------------------------------------------------------- Generate specification files under: /specs/backend/architecture.md /specs/backend/database.md /specs/backend/authentication.md /specs/backend/api.md /specs/features/backend-tasks.md The backend must be secure, production-ready, and fully integrated with the frontend.

## Assistant Response Summary

Successfully created comprehensive backend specification for JWT authentication and task management. The following specification documents were created:

1. Main feature specification: `/specs/features/backend-tasks.md`
2. Architecture specification: `/specs/backend/architecture.md`
3. Database specification: `/specs/backend/database.md`
4. Authentication specification: `/specs/backend/authentication.md`
5. API specification: `/specs/backend/api.md`
6. Quality checklist: `/specs/features/checklists/requirements.md`

The specifications were initially created with implementation details but were subsequently updated to be more technology-agnostic while preserving essential requirements. All checklist items have been validated and completed successfully.

## Outcome

The backend specification is complete and ready for the next phase (planning). The specifications include all required components for a secure, production-ready backend with JWT authentication, multi-user task isolation, and full CRUD operations for tasks.