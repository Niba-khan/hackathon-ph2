# Data Model: Backend Authentication System

**Feature**: Backend Authentication System
**Date**: Wednesday, February 11, 2026

## Entity Definitions

### User Entity

The User entity represents an authenticated user in the system with credentials and metadata.

#### Fields
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID | Primary Key, Not Null | Unique identifier for each user |
| email | String(255) | UNIQUE, INDEXED, Not Null | User's email address (used for login) |
| hashed_password | String | Not Null | BCrypt hashed password |
| created_at | DateTime | Not Null | Timestamp when user was registered |

#### Relationships
- One-to-many with Task entity (one user can have many tasks)

#### Indexes
- `idx_users_email`: Unique index on `email` field for efficient login lookups

#### Validation Rules
- `email` must be a valid email format
- `email` must be unique across all users
- `hashed_password` must be properly hashed (not plain text)

### Task Entity

The Task entity represents a todo item associated with a specific user, with title, description, completion status, and timestamps.

#### Fields
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID | Primary Key, Not Null | Unique identifier for each task |
| title | String(200) | Not Null, Length 1-200 | Task title (1-200 characters) |
| description | Text | Optional | Detailed task description |
| completed | Boolean | Not Null, Default False | Task completion status |
| user_id | UUID | Not Null, Foreign Key, INDEXED | ID of the user who owns the task |
| created_at | DateTime | Not Null | Timestamp when task was created |
| updated_at | DateTime | Not Null | Timestamp when task was last updated |

#### Relationships
- Many-to-one with User entity (many tasks belong to one user)

#### Indexes
- `idx_tasks_user_id`: Index on `user_id` field for optimized queries filtering by user
- `idx_tasks_completed`: Index on `completed` field for optimized queries filtering by completion status

#### Validation Rules
- `title` must be between 1 and 200 characters
- `user_id` must match an existing user in the database
- `completed` can be toggled between true/false states

## Entity Operations

### User Operations

#### Create Operation
- Requires: `email`, `password` (plain text, to be hashed)
- Sets: `id` (auto-generated UUID), `hashed_password` (from plain text), `created_at` (current timestamp)
- Validates: Email format, uniqueness of email
- Result: New user record with hashed password

#### Read Operation
- Retrieves user information based on JWT token
- Does not return password information
- Result: User details (id, email, created_at)

### Task Operations

#### Create Operation
- Requires: `title` (1-200 chars), optional `description`, authenticated `user_id`
- Sets: `id` (auto-generated UUID), `completed` (default false), `user_id` (from JWT), `created_at`, `updated_at` (both to current timestamp)
- Validates: Title length (1-200 chars), user ownership
- Result: Created task with user association

#### Read Operation
- Filters all queries by authenticated `user_id` from JWT
- Supports filtering by `completed` status
- Supports sorting by `created_at`, `title`, or other fields
- Result: Tasks belonging only to authenticated user

#### Update Operation
- Updates: `title`, `description`, `completed`
- Updates: `updated_at` to current timestamp
- Validates: Ownership via JWT user_id matching task's user_id
- Result: Updated task record

#### Delete Operation
- Removes the task record
- Validates: Ownership via JWT user_id matching task's user_id
- Result: Deletion confirmation or error if not authorized

## Data Integrity Constraints

### Business Rules
1. A user can only access/modify their own tasks (verified via user_id from JWT)
2. All timestamps are managed automatically by the system
3. Email addresses must be unique across all users
4. Passwords must be properly hashed before storage

### Security Constraints
1. All queries must filter by authenticated user_id to prevent unauthorized access
2. The user_id is extracted from the JWT token, not from request body
3. No user's task data should be accessible to other users
4. Plain text passwords are never stored in the database