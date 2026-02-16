# Quickstart Guide: Secure Task Management Backend (Resource Server)

**Feature**: Secure Task Management Backend
**Date**: Wednesday, February 11, 2026

## Getting Started

This guide will help you set up and run the secure task management backend for the Phase II Hackathon Todo Application. This backend acts as a resource server that verifies JWT tokens issued by Better Auth on the frontend.

## Prerequisites

- Python 3.11 or higher
- pip package manager
- Access to Neon Serverless PostgreSQL database
- Better Auth configured for JWT token issuance on the frontend

## Environment Setup

1. Clone the repository:
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
BETTER_AUTH_SECRET=your_better_auth_secret_key
BETTER_AUTH_URL=http://localhost:3000
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

- `GET /api/tasks` - Retrieve all tasks for the authenticated user
- `POST /api/tasks` - Create a new task for the authenticated user
- `PUT /api/tasks/{task_id}` - Update an existing task
- `PATCH /api/tasks/{task_id}/toggle` - Toggle task completion status
- `DELETE /api/tasks/{task_id}` - Delete a task

## Testing the API

To test the API endpoints, you'll need a valid JWT token from Better Auth:

1. Authenticate through the frontend to obtain a JWT token from Better Auth
2. Include the token in the Authorization header: `Authorization: Bearer <your-jwt-token>`
3. Make requests to the API endpoints

Example curl command:
```bash
curl -X GET http://localhost:8000/api/tasks \
  -H "Authorization: Bearer <your-jwt-token>" \
  -H "Content-Type: application/json"
```

## Important Notes

- This backend acts as a resource server and does not handle authentication
- Authentication is handled entirely by Better Auth on the frontend
- The backend only verifies JWT tokens issued by Better Auth
- No signup, signin, or logout endpoints exist on this backend
- All user identification comes from the JWT token, not from request bodies

## Development

For development, use the `--reload` flag with uvicorn to automatically reload the server when code changes:

```bash
uvicorn main:app --reload --port 8000
```

## Troubleshooting

- If you get database connection errors, verify your `DATABASE_URL` is correct
- If authentication fails, ensure your `BETTER_AUTH_SECRET` matches the one used by Better Auth
- Check that your frontend is configured to send JWT tokens in the Authorization header
- Remember that this backend only verifies tokens - authentication must happen on the frontend