# maji_mazuri/__init__.py
from models import Base, engine, Session, init_db
from cli import cli

__version__ = "0.1.0"
__all__ = ['Base', 'engine', 'Session', 'init_db', 'cli']

# Initialize database when package is imported
init_db()