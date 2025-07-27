from sqlalchemy import Column, Integer, String, ForeignKey
from database.db import Base

class Item(Base):
    __tablename__ = "item"
    item_id = Column(Integer, primary_key=True, index=True)
    item_name = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey("item_category.category_id"))
    type_id = Column(Integer, ForeignKey("item_type.type_id"))
    expense_type_id = Column(Integer, ForeignKey("item_expense_type.expense_type_id"))
