# API Specification: Task Management Endpoints

**Feature**: Secure Task Management Backend
**Created**: Wednesday, February 11, 2026
**Status**: Draft

## API Overview

The backend provides RESTful API endpoints for task management with token-based authentication. All endpoints require valid authentication tokens and enforce user isolation.

## Base Path

`/api/tasks`

## Authentication Requirements

All endpoints require token authentication via `Authorization: Bearer <token>` header. Invalid or missing tokens result in HTTP 401 responses.

## Response Format

The API uses a consistent response format:

Success:
```
{
  "success": true,
  "data": { ... }
}
```

Error:
```
{
  "success": false,
  "error": "error message"
}
```

## Endpoints

### 1. GET /api/tasks

**Description**: Retrieve all tasks for the authenticated user

**Authentication**: Required (token)

**Query Parameters**:
- `status`: Filter by task status (all/pending/completed)
- `sort`: Sort by criteria (created/title/due_date)

**Response**:
- 200 OK: List of user's tasks
- 401 Unauthorized: Invalid or missing authentication token
- 500 Internal Server Error: Database connection issues

**Example Request**:
```
GET /api/tasks?status=pending&sort=created
Authorization: Bearer <auth_token>
```

**Example Response**:
```
{
  "success": true,
  "data": [
    {
      "id": "uuid-string",
      "title": "Sample task",
      "description": "Task description",
      "completed": false,
      "user_id": "user-id-from-token",
      "created_at": "2023-01-01T00:00:00Z",
      "updated_at": "2023-01-01T00:00:00Z"
    }
  ]
}
```

### 2. POST /api/tasks

**Description**: Create a new task for the authenticated user

**Authentication**: Required (token)

**Request Body**:
```json
{
  "title": "Task title (1-200 chars)",
  "description": "Optional task description"
}
```

**Validation**:
- Title length: 1-200 characters
- Description: Optional, any length

**Response**:
- 201 Created: Task successfully created
- 400 Bad Request: Invalid request body
- 401 Unauthorized: Invalid or missing authentication token
- 500 Internal Server Error: Database connection issues

**Example Request**:
```
POST /api/tasks
Authorization: Bearer <auth_token>
Content-Type: application/json

{
  "title": "New task",
  "description": "Task details"
}
```

**Example Response**:
```
{
  "success": true,
  "data": {
    "id": "uuid-string",
    "title": "New task",
    "description": "Task details",
    "completed": false,
    "user_id": "user-id-from-token",
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z"
  }
}
```

### 3. PUT /api/tasks/{task_id}

**Description**: Update an existing task for the authenticated user

**Authentication**: Required (token)

**Path Parameter**:
- `task_id`: UUID of the task to update

**Request Body**:
```json
{
  "title": "Updated task title",
  "description": "Updated task description"
}
```

**Response**:
- 200 OK: Task successfully updated
- 401 Unauthorized: Invalid or missing authentication token
- 404 Not Found: Task doesn't exist or belongs to another user
- 400 Bad Request: Invalid request body
- 500 Internal Server Error: Database connection issues

**Example Request**:
```
PUT /api/tasks/task-uuid-here
Authorization: Bearer <auth_token>
Content-Type: application/json

{
  "title": "Updated task",
  "description": "Updated details"
}
```

**Example Response**:
```
{
  "success": true,
  "data": {
    "id": "task-uuid-here",
    "title": "Updated task",
    "description": "Updated details",
    "completed": false,
    "user_id": "user-id-from-token",
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-02T00:00:00Z"
  }
}
```

### 4. PATCH /api/tasks/{task_id}/toggle

**Description**: Toggle the completion status of a task

**Authentication**: Required (token)

**Path Parameter**:
- `task_id`: UUID of the task to toggle

**Response**:
- 200 OK: Task completion status successfully toggled
- 401 Unauthorized: Invalid or missing authentication token
- 404 Not Found: Task doesn't exist or belongs to another user
- 500 Internal Server Error: Database connection issues

**Example Request**:
```
PATCH /api/tasks/task-uuid-here/toggle
Authorization: Bearer <auth_token>
```

**Example Response**:
```
{
  "success": true,
  "data": {
    "id": "task-uuid-here",
    "title": "Sample task",
    "description": "Task description",
    "completed": true,
    "user_id": "user-id-from-token",
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-02T00:00:00Z"
  }
}
```

### 5. DELETE /api/tasks/{task_id}

**Description**: Delete a task for the authenticated user

**Authentication**: Required (token)

**Path Parameter**:
- `task_id`: UUID of the task to delete

**Response**:
- 200 OK: Task successfully deleted
- 401 Unauthorized: Invalid or missing authentication token
- 404 Not Found: Task doesn't exist or belongs to another user
- 500 Internal Server Error: Database connection issues

**Example Request**:
```
DELETE /api/tasks/task-uuid-here
Authorization: Bearer <auth_token>
```

**Example Response**:
```
{
  "success": true,
  "data": null
}
```

## Common Error Responses

### 401 Unauthorized
- Cause: Invalid, expired, or missing authentication token
- Response:
```json
{
  "success": false,
  "error": "Unauthorized: Invalid or missing authentication token"
}
```

### 404 Not Found
- Cause: Task doesn't exist or belongs to another user
- Response:
```json
{
  "success": false,
  "error": "Resource not found or access denied"
}
```

### 400 Bad Request
- Cause: Invalid request body or parameters
- Response:
```json
{
  "success": false,
  "error": "Invalid request: [specific validation error]"
}
```

### 500 Internal Server Error
- Cause: Unexpected server error
- Response:
```json
{
  "success": false,
  "error": "Internal server error occurred"
}
```