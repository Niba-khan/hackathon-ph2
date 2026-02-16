---

description: "Task list template for feature implementation"
---

# Tasks: Next.js Frontend for Todo Application

**Input**: Design documents from `/specs/1-frontend-spec/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

<!--
  ============================================================================
  IMPORTANT: The tasks below are SAMPLE TASKS for illustration purposes only.

  The /sp.tasks command MUST replace these with actual tasks based on:
  - User stories from spec.md (with their priorities P1, P2, P3...)
  - Feature requirements from plan.md
  - Entities from data-model.md
  - Endpoints from contracts/

  Tasks MUST be organized by user story so each story can be:
  - Implemented independently
  - Tested independently
  - Delivered as an MVP increment

  DO NOT keep these sample tasks in the generated tasks.md file.
  ============================================================================
-->

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create monorepo structure per implementation plan with apps/frontend and apps/backend
- [ ] T002 Initialize Next.js 16+ project in apps/frontend with TypeScript and Tailwind CSS
- [ ] T003 Initialize FastAPI project in apps/backend with SQLModel and Pydantic dependencies
- [ ] T004 [P] Configure linting and formatting tools for both frontend and backend

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [ ] T005 Setup Neon PostgreSQL database schema and migrations framework
- [ ] T006 [P] Implement Better Auth authentication framework with JWT token issuance
- [ ] T007 [P] Setup JWT verification middleware in FastAPI backend
- [ ] T008 Create base models/entities that all stories depend on
- [ ] T009 Configure error handling and logging infrastructure
- [ ] T010 Setup environment configuration management with BETTER_AUTH_SECRET

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Secure Authentication (Priority: P1) 🎯 MVP

**Goal**: Users can securely log in and access their personal task dashboard.

**Independent Test**: Users can register for an account, log in with their credentials, and be redirected to their personal dashboard.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [ ] T011 [P] [US1] Contract test for authentication endpoints in tests/contract/test_auth.py
- [ ] T012 [P] [US1] Integration test for user registration and login flow in tests/integration/test_auth_flow.py

### Implementation for User Story 1

- [ ] T013 [P] [US1] Create User model in apps/backend/models/user.py
- [ ] T014 [P] [US1] Create Task model in apps/backend/models/task.py with user_id foreign key
- [ ] T015 [US1] Implement Task service in apps/backend/services/task_service.py (depends on T013, T014)
- [ ] T016 [US1] Implement task CRUD endpoints in apps/backend/api/tasks.py
- [ ] T017 [US1] Add JWT authentication validation to task endpoints
- [ ] T018 [US1] Add user isolation filtering to all task operations
- [ ] T019 [US1] Create TaskList component in apps/frontend/components/TaskList.tsx
- [ ] T020 [US1] Create TaskForm component in apps/frontend/components/TaskForm.tsx
- [ ] T021 [US1] Integrate frontend with backend API using centralized API logic in apps/frontend/lib/api.ts

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Task Management Dashboard (Priority: P1)

**Goal**: Users can view, create, update, and delete their tasks in a responsive interface.

**Independent Test**: Users can perform all CRUD operations on their tasks through the dashboard interface.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [ ] T022 [P] [US2] Contract test for task endpoints in tests/contract/test_tasks.py
- [ ] T023 [P] [US2] Integration test for task CRUD operations in tests/integration/test_task_crud.py

### Implementation for User Story 2

- [ ] T024 [P] [US2] Create Task model in apps/frontend/models/task.ts
- [ ] T025 [US2] Implement Task service in apps/frontend/services/task_service.ts
- [ ] T026 [US2] Implement task dashboard page in apps/frontend/app/dashboard/page.tsx
- [ ] T027 [US2] Integrate with User Story 1 components (if needed)

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Responsive UI Experience (Priority: P2)

**Goal**: The UI adapts appropriately to mobile, tablet, and desktop screen sizes with optimal layouts for each.

**Independent Test**: The UI adapts appropriately to mobile, tablet, and desktop screen sizes with optimal layouts for each.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [ ] T028 [P] [US3] Contract test for responsive components in tests/contract/test_responsive.py
- [ ] T029 [P] [US3] Integration test for responsive behavior in tests/integration/test_responsive.py

### Implementation for User Story 3

- [ ] T030 [P] [US3] Create responsive layout components in apps/frontend/components/layout/
- [ ] T031 [US3] Implement responsive design for dashboard in apps/frontend/app/dashboard/page.tsx
- [ ] T032 [US3] Implement responsive design for task components in apps/frontend/components/

**Checkpoint**: All user stories should now be independently functional

---

[Add more user story phases as needed, following the same pattern]

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] TXXX [P] Documentation updates in docs/
- [ ] TXXX Code cleanup and refactoring
- [ ] TXXX Performance optimization across all stories
- [ ] TXXX [P] Additional unit tests (if requested) in tests/unit/
- [ ] TXXX Security hardening - ensure all endpoints validate JWT and enforce user isolation
- [ ] TXXX Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Contract test for authentication endpoints in tests/contract/test_auth.py"
Task: "Integration test for user registration and login flow in tests/integration/test_auth_flow.py"

# Launch all models for User Story 1 together:
Task: "Create User model in apps/backend/models/user.py"
Task: "Create Task model in apps/backend/models/task.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
- Ensure all database queries filter by authenticated user ID to maintain user isolation
- All API endpoints must validate JWT signature and extract user identity from token
- Unauthorized access must return HTTP 401; cross-user resource access must return HTTP 404

---

## Updated Tasks for Next.js Frontend Implementation

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create apps/frontend directory structure per plan.md
- [X] T002 [P] Initialize Next.js 16+ project with TypeScript in apps/frontend
- [X] T003 [P] Configure Tailwind CSS in apps/frontend
- [X] T004 [P] Set up basic ESLint and Prettier configuration in apps/frontend
- [X] T005 Create initial directory structure: app/, components/, lib/, hooks/, styles/, public/

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [ ] T006 [P] Install Better Auth dependencies: npm install better-auth @better-auth/react
- [X] T007 [P] Install SWR for data fetching: npm install swr
- [X] T008 [P] Install additional dependencies: npm install @types/node @types/react
- [X] T009 Create lib/api.ts with basic API client setup
- [X] T010 Create lib/auth.ts with authentication utilities
- [X] T011 Create hooks/use-tasks.ts for task-related data fetching
- [X] T012 Create basic type definitions for User and Task entities in types/index.ts

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Secure Authentication (Priority: P1) 🎯 MVP

**Goal**: Users can securely log in and access their personal task dashboard.

**Independent Test**: Users can register for an account, log in with their credentials, and be redirected to their personal dashboard.

### Implementation for User Story 1

- [X] T013 [P] [US1] Create app/layout.tsx with basic layout structure
- [X] T014 [P] [US1] Create app/page.tsx for landing page with hero section
- [X] T015 [US1] Create app/login/page.tsx with email/password form
- [X] T016 [US1] Create app/signup/page.tsx with registration form
- [X] T017 [US1] Implement authentication logic in lib/auth.ts
- [ ] T018 [US1] Create components/auth/login-form.tsx with form validation
- [ ] T019 [US1] Create components/auth/signup-form.tsx with form validation
- [ ] T020 [US1] Implement protected route middleware for dashboard
- [X] T021 [US1] Create components/ui/alert.tsx for error messages
- [ ] T022 [US1] Add redirect logic after successful login/signup

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Task Management Dashboard (Priority: P1)

**Goal**: Users can view, create, update, and delete their tasks in a responsive interface.

**Independent Test**: Users can perform all CRUD operations on their tasks through the dashboard interface.

### Implementation for User Story 2

- [X] T023 [P] [US2] Create app/dashboard/page.tsx for dashboard route
- [X] T024 [P] [US2] Create components/dashboard/task-list.tsx for displaying tasks
- [X] T025 [P] [US2] Create components/dashboard/task-card.tsx for individual task display
- [X] T026 [P] [US2] Create components/dashboard/task-form.tsx for task creation/editing
- [X] T027 [P] [US2] Create components/dashboard/filter-tabs.tsx for task filtering
- [X] T028 [US2] Implement getTasks() function in lib/api.ts
- [X] T029 [US2] Implement createTask() function in lib/api.ts
- [ ] T030 [US2] Implement updateTask() function in lib/api.ts
- [X] T031 [US2] Implement deleteTask() function in lib/api.ts
- [X] T032 [US2] Implement toggleTask() function in lib/api.ts
- [X] T033 [US2] Connect dashboard components to API functions
- [X] T034 [US2] Create components/ui/modal.tsx for confirmation modal
- [X] T035 [US2] Create components/ui/button.tsx for consistent buttons
- [X] T036 [US2] Create components/ui/input.tsx for consistent inputs
- [X] T037 [US2] Create components/ui/label.tsx for form labels

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Responsive UI Experience (Priority: P2)

**Goal**: The UI adapts appropriately to mobile, tablet, and desktop screen sizes with optimal layouts for each.

**Independent Test**: The UI adapts appropriately to mobile, tablet, and desktop screen sizes with optimal layouts for each.

### Implementation for User Story 3

- [X] T038 [P] [US3] Create components/layout/navbar.tsx with responsive design
- [X] T039 [P] [US3] Create components/layout/sidebar.tsx for desktop view
- [X] T040 [P] [US3] Create components/ui/loading-spinner.tsx for loading states
- [X] T041 [P] [US3] Create components/ui/empty-state.tsx for empty states
- [ ] T042 [US3] Update dashboard layout for mobile responsiveness
- [ ] T043 [US3] Implement sticky add-task button for mobile
- [X] T044 [US3] Create components/ui/confirmation-modal.tsx for delete confirmations
- [ ] T045 [US3] Add responsive classes to all UI components
- [ ] T046 [US3] Implement mobile-first approach with Tailwind responsive prefixes
- [ ] T047 [US3] Add smooth transitions and hover effects per UI design principles

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T048 [P] Add proper TypeScript types for all API responses
- [ ] T049 [P] Add accessibility attributes to all components
- [ ] T050 [P] Add proper meta tags and SEO elements
- [ ] T051 [P] Add error boundaries for better error handling
- [X] T052 [P] Add loading states and skeleton screens during data fetching
- [ ] T053 [P] Add form validation for all user inputs
- [X] T054 [P] Add proper error handling for API failures
- [ ] T055 [P] Add token refresh mechanism for JWT expiration
- [X] T056 [P] Add global error handler that redirects to login on 401
- [X] T057 [P] Update styles/globals.css with consistent design system
- [ ] T058 [P] Add unit tests for critical components
- [ ] T059 [P] Run quickstart validation to ensure everything works together

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Depends on US1 (auth)
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Components before pages
- Core functionality before UI polish
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- Components within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 2

```bash
# Launch all components for User Story 2 together:
Task: "Create components/dashboard/task-list.tsx for displaying tasks"
Task: "Create components/dashboard/task-card.tsx for individual task display"
Task: "Create components/dashboard/task-form.tsx for task creation/editing"
Task: "Create components/dashboard/filter-tabs.tsx for task filtering"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
- Ensure all database queries filter by authenticated user ID to maintain user isolation
- All API endpoints must validate JWT signature and extract user identity from token
- Unauthorized access must return HTTP 401; cross-user resource access must return HTTP 404