from sqlalchemy import Column, Integer, String
from database.db import Base

class ItemCategory(Base):
    __tablename__ = "item_category"
    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(255), nullable=False)
