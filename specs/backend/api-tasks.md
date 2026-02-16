# API Specification: Task Management Endpoints

## Task API Overview

The task management API provides endpoints for authenticated users to create, read, update, and delete their personal tasks. All endpoints require JWT authentication and enforce user isolation.

## Base Path

`/api/tasks`

## Authentication Requirements

All endpoints require a valid JWT token in the Authorization header:
`Authorization: Bearer <token>`

Invalid or missing tokens will result in HTTP 401 Unauthorized responses.

## Task Endpoints

### 1. GET /api/tasks

**Description**: Retrieve all tasks for the authenticated user

**Authentication Required**: Yes

**Query Parameters**:
- `status`: Filter by task status (all/pending/completed)
- `sort`: Sort by criteria (created/title/due_date)

**Response**:
- 200 OK: Successfully retrieved tasks
- 401 Unauthorized: Invalid or missing JWT token
- 500 Internal Server Error: Database connection issues

**Success Response**:
```json
{
  "success": true,
  "data": [
    {
      "id": "uuid-string",
      "title": "Task title",
      "description": "Task description",
      "completed": false,
      "user_id": "user-id-from-jwt",
      "created_at": "2023-01-01T00:00:00Z",
      "updated_at": "2023-01-01T00:00:00Z"
    }
  ]
}
```

### 2. POST /api/tasks

**Description**: Create a new task for the authenticated user

**Authentication Required**: Yes

**Request Body**:
```json
{
  "title": "New task title (1-200 chars)",
  "description": "Optional task description"
}
```

**Validation**:
- Title length: 1-200 characters
- Description: Optional, any length

**Response**:
- 201 Created: Task successfully created
- 400 Bad Request: Invalid request body
- 401 Unauthorized: Invalid or missing JWT token
- 500 Internal Server Error: Database connection issues

**Success Response**:
```json
{
  "success": true,
  "data": {
    "id": "new-uuid-string",
    "title": "New task title",
    "description": "Optional task description",
    "completed": false,
    "user_id": "user-id-from-jwt",
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  }
}
```

### 3. PUT /api/tasks/{task_id}

**Description**: Update an existing task for the authenticated user

**Authentication Required**: Yes

**Path Parameter**:
- `task_id`: UUID of the task to update

**Request Body**:
```json
{
  "title": "Updated task title",
  "description": "Updated task description",
  "completed": false
}
```

**Response**:
- 200 OK: Task successfully updated
- 401 Unauthorized: Invalid or missing JWT token
- 404 Not Found: Task doesn't exist or belongs to another user
- 400 Bad Request: Invalid request body
- 500 Internal Server Error: Database connection issues

**Success Response**:
```json
{
  "success": true,
  "data": {
    "id": "existing-uuid-string",
    "title": "Updated task title",
    "description": "Updated task description",
    "completed": false,
    "user_id": "user-id-from-jwt",
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-02T00:00:00Z"
  }
}
```

### 4. PATCH /api/tasks/{task_id}/toggle

**Description**: Toggle the completion status of a task

**Authentication Required**: Yes

**Path Parameter**:
- `task_id`: UUID of the task to toggle

**Response**:
- 200 OK: Task completion status successfully toggled
- 401 Unauthorized: Invalid or missing JWT token
- 404 Not Found: Task doesn't exist or belongs to another user
- 500 Internal Server Error: Database connection issues

**Success Response**:
```json
{
  "success": true,
  "data": {
    "id": "existing-uuid-string",
    "title": "Task title",
    "description": "Task description",
    "completed": true,
    "user_id": "user-id-from-jwt",
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-02T00:00:00Z"
  }
}
```

### 5. DELETE /api/tasks/{task_id}

**Description**: Delete a task for the authenticated user

**Authentication Required**: Yes

**Path Parameter**:
- `task_id`: UUID of the task to delete

**Response**:
- 200 OK: Task successfully deleted
- 401 Unauthorized: Invalid or missing JWT token
- 404 Not Found: Task doesn't exist or belongs to another user
- 500 Internal Server Error: Database connection issues

**Success Response**:
```json
{
  "success": true,
  "data": null
}
```

## Security Implementation

### User Isolation
- All task operations filter by user_id extracted from JWT token
- Never accept user_id from request body or URL parameters
- Return HTTP 404 if attempting to access another user's resources

### Error Responses
- Invalid JWT → HTTP 401 Unauthorized
- Missing JWT → HTTP 401 Unauthorized
- Accessing another user's task → HTTP 404 Not Found
- Malformed request → HTTP 400 Bad Request
- Internal server error → HTTP 500 Internal Server Error