from sqlmodel import create_engine, Session
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from core.config import settings
from urllib.parse import urlparse, parse_qs, urlunparse
import os

def prepare_database_url(url: str) -> str:
    """
    Prepare database URL for asyncpg by removing incompatible query parameters.
    asyncpg doesn't support sslmode in the URL - it's passed via connect_args instead.
    """
    parsed = urlparse(url)
    query_params = parse_qs(parsed.query)
    
    # Remove sslmode and channel_binding as they're handled by connect_args
    query_params.pop('sslmode', None)
    query_params.pop('channel_binding', None)
    
    # Reconstruct query string
    new_query = '&'.join(f"{k}={v[0]}" for k, v in query_params.items())
    
    # Reconstruct URL without sslmode/channel_binding
    new_url = urlunparse((
        parsed.scheme,
        parsed.netloc,
        parsed.path,
        parsed.params,
        new_query,
        parsed.fragment
    ))
    
    return new_url

# Prepare connection arguments for asyncpg
# asyncpg expects ssl=True for SSL connections
connect_args = {"ssl": True}

# Create async engine using the database URL from settings
database_url = prepare_database_url(settings.database_url)
async_engine = create_async_engine(database_url, connect_args=connect_args)

# Create async session maker
AsyncSessionLocal = async_sessionmaker(bind=async_engine, class_=AsyncSession)

# Sync engine for sync operations if needed
sync_engine = create_engine(database_url)

def get_sync_session():
    """Get a synchronous database session"""
    with Session(sync_engine) as session:
        yield session

async def get_async_session():
    """Get an asynchronous database session"""
    async with AsyncSessionLocal() as session:
        yield session