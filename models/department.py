from sqlalchemy import Column, Integer, String, ForeignKey
from database.db import Base

class Department(Base):
    __tablename__ = "department"
    department_id = Column(Integer, primary_key=True, index=True)
    department_name = Column(String(255), nullable=False)
    entity_id = Column(Integer, ForeignKey("entity.entity_id"))
