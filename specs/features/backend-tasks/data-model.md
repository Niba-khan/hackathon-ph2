# Data Model: Secure Task Management Backend (Resource Server)

**Feature**: Secure Task Management Backend
**Date**: Wednesday, February 11, 2026

## Entity Definitions

### Task Entity

The Task entity represents a todo item associated with a specific user, with title, description, completion status, and timestamps. The user association is determined by the user_id extracted from the JWT token, not from request data.

#### Fields
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | UUID | Primary Key, Not Null | Unique identifier for each task |
| title | String (200) | Not Null, Length 1-200 | Task title (validated to be between 1 and 200 characters) |
| description | Text | Optional | Detailed task description |
| completed | Boolean | Not Null, Default False | Task completion status |
| user_id | String | Not Null, Indexed | ID of the user who owns the task (extracted from JWT, not from request) |
| created_at | DateTime | Not Null | Timestamp when task was created |
| updated_at | DateTime | Not Null | Timestamp when task was last updated |

#### Relationships
- The `user_id` field establishes a logical relationship to the user (though the actual User entity is managed by Better Auth)

#### Indexes
- `idx_tasks_user_id`: Index on `user_id` field for optimized queries filtering by user
- `idx_tasks_completed`: Index on `completed` field for optimized queries filtering by completion status

#### Validation Rules
- `title` must be between 1 and 200 characters
- `user_id` must match the authenticated user's ID from JWT token
- `created_at` and `updated_at` are automatically managed by the system

#### State Transitions
- `completed` field can transition from `false` to `true` and vice versa
- All other fields can be updated except `id` and `user_id`

## Entity Operations

### Create Operation
- Requires: `title` (1-200 chars), optional `description`
- Sets: `id` (auto-generated UUID), `completed` (default false), `user_id` (from JWT), `created_at`, `updated_at` (both to current timestamp)
- Note: `user_id` comes from JWT token, not from request body

### Read Operation
- Filters all queries by `user_id` to ensure user isolation
- Supports filtering by `completed` status
- Supports sorting by `created_at`, `title`, or other fields

### Update Operation
- Updates: `title`, `description`, `completed`
- Updates: `updated_at` to current timestamp
- Verifies ownership through `user_id` matching authenticated user from JWT

### Delete Operation
- Removes the task record
- Verifies ownership through `user_id` matching authenticated user from JWT

## Data Integrity Constraints

### Business Rules
1. A task can only be accessed/modified by the user who owns it (verified via `user_id` from JWT)
2. All timestamps are managed automatically by the system
3. Title length must be between 1 and 200 characters
4. The `user_id` field cannot be modified after creation and is always taken from the JWT token

### Security Constraints
1. All queries must filter by `user_id` to prevent unauthorized access
2. The `user_id` is extracted from the JWT token, not from request body
3. No task data should be accessible to users who don't own it
4. No password or authentication data is stored in the backend database