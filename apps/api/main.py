import logging
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from core.config import settings
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from jose import JWTError
from sqlalchemy.exc import SQLAlchemyError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = FastAPI(title="Secure Task Management API", version="1.0.0")

# Add CORS middleware to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global exception handlers
@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request: Request, exc):
    """
    Global handler for HTTP exceptions.
    """
    logger.error(f"HTTP Exception: {exc.status_code} - {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": False, "error": exc.detail}
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc):
    """
    Global handler for validation errors.
    """
    logger.error(f"Validation Error: {exc}")
    return JSONResponse(
        status_code=400,
        content={"success": False, "error": f"Validation error: {str(exc)}"}
    )

@app.exception_handler(JWTError)
async def jwt_exception_handler(request: Request, exc):
    """
    Global handler for JWT errors.
    """
    logger.error(f"JWT Error: {exc}")
    return JSONResponse(
        status_code=401,
        content={"success": False, "error": f"Authentication error: {str(exc)}"}
    )

@app.exception_handler(SQLAlchemyError)
async def database_exception_handler(request: Request, exc):
    """
    Global handler for database errors.
    """
    logger.error(f"Database Error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"success": False, "error": "Database error occurred"}
    )

@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc):
    """
    Global handler for general exceptions.
    """
    logger.error(f"General Exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"success": False, "error": "Internal server error"}
    )

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the Secure Task Management API"}

# Include API routes
from api.routes import tasks
from api.routes import auth
app.include_router(auth.router, prefix="/api", tags=["auth"])
app.include_router(tasks.router, prefix="/api", tags=["tasks"])