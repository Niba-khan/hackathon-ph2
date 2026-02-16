# Implementation Plan: Next.js Frontend for Todo Application

**Branch**: `1-frontend-spec` | **Date**: 2026-02-11 | **Spec**: [link]
**Input**: Feature specification from `/specs/1-frontend-spec/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a secure, responsive Next.js frontend for the todo application with JWT-based authentication using Better Auth. The frontend will provide a professional dashboard UI supporting full CRUD operations with a clean, modern design following SaaS UI standards.

## Technical Context

**Language/Version**: TypeScript 5.3+, Next.js 16+
**Primary Dependencies**: Next.js 16+, React, Tailwind CSS, Better Auth, SWR/react-query
**Storage**: Browser storage for JWT tokens (preferably httpOnly cookies)
**Testing**: Jest, React Testing Library, Playwright
**Target Platform**: Web application (responsive)
**Project Type**: Monorepo with clear separation of frontend, backend, and database layers
**Performance Goals**: Fast loading, responsive UI, minimal bundle size
**Constraints**: JWT-based authentication, user task isolation, secure API endpoints
**Scale/Scope**: Multi-user todo application with secure data isolation

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- Multi-User Security: All endpoints must validate JWT signatures and enforce user isolation
- Full-Stack Architecture: Clear separation of frontend (Next.js) and backend (FastAPI)
- Database Integrity: Proper handling of data from PostgreSQL via backend
- Spec-Driven Development: All implementation follows specifications in /specs directory
- Agent Governance: Specialized agents with defined responsibilities
- API Security Compliance: All API calls require Authorization header with JWT

## Project Structure

### Documentation (this feature)

```text
specs/1-frontend-spec/
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
├── frontend/            # Next.js 16+ application
│   ├── app/             # App Router pages
│   │   ├── layout.tsx
│   │   ├── page.tsx     # Landing page
│   │   ├── login/page.tsx
│   │   ├── signup/page.tsx
│   │   └── dashboard/page.tsx
│   ├── components/      # Reusable UI components
│   │   ├── ui/          # Base UI components (buttons, inputs, etc.)
│   │   ├── auth/        # Authentication-related components
│   │   ├── dashboard/   # Dashboard-specific components
│   │   └── layout/      # Layout components (navbar, sidebar)
│   ├── lib/             # Shared utilities and API logic
│   │   ├── api.ts       # Centralized API client
│   │   └── auth.ts      # Authentication utilities
│   ├── hooks/           # Custom React hooks
│   ├── styles/          # Global styles and Tailwind config
│   │   └── globals.css
│   └── public/          # Static assets
└── backend/             # FastAPI application (separate team responsibility)
    ├── api/
    ├── models/
    ├── auth/
    └── tests/

# Configuration and documentation
.specify/                # Spec-Kit Plus configuration
specs/                   # Feature specifications
.history/                # Prompt history records
```

**Structure Decision**: Following the constitution's requirement for monorepo structure with clear separation of frontend, backend, and database layers. The frontend uses Next.js with App Router, and communicates with the backend via secure API calls using JWT authentication.

## Implementation Strategy

### Phase A – Project Setup
**Goal**: Establish the Next.js project with proper configuration and dependencies.

**Files to create**:
- package.json with Next.js, TypeScript, Tailwind CSS dependencies
- tsconfig.json for TypeScript configuration
- tailwind.config.js and postcss.config.js for styling
- .gitignore with appropriate exclusions
- README.md with project overview

**Dependencies**: Node.js 18+, npm/yarn

**Completion criteria**:
- Next.js development server runs without errors
- Tailwind CSS classes are applied correctly
- TypeScript compilation succeeds
- Project structure matches defined architecture

### Phase B – Authentication Setup
**Goal**: Implement Better Auth for secure user authentication with JWT handling.

**Files to create**:
- lib/auth.ts for authentication utilities
- app/login/page.tsx for login functionality
- app/signup/page.tsx for registration
- Middleware to protect routes

**Dependencies**: Phase A completion, backend authentication API

**Completion criteria**:
- Users can register for new accounts
- Users can log in with valid credentials
- JWT tokens are stored securely
- Protected routes redirect unauthenticated users to login

### Phase C – Layout & UI Foundation
**Goal**: Create the foundational UI components and global layout.

**Files to create**:
- app/layout.tsx for root layout
- app/page.tsx for landing page
- components/layout/navbar.tsx for navigation
- components/layout/sidebar.tsx for desktop sidebar
- styles/globals.css for global styles
- components/ui/ folder with base components (button, input, etc.)

**Dependencies**: Phase A completion

**Completion criteria**:
- Consistent design system implemented
- Responsive layout works across devices
- Navigation works between pages
- UI follows SaaS design standards

### Phase D – Dashboard Core Features
**Goal**: Implement the main dashboard functionality for task management.

**Files to create**:
- app/dashboard/page.tsx for dashboard route
- components/dashboard/task-list.tsx for displaying tasks
- components/dashboard/task-card.tsx for individual task display
- components/dashboard/task-form.tsx for task creation/editing
- components/dashboard/filter-tabs.tsx for task filtering

**Dependencies**: Phase B completion, backend task API

**Completion criteria**:
- Users can view their tasks
- Users can create new tasks
- Users can filter tasks by status (All, Pending, Completed)
- Basic task CRUD operations work

### Phase E – API Integration
**Goal**: Connect frontend to backend APIs with proper JWT handling.

**Files to create/modify**:
- lib/api.ts for centralized API client
- hooks/use-tasks.ts for task-related data fetching
- Update dashboard components to use API data
- Error handling for API responses

**Dependencies**: Phase D completion, backend API availability

**Completion criteria**:
- All CRUD operations connect to backend
- JWT tokens are attached to requests automatically
- API errors are handled gracefully
- Loading states are properly displayed

### Phase F – UX Polish & Responsiveness
**Goal**: Enhance user experience with polish and ensure responsiveness.

**Files to create/modify**:
- components/ui/loading-spinner.tsx for loading states
- components/ui/empty-state.tsx for empty states
- components/ui/confirmation-modal.tsx for delete confirmations
- Update all components for mobile responsiveness
- Add smooth animations and transitions

**Dependencies**: Phase E completion

**Completion criteria**:
- UI is fully responsive across all device sizes
- Loading states provide feedback during operations
- Empty states guide users appropriately
- Animations enhance user experience

### Phase G – Testing & Hardening
**Goal**: Ensure quality and reliability of the frontend application.

**Files to create**:
- tests/ folder with unit and integration tests
- Update components for testability
- Add accessibility attributes
- Performance optimizations

**Dependencies**: All previous phases

**Completion criteria**:
- Test coverage meets project standards
- Application passes accessibility audits
- Performance metrics meet requirements
- No critical security vulnerabilities

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |

## Detailed Implementation Steps

### Section 3: Authentication Implementation Plan

1. Install Better Auth: `npm install better-auth @better-auth/react`
2. Configure Better Auth in the frontend with JWT plugin
3. Set up environment variables for authentication
4. Create auth client setup in lib/auth.ts
5. Implement protected route middleware for dashboard
6. Create redirect logic for unauthenticated users
7. Implement JWT attachment to API client in lib/api.ts

### Section 4: UI Implementation Plan

1. Global Layout (app/layout.tsx) - Server Component
   - File path: app/layout.tsx
   - Dependencies: Tailwind CSS, fonts
   - Props: children

2. Navbar (components/layout/navbar.tsx) - Client Component
   - File path: components/layout/navbar.tsx
   - Dependencies: next/link, auth utilities
   - Props: isLoggedIn, user info

3. Sidebar (components/layout/sidebar.tsx) - Client Component (desktop only)
   - File path: components/layout/sidebar.tsx
   - Dependencies: next/link, auth utilities
   - Props: user info

4. TaskList (components/dashboard/task-list.tsx) - Client Component
   - File path: components/dashboard/task-list.tsx
   - Dependencies: TaskCard, SWR for data fetching
   - Props: tasks array, callbacks for task operations

5. TaskCard (components/dashboard/task-card.tsx) - Client Component
   - File path: components/dashboard/task-card.tsx
   - Dependencies: UI components (buttons, etc.)
   - Props: task object, callbacks for task operations

6. TaskForm (components/dashboard/task-form.tsx) - Client Component
   - File path: components/dashboard/task-form.tsx
   - Dependencies: UI components (inputs, buttons)
   - Props: initial data (for editing), submit callback

7. FilterTabs (components/dashboard/filter-tabs.tsx) - Client Component
   - File path: components/dashboard/filter-tabs.tsx
   - Dependencies: UI components (buttons)
   - Props: current filter, filter change callback

8. EmptyState (components/ui/empty-state.tsx) - Client Component
   - File path: components/ui/empty-state.tsx
   - Dependencies: UI components
   - Props: message, icon

9. Loading Skeleton (components/ui/loading-spinner.tsx) - Client Component
   - File path: components/ui/loading-spinner.tsx
   - Dependencies: Tailwind CSS
   - Props: none

### Section 5: API Integration Plan

Implementation steps for lib/api.ts:
1. Create base API client with axios/fetch
2. Implement JWT token retrieval and attachment
3. Add global error handling for 401 responses
4. Create typed interfaces for Task entity
5. Implement specific API functions:
   - getTasks(): Promise<Task[]>
   - createTask(taskData): Promise<Task>
   - updateTask(taskId, taskData): Promise<Task>
   - toggleTask(taskId): Promise<Task>
   - deleteTask(taskId): Promise<void>

Integration order:
1. getTasks() - to display tasks on dashboard
2. createTask() - to add new tasks
3. updateTask() - to modify existing tasks
4. toggleTask() - to change completion status
5. deleteTask() - to remove tasks

### Section 6: State Management Plan

- Server Components: Use for initial data fetching and rendering static content
- Client Components: Use for interactive elements and local state
- Local state: Use React useState for UI state (filters, form data)
- Global state: Leverage SWR for server state (tasks, user data)
- Loading strategy: Use SWR's built-in loading states and suspense
- Error handling: Use SWR's error handling and custom error boundaries

### Section 7: Responsiveness Strategy

- Breakpoints: Use Tailwind's default breakpoints (sm: 640px, md: 768px, lg: 1024px, xl: 1280px)
- Mobile-first approach: Design for mobile first, then enhance for larger screens
- Layout adjustments: Use flexbox/grid with responsive classes
- Sticky add-task button: Fixed positioning at bottom on mobile screens

### Section 8: Quality Standards

- Code organization: Follow Next.js App Router conventions
- Naming conventions: Use PascalCase for components, camelCase for functions
- Component size: Limit components to < 200 lines when possible
- Reusability: Extract common UI elements to shared components
- Accessibility: Follow WCAG 2.1 AA guidelines
- Tailwind usage: Use utility classes consistently, avoid arbitrary values

### Section 9: Risk Mitigation

- JWT mismatch issues: Implement token refresh mechanism
- Hydration issues: Use 'use client' directive appropriately, handle server/client state differences
- Server/Client boundary problems: Carefully manage where state is handled
- API 401 handling: Implement global error handler that redirects to login

### Section 10: Final Deliverable Checklist

- [ ] Authentication working (login, signup, logout)
- [ ] Protected routes working (dashboard requires auth)
- [ ] CRUD operations working (create, read, update, delete tasks)
- [ ] UI responsive (works on mobile, tablet, desktop)
- [ ] No console errors (clean browser console)
- [ ] Clean TypeScript build (no type errors)
- [ ] API integration complete (all endpoints connected)
- [ ] Loading states implemented (during data fetching)
- [ ] Error handling in place (for API failures)
- [ ] Form validation working (client-side)