# API Specification: Authentication Endpoints

## Authentication API Overview

The authentication API provides endpoints for user registration, login, and user information retrieval. All endpoints follow the consistent response format and implement proper security measures.

## Base Path

`/api/auth`

## Authentication Endpoints

### 1. POST /api/auth/signup

**Description**: Register a new user account

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Validation**:
- Email must be a valid email format
- Password must meet strength requirements (minimum 8 characters, with uppercase, lowercase, number, and special character)

**Response**:
- 200 OK: User registered successfully, JWT token returned
- 400 Bad Request: Invalid email format, weak password, or validation error
- 409 Conflict: Email already exists

**Success Response**:
```json
{
  "success": true,
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
  }
}
```

### 2. POST /api/auth/login

**Description**: Authenticate user and return JWT token

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "securePassword123"
}
```

**Response**:
- 200 OK: Login successful, JWT token returned
- 401 Unauthorized: Invalid credentials

**Success Response**:
```json
{
  "success": true,
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "token_type": "bearer"
  }
}
```

### 3. GET /api/auth/me

**Description**: Get authenticated user information

**Authentication Required**: Bearer token in Authorization header

**Headers**:
- `Authorization: Bearer <token>`

**Response**:
- 200 OK: User information returned
- 401 Unauthorized: Invalid or missing token

**Success Response**:
```json
{
  "success": true,
  "data": {
    "id": "user-uuid",
    "email": "user@example.com",
    "created_at": "2023-01-01T00:00:00Z"
  }
}
```

### 4. POST /api/auth/logout

**Description**: Logout user (optional for stateless JWT)

**Authentication Required**: Bearer token in Authorization header

**Headers**:
- `Authorization: Bearer <token>`

**Response**:
- 200 OK: Logout successful
- 401 Unauthorized: Invalid or missing token

**Success Response**:
```json
{
  "success": true,
  "data": null
}
```

## JWT Token Structure

The JWT tokens contain the following claims:

- `sub`: User ID (subject)
- `email`: User's email address
- `exp`: Token expiration timestamp
- `iat`: Token issued at timestamp

## Security Requirements

- Passwords are hashed using bcrypt before storage
- JWT tokens are signed with a secure secret key (HS256 algorithm)
- Tokens expire after 60 minutes (configurable)
- Invalid tokens return HTTP 401 Unauthorized
- No sensitive information is stored in JWT payload