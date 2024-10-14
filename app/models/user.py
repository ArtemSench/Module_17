from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Module_17.app.backend.db import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    firstname = Column(String, nullable=True)
    lastname = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    slug = Column(String, unique=True, index=True)

    # Связь с моделью Task
    tasks = relationship("Task", back_populates="user")