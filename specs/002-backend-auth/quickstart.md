# Quickstart Guide: Backend Authentication System

**Feature**: Backend Authentication System
**Date**: Wednesday, February 11, 2026

## Getting Started

This guide will help you set up and run the backend authentication system for the Phase II Hackathon Todo Application. The system handles user registration, login, JWT token generation, and secure task management with user isolation.

## Prerequisites

- Python 3.11 or higher
- pip package manager
- Access to Neon Serverless PostgreSQL database
- Git (optional, for cloning the repository)

## Environment Setup

1. Clone the repository (if needed):
   ```bash
   git clone <repository-url>
   cd hackathon2
   ```

2. Navigate to the backend directory:
   ```bash
   cd apps/api
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables

Create a `.env` file in the `apps/api` directory with the following variables:

```env
DATABASE_URL=postgresql://username:password@host:port/database_name
JWT_SECRET_KEY=your-super-secret-jwt-signing-key-here-make-it-long-and-random
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

## Database Setup

1. Ensure your Neon Serverless PostgreSQL database is created and accessible.

2. Run the initial database migration (if using alembic):
   ```bash
   alembic revision --autogenerate -m "Initial migration"
   alembic upgrade head
   ```

3. Alternatively, if using SQLModel's create_all (for development):
   ```bash
   python -c "from db.models import *; from db.session import engine; from sqlmodel import SQLModel; SQLModel.metadata.create_all(engine)"
   ```

## Running the Backend

1. Start the backend server:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

2. The API will be available at `http://localhost:8000`

## API Endpoints

Once running, the following endpoints will be available:

### Authentication Endpoints
- `POST /api/auth/signup` - Register a new user
- `POST /api/auth/login` - Authenticate user and get JWT token
- `GET /api/auth/me` - Get authenticated user info
- `POST /api/auth/logout` - Logout user (stateless JWT)

### Task Management Endpoints
- `GET /api/tasks` - Retrieve all tasks for the authenticated user
- `POST /api/tasks` - Create a new task for the authenticated user
- `PUT /api/tasks/{task_id}` - Update an existing task
- `PATCH /api/tasks/{task_id}/toggle` - Toggle task completion status
- `DELETE /api/tasks/{task_id}` - Delete a task

## Testing the API

### Authentication Flow
1. Register a new user:
   ```bash
   curl -X POST http://localhost:8000/api/auth/signup \
     -H "Content-Type: application/json" \
     -d '{"email": "user@example.com", "password": "securePassword123"}'
   ```

2. Login to get a JWT token:
   ```bash
   curl -X POST http://localhost:8000/api/auth/login \
     -H "Content-Type: application/json" \
     -d '{"email": "user@example.com", "password": "securePassword123"}'
   ```

3. Use the JWT token to access protected endpoints:
   ```bash
   curl -X GET http://localhost:8000/api/tasks \
     -H "Authorization: Bearer <your-jwt-token>" \
     -H "Content-Type: application/json"
   ```

### Task Management Flow
1. Create a task:
   ```bash
   curl -X POST http://localhost:8000/api/tasks \
     -H "Authorization: Bearer <your-jwt-token>" \
     -H "Content-Type: application/json" \
     -d '{"title": "My first task", "description": "Task details"}'
   ```

2. Retrieve all tasks:
   ```bash
   curl -X GET http://localhost:8000/api/tasks \
     -H "Authorization: Bearer <your-jwt-token>" \
     -H "Content-Type: application/json"
   ```

3. Update a task:
   ```bash
   curl -X PUT http://localhost:8000/api/tasks/<task-id> \
     -H "Authorization: Bearer <your-jwt-token>" \
     -H "Content-Type: application/json" \
     -d '{"title": "Updated task title", "completed": true}'
   ```

4. Toggle task completion:
   ```bash
   curl -X PATCH http://localhost:8000/api/tasks/<task-id>/toggle \
     -H "Authorization: Bearer <your-jwt-token>"
   ```

5. Delete a task:
   ```bash
   curl -X DELETE http://localhost:8000/api/tasks/<task-id> \
     -H "Authorization: Bearer <your-jwt-token>"
   ```

## Development

For development, use the `--reload` flag with uvicorn to automatically reload the server when code changes:

```bash
uvicorn main:app --reload --port 8000
```

## Troubleshooting

- If you get database connection errors, verify your `DATABASE_URL` is correct
- If authentication fails, ensure your `JWT_SECRET_KEY` is properly set and matches the format
- Check that your JWT tokens are being sent in the Authorization header as "Bearer <token>"
- If you get 401 errors, verify that your JWT token is valid and not expired
- Make sure the frontend is configured to send JWT tokens in the Authorization header