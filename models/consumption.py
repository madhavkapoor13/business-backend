from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class Consumption(Base):
    __tablename__ = "consumptions"

    id = Column(Integer, primary_key=True, index=True)
    indent_id = Column(String)
    indent_date = Column(String)
    indent_amount = Column(Float)
    po_date = Column(String)
    po_amount = Column(Float)
    po_file = Column(String)
    invoice_date = Column(String)
    invoice_amount = Column(Float)
    invoice_file = Column(String)
    remarks = Column(String)
