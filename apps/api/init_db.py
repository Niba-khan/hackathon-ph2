"""
Database initialization script.
Creates all tables defined in the models.
"""
import asyncio
from sqlmodel import SQLModel
from db.session import async_engine
from db.models import User, Task  # Import models to ensure they're registered


async def init_db():
    """
    Initialize the database by creating all tables.
    """
    print("Creating database tables...")
    
    # Create all tables
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    
    print("Database tables created successfully!")


if __name__ == "__main__":
    asyncio.run(init_db())
