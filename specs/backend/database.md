# Database Specification: Neon Serverless PostgreSQL for Task Management

## Database Overview

The backend uses Neon Serverless PostgreSQL as the primary data store, accessed through SQLModel for object-relational mapping. The database design emphasizes security, performance, and multi-user isolation.

## Database Configuration

- **Provider**: Neon Serverless PostgreSQL
- **Connection String**: `postgresql://neondb_owner:npg_ALn8w2VXuimk@ep-bold-thunder-ais27zzv-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require`
- **Engine**: Async SQLModel engine with connection pooling
- **Session Management**: async_sessionmaker for proper async database operations

## Schema Design

### User Table

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | Primary Key | Unique identifier for each user |
| email | VARCHAR(255) | UNIQUE, NOT NULL, Indexed | User's email address (used for login) |
| hashed_password | VARCHAR(255) | NOT NULL | BCrypt hashed password |
| created_at | TIMESTAMP | NOT NULL | Timestamp when user was registered |

### Task Table

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| id | UUID | Primary Key | Unique identifier for each task |
| title | VARCHAR(200) | NOT NULL | Task title (1-200 characters) |
| description | TEXT | Optional | Detailed task description |
| completed | BOOLEAN | NOT NULL, Default FALSE | Task completion status |
| user_id | UUID | NOT NULL, Foreign Key, Indexed | ID of the user who owns the task |
| created_at | TIMESTAMP | NOT NULL | Timestamp when task was created |
| updated_at | TIMESTAMP | NOT NULL | Timestamp when task was last updated |

### Indexes

- `users.email`: Unique index for efficient login lookups
- `tasks.user_id`: Index on `user_id` field for optimized queries filtering by user
- `tasks.completed`: Index on `completed` field for optimized queries filtering by completion status

## Data Access Patterns

### Security Requirements
- All queries must filter by authenticated user_id
- Multi-user isolation enforced at query level
- Never expose another user's data
- Passwords are never stored in plain text

### Timestamp Management
- `created_at` automatically set on record creation
- `updated_at` automatically updated on record modification (for tasks)

## Session Management

- Async database sessions using async_sessionmaker
- Dependency injection for session management in API endpoints
- Proper cleanup after each request
- Connection pooling optimized for Neon Serverless

## Migration Strategy

- Initial schema creation using SQLModel's create_all method
- Future schema changes handled through Alembic migrations
- Backward compatibility maintained for existing data