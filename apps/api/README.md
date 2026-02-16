# Secure Task Management Backend

This is a secure, production-ready backend for the Phase II Hackathon Todo Application. The system acts as a resource server that verifies JWT tokens issued by Better Auth on the frontend. The backend uses FastAPI with SQLModel ORM to provide JWT-verified CRUD operations for tasks with strict user isolation. The backend integrates with Neon Serverless PostgreSQL for data persistence and is fully compatible with the existing Next.js frontend using Better Auth for JWT token issuance.

## Prerequisites

- Python 3.11 or higher
- pip package manager
- Access to Neon Serverless PostgreSQL database
- Better Auth configured for JWT token issuance on the frontend

## Setup Instructions

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

- `GET /api/tasks` - Retrieve all tasks for the authenticated user
- `POST /api/tasks` - Create a new task for the authenticated user
- `PUT /api/tasks/{task_id}` - Update an existing task
- `PATCH /api/tasks/{task_id}/toggle` - Toggle task completion status
- `DELETE /api/tasks/{task_id}` - Delete a task

Authentication endpoints:
- `POST /api/auth/signup` - Register a new user
- `POST /api/auth/login` - Authenticate user and get JWT token
- `GET /api/auth/me` - Get authenticated user information
- `POST /api/auth/logout` - Logout user

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

## Security Features

- JWT-based authentication with Better Auth integration
- Strict user isolation - users can only access their own tasks
- Passwords are securely hashed using bcrypt
- All queries filter by authenticated user ID extracted from JWT
- Automatic token expiration validation
- Proper error responses without exposing internal details
- Input validation for all request parameters

## Architecture

- **Framework**: FastAPI for high-performance async API development
- **Database**: SQLModel with Neon Serverless PostgreSQL
- **Authentication**: JWT tokens verified using BETTER_AUTH_SECRET
- **Security**: All endpoints require Authorization header with JWT
- **Response Format**: Consistent JSON with success/error structure