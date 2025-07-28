from sqlalchemy import Column, Integer, String
from database.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255), unique=True, index=True) # Added length
    hashed_password = Column(String(255)) # Added length
    role = Column(String(50), default="user") # Added length