from sqlalchemy import Column, Integer, String
from database.db import Base

class ItemExpenseType(Base):
    __tablename__ = "item_expense_type"
    expense_type_id = Column(Integer, primary_key=True, index=True)
    expense_type_name = Column(String(255), nullable=False)
