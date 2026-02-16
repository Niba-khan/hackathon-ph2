<!-- SYNC IMPACT REPORT:
  - Version change: 1.0.0 → 1.1.0
  - Modified principles: All principles replaced with specific project principles
  - Added sections: System Vision, Technology Stack, Architectural Principles, Agent Governance Model, API Security Policy, Database Policy, Frontend Policy, Testing Requirements, Phase Boundary
  - Removed sections: Original template placeholders
  - Templates requiring updates: 
    - .specify/templates/plan-template.md ✅ updated
    - .specify/templates/spec-template.md ✅ updated
    - .specify/templates/tasks-template.md ✅ updated
  - Follow-up TODOs: None
-->

# Hackathon Todo – Phase II Full-Stack Web Application Constitution

## Core Principles

### I. Multi-User Security
The system must support multiple authenticated users with strict user task isolation. JWT-based authentication must be implemented with proper token verification on all protected endpoints. Backend services must validate JWT signatures independently and never trust user_id from request bodies or URLs. All database queries must filter by authenticated user ID to prevent unauthorized access.

### II. Full-Stack Architecture
The system must follow a monorepo structure with clear separation of frontend, backend, and database layers. Frontend (Next.js 16+, TypeScript, Tailwind CSS) and backend (Python FastAPI, SQLModel ORM) must be independently testable. Better Auth must be used for JWT token issuance with shared secrets via BETTER_AUTH_SECRET environment variable.

### III. Database Integrity
Data must persist in Neon Serverless PostgreSQL with proper indexing and foreign key relationships. The tasks table must include a user_id foreign key with indexes on both user_id and completed columns. All task records must be associated with a user, and created_at and updated_at timestamps must be maintained.

### IV. Spec-Driven Development
All specifications must live inside the /specs directory and serve as the source of truth for implementation. The system must follow spec-driven development principles with clear separation of concerns between different layers. Implementation must strictly follow specifications without deviation.

### V. Agent Governance
The system must utilize specialized agents with clearly defined responsibilities: spec-writer-agent, architecture-planner-agent, database-engineer-agent, backend-engineer-agent, frontend-engineer-agent, and integration-tester-agent. Agents must respect specification hierarchy and not override responsibilities of other agents.

### VI. API Security Compliance
All REST endpoints must be under /api/, require Authorization: Bearer <token>, validate JWT signature and expiration, and extract user identity from token. Endpoints must filter all task operations by authenticated user and must not accept user_id from client for authorization purposes.

## System Vision
The system must transform the completed Phase I console-based todo application into a secure, multi-user, full-stack web application using Next.js (App Router), FastAPI, SQLModel, and Neon Serverless PostgreSQL. The application must enforce strict user task isolation and follow spec-driven development principles.

## Technology Stack
Frontend: Next.js 16+, TypeScript, Tailwind CSS, Better Auth (JWT enabled)
Backend: Python FastAPI, SQLModel ORM, JWT verification middleware
Database: Neon Serverless PostgreSQL
Authentication: Better Auth issuing JWT tokens with shared secret via BETTER_AUTH_SECRET environment variable

## Architectural Principles
1. Monorepo structure must be used.
2. All specifications must live inside /specs directory.
3. Agents must operate according to defined responsibilities.
4. Frontend and backend must be independently testable.
5. JWT token is the only source of user identity.
6. No user_id should be trusted from request body or URL.
7. Backend must extract user identity only from verified JWT.
8. All database queries must filter by authenticated user ID.
9. Unauthorized access must return HTTP 401.
10. Cross-user resource access must return HTTP 404.

## Agent Governance Model
The system must include the following agents:
1. spec-writer-agent - Responsible for writing and updating structured specifications.
2. architecture-planner-agent - Responsible for defining system architecture and security flow.
3. database-engineer-agent - Responsible for Neon configuration, models, and migrations.
4. backend-engineer-agent - Responsible for implementing secure REST API with JWT verification.
5. frontend-engineer-agent - Responsible for UI implementation and API integration.
6. integration-tester-agent - Responsible for validating full-stack behavior and user isolation.

Agents must respect specification hierarchy and not override responsibilities of other agents, following separation of concerns strictly.

## API Security Policy
All REST endpoints must be under /api/, require Authorization: Bearer <token>, validate JWT signature, validate token expiration, extract user identity from token, and filter all task operations by authenticated user. Endpoints must not accept user_id from client for authorization or return data belonging to another user.

## Database Policy
The database must include a tasks table with a user_id foreign key, index user_id column, index completed column, and maintain created_at and updated_at timestamps. All task records must be associated with a user.

## Frontend Policy
The frontend must use Better Auth for login/signup, enable JWT token issuance, attach JWT token to all API requests, redirect unauthenticated users to login, and centralize API logic inside /lib/api.ts.

## Testing Requirements
Integration testing must verify: no token → 401, invalid token → 401, expired token → 401, User A cannot access User B tasks, CRUD operations persist correctly, and data remains after logout/login.

## Phase Boundary
Phase II scope includes: Authentication, Secure CRUD, Multi-user isolation, Database persistence, Full frontend-backend integration.
Phase II excludes: AI chatbot, Natural language task generation, Advanced analytics.

## Governance
All implementation must strictly follow specifications in /specs directory. Specifications are the source of truth. Amendments require documentation and approval. The constitution supersedes all other practices.

**Version**: 1.1.0 | **Ratified**: 2026-02-11 | **Last Amended**: 2026-02-11