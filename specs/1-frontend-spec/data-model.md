# Data Model: Next.js Frontend for Todo Application

## Entities

### User
Represents an authenticated user with unique identifier and authentication credentials.

**Fields**:
- id: string (unique identifier)
- email: string (user's email address)
- createdAt: Date (account creation timestamp)
- updatedAt: Date (last update timestamp)

**Validation rules**:
- email must be a valid email format
- email must be unique
- id must be unique

### Task
Represents a todo item associated with a specific user, with title, description, and completion status.

**Fields**:
- id: string (unique identifier)
- userId: string (foreign key to User)
- title: string (task title)
- description?: string (optional task description)
- completed: boolean (completion status)
- createdAt: Date (task creation timestamp)
- updatedAt: Date (last update timestamp)

**Validation rules**:
- title must not be empty
- userId must reference an existing user
- completed defaults to false

**State transitions**:
- pending → completed (when user marks task as done)
- completed → pending (when user unmarks task as done)

## Relationships
- User (1) → Task (Many): A user can have many tasks
- Task (Many) → User (1): Each task belongs to one user