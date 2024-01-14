from sqlalchemy import String, Integer, Column, Boolean
from database import Base, engine


def create_tables():
    """
    Creates all tables in the database.
    """
    Base.metadata.create_all(engine)


class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True)
    message = Column(String(255), nullable=False)
    status = Column(Boolean,default=False)
