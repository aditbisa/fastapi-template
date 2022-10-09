from typing import Generator

from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.configs import get_db_settings


def get_db_url() -> str:
    """
    Get database url.
    """
    settings = get_db_settings()

    engine = settings.engine
    host = settings.host
    port = settings.port
    user = settings.user
    password = settings.password.get_secret_value()
    database = settings.database

    return f"{engine}://{user}:{password}@{host}:{port}/{database}"


def get_db() -> Generator:
    """
    Create session and close when all done.
    """
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


engine = create_engine(get_db_url())
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
