from sqlalchemy import Column, Integer, String, Float
from database.db import Base

class Consumption(Base):
    __tablename__ = "consumptions"

    id = Column(Integer, primary_key=True, index=True)
    indent_id = Column(String(255)) # Added a suitable length
    indent_date = Column(String(50)) # Added a suitable length (e.g., 'YYYY-MM-DD')
    indent_amount = Column(Float)
    po_date = Column(String(50)) # Added a suitable length
    po_amount = Column(Float)
    po_file = Column(String(255)) # Added a suitable length for file names/paths
    invoice_date = Column(String(50)) # Added a suitable length
    invoice_amount = Column(Float)
    invoice_file = Column(String(255)) # Added a suitable length for file names/paths
    remarks = Column(String(500)) # Added a suitable length