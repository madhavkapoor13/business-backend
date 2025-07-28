from sqlalchemy import Column, Integer, Float, String, Boolean, ForeignKey
from database.db import Base

class Provision(Base):
    __tablename__ = "provisioning"

    id = Column(Integer, primary_key=True, index=True)
    entity_id = Column(Integer, ForeignKey("entity.entity_id"))
    department_id = Column(Integer, ForeignKey("department.department_id"))
    financial_year_id = Column(Integer, ForeignKey("financial_year.financial_year_id"))
    quarter_id = Column(Integer, ForeignKey("financial_quarter.quarter_id"))
    item_id = Column(Integer, ForeignKey("item.item_id"))
    quantity = Column(Integer)
    approx_price = Column(Float)
    remarks = Column(String(500)) # Added a suitable length for remarks
    is_special_provisioning = Column(Boolean)
    is_budget_frozen = Column(Boolean)
    created_by = Column(String(255)) # Added a suitable length for created_by