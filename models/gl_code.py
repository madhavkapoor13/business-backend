from sqlalchemy import Column, Integer, String
from database.db import Base

class GLCode(Base):
    __tablename__ = "gl_code"
    gl_code_id = Column(Integer, primary_key=True, index=True)
    gl_code = Column(String, nullable=False)
    description = Column(String)
