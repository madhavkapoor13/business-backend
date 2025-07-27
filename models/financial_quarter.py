from sqlalchemy import Column, Integer, String
from database.db import Base

class FinancialQuarter(Base):
    __tablename__ = "financial_quarter"
    quarter_id = Column(Integer, primary_key=True, index=True)
    quarter_name = Column(String, nullable=False)
