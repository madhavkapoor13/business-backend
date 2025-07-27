from sqlalchemy import Column, Integer, String
from database.db import Base

class Entity(Base):
    __tablename__ = "entity"
    entity_id = Column(Integer, primary_key=True, index=True)
    entity_name = Column(String, nullable=False)
