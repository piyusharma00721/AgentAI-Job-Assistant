# database/db.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.settings import settings

# Use your environment-based database URL
DATABASE_URL = settings.DATABASE_URL

if DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set in the configuration.")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Configure a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models to inherit from
Base = declarative_base()

# ✅ This line is the key to auto-creating tables
def init_db():
    from database import models  # Make sure it loads model metadata
    try:
        print("Creating tables...")
        Base.metadata.create_all(bind=engine)  # ✅ Now it can see UserToken
        print("Tables created.")
    except Exception as e:
        print("Error while creating tables:", e)

# Dependency function to inject DB session into FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
