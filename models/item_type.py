from sqlalchemy import Column, Integer, String
from database.db import Base

class ItemType(Base):
    __tablename__ = "item_type"
    type_id = Column(Integer, primary_key=True, index=True)
    type_name = Column(String, nullable=False)
