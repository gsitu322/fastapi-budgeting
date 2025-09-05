from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Example: DATABASE_URL from environment variable or default
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()


# Dependency to use in routers
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
