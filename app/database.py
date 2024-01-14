from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the SQLAlchemy engine
engine = create_engine(
    'postgresql://postgres:rootadmin@localhost:5432/QuizApplication', echo=True)

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Define the SQLAlchemy session factory
SessionLocal = sessionmaker(bind=engine)
