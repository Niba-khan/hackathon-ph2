---
id: 005
title: "Backend Plan Update for Frontend Auth Integration"
stage: plan
date_iso: "2026-02-11"
surface: "agent"
model: "OpenAI GPT-4"
feature: "backend-jwt-tasks"
branch: "001-backend-jwt-tasks"
user: "user"
command: "/sp.plan"
labels: ["planning", "backend", "authentication", "resource-server"]
links:
  spec: "../specs/features/backend-tasks.md"
  plan: "./backend-tasks/plan.md"
  ticket: null
  adr: null
  pr: null
files_yaml: |
  - /specs/features/backend-tasks/plan.md
  - /specs/features/backend-tasks/research.md
  - /specs/features/backend-tasks/data-model.md
  - /specs/features/backend-tasks/quickstart.md
  - /specs/features/backend-tasks/contracts/task-api-contract.yaml
tests_yaml: []
outcome: "Successfully updated backend plan to align with frontend authentication architecture"
evaluation: "Plan now reflects resource server pattern with JWT verification only, removing auth endpoints"
---

# Prompt History Record: Backend Plan Update for Frontend Auth Integration

## Original User Prompt

Update the backend execution plan for Phase II of the Hackathon Todo Application to align authentication architecture with the frontend.

Context:
- Frontend uses Better Auth for signup, signin, logout.
- Better Auth issues JWT tokens.
- Backend currently has signup, signin, logout endpoints.
- Backend must now act only as a protected resource server.
- Backend must verify JWT tokens but must NOT handle authentication logic.

Objective:
Refactor backend plan so that:

- Authentication is fully handled by frontend (Better Auth).
- Backend removes redundant signup/signin/logout routes.
- Backend only verifies JWT and protects task endpoints.
- Architecture follows constitution.md strictly.

-------------------------------------------------------
SECTION 1: AUTHENTICATION ARCHITECTURE DECISION
-------------------------------------------------------

Define final architecture:

Frontend:
- Handles signup/login/logout
- Receives JWT
- Sends Authorization: Bearer <token> to backend

Backend:
- Does NOT generate JWT
- Does NOT store passwords
- Does NOT implement signup/signin/logout
- Only verifies JWT signature using BETTER_AUTH_SECRET
- Extracts user_id from token
- Protects task endpoints

-------------------------------------------------------
SECTION 2: REMOVE AUTH ENDPOINTS PLAN
-------------------------------------------------------

Define steps to:

1. Remove:
   - /signup
   - /signin
   - /logout
2. Remove password hashing logic
3. Remove user password storage (if exists)
4. Keep only user_id extracted from JWT
5. Keep optional lightweight User model only if needed for relations

-------------------------------------------------------
SECTION 3: JWT VERIFICATION PLAN
-------------------------------------------------------

Implement:

- get_current_user() dependency
- Decode JWT using BETTER_AUTH_SECRET
- Validate expiration
- Extract user_id from payload
- Raise 401 if invalid

Ensure:
- No endpoint accepts user_id from request body
- All queries filter by JWT user_id

-------------------------------------------------------
SECTION 4: DATABASE ADJUSTMENT PLAN
-------------------------------------------------------

Tasks table must contain:
- user_id (string, indexed)

No password storage required.

User table optional:
- If used, must NOT store passwords
- Only store user metadata if required

-------------------------------------------------------
SECTION 5: API ROUTE STRUCTURE
-------------------------------------------------------

Final backend routes:

/api/tasks
- GET
- POST
- PUT
- PATCH /toggle
- DELETE

All routes:
- Require get_current_user dependency
- Enforce ownership filtering

-------------------------------------------------------
SECTION 6: FRONTEND INTEGRATION CONFIRMATION
-------------------------------------------------------

Verify:

- Backend accepts JWT from frontend
- CORS allows http://localhost:3000
- Response format matches frontend API client
- 401 returned for missing/invalid token

-------------------------------------------------------
SECTION 7: SECURITY HARDENING
-------------------------------------------------------

Ensure:

- No password handling logic exists
- No JWT generation logic exists
- Only signature verification
- No sensitive error leaks
- Proper exception handling

-------------------------------------------------------
SECTION 8: FINAL CLEAN ARCHITECTURE SUMMARY
-------------------------------------------------------

Produce a final summary describing:

- Frontend as Authentication Provider
- Backend as Resource Server
- JWT as identity bridge
- Strict user isolation enforcement

The updated plan must reflect a clean, modern, secure full-stack architecture suitable for production SaaS applications.

## Assistant Response Summary

Successfully updated the backend implementation plan to align with frontend authentication architecture. The following artifacts were created:

1. Updated implementation plan: `/specs/features/backend-tasks/plan.md`
2. Research findings: `/specs/features/backend-tasks/research.md`
3. Data model: `/specs/features/backend-tasks/data-model.md`
4. Quickstart guide: `/specs/features/backend-tasks/quickstart.md`
5. API contracts: `/specs/features/backend-tasks/contracts/task-api-contract.yaml`

The plan now reflects a resource server pattern where the backend only verifies JWT tokens issued by Better Auth on the frontend, without handling authentication itself. All authentication endpoints have been removed, and the backend focuses solely on protecting task resources based on verified JWT tokens.

## Outcome

The backend plan has been successfully updated to follow the resource server pattern, with clear separation of concerns between frontend authentication and backend resource protection. The architecture now properly follows the constitution's requirements for API security and full-stack separation.