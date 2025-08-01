# app/__init__.py

# Import only available models
from .models import User
from .database import engine, get_session, create_db_and_tables
from .auth import router as auth_router

# Only include what actually exists
__all__ = [
    'engine',
    'get_session',
    'create_db_and_tables',
    'User',
    'auth_router'
]