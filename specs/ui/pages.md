# Pages Specification: Next.js Frontend for Todo Application

## Overview
This document specifies the page structure and functionality for the Next.js frontend of the Todo application. All pages must follow the UI design principles and authentication flow defined in the main specification.

## Page Specifications

### 1. Landing Page (`/`)
**Purpose**: Entry point for unauthenticated users to learn about the application and sign up.

**Components Used**:
- Navbar (public version)
- Hero section
- Feature highlights
- Call-to-action buttons

**Functionality**:
- Display marketing content about the application
- Provide navigation to login/signup pages
- Showcase key features of the todo application

**Authentication**: Public access

### 2. Login Page (`/login`)
**Purpose**: Allow existing users to authenticate and access their dashboard.

**Components Used**:
- Email input field
- Password input field
- Submit button
- Error message display
- Link to signup page

**Functionality**:
- Collect user credentials
- Authenticate with backend via Better Auth
- Store JWT token securely upon successful authentication
- Redirect to dashboard upon successful login
- Display error messages for failed authentication attempts

**Authentication**: Public access

### 3. Signup Page (`/signup`)
**Purpose**: Allow new users to create an account and access the application.

**Components Used**:
- Email input field
- Password input field
- Confirm password field
- Submit button
- Validation messages

**Functionality**:
- Collect user registration information
- Validate input fields (email format, password strength, matching passwords)
- Register new user via Better Auth
- Store JWT token securely upon successful registration
- Redirect to dashboard upon successful signup

**Authentication**: Public access

### 4. Dashboard Page (`/dashboard`)
**Purpose**: Main interface for authenticated users to manage their tasks.

**Components Used**:
- Navbar (authenticated version)
- Sidebar (desktop view)
- TaskList
- TaskForm
- FilterTabs
- LoadingSpinner
- EmptyState (when no tasks)

**Functionality**:
- Display user's tasks in a responsive layout
- Provide form to create new tasks
- Allow filtering tasks (All/Pending/Completed)
- Enable task completion toggling
- Allow task deletion with confirmation
- Provide logout functionality
- Handle loading states during data fetching
- Display empty state when no tasks exist

**Authentication**: Protected route - requires valid JWT token
- If no token exists, redirect to `/login`
- If token is invalid/expired, redirect to `/login`

### 5. Protected Route Handling
**Purpose**: Ensure unauthorized access to protected pages is prevented.

**Functionality**:
- Check for valid JWT token before rendering protected content
- Redirect to login page if token is missing or invalid
- Handle token refresh if supported by Better Auth