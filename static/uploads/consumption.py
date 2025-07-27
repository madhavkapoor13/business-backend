from pydantic import BaseModel

class ConsumptionBase(BaseModel):
    indent_id: str
    indent_date: str
    indent_amount: float
    po_date: str
    po_amount: float
    invoice_date: str
    invoice_amount: float
    remarks: str
