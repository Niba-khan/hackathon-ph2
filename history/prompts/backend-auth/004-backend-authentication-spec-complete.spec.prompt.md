---
id: 004
title: "Backend Authentication Spec Complete"
stage: spec
date_iso: "2026-02-11"
surface: "agent"
model: "OpenAI GPT-4"
feature: "backend-auth"
branch: "002-backend-auth"
user: "user"
command: "/sp.specify"
labels: ["specification", "backend", "authentication", "jwt"]
links:
  spec: "../specs/features/backend-auth/spec.md"
  plan: "./backend-auth/plan.md"
  tasks: "./backend-auth/tasks.md"
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - /specs/backend/authentication.md
  - /specs/backend/database.md
  - /specs/backend/api-auth.md
  - /specs/backend/api-tasks.md
  - /specs/features/backend-auth/spec.md
tests_yaml: []
outcome: "Successfully created complete backend authentication specification"
evaluation: "All required specification files created according to requirements with proper security measures and architecture"
---

# Prompt History Record: Backend Authentication Specification

## Original User Input

Create a complete backend authentication specification for Phase II of the Hackathon Todo Application. Reference: - Follow constitution.md strictly. - Backend will now act as Authentication Authority. - Remove dependency on Better Auth. - Backend must generate and verify JWT tokens internally. - Ensure seamless integration with existing task endpoints. Objective: Design a secure, production-ready FastAPI backend that includes: - User registration (signup) - User login (signin) - JWT token generation - Token-based authentication - Secure password hashing - Multi-user task isolation - Integration with Neon PostgreSQL - Full compatibility with frontend Environment Variables: DATABASE_URL = 'postgresql://neondb_owner:npg_ALn8w2VXuimk@ep-bold-thunder-ais27zzv-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require' JWT_SECRET_KEY = generate secure key JWT_ALGORITHM = HS256 ACCESS_TOKEN_EXPIRE_MINUTES = 60 ------------------------------------------------------- SECTION 1: AUTHENTICATION ARCHITECTURE ------------------------------------------------------- Backend Responsibilities: - Handle user signup - Hash passwords using bcrypt - Store hashed password in database - Authenticate user credentials - Generate JWT access tokens - Validate JWT on protected routes - Extract user_id from token - Enforce task isolation JWT must contain: - sub (user_id) - email - exp (expiration) ------------------------------------------------------- SECTION 2: PROJECT STRUCTURE ------------------------------------------------------- /apps/api/ ├── main.py ├── core/ │ ├── config.py │ ├── security.py # JWT creation & verification │ └── hashing.py # bcrypt password hashing ├── db/ │ ├── session.py │ └── models.py # User + Task models ├── api/ │ ├── deps.py # get_current_user │ └── routes/ │ ├── auth.py # signup/login/logout │ └── tasks.py ├── schemas/ │ ├── user.py │ └── task.py └── services/ ├── auth_service.py └── task_service.py ------------------------------------------------------- SECTION 3: DATABASE MODELS ------------------------------------------------------- User table: - id (UUID, primary key) - email (unique, indexed) - hashed_password (string) - created_at (timestamp) Task table: - id (UUID, primary key) - title (string) - description (string, optional) - completed (boolean) - user_id (foreign key to users.id, indexed) - created_at - updated_at Requirements: - Enforce unique email - Index user_id in tasks - Automatic timestamps ------------------------------------------------------- SECTION 4: AUTH ENDPOINTS ------------------------------------------------------- Base path: /api/auth 1. POST /signup - Accept email + password - Validate email format - Validate password strength - Hash password - Store user - Return JWT token 2. POST /login - Accept email + password - Verify credentials - Generate JWT token - Return token 3. GET /me - Return authenticated user info - Requires JWT 4. POST /logout - Optional (stateless JWT) - Return success message ------------------------------------------------------- SECTION 5: TASK ENDPOINTS (Protected) ------------------------------------------------------- Base path: /api/tasks All require Authorization: Bearer <token> - GET / - POST / - PUT /{task_id} - PATCH /{task_id}/toggle - DELETE /{task_id} All queries must filter by authenticated user_id. ------------------------------------------------------- SECTION 6: SECURITY SPECIFICATION ------------------------------------------------------- Password Hashing: - Use bcrypt - Never store plain text passwords JWT: - Use python-jose - Validate expiration - Reject invalid tokens with HTTP 401 - Use Bearer authentication scheme Security Rules: - Never accept user_id from client - Always extract from JWT - Return 404 if accessing another user's task ------------------------------------------------------- SECTION 7: RESPONSE FORMAT ------------------------------------------------------- Success: { "success": true, "data": ... } Error: { "success": false, "error": "message" } ------------------------------------------------------- SECTION 8: FRONTEND INTEGRATION ------------------------------------------------------- Frontend must: - Call /api/auth/signup - Call /api/auth/login - Store JWT securely - Send Authorization header on all task requests - Handle 401 by redirecting to login ------------------------------------------------------- SECTION 9: TESTING REQUIREMENTS ------------------------------------------------------- Verify: - Duplicate email blocked - Invalid login rejected - Password hashing works - JWT expires properly - Protected endpoints reject missing token - User A cannot access User B tasks - CRUD works fully ------------------------------------------------------- SECTION 10: OUTPUT FILES ------------------------------------------------------- Generate specification files under: /specs/backend/authentication.md /specs/backend/database.md /specs/backend/api-auth.md /specs/backend/api-tasks.md /specs/features/backend-auth.md The backend must be fully self-contained, secure, production-ready, and suitable for hackathon evaluation.

## Response Summary

Successfully created a complete backend authentication specification for the Phase II Hackathon Todo Application. The following specification files were created:

1. `/specs/backend/authentication.md` - Overview of the authentication system architecture
2. `/specs/backend/database.md` - Database schema and configuration for users and tasks
3. `/specs/backend/api-auth.md` - Authentication API endpoints specification
4. `/specs/backend/api-tasks.md` - Task management API endpoints specification
5. `/specs/features/backend-auth/spec.md` - Complete feature specification with user stories and requirements

The specification includes all required functionality:
- User registration (signup) with email validation and password strength requirements
- User login (signin) with credential verification
- JWT token generation and verification
- Secure password hashing using bcrypt
- Multi-user task isolation with proper filtering
- Integration with Neon PostgreSQL
- Full compatibility with frontend
- Proper security measures and error handling

The backend follows a resource-based architecture where it acts as the authentication authority, generating and verifying JWT tokens internally without relying on external services like Better Auth. The system enforces strict user isolation, ensuring that users can only access their own tasks.