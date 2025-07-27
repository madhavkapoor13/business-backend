from sqlalchemy import Column, Integer
from database.db import Base

class FinancialYear(Base):
    __tablename__ = "financial_year"
    financial_year_id = Column(Integer, primary_key=True, index=True)
    start_year = Column(Integer, nullable=False)
    end_year = Column(Integer, nullable=False)
