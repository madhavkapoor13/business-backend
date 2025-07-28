from pydantic import BaseModel

class FinancialQuarterCreate(BaseModel):
    quarter_name: str

class ShowFinancialQuarter(BaseModel):
    quarter_id: int
    quarter_name: str

    class Config:
        from_attributes = True